variable "tags" {
  description = "The tags to add to the new instance."
  type = map(string)
}

variable "certificate_arn" {
  description = "The ARN of the certificate to use for the instance."
  type = string
}

variable "route_zone_id" {
  description = "The ID of the route table zone to use for the instance."
  type = string
}

variable "environment" {
  description = "The environment to use for the instance."
  type = string
}

variable "doppler_token" {
  description = "The port of the database."
  type = string
}

variable "region" {
  description = "The region to use for the instance."
  type = string
}

variable "vpc_id" {
  description = "The ID of the VPC to use for the instance."
  type = string
}

variable "public_subnets" {
  description = "The IDs of the public subnets to use for the instance."
  type = list(string)
}

variable "account_id" {
  description = "The account id"
  type = string
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
