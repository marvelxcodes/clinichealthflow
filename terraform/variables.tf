variable "aws_region" {
  description = "AWS region for HealthNivaran infrastructure"
  type        = string
  default     = "ap-south-1"
}

variable "cluster_name" {
  description = "EKS cluster name"
  type        = string
  default     = "healthnivaran-eks"
}

variable "environment" {
  description = "Deployment environment label"
  type        = string
  default     = "dev"
}
