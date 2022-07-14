# The name of the bucket to hold the terraform state
variable "tf-bucket-name" {
  default     = "leetbot-tf-state"
  type        = string
  description = "Name of the S3 bucket to store terraform state"
}

# A list of allowed availability zones
variable "availability_zone" {
  description = "A list of allowed availability zones."
  type        = list(any)
  default     = ["us-east-1a", "us-east-1c"]
}

# A boolean flag to map the public IP on launch for public subnets
variable "map_public_ip" {
  description = "Specify true to indicate that instances launched into the subnet should be assigned a public IP address."
  type        = bool
  default     = true
}

# The CIDR block for the public subnet. This block should be a range within the above VPC CIDR
variable "public_cidr_1" {
  description = "The CIDR block for the first public subnet."
  type        = string
  default     = "10.0.1.0/24"
}

# The CIDR block for the public subnet. This block should be a range within the above VPC CIDR
variable "public_cidr_2" {
  description = "The CIDR block for the second public subnet."
  type        = string
  default     = "10.0.2.0/24"
}

# The CIDR block for the first private subnet. This block should be a range within the above VPC CIDR
variable "private_cidr_1" {
  description = "The CIDR block for the first private subnet."
  type        = string
  default     = "10.0.3.0/24"
}

# The CIDR block for the second private subnet. This block should be a range within the above VPC CIDR
variable "private_cidr_2" {
  description = "The CIDR block for the second private subnet."
  type        = string
  default     = "10.0.4.0/24"
}
