variable "name" {
  description = "The name to use for amazon mq"
  type        = string
}

variable "namespace" {
  description = "The namespace to use for amazon mq"
  type        = string
}

variable "mq_admin_password" {
  description = "The password for the mq admin user"
  type        = string
}

variable "mq_admin_user" {
  description = "The username for the mq admin user"
  type        = string
}

variable "mq_application_password" {
  description = "The password for the mq application user"
  type        = string
}

variable "mq_application_user" {
  description = "The username for the mq application user"
  type        = string
}

variable "vpc_id" {
  description = "The vpc id to use for amazon mq"
  type        = string
}

variable "subnet_ids" {
  description = "The subnet ids to use for amazon mq"
  type        = list(string)
}

variable "allowed_security_group_ids" {
  description = "The security group ids to use for amazon mq"
  type        = list(string)
}

variable "tags" {
  description = "The tags to use for amazon mq"
  type        = map(string)
}

variable "environment" {
  description = "The environment to use for amazon mq"
  type        = string
}

variable "apply_immediately" {
  description = "If true, the modifications will be applied as soon as possible, regardless of the PreferredMaintenanceWindow setting"
  type        = bool
  default     = true
}

variable "auto_minor_version_upgrade" {
  description = "If true, minor engine upgrades will be applied automatically to the broker during the maintenance window"
  type        = bool
  default     = true
}

variable "deployment_mode" {
  description = "The deployment mode of the broker"
  type        = string
  default     = "SINGLE_INSTANCE"
}

variable "engine_type" {
  description = "Type of broker engine, `ActiveMQ` or `RabbitMQ`"
  type        = string
  default     = "ActiveMQ"
}

variable "engine_version" {
  description = "The version of the broker engine"
  type        = string
  default = "5.17.2"
}

variable "host_instance_type" {
  description = "The broker's instance type"
  type        = string
  default     = "mq.t3.micro"
}

variable "publicly_accessible" {
  description = "If true, the broker will be accessible from outside of the VPC that it is created in"
  type        = bool
  default     = true
}

variable "general_log_enabled" {
  description = "If true, general logging is enabled"
  type        = bool
  default     = true
}

variable "audit_log_enabled" {
  description = "If true, audit logging is enabled"
  type        = bool
  default     = true
}

variable "kms_ssm_key_arn" {
  description = "The ARN of the KMS key used for encryption at rest"
  type        = string
  default     = "alias/aws/ssm"
}

variable "encryption_enabled" {
  description = "If true, encryption is enabled"
  type        = bool
  default     = true
}

variable "use_aws_owned_key" {
  description = "If true, the broker will use a key managed by Amazon MQ"
  type        = bool
  default     = true
}

variable "ssm_path" {
  description = "The SSM path to use for storing the broker credentials"
  type        = string
  default     = "mq"
}
