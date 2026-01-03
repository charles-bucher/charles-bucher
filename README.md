# Hi, I'm Charles Bucher 👋

<div align="center">

![AWS](https://img.shields.io/badge/AWS-Cloud_Learning-FF9900?style=for-the-badge&logo=amazon-aws&logoColor=white)
![Terraform](https://img.shields.io/badge/Terraform-IaC-7B42BC?style=for-the-badge&logo=terraform&logoColor=white)
![Python](https://img.shields.io/badge/Python-Automation-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)

**Self-Taught AWS Cloud Engineer** 🚀  
*Career transition from delivery driver to cloud operations*

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=flat-square&logo=linkedin)](https://linkedin.com/in/charles-bucher-cloud)
[![Portfolio](https://img.shields.io/badge/Portfolio-View-success?style=flat-square)](https://charles-bucher.github.io)
[![Open to Work](https://img.shields.io/badge/Status-Open_to_Work-brightgreen?style=flat-square)](mailto:charles.bucher.cloud@gmail.com)

</div>

---

## 🎯 About Me

I'm a **self-taught cloud engineer** building hands-on AWS skills through real-world projects. I spent the last year learning AWS while working as a delivery driver, and now I'm ready for my first cloud role.

**What I'm Looking For:**
- Entry-level AWS Cloud Support / SysOps roles
- Junior DevOps Engineer positions
- Cloud Operations Engineer (remote preferred)
- Contract opportunities through staffing agencies

**Current Status:**
```
✅ Built 3 comprehensive AWS lab environments
✅ Deployed infrastructure with Terraform
✅ Created troubleshooting scenarios with documentation
🔄 Studying for AWS Solutions Architect Associate
📋 Adding automation & CI/CD projects
```

---

## 💼 What I Can Do (Honestly)

| Skill Area | Level | Proof |
|------------|-------|-------|
| **AWS Console** | Comfortable | Screenshots throughout repos |
| **EC2, VPC, S3** | Learning | Deployed real infrastructure |
| **IAM, Security Groups** | Basic | Can configure policies |
| **CloudWatch Logs** | Basic | Can troubleshoot with logs |
| **Terraform** | Beginner | Have working IaC code |
| **Python Scripts** | Basic | Simple automation |
| **Git/GitHub** | Comfortable | You're looking at it |
| **Documentation** | Strong | Professional docs in all repos |
| **Troubleshooting** | Learning | Built error-driven labs |

**Translation:** I'm entry-level, but I've actually touched AWS and built things. I can prove it.

---

## 🔧 Featured Projects

### 1️⃣ [AWS Cloud Support Simulator](https://github.com/charles-bucher/AWS_Cloud_Support_Sim)
**My flagship portfolio project** - Real-world AWS troubleshooting scenarios

<a href="https://github.com/charles-bucher/AWS_Cloud_Support_Sim">
  <img src="https://raw.githubusercontent.com/charles-bucher/AWS_Cloud_Support_Sim/main/screenshots/00_lab_environment_verified.png" alt="Lab Environment" width="600">
</a>

*Fully functional AWS lab environment deployed with Terraform*

**What's Inside:**
- ✅ Complete VPC with subnets, routing, security groups
- ✅ EC2, S3, Lambda, IAM configurations
- ✅ CloudWatch monitoring and alarms
- ✅ Security hardening with GuardDuty

<details>
<summary><b>🏗️ Architecture & Infrastructure</b></summary>

<br>

#### VPC Architecture
<img src="https://raw.githubusercontent.com/charles-bucher/AWS_Cloud_Support_Sim/main/screenshots/01_vpc_architecture_setup.png" alt="VPC Setup" width="600">

*Custom VPC with public/private subnets, IGW, and route tables*

<br>

#### Network Configuration
<img src="https://raw.githubusercontent.com/charles-bucher/AWS_Cloud_Support_Sim/main/screenshots/02_vpc_subnets_routing.png" alt="Subnets & Routing" width="600">

*Detailed subnet configuration and routing tables*

<br>

#### Security Hardening
<img src="https://raw.githubusercontent.com/charles-bucher/AWS_Cloud_Support_Sim/main/screenshots/03_security_groups_network_acls.png" alt="Security Groups" width="600">

*Security Groups and Network ACLs configured for defense in depth*

</details>

<details>
<summary><b>🔐 IAM & Storage</b></summary>

<br>

#### IAM Roles & Policies
<img src="https://raw.githubusercontent.com/charles-bucher/AWS_Cloud_Support_Sim/main/screenshots/04_iam_roles_policies_setup.png" alt="IAM Setup" width="600">

*IAM roles configured with least privilege policies*

<br>

#### S3 Bucket Configuration
<img src="https://raw.githubusercontent.com/charles-bucher/AWS_Cloud_Support_Sim/main/screenshots/06_s3_bucket_setup.png" alt="S3 Setup" width="600">

*S3 buckets with versioning, encryption, and access policies*

</details>

<details>
<summary><b>📊 Monitoring & Security</b></summary>

<br>

#### CloudWatch Dashboard
<img src="https://raw.githubusercontent.com/charles-bucher/AWS_Cloud_Support_Sim/main/screenshots/09_cloudwatch_monitoring_dashboard.png" alt="CloudWatch" width="600">

*Custom CloudWatch dashboard for monitoring metrics and logs*

</details>

**Skills Demonstrated:** VPC design, IAM governance, Infrastructure as Code, security best practices, monitoring

**Tech Stack:** AWS (EC2, VPC, S3, Lambda, CloudWatch), Terraform, Python

---

### 2️⃣ [AWS Error-Driven Troubleshooting Lab](https://github.com/charles-bucher/AWS_Error_Driven_Troubleshooting_Lab)
**Hands-on troubleshooting scenarios** - I broke things on purpose to learn how to fix them

**Real Incidents I Created & Solved:**

<details>
<summary><b>🔴 Incident 001: EC2 SSH Lockout</b></summary>

<br>

<img src="https://raw.githubusercontent.com/charles-bucher/AWS_Error_Driven_Troubleshooting_Lab/main/001-ec2-ssh-lockout/001_screenshots/05_ec2_instances.png" alt="EC2 SSH Issue" width="600">

**Problem:** Unable to SSH into EC2 instance  
**Investigation:** Security Group had port 22 blocked  
**Solution:** Fixed Security Group rules, verified connectivity  
**Learning:** Always check Security Groups first when troubleshooting connectivity

</details>

<details>
<summary><b>🔴 Incident 002: S3 Public Bucket Exposure</b></summary>

<br>

<img src="https://raw.githubusercontent.com/charles-bucher/AWS_Error_Driven_Troubleshooting_Lab/main/002-s3-public-bucket/002_screenshots/04_full_audit_workflow.png" alt="S3 Remediation" width="600">

**Problem:** S3 bucket accidentally made public  
**Investigation:** Audited bucket policies and ACLs  
**Solution:** Implemented bucket policy remediation, enabled block public access  
**Learning:** Multi-layered security approach prevents exposure

</details>

<details>
<summary><b>🔴 Incident 003: Lambda Function Timeout</b></summary>

<br>

<img src="https://raw.githubusercontent.com/charles-bucher/AWS_Error_Driven_Troubleshooting_Lab/main/003-lambda-timeout/003_screenshots/04_remediate_issue.png" alt="Lambda Fix" width="600">

**Problem:** Lambda function timing out at 3 seconds  
**Investigation:** Analyzed CloudWatch Logs, identified inefficient code  
**Solution:** Increased timeout, optimized code, added error handling  
**Learning:** CloudWatch Logs tell you exactly what's wrong

</details>

**Skills Demonstrated:** Troubleshooting methodology, root cause analysis, incident response, documentation

**Tech Stack:** AWS (EC2, S3, Lambda, CloudWatch), Python remediation scripts

---

### 3️⃣ [CloudOps Lab](https://github.com/charles-bucher/CloudOpsLab)
**Automation & monitoring practice** - Learning operational excellence

<details>
<summary><b>📡 Automated Monitoring</b></summary>

<br>

#### CloudWatch Alarms & SNS Notifications
<img src="https://raw.githubusercontent.com/charles-bucher/CloudOpsLab/main/automation/screenshots/CloudWatch%20alarm%20firing%20or%20SNS%20notification.png" alt="CloudWatch Alarm" width="600">

*Automated monitoring with email alerts via SNS*

<br>

#### EC2 Auto-Recovery
<img src="https://raw.githubusercontent.com/charles-bucher/CloudOpsLab/main/automation/screenshots/ec2-auto-recovery-error.png" alt="EC2 Recovery" width="600">

*Configured EC2 auto-recovery for system status checks*

</details>

<details>
<summary><b>🛡️ Security Monitoring</b></summary>

<br>

#### GuardDuty Security Monitoring
<img src="https://raw.githubusercontent.com/charles-bucher/CloudOpsLab/main/monitoring/screenshots/GuardDuty%20enabled%20in%20AWS%20console.png" alt="GuardDuty" width="600">

*GuardDuty enabled for threat detection*

<br>

#### Security Issues Detection
<img src="https://raw.githubusercontent.com/charles-bucher/CloudOpsLab/main/monitoring/screenshots/issues%20detected%20summary.png" alt="Issues Detected" width="600">

*Security audit findings and remediation tracking*

</details>

**Skills Demonstrated:** Automation, monitoring, alerting, security auditing, operational workflows

**Tech Stack:** AWS (CloudWatch, GuardDuty, SNS, CloudTrail), Python automation scripts

---

## 🛠️ Tech Stack & Tools

### Cloud Platform
```
AWS Services I've Actually Used:
├─ Compute: EC2 (instances, SSH, troubleshooting)
├─ Storage: S3 (buckets, policies, versioning, encryption)
├─ Networking: VPC, Subnets, Route Tables, IGW, Security Groups, NACLs
├─ Security: IAM (roles, policies, users), GuardDuty
├─ Monitoring: CloudWatch (logs, metrics, alarms, dashboards)
├─ Serverless: Lambda (functions, IAM, timeouts)
└─ Audit: CloudTrail (API logging, investigation)
```

### Infrastructure as Code
![Terraform](https://img.shields.io/badge/Terraform-7B42BC?style=flat-square&logo=terraform&logoColor=white)
![CloudFormation](https://img.shields.io/badge/CloudFormation-FF9900?style=flat-square&logo=amazon-aws&logoColor=white)

**What I Can Do:**
- Deploy VPC environments with Terraform
- Create modular, reusable infrastructure code
- Use variables and outputs effectively
- Manage state files properly

### Scripting & Automation
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Bash](https://img.shields.io/badge/Bash-4EAA25?style=flat-square&logo=gnu-bash&logoColor=white)
![PowerShell](https://img.shields.io/badge/PowerShell-5391FE?style=flat-square&logo=powershell&logoColor=white)

**What I've Built:**
- Error simulation scripts
- Automated remediation workflows
- Monitoring setup scripts
- Basic automation tasks

### Version Control & Documentation
![Git](https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-100000?style=flat-square&logo=github&logoColor=white)
![Markdown](https://img.shields.io/badge/Markdown-000000?style=flat-square&logo=markdown&logoColor=white)

---

## 📚 Currently Learning

**AWS Solutions Architect - Associate**
- Studying: Stephane Maarek's Udemy course
- Practice: Tutorials Dojo labs and exams
- Hands-on: Building projects to reinforce concepts

**Next Skills on My List:**
- [ ] Auto Scaling Groups & Elastic Load Balancers
- [ ] RDS and database fundamentals
- [ ] Container basics (ECS)
- [ ] CI/CD pipelines (CodePipeline, CodeBuild)
- [ ] AWS Systems Manager

---

## 📊 GitHub Stats

<div align="center">

<a href="https://github.com/charles-bucher">
  <img height="180em" src="https://github-readme-stats.vercel.app/api?username=charles-bucher&show_icons=true&theme=default&hide_border=true&count_private=true" alt="Charles's GitHub Stats"/>
</a>

<a href="https://github.com/charles-bucher">
  <img height="180em" src="https://github-readme-stats.vercel.app/api/top-langs/?username=charles-bucher&layout=compact&hide_border=true&theme=default" alt="Top Languages"/>
</a>

</div>

---

## 🎯 My Story (The Real One)

I'm 40 years old, married with three kids, and I've been working as a delivery driver while teaching myself cloud engineering. I have a felony record from 2003 (clean since 2008), and I know that means I need to work twice as hard to prove myself.

**Why Cloud?**
- My family deserves better than paycheck-to-paycheck living
- I'm good at solving technical problems
- I love learning new technology
- Remote cloud roles offer stability and growth

**Why Trust Me?**
- ✅ Every screenshot in my repos is from MY AWS account
- ✅ I spent my own money learning ($20+/month on AWS)
- ✅ I worked on these projects after 10-hour delivery shifts
- ✅ I document everything professionally

**What I'm Not:**
- ❌ A senior engineer pretending to be entry-level
- ❌ Someone who just copied tutorials
- ❌ A paper cert chaser with no hands-on
- ❌ Someone who will give up when it gets hard

**What I Am:**
- ✅ Self-taught and proud of it
- ✅ Honest about my skill level (entry-level)
- ✅ Willing to start small and prove myself
- ✅ Ready to outwork anyone for this opportunity

---

## 💬 Let's Connect

I'm actively looking for **entry-level AWS Cloud Support, SysOps, or DevOps roles** (remote preferred).

**Best Ways to Reach Me:**

<div align="center">

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/charles-bucher-cloud)
[![Email](https://img.shields.io/badge/Email-Contact-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:charles.bucher.cloud@gmail.com)
[![Portfolio](https://img.shields.io/badge/Portfolio-Visit-success?style=for-the-badge)](https://charles-bucher.github.io)

</div>

**What I'm Open To:**
- Full-time W2 positions
- Contract work through staffing agencies
- Freelance AWS projects
- Remote opportunities (Florida-based)
- Hybrid roles in Tampa Bay area

**Salary Expectations:** $50k+ (realistic for entry-level, just need to break in)

---

## 📝 Quick Facts

```yaml
name: Charles Bucher
role: Self-Taught Cloud Engineer
location: Pinellas Park, Florida
status: Open to Work
focus: AWS Cloud Operations

skills:
  cloud: [AWS, Terraform, CloudFormation]
  scripting: [Python, Bash, PowerShell]
  tools: [Git, VS Code, Linux]
  soft_skills: [Documentation, Troubleshooting, Self-Learning]

currently_learning:
  - AWS Solutions Architect Associate
  - Advanced networking concepts
  - Container orchestration

ideal_role:
  - AWS Cloud Support Associate
  - Junior SysOps Administrator
  - Cloud Operations Engineer
  - Entry-level DevOps Engineer

fun_fact: "I debug AWS issues faster than I delivered packages"
```

---

## 🏆 Why Hire Me?

**What Makes Me Different:**

1. **Proof Over Promises** - All my repos have real AWS screenshots showing actual work
2. **Self-Starter** - Taught myself cloud while working 50+ hours/week
3. **Problem Solver** - Built entire labs by breaking things and fixing them
4. **Great Communicator** - Professional documentation in every project
5. **Hungry** - This isn't a hobby, it's my family's future

**I'm Not Asking for a Senior Role:**
- I know I'm entry-level
- I'm willing to start at the bottom
- I'll take contract work to prove myself
- I just need someone to give me a shot

---

## 📌 Featured Repositories

<div align="center">

[![AWS Cloud Support Sim](https://github-readme-stats.vercel.app/api/pin/?username=charles-bucher&repo=AWS_Cloud_Support_Sim&theme=default&hide_border=true)](https://github.com/charles-bucher/AWS_Cloud_Support_Sim)
[![Error-Driven Lab](https://github-readme-stats.vercel.app/api/pin/?username=charles-bucher&repo=AWS_Error_Driven_Troubleshooting_Lab&theme=default&hide_border=true)](https://github.com/charles-bucher/AWS_Error_Driven_Troubleshooting_Lab)

[![CloudOps Lab](https://github-readme-stats.vercel.app/api/pin/?username=charles-bucher&repo=CloudOpsLab&theme=default&hide_border=true)](https://github.com/charles-bucher/CloudOpsLab)
[![Portfolio Site](https://github-readme-stats.vercel.app/api/pin/?username=charles-bucher&repo=charles-bucher.github.io&theme=default&hide_border=true)](https://github.com/charles-bucher/charles-bucher.github.io)

</div>

---

<div align="center">

**⭐ If you find my work interesting, please star my repositories!**

*Built with ☕ and determination by a delivery driver learning to code*

**Charles Bucher** | Self-Taught Cloud Engineer  
*"I can't fake experience, so I'm building proof instead"*

---

![Visitor Count](https://visitor-badge.laobi.icu/badge?page_id=charles-bucher.charles-bucher)
![Profile Views](https://komarev.com/ghpvc/?username=charles-bucher&color=brightgreen)

</div>