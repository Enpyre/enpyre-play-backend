resource "aws_kms_key" "mq_broker" {
  description             = "KMS key for MQ broker"
  deletion_window_in_days = 7
  enable_key_rotation     = true
  tags                    = var.tags
}
