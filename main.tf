provider "aws" {
  region = var.region
}

resource "aws_iam_user" "lake_user" {
  name = var.username
}

resource "random_pet" "data_name" {
  length    = 3
  separator = "-"
}

resource "aws_s3_bucket" "lake_bucket" {
  bucket = "${var.username}-data-lake-bucket"
  acl    = "private"
}

data "aws_iam_policy_document" "s3_policy" {
  statement {
    actions   = ["s3:ListAllMyBuckets"]
    resources = ["arn:aws:s3:::${var.username}/*"]
    effect = "Allow"
  }
  statement {
    actions   = ["s3:*"]
    resources = [aws_s3_bucket.lake_bucket.arn]
    effect = "Allow"
  }
}
