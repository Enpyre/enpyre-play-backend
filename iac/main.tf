terraform {
  required_version  = ">= 1.1.0"

  backend "remote" {
    hostname = "app.terraform.io"
    organization = "Pubnic"

    workspaces {
      name = "enpyre-play-backend"
    }
  }

  required_providers {
      aws = {
          source    = "hashicorp/aws",
          version   = "~> 3.27"
      }
  }
}

provider "aws" {
  # region  = "us-east-1"
  # profile = "pubnic"
}

module "common" {
  source = "./modules/common"

  certificate_arn   = var.certificate_arn
  environment       = var.environment
  vpc_id            = var.vpc_id
  public_subnet_ids = var.public_subnets

  tags              = var.tags
}

module "enpyre_play" {
  source = "./modules/enpyre_play"

  environment             = var.environment
  route_zone_id           = var.route_zone_id
  lb_dns_name             = module.common.lb_dns_name
  lb_zone_id              = module.common.lb_zone_id
  region                  = var.region
  subnet_ids              = var.public_subnets
  doppler_token           = var.doppler_token
  alb_security_group_id   = module.common.alb_security_group_id
  vpc_id                  = var.vpc_id
  listener_arn            = module.common.listener_arn
  account_id              = var.account_id

  mq_admin_password       = var.mq_admin_password
  mq_admin_user           = var.mq_admin_user
  mq_application_password = var.mq_application_password
  mq_application_user     = var.mq_application_user

  tags                    = var.tags

  depends_on              = [module.common]
}
