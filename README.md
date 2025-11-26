# 👋 Hi, I'm Charles Bucher

**Self-Taught AWS Cloud Support Engineer | 15 Years Operations Experience | Building Real-World Skills Through Hands-On Labs**

I spent 15 years managing high-volume operations, troubleshooting technical systems, and training teams. Now I'm transitioning to cloud support by building production-style AWS environments and documenting every failure, fix, and lesson learned.

📍 Pinellas Park, Florida | 📧 quietopscb@gmail.com | 🌐 [Portfolio](https://charles-bucher.github.io) | 🔗 [LinkedIn](https://www.linkedin.com/in/charles-bucher-cloud)

---

## 🛠️ Technical Skills

**AWS Services**  
EC2 • RDS • VPC • S3 • Lambda • CloudWatch • SNS • GuardDuty • IAM • Application Load Balancer

**Infrastructure & Automation**  
Terraform • CloudFormation • Python (Boto3, Flask) • Bash scripting • GitHub Actions

**Cloud Support Fundamentals**  
Troubleshooting multi-tier applications • Incident response workflows • CloudWatch log analysis • Security group debugging • IAM policy troubleshooting • Root cause analysis documentation • SLA-based escalation procedures

---

## 🎯 Certifications & Learning Path

**Current Focus:**  
📖 AWS Certified Cloud Practitioner — Exam scheduled December 2025

**Next Steps:**  
📅 AWS Solutions Architect Associate — Target Q1 2026  
📅 CompTIA A+ — Target Q2 2026

---

## 💻 Featured Projects: Real-World Cloud Support Scenarios

These projects simulate actual cloud support work. I built them to learn troubleshooting, incident response, and operational workflows—the same skills I'd use in a Cloud Support Engineer or NOC role.

---

### 🔍 Project 1: AWS Monitoring & Observability Lab

**[View Repository →](https://github.com/charles-bucher/aws_monitoring_observability)**

#### What This Simulates
A production monitoring system where CloudWatch detects performance issues, triggers alerts, and notifies the support team—exactly what happens in real NOC or cloud support environments.

#### What I Built
- **EC2 monitoring pipeline:** Tracks CPU, memory, disk, and network metrics in real-time
- **Automated alerting:** CloudWatch alarms trigger SNS notifications when thresholds are breached (CPU >80%, disk >90%)
- **Incident response workflow:** Documented step-by-step process from alert → diagnosis → resolution
- **Dashboard integration:** Connected CloudWatch metrics to basic monitoring dashboards

#### Technical Implementation
```
EC2 Instance → CloudWatch Metrics → Alarm Triggers → SNS Topic → Email/SMS Alert
```

**Technologies:** Python, AWS CloudWatch, SNS, EC2, Lambda, CloudWatch Logs  
**Key Learning:** Alarm configuration, metric analysis, notification workflows, log troubleshooting

#### Real Support Scenarios I Practiced
- **Scenario 1:** High CPU alert triggered → Investigated processes → Identified runaway script → Documented resolution
- **Scenario 2:** Disk space alert → Analyzed CloudWatch logs → Found large log files → Created cleanup automation
- **Scenario 3:** Network spike detected → Checked VPC flow logs → Identified traffic source → Updated security groups

---

### 🔐 Project 2: GuardDuty Security Automation

**[View Repository →](https://github.com/charles-bucher/cloudOps-guardDuty-automation)**

#### What This Simulates
Automated security monitoring where threats are detected, logged, and escalated without manual intervention—similar to how SOC and NOC teams handle security incidents.

#### What I Built
- **Infrastructure as Code:** Terraform deployment of complete GuardDuty + CloudWatch + Lambda stack
- **Automated threat detection:** GuardDuty findings automatically trigger CloudWatch Events
- **Incident tracking:** Lambda function creates GitHub issues with threat details, severity, and AWS resource info
- **CI/CD pipeline:** GitHub Actions automates infrastructure updates and testing

#### Technical Implementation
```
GuardDuty Finding → EventBridge Rule → Lambda Function → GitHub API → Issue Created → Notification Sent
```

**Technologies:** Terraform, AWS GuardDuty, EventBridge, Lambda (Python), GitHub Actions, CloudWatch  
**Key Learning:** Infrastructure as code, event-driven architecture, security automation, CI/CD workflows

#### Real Support Scenarios I Practiced
- **Scenario 1:** Simulated unauthorized API calls → GuardDuty detected → Automated ticket creation → Documented investigation
- **Scenario 2:** Suspicious network activity → Lambda parsed finding → Created issue with remediation steps
- **Scenario 3:** IAM credential exposure → Automated alert → Practiced incident escalation workflow

---

### ⚙️ Project 3: Multi-Tier Application Troubleshooting Lab

**[View Repository →](https://github.com/charles-bucher/Multi-Tier-App-Troubleshooting-Playground)**

#### What This Simulates
Real customer support tickets where cloud infrastructure breaks and you have to diagnose the problem, fix it, and document everything—exactly what Cloud Support Engineers do daily.

#### What I Built
- **Full-stack AWS application:** Web tier (EC2) → Application tier (EC2) → Database tier (RDS)
- **Complete networking:** VPC, public/private subnets, NAT gateway, security groups, Application Load Balancer
- **Intentional failure scenarios:** Pre-configured problems that break the app in realistic ways
- **Troubleshooting documentation:** Step-by-step diagnosis process for each scenario

#### Technical Implementation
```
ALB → EC2 Web Servers (Public Subnet) → EC2 App Servers (Private Subnet) → RDS MySQL (Private Subnet)
Monitored via CloudWatch | Deployed via CloudFormation | Version controlled in GitHub
```

**Technologies:** CloudFormation, EC2, RDS, VPC, Application Load Balancer, Route 53, IAM, CloudWatch  
**Key Learning:** Multi-tier architecture, networking fundamentals, security groups, database connectivity, load balancer configuration

#### Real Support Tickets I Created & Solved

**TICKET #001: "Website returns 502 Bad Gateway"**
- **Problem:** Application Load Balancer showing all targets unhealthy
- **Diagnosis:** Security group on app servers missing inbound rule from ALB
- **Resolution:** Updated security group sg-xxxxx to allow traffic from ALB security group
- **Time to Resolution:** 12 minutes
- [View full troubleshooting steps →](link)

**TICKET #002: "Can't SSH to EC2 instance"**
- **Problem:** Connection timeout when attempting SSH from customer's IP
- **Diagnosis:** Security group only allowing SSH from 10.0.0.0/8 (internal network)
- **Resolution:** Added inbound rule for customer's IP range 203.0.113.0/24
- **Time to Resolution:** 8 minutes
- [View full troubleshooting steps →](link)

**TICKET #003: "Application can't connect to database"**
- **Problem:** App servers returning database connection errors
- **Diagnosis:** RDS security group blocking traffic from app server subnet
- **Resolution:** Updated RDS security group to allow MySQL (3306) from app subnet CIDR
- **Time to Resolution:** 15 minutes
- [View full troubleshooting steps →](link)

**TICKET #004: "IAM Access Denied errors in CloudWatch Logs"**
- **Problem:** EC2 instance profile missing permissions to write logs
- **Diagnosis:** IAM role policy didn't include CloudWatch Logs permissions
- **Resolution:** Updated IAM policy with logs:PutLogEvents and logs:CreateLogStream
- **Time to Resolution:** 10 minutes
- [View full troubleshooting steps →](link)

---

### 📊 Project 4: NOC Monitoring Dashboard

**[View Repository →](https://github.com/charles-bucher/NOC-Toolkit-Automation)**

#### What This Simulates
A Network Operations Center monitoring dashboard that shows device health, uptime, and alerts—similar to what NOC technicians use to monitor infrastructure 24/7.

#### What I Built
- **Python Flask dashboard:** Real-time display of network device status
- **JSON API integration:** Pulls device data from simulated endpoints (uptime, health, response time)
- **Automated alerting:** Detects when devices go offline and triggers notifications
- **Status tracking:** Visual indicators for device health (online/offline/degraded)

#### Technical Implementation
```
Device Endpoints (JSON) → Python Polling Script → Flask Web App → Real-Time Dashboard Display
Alert Logic → Email/Slack Notification on Device Failure
```

**Technologies:** Python, Flask, JSON APIs, HTML/CSS, basic networking concepts  
**Key Learning:** Real-time monitoring, API integration, alert management, dashboard design, NOC workflows

#### What This Demonstrates for NOC Roles
- Monitoring multiple devices simultaneously
- Recognizing patterns in device failures
- Triaging alerts by severity
- Documenting incidents for escalation
- Understanding uptime/downtime tracking

---

## 🎯 Why I'm Making This Career Transition

### My Operations Background (15 Years)
For 15 years, I managed high-volume delivery operations where I:
- Troubleshot point-of-sale systems, online ordering platforms, and delivery integrations
- Maintained 99%+ operational uptime through systematic incident response
- Trained 40+ staff on technical systems and operational procedures
- Documented recurring issues and created resolution guides (reduced MTTR by 30%)
- Communicated technical problems to non-technical stakeholders during outages

### Why Cloud Support?
During COVID, I discovered AWS while automating personal projects. I realized cloud operations combined everything I loved about my operations work—troubleshooting under pressure, technical systems, helping people—but with modern cloud technology.

So I went all-in: nights after delivery shifts, weekends, every spare hour. I built AWS environments from scratch, broke them intentionally, fixed them, and documented everything. Not just tutorials—real production-style scenarios with actual troubleshooting workflows.

### What I Bring to Cloud Support Roles
✅ **Systematic troubleshooting:** 15 years of diagnosing technical issues under time pressure  
✅ **Customer communication:** Clear explanations of technical problems to frustrated customers  
✅ **Incident management:** Documented escalation procedures and SLA-based workflows  
✅ **Training experience:** Taught 40+ people technical systems and processes  
✅ **Operational mindset:** Understanding of uptime, monitoring, and proactive problem-solving  
✅ **Self-directed learning:** Built production-level AWS skills entirely through hands-on projects

### What I'm Looking For
Entry-level **Cloud Support Engineer**, **NOC Technician**, or **Technical Support Specialist** roles where I can apply operational experience + hands-on AWS skills.

**Location:** Remote preferred (Florida-based), open to hybrid in Tampa Bay area  
**Compensation:** Realistic entry-level expectations—I'm asking for a chance to prove I can do the work, not mid-level pay for entry-level experience

---

## 📈 My Learning Approach

I don't just watch tutorials. I build real systems, break them, and fix them.

**My Process:**
1. **Deploy** infrastructure using CloudFormation/Terraform
2. **Monitor** using CloudWatch, logs, and metrics
3. **Break** something intentionally (security group, IAM policy, network config)
4. **Troubleshoot** using AWS console, CLI, and logs
5. **Document** the entire process like a support ticket
6. **Automate** the fix so it doesn't happen again

This mirrors actual cloud support work: customer reports issue → you investigate → diagnose root cause → implement fix → document resolution → prevent recurrence.

---

## 📊 GitHub Activity

![Charles's GitHub Stats](https://github-readme-stats.vercel.app/api?username=charles-bucher&show_icons=true&theme=dark&hide_border=true)

![Top Languages](https://github-readme-stats.vercel.app/api/top-langs/?username=charles-bucher&layout=compact&theme=dark&hide_border=true)

---

## 💼 Open to Opportunities

**Full-Time Roles:** Cloud Support Engineer, NOC Technician, Technical Support Specialist, Help Desk  
**Contract/Freelance:** AWS infrastructure setup, troubleshooting, monitoring configuration  
**Internships:** Willing to prove myself through paid internship or contract-to-hire

---

## 📫 Let's Connect

💼 **LinkedIn:** [linkedin.com/in/charles-bucher-cloud](https://www.linkedin.com/in/charles-bucher-cloud)  
🌐 **Portfolio:** [charles-bucher.github.io](https://charles-bucher.github.io)  
📧 **Email:** quietopscb@gmail.com  
📍 **Location:** Pinellas Park, Florida (Tampa Bay Area)

---

## 🤝 What I Can Help With (Freelance/Contract)

If you need help with:
- AWS EC2 instance setup and configuration
- CloudWatch monitoring and alert setup
- Basic VPC and security group configuration
- S3 bucket setup and permissions
- RDS database deployment
- IAM policy troubleshooting
- Infrastructure documentation

I'm available for small projects at competitive entry-level rates. Let's talk.

---

**Note:** All projects in this portfolio are learning environments built on my personal AWS account. They demonstrate hands-on technical skills and cloud support workflows, not production business metrics. I'm honest about being self-taught and ready to prove these skills in a professional environment.