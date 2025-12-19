# ☁️ Charles Bucher - Aspiring AWS Cloud Support Engineer

**Seeking Entry-Level Cloud Support | AWS Troubleshooting & Automation**

[![Portfolio](https://img.shields.io/badge/Portfolio-Live_Site-blue)](https://charles-bucher.github.io/)
[![Email](https://img.shields.io/badge/Email-Contact_Me-red)](mailto:quietopscb@gmail.com)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5)](https://linkedin.com/in/charles-bucher-cloud)

📍 Largo, FL | 🕒 Any Shift | 📧 <24hr Response | 📅 Available Immediately

---

## ⚡ What I Bring to Your Team

I'm an **entry-level candidate who learns by doing** - built these projects while working full-time and raising a family. 7 months intensive hands-on practice since May 2025.

✅ **3 troubleshooting scenarios** documented start-to-finish with root cause analysis  
✅ **4 hands-on projects** - CloudWatch monitoring, Lambda automation, cost tools  
✅ **500+ lines Python/Boto3** - built diagnostic tools to solve real problems  
✅ **298 GitHub commits** in 7 months - consistent builder, not a sprinter  
✅ **10+ years customer service** - logistics background, patient problem-solver  
✅ **Studying for AWS SAA** - targeting certification Q1 2026

**What makes me different:** I don't just watch tutorials - I break things, troubleshoot them, and document how I fixed them.

---

## 🔥 Portfolio Projects

### 1️⃣ [AWS Error-Driven Troubleshooting Lab](https://github.com/charles-bucher/AWS_Error_Driven_Troubleshooting_Lab) ⭐
**3 practice scenarios** - intentionally broke AWS services, learned how to fix them

| Issue | What I Learned | How I Fixed It |
|-------|----------------|----------------|
| EC2 unreachable | Security groups block by default | Added inbound rule for port 22 |
| VPC routing failed | Routes aren't automatic | Updated route table to point to IGW |
| S3 access denied | IAM is deny-by-default | Updated policy with s3:GetObject permission |

**What I Learned:** Systematic troubleshooting methodology - check logs first, isolate the problem, verify the fix  
**Tech Used:** EC2, VPC, CloudWatch, IAM, Security Groups

---

### 2️⃣ [Cloud Support Simulation](https://github.com/charles-bucher/cloud-support-simulation)
**Practice customer scenarios** - built tools to simulate real support tickets

- **Scenario #1:** IAM access denied troubleshooting with Python diagnostic tool
- **Scenario #2:** VPC connectivity debugging (network ACLs, security groups, routing)
- Python scripts (900+ lines) that check policies, test connectivity, suggest fixes
- Wrote customer communication templates (how to explain technical issues)
- Documented root cause analysis for each scenario

<details>
<summary>💻 View Tool Output Examples (Click to expand)</summary>

### IAM Troubleshooting Tool
```bash
$ python3 policy-validator.py --username john-doe --bucket my-bucket

🔍 Starting IAM diagnosis for user: john-doe

✅ User 'john-doe' exists
⚠️  Permission boundary detected: arn:aws:iam::123456789012:policy/DevBoundary
✅ Found 2 policies attached to user
❌ Action 's3:GetObject' on 'arn:aws:s3:::my-bucket/*' is DENIED

💡 RECOMMENDATIONS:
   1. Remove or update permission boundary if it's too restrictive
   2. Check for explicit DENY in bucket policy
```

### VPC Network Diagnostic Tool
```bash
$ python3 network-diagnostic.py --source i-abc123 --destination i-def456 --port 3306

🔍 Diagnosing connectivity: i-abc123 → i-def456:3306/tcp

✅ Instances found and running
⚠️  Security group sg-db456 does NOT allow inbound tcp/3306
❌ NACL acl-db789 DENIES inbound traffic on port 3306

❌ CONNECTIVITY BLOCKED
   2 blocking issue(s) found
```

</details>

**What I Learned:** How to translate technical errors into customer-friendly explanations  
**Tech Used:** Python, IAM, VPC, S3, GuardDuty, Security Groups, Network ACLs

---

### 3️⃣ [AWS CloudOps Suite](https://github.com/charles-bucher/AWS_Cloudops_Suite)
**Automated monitoring practice** - built alert pipeline using CloudWatch and Lambda

- Set up CloudWatch to track EC2 metrics (CPU, disk, memory)
- Wrote Lambda function that triggers when thresholds are breached
- Configured SNS to send email alerts
- Used Terraform to deploy everything as code

<details>
<summary>💻 View Architecture & Sample Output (Click to expand)</summary>

### Monitoring Pipeline
```
CloudWatch Metrics → CloudWatch Alarms → Lambda Function → SNS Topic → Email/SMS Alert
       ↓                    ↓                   ↓              ↓
   EC2 Instances      Threshold Breach    Process Alert   Notify Team
```

### Sample Alert
```json
{
  "AlarmName": "high-cpu-alert-web-server-01",
  "AlarmDescription": "CPU utilization exceeded 80%",
  "Timestamp": "2025-12-19T14:30:00.000Z",
  "InstanceId": "i-0123456789abcdef",
  "MetricValue": 87.5,
  "Threshold": 80.0,
  "Action": "Investigate high CPU usage"
}
```

</details>

**What I Learned:** Event-driven architecture, Lambda functions, Infrastructure as Code basics  
**Tech Used:** Lambda, CloudWatch, SNS, Terraform, Python

---

### 4️⃣ [AWS Cost Optimization Dashboard](https://github.com/charles-bucher/AWS_Cost_Optimization_Dashboard)
**Practice project** - built tool to find wasteful AWS spending

- Python script using Boto3 to query EC2, EBS, RDS, and Cost Explorer
- Finds stopped instances, unattached volumes, idle databases
- Generates report with potential savings
- Learned error handling, logging, and production code practices

<details>
<summary>📸 View Sample Output (Click to expand)</summary>

### Cost Optimization Report
```
☁️ AWS Cost Optimization Dashboard
Generated: 2025-12-19 14:45:00

💰 COST SAVINGS OPPORTUNITIES FOUND:

1. Stopped EC2 Instances (Still Paying for EBS)
   - i-abc123 (stopped 45 days) → Save $24/month
   - i-def456 (stopped 30 days) → Save $18/month
   - i-ghi789 (stopped 60 days) → Save $36/month

2. Unattached EBS Volumes
   - vol-123abc (100GB) → Save $10/month
   - vol-456def (50GB) → Save $5/month

3. Idle RDS Instances (Low CPU/Connections)
   - db-prod-old (2% CPU, 0 connections) → Save $180/month

4. Old EBS Snapshots (>90 days)
   - 15 snapshots → Save $45/month

TOTAL MONTHLY SAVINGS: $318/month ($3,816/year)

💡 RECOMMENDATIONS:
   1. Terminate or snapshot stopped instances
   2. Delete unattached EBS volumes after backup
   3. Consider RDS Aurora Serverless for variable workloads
   4. Implement snapshot lifecycle policies
```

</details>

**What I Learned:** Working with multiple AWS APIs, data analysis, presenting findings clearly  
**Tech Used:** Python, Boto3, Cost Explorer, CloudWatch

---

## 🛠️ Technical Skills (What I'm Learning & Practicing)

**AWS Services (Hands-On Practice):**
EC2 • VPC • IAM • S3 • Lambda • CloudWatch • CloudTrail • Security Groups • NACLs • Route53 • GuardDuty

*Still learning all of these - comfortable with basics, building knowledge through projects*

**Languages & Tools:**
Python • Boto3 • Bash • Git • Linux (Ubuntu) • Terraform • JSON • YAML • Markdown

**What I'm Getting Better At:**
- Basic incident troubleshooting & asking the right questions
- Reading CloudWatch logs & understanding error messages
- Debugging IAM permission issues (policies, roles, boundaries)
- Understanding VPC networking (routing, security groups, NACLs)
- Writing Python scripts with error handling
- Creating clear technical documentation
- Explaining technical problems in simple terms

**Certifications:**
🎯 Studying for AWS Solutions Architect Associate (no test scheduled yet, targeting early 2026)

---

## 💼 Why I'm Ready for Entry-Level Cloud Support

**What I Bring Technically:**
- 4 hands-on projects (not just tutorials - I built these from scratch)
- 3 documented troubleshooting scenarios showing my thought process
- Python tools that actually work and solve problems
- Understanding of AWS fundamentals (networking, IAM, compute, storage)
- Know how to read docs, search effectively, and ask good questions

**Transferable Skills from Customer Service:**
- 10+ years dealing with frustrated customers in logistics
- Can explain technical issues to people who aren't technical
- Patient when troubleshooting - I don't give up easily
- Good written communication (emails, documentation)
- Know when to escalate vs when to keep digging

**Work Style:**
- Available any shift (24/7, nights, weekends, rotating, on-call)
- Built all 4 projects while working full-time - I know how to hustle
- Comfortable learning on the job with guidance
- Okay with not knowing everything - I'll research and ask questions
- Proven self-starter - nobody made me do this, I wanted it

**Being Honest:**
- This is entry-level work - I'm not pretending to be senior
- I'll need training and mentorship, and I'll soak it up
- I learn fast when given clear direction
- I'm looking for a career, not a job - I want to grow with a company long-term

---

## 📊 GitHub Stats

![GitHub Stats](https://github-readme-stats.vercel.app/api?username=charles-bucher&show_icons=true&theme=github_dark&hide_border=true&include_all_commits=true&count_private=true)

**298 contributions** | 7 months learning | 4 practice projects | 500+ lines code written

---

## 📫 Contact

**Charles Bucher** | Seeking Entry-Level AWS Cloud Support Role

📧 [quietopscb@gmail.com](mailto:quietopscb@gmail.com) • 💼 [LinkedIn](https://linkedin.com/in/charles-bucher-cloud) • 🌐 [Portfolio](https://charles-bucher.github.io/) • 📄 [Indeed](https://profile.indeed.com/p/charlesb-x0xr5fx)

📍 Largo, Florida | ⏱️ Response: <24hrs | 📅 Available: Immediate

---

## 🚀 Hiring Manager Quick Links

[![View All Projects](https://img.shields.io/badge/📂-All_Projects-blue?style=for-the-badge)](https://github.com/charles-bucher?tab=repositories)
[![Schedule Interview](https://img.shields.io/badge/📅-Schedule_Interview-green?style=for-the-badge)](mailto:quietopscb@gmail.com?subject=Cloud%20Support%20Interview%20-%20Charles%20Bucher)
[![View Portfolio](https://img.shields.io/badge/🌐-Live_Portfolio-orange?style=for-the-badge)](https://charles-bucher.github.io/)

---

**Last Updated:** December 2025 • Learning Every Day • Building Real Projects • Ready for Entry-Level Work