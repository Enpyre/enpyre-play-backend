output "task_security_group_id" {
  value = aws_security_group.nsg_task.id
  description = "Task Security Group"
}
