module "ecs" {
  source = "../ecs"

  app = "enpyre-play-celery"
  environment     = var.environment
  spot            = true
  ecs_cpu         = 256
  ecs_memory      = 512
  image           = "${var.account_id}.dkr.ecr.${var.region}.amazonaws.com/enpyre-play:latest"
  container_command = ["./start_celery.sh"]
  container_env   = [
    {
      "name": "DOPPLER_TOKEN",
      "value": var.doppler_token
    }
  ]
  region                              = var.region
  replicas                            = 2
  ecs_autoscale_max_instances         = 2
  ecs_autoscale_min_instances         = 2
  deployment_minimum_healthy_percent  = 50
  rollback_if_deployment_fails        = true
  subnet_ids                          = var.subnet_ids
  logs_retention_in_days              = 7
  tags                                = var.tags
  deregistration_delay                = 5
  health_check_command = [
    "doppler run -- celery -A enpyre_play status"
  ]
  route_zone_id                       = var.route_zone_id
  lb_dns_name                         = var.lb_dns_name
  lb_zone_id                          = var.lb_zone_id
  alb_security_group_id               = var.alb_security_group_id
  vpc_id                              = var.vpc_id
  listener_arn                        = var.listener_arn
  assign_public_ip                    = true
  account_id                          = var.account_id
}
