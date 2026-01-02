# Charles Bucher – Cloud & DevOps Portfolio

Welcome! This repo is my **GitHub profile repository**, summarizing my cloud/DevOps skills and projects.

## About Me
- Cloud Support / SysOps / DevOps aspiring professional
- AWS-focused troubleshooting, automation, and operational excellence
- Strong emphasis on IaC, monitoring, and error-driven labs

## Featured Repositories
| Repo | Purpose |
|------|---------|
| [AWS_Cloud_Support_Sim](./AWS_Cloud_Support_Sim) | Flagship lab repo: real-world AWS troubleshooting scenarios |
| [AWS_Error_Driven_Troubleshooting_Lab](./AWS_Error_Driven_Troubleshooting_Lab) | Error-driven labs with hands-on remediation exercises |
| [CloudOpsLab](./CloudOpsLab) | CloudOps practice, automation scripts, and operational exercises |

## Skills Demonstrated
- **AWS Core Services**: EC2, S3, IAM, Lambda, CloudWatch
- **Infrastructure as Code**: Terraform, CloudFormation
- **Monitoring & Troubleshooting**: Alarms, Logs, Tickets
- **Automation**: Scripts, remediation workflows
- **Operational Excellence**: Error-driven labs, SysOps mindset

## Optional IaC Example
You can explore a minimal Terraform example below:

\\\hcl
provider "aws" {
  region = "us-east-1"
}

resource "aws_s3_bucket" "example_bucket" {
  bucket = "example-bucket-demo"
  acl    = "private"
}
\\\

---

This profile repo is **not a lab repo** — it’s a portfolio summary linking to my practical labs.
