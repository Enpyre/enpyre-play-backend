resource "aws_lb_listener_rule" "frontend_https" {
  count = var.container_port == null ? 0 : 1
  listener_arn = var.listener_arn

  action {
    type = "forward"
    target_group_arn = aws_alb_target_group.main[0].arn
  }

  condition {
    host_header {
      values = [var.domain]
    }
  }

  tags = var.tags

  depends_on = [aws_alb_target_group.main]
}
