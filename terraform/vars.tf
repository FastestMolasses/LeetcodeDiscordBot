variable "tf-bucket-name" {
  default     = "leetbot-tf-state"
  type        = string
  description = "Name of the S3 bucket to store terraform state"
}
