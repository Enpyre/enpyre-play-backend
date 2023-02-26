resource "aws_ecs_cluster" "app" {
  name = "${var.app}-${var.environment}"
  capacity_providers = ["FARGATE", "FARGATE_SPOT"]
  default_capacity_provider_strategy {
    capacity_provider = var.spot ? "FARGATE_SPOT" : "FARGATE"
    weight = 1
  }
  setting {
    name  = "containerInsights"
    value = "enabled"
  }
  tags = var.tags
}

resource "aws_appautoscaling_target" "app_scale_target" {
  service_namespace  = "ecs"
  resource_id        = "service/${aws_ecs_cluster.app.name}/${aws_ecs_service.app.name}"
  scalable_dimension = "ecs:service:DesiredCount"
  max_capacity       = var.ecs_autoscale_max_instances
  min_capacity       = var.ecs_autoscale_min_instances
}

resource "aws_ecs_task_definition" "app" {
  family                   = "${var.app}-${var.environment}"
  requires_compatibilities = ["FARGATE"]
  network_mode             = "awsvpc"
  cpu                      = var.ecs_cpu
  memory                   = var.ecs_memory
  execution_role_arn       = aws_iam_role.ecsTaskExecutionRole.arn

  # defined in role.tf
  task_role_arn = aws_iam_role.app_role.arn

  container_definitions = jsonencode([
  {
    "name": "${var.app}",
    "image": "${var.image}",
    "essential": true,
    "command": var.container_command != [] ? var.container_command : null,
    "portMappings": var.container_port == null ? [] : [
      {
        "containerPort": var.container_port,
        "hostPort": var.container_port,
        "protocol": "tcp"
      }
    ],
    "environment": var.container_env,
    "logConfiguration": {
      "logDriver": "awslogs",
      "options": {
        "awslogs-group": "/fargate/service/${var.app}-${var.environment}",
        "awslogs-region": "${var.region}",
        "awslogs-stream-prefix": "ecs"
      }
    },
    "healthCheck": {
      "command": var.health_check_command == [] ? [
        "CMD-SHELL",
        "curl -f http://localhost:${var.container_port}${var.health_check} || exit 1"
      ] : concat([
        "CMD-SHELL",
      ], var.health_check_command),
      "interval": var.health_check_interval,
      "timeout": var.health_check_timeout,
      "retries": 3,
      "startPeriod": 60
    }
  }
])


  tags = var.tags
}

resource "aws_ecs_service" "app" {
  name            = "${var.app}-${var.environment}"
  cluster         = aws_ecs_cluster.app.id
  launch_type     = "FARGATE"
  task_definition = aws_ecs_task_definition.app.arn
  deployment_maximum_percent = var.deployment_maximum_percent
  deployment_minimum_healthy_percent = var.deployment_minimum_healthy_percent
  desired_count   = var.replicas
  force_new_deployment = true
  health_check_grace_period_seconds = 60

  deployment_circuit_breaker {
    enable = var.rollback_if_deployment_fails
    rollback = var.rollback_if_deployment_fails
  }

  network_configuration {
    security_groups = [var.alb_security_group_id]
    subnets         = var.subnet_ids
    assign_public_ip = var.assign_public_ip
  }

  dynamic "load_balancer" {
    for_each = var.container_port == null ? [] : [1]

    content {
      target_group_arn = aws_alb_target_group.main[0].id
      container_name   = var.app
      container_port   = var.container_port
    }
  }

  tags                    = var.tags
  enable_ecs_managed_tags = true
  propagate_tags          = "SERVICE"
}

# https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_execution_IAM_role.html
resource "aws_iam_role" "ecsTaskExecutionRole" {
  name               = "${var.app}-${var.environment}-ecs"
  assume_role_policy = data.aws_iam_policy_document.assume_role_policy.json
}

data "aws_iam_policy_document" "assume_role_policy" {
  statement {
    actions = ["sts:AssumeRole"]

    principals {
      type        = "Service"
      identifiers = ["ecs-tasks.amazonaws.com"]
    }
  }
}

resource "aws_iam_role_policy_attachment" "ecsTaskExecutionRole_policy" {
  role       = aws_iam_role.ecsTaskExecutionRole.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AmazonECSTaskExecutionRolePolicy"
}

resource "aws_cloudwatch_log_group" "logs" {
  name              = "/fargate/service/${var.app}-${var.environment}"
  retention_in_days = var.logs_retention_in_days
  tags              = var.tags
}
