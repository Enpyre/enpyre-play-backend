
variable "app" {
  description = "The name of the app"
  type = string
}

variable "environment" {
  description = "The environment to deploy to"
  type = string
}

variable "spot" {
  description = "If the app is a spot app"
  type = bool
  default = true
}

variable "ecs_autoscale_max_instances" {
  description = "The maximum number of instances to run"
  type = number
  default = 1
}

variable "ecs_autoscale_min_instances" {
  description = "The minimum number of instances to run"
  type = number
  default = 1
}

variable "ecs_cpu" {
  description = "The number of cpu units to allocate"
  type = number
  default = 256
}

variable "ecs_memory" {
  description = "The amount of memory to allocate"
  type = number
  default = 512
}

variable "image" {
  description = "The image to run"
  type = string
}

variable "container_port" {
  description = "The port to expose"
  type = number
  default = null
}

variable "container_env" {
  description = "The environment variables"
  type = list(map(string))
}

variable "region" {
  description = "The region to deploy to"
  type = string
}

variable "tags" {
  description = "The tags to apply to the service"
  type = map(string)
}

variable "replicas" {
  description = "The number of replicas to run"
  type = number
  default = 1
}

variable "subnet_ids" {
  description = "The subnet ids to deploy to"
  type = list(string)
}

variable "logs_retention_in_days" {
  description = "The number of days to keep logs"
  type = number
  default = 7
}

variable "deregistration_delay" {
  description = "The time to wait before deregistering a target"
  type = number
  default = 30
}

variable "health_check" {
  description = "The path to the health check for the load balancer to know if the container(s) are ready"
  type = string
  default = "/"
}

variable "health_check_matcher" {
  description = "The matcher to use for the health check"
  type = string
  default = "200"
}

variable "health_check_interval" {
  description = "The interval to use for the health check"
  type = number
  default = 30
}

variable "health_check_timeout" {
  description = "The timeout to use for the health check"
  type = number
  default = 10
}

variable "route_zone_id" {
  description = "The route53 zone id to use for the load balancer"
  type = string
}

variable "domain" {
  description = "The domain to use for the route53 record"
  type = string
  default = null
}

variable "lb_dns_name" {
  description = "The dns name of the load balancer"
  type = string
  default = null
}

variable "lb_zone_id" {
  description = "The zone id of the load balancer"
  type = string
  default = null
}

variable "alb_security_group_id" {
  description = "The security group id to use for the load balancer"
  type = string
}

variable "vpc_id" {
  description = "The vpc id to use for the load balancer"
  type = string
}

variable "listener_arn" {
  description = "The arn of the listener to use for the load balancer"
  type = string
}

variable "assign_public_ip" {
  description = "If the service should have a public ip"
  type = bool
}

variable "account_id" {
  description = "The account id to use for the load balancer roles"
  type = string
}

variable "deployment_maximum_percent" {
  description = "The maximum number of instances to deploy at once"
  type = number
  default = 200
}

variable "deployment_minimum_healthy_percent" {
  description = "The minimum number of instances to keep healthy"
  type = number
  default = 100
}

variable "rollback_if_deployment_fails" {
  description = "If the deployment should rollback if it fails"
  type = bool
  default = true
}

variable "container_command" {
  description = "The command to run for the task"
  type = list(string)
  default = []
}

variable "health_check_command" {
  description = "The command to run for the health check"
  type = list(string)
  default = null
}
