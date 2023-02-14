module "mq_broker" {
  source = "cloudposse/mq-broker/aws"
  version = "2.0.1"

  name = var.name
  namespace = var.namespace
  environment = var.environment
  stage = var.environment

  mq_admin_password = [var.mq_admin_password]
  mq_admin_user = [var.mq_admin_user]
  mq_application_password = [var.mq_application_password]
  mq_application_user = [var.mq_application_user]

  vpc_id     = var.vpc_id
  subnet_ids = var.subnet_ids

  allowed_security_group_ids = var.allowed_security_group_ids
  allowed_ingress_ports      = [8162, 5671]


  apply_immediately          = var.apply_immediately
  auto_minor_version_upgrade = var.auto_minor_version_upgrade
  deployment_mode            = var.deployment_mode
  engine_type                = var.engine_type
  engine_version             = var.engine_version
  host_instance_type         = var.host_instance_type
  publicly_accessible        = var.publicly_accessible
  general_log_enabled        = var.general_log_enabled
  audit_log_enabled          = var.audit_log_enabled
  kms_ssm_key_arn            = var.kms_ssm_key_arn
  encryption_enabled         = var.encryption_enabled
  kms_mq_key_arn             = aws_kms_key.mq_broker.arn
  use_aws_owned_key          = var.use_aws_owned_key

  ssm_path = var.ssm_path

  security_group_create_before_destroy = true

  tags = var.tags
}
