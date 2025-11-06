# 👋 Charles Bucher  
**Cloud Engineer  Terraform • AWS • Python  Built, Documented & Tore Down Infra with Lifecycle Proof


## 🧠 Who I Am  
   I’m a hands-on cloud builder breaking in through support, pushing toward full cloud engineering. I design modular AWS infrastructure, automate what breaks, and document every fix like it’s meant to be inherited. My repos aren’t just technical—they’re reproducible, teardown-proof, and built to prove ownership



## 🧰 Projects That Prove It  
- [cloudOps-guardDuty-automation](https://github.com/charles-bucher/cloudOps-guardDuty-automation)  
  Automates GuardDuty threat detection with EventBridge filtering, SNS alerts, and secure S3 export. Includes teardown logic, lifecycle tagging, and screenshots.

- [aws_monitoring_observability](https://github.com/charles-bucher/aws_monitoring_observability)  
  Deploys EC2 monitoring with CloudWatch dashboards, alarms, and SNS notifications. Built for proactive incident response and modular observability.



# 📸 GuardDuty Automation — Screenshot Proof

This repo documents modular AWS infrastructure built for GuardDuty automation, with teardown hygiene and lifecycle clarity. Below are screenshots capturing key stages of deployment, automation flow, and teardown.

---

## 🔁 Lifecycle Overview

| Stage            | Screenshot                                  | Description                                                  |
|------------------|---------------------------------------------|--------------------------------------------------------------|
| Clone & Setup    | `clone_Repo.png`                            | Repo cloned locally to begin Terraform provisioning.         |
| Terraform Ready  | `terraform_installed.png`                   | Terraform binary installed and verified.                     |
| Infra Created    | `terraform_made.png`, `terraform-plan.png`  | Resources defined and planned for deployment.                |
| Plan Confirmed   | `tf_plan_screenshot.png`                    | Terraform plan output confirms tagged, modular resources.    |
| Infra Deployed   | `deployed.png`                              | Infrastructure successfully deployed.                        |
| GuardDuty Active | `guardduty-running.png`, `guardduty-instance-running.png` | GuardDuty enabled and monitoring EC2 instance.               |
| Alert Triggered  | `Screenshot 2025-10-09 111039.png`          | GuardDuty finding triggered automation flow.                 |
| Infra Destroyed  | `destroy.png`                               | Clean teardown confirmed — no orphaned assets remain.        |

---

## 🧼 Teardown Hygiene

- All resources tagged for lifecycle clarity.
- Screenshots timestamped and tied to specific stages.
- Teardown confirmed via `terraform destroy` with zero residuals.

---

## 🧠 Why This Matters

This repo isn’t just technical — it’s reproducible, teardown-proof, and built to prove ownership. Every screenshot backs a lifecycle stage. Every fix is documented like it’s meant to be inherited.

> 💬 Built for support engineers, cloud learners, and underdogs who need visual proof of transformation.


---

## 🔧 1. Terraform Deployment

![Terraform apply output](screenshots/terraform-apply-output.png)  
*Modular Terraform deployment with tagged resources and lifecycle-aware naming.*

---

## 🛡️ 2. GuardDuty Findings Trigger

![GuardDuty finding](screenshots/guardduty-finding.png)  
*GuardDuty detects suspicious activity and triggers automation via EventBridge.*

---

## 🔁 3. EventBridge → Lambda Flow

![EventBridge rule](screenshots/eventbridge-rule.png)  
*EventBridge routes findings to Lambda for automated response.*

![Lambda function](screenshots/lambda-function.png)  
*Lambda function parses findings and initiates tagging, notification, or remediation.*

---

## 📬 4. SNS Notification

![SNS topic](screenshots/sns-topic.png)  
*Security alerts published to SNS for visibility and escalation.*

---

## 🧹 5. Teardown Hygiene

![Terraform destroy output](screenshots/terraform-destroy-output.png)  
*Clean teardown with no orphaned assets. All resources tagged and removed.*

---

## 📚 Repo Hygiene

- All screenshots are timestamped



## 🧱 My Stack  
Terraform • AWS • Python • CloudWatch • GitHub Actions • PowerShell  

## 🧠 Cloud Engineer Proof  
- Infra that deploys, alerts, and tears down clean  
- Screenshot-driven documentation for reproducibility and recruiter clarity  
- Support tooling built from real AWS incidents  
- Lifecycle tagging and teardown hygiene baked in  
- Security-first modules with encryption and versioning  
- CI/CD pipelines and modular automation for scale  

## 🧠 My Philosophy  
Every fix is a transformation arc. Every repo is a survival story. I build for clarity, not perfection—and I document like someone who wants others to learn from it. I’m not leaving DevOps. I’m building toward Cloud Engineering, one repo at a time.

## 📫 Let’s Connect  
🌐 [charles-bucher.github.io](https://charles-bucher.github.io)  
💼 [LinkedIn](https://www.linkedin.com/in/charles-bucher)  
📧 quietopscb@gmail.com  
