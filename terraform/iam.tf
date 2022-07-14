resource "aws_iam_role" "ec2_leetbot_role" {
  name = "ec2_leetbot_role"

  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": "ec2.amazonaws.com"
      },
      "Effect": "Allow"
    }
  ]
}
EOF

  tags = {
    project = "Leetbot"
  }
}

resource "aws_iam_instance_profile" "ec2_leetbot_profile" {
  name = "ec2_leetbot_profile"
  role = aws_iam_role.ec2_leetbot_role.name
}

resource "aws_iam_role_policy" "ec2_policy" {
  name = "ec2_policy"
  role = aws_iam_role.ec2_leetbot_role.id

  policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": [
        "ecr:GetAuthorizationToken",
        "ecr:BatchGetImage",
        "ecr:GetDownloadUrlForLayer"
      ],
      "Effect": "Allow",
      "Resource": "*"
    }
  ]
}
EOF
}
