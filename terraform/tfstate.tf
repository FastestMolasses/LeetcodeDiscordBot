# Used to hold the terraform state
resource "aws_s3_bucket" "leetbot_tf_state" {
  bucket = var.tf-bucket-name
}

# Allow versioning for the terraform state
resource "aws_s3_bucket_versioning" "leetbot_tf_state_versioning" {
  bucket = aws_s3_bucket.leetbot_tf_state.id
  versioning_configuration {
    status = "Enabled"
  }
}

# Used for terraform state "locking"
resource "aws_dynamodb_table" "terraform_locks" {
  name         = "leetbot-tf-state-lock"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "LockID"
  attribute {
    name = "LockID"
    type = "S"
  }
}

# Save the terraform state in S3
terraform {
  backend "s3" {
    profile        = "personal"
    key            = "global/s3/terraform.tfstate"
    region         = "us-east-1"
    dynamodb_table = "leetbot-tf-state-lock"
    encrypt        = true
    bucket         = "leetbot-tf-state"
  }
}
