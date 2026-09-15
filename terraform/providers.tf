terraform {
  required_version = ">= 1.6.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }

  # Remote state — uncomment once the S3 bucket + DynamoDB table exist
  # backend "s3" {
  #   bucket         = "devops-demo-tfstate"
  #   key            = "devops-demo/terraform.tfstate"
  #   region         = "ap-south-1"
  #   dynamodb_table = "devops-demo-tf-locks"
  #   encrypt        = true
  # }
}

provider "aws" {
  region = var.aws_region
}