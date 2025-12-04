# 👋 Charles Bucher

**Self-Taught Cloud Engineer | AWS | Python | Terraform**

📍 Pinellas Park, Florida  
✉️ quietopscb@gmail.com  
🔗 [GitHub](https://github.com/charles-bucher) • [LinkedIn](https://linkedin.com/in/charles-bucher-cloud)

---

## 👨‍💻 About Me

I'm building cloud infrastructure skills through hands-on AWS projects. Coming from a non-traditional background, I'm self-teaching cloud engineering, DevOps practices, and automation to transition into tech.

**What I'm Learning:**
- AWS core services (EC2, S3, VPC, CloudFormation, Lambda, GuardDuty)
- Infrastructure as Code with Terraform and CloudFormation
- Python automation and Boto3 SDK
- Cloud security and monitoring practices

**Current Focus:** Building portfolio projects that demonstrate practical AWS troubleshooting and automation skills for Cloud Support and DevOps roles.

---

## 🛠️ Technical Skills

**Cloud Platform:** AWS (EC2, S3, VPC, CloudFormation, CloudWatch, GuardDuty, Security Groups, IAM)

**Infrastructure as Code:** Terraform • CloudFormation

**Languages & Scripting:** Python • Bash • PowerShell

**Tools & Platforms:** Git • VS Code • AWS CLI • Linux • Windows Server

**Learning:** Docker • Kubernetes • CI/CD pipelines

---

## 📂 Featured Projects

### 🔧 [AWS_Cloud_Support_Sim](https://github.com/charles-bucher/AWS_Cloud_Support_Sim)

Hands-on AWS troubleshooting scenarios simulating cloud support workflows.

**What I Built:**
- EC2 network connectivity diagnostics
- Security group configuration and management
- CloudFormation infrastructure deployment
- GuardDuty security monitoring with Python automation
- CloudWatch metrics and alerting

**Tech Stack:** AWS (EC2, VPC, S3, CloudFormation, GuardDuty, CloudWatch) • Python • Boto3 • Git

<details>
<summary>🏗️ Architecture Diagram</summary>

```mermaid
graph TB
    subgraph "AWS Cloud Support Simulation"
        A[Customer Report] --> B[Troubleshooting Start]
        B --> C{Issue Type?}
        
        C -->|Network| D[VPC/Security Group Check]
        C -->|Security| E[GuardDuty Findings]
        C -->|Infrastructure| F[CloudFormation Stack]
        
        D --> G[EC2 Connectivity Tests]
        G --> H[Route Tables/IGW]
        H --> I[Resolution Applied]
        
        E --> J[Python Automation]
        J --> K[Alert Notifications]
        K --> I
        
        F --> L[Stack Deployment]
        L --> M[Resource Validation]
        M --> I
        
        I --> N[Documentation]
        N --> O[Screenshots Captured]
    end
    
    style A fill:#ff6b6b
    style I fill:#51cf66
    style O fill:#4dabf7
```

</details>

<details>
<summary>📸 Implementation Screenshots</summary>

#### EC2 Network Connectivity Testing
![Network Testing](https://raw.githubusercontent.com/charles-bucher/charles-bucher/main/screenshots/CloudSupport_01_EC2-Network-Connectivity-Tester.png)
*Validated VPC configuration, route tables, and Internet Gateway with ping diagnostics (59ms avg latency)*

---

#### Security Group Configuration
![Security Groups](https://raw.githubusercontent.com/charles-bucher/charles-bucher/main/screenshots/CloudSupport_02_EC2-Security-Group-Manager.png)
*Configured inbound rules for HTTPS (443) and SSH (22) with least-privilege access*

---

#### CloudFormation Stack Deployment
![CloudFormation](https://raw.githubusercontent.com/charles-bucher/charles-bucher/main/screenshots/CloudSupport_03_CloudFormation-Troubleshooting-Stack%20-.png)
*Deployed EC2 troubleshooting environment with CloudFormation (CREATE_COMPLETE status)*

---

#### Git Version Control Workflow
![Git Workflow](https://raw.githubusercontent.com/charles-bucher/charles-bucher/main/screenshots/CloudSupport_04_AWS-Cloud-Support-Portfolio.png)
*Established professional Git repository with Python virtual environment and modular structure*

---

#### GuardDuty Security Monitoring
![GuardDuty](https://raw.githubusercontent.com/charles-bucher/charles-bucher/main/screenshots/CloudSupport_05_Python-AWS-Project-Template%20.png)
*Automated security findings monitoring with Python and Boto3 SDK*

</details>

---

### 🔧 [AWS_CloudOps_Suite](https://github.com/charles-bucher/AWS_Cloudops_Suite)

Full CloudOps pipeline with monitoring, alerting, and Terraform provisioning.

**What I Built:**
- Automated incident monitoring and alerting
- Terraform infrastructure provisioning
- CloudWatch dashboards and metrics
- Security scanning with GuardDuty

**Tech Stack:** Terraform • AWS CloudWatch • Python • GuardDuty • S3

<details>
<summary>🏗️ CloudOps Workflow Diagram</summary>

```mermaid
graph LR
    subgraph "CloudOps Monitoring Pipeline"
        A[CloudWatch Metrics] --> B[Threshold Detection]
        B --> C{Alert Triggered?}
        
        C -->|Yes| D[SNS Notification]
        C -->|No| A
        
        D --> E[Lambda Function]
        E --> F[Auto-Remediation]
        
        G[GuardDuty] --> H[Security Findings]
        H --> I[Python Monitor Script]
        I --> J[S3 Findings Bucket]
        J --> K[Email Alert]
        
        L[Terraform] --> M[Infrastructure Provisioning]
        M --> N[EC2/VPC/S3]
        N --> A
        
        F --> O[Incident Logged]
        K --> O
        O --> P[CloudWatch Dashboard]
    end
    
    style D fill:#ffd43b
    style F fill:#51cf66
    style K fill:#ff6b6b
    style P fill:#4dabf7
```

</details>

<details>
<summary>📸 Implementation Screenshots</summary>

#### CloudWatch Monitoring Dashboard
![CloudWatch](https://raw.githubusercontent.com/charles-bucher/charles-bucher/main/screenshots/CloudOps_01_CloudWatch-Monitoring.png)
*Real-time CPU utilization monitoring with custom metrics and alarms*

---

#### GuardDuty Automated Findings Monitor
![GuardDuty](https://raw.githubusercontent.com/charles-bucher/charles-bucher/main/screenshots/CloudOps_02_GuardDuty-Automation.png)
*Python script continuously monitors GuardDuty for security findings with email alerts*

---

#### S3 Bucket Management
![S3 Buckets](https://raw.githubusercontent.com/charles-bucher/charles-bucher/main/screenshots/CloudOps_03_S3-Bucket-Management.png)
*Configured S3 buckets for Terraform state and GuardDuty findings storage*

---

#### Terraform Infrastructure State
![Terraform](https://raw.githubusercontent.com/charles-bucher/charles-bucher/main/screenshots/CloudOps_04_Terraform-State.png)
*Terraform v1.13.2 managing infrastructure state for reproducible deployments*

</details>

---

### 🔧 [Multi-Tier-App-Troubleshooting-Playground](https://github.com/charles-bucher/Multi-Tier-App-Troubleshooting-Playground)

Simulates a broken multi-tier application for troubleshooting practice.

**What I Built:**
- Frontend, backend, and database layer deployment
- Intentional misconfigurations for troubleshooting scenarios
- Step-by-step resolution documentation

**Tech Stack:** AWS (EC2, RDS, VPC) • CloudFormation • Python • MySQL

<details>
<summary>🏗️ Multi-Tier Architecture Diagram</summary>

```mermaid
graph TB
    subgraph "Multi-Tier Application Architecture"
        A[User Request] --> B[Load Balancer]
        B --> C[Frontend EC2]
        C --> D[Backend API EC2]
        D --> E[RDS MySQL Database]
        
        F[Troubleshooting Scenarios]
        F --> G[❌ Security Group Misconfiguration]
        F --> H[❌ Backend API Connection Failure]
        F --> I[❌ Database Credentials Error]
        
        G --> J[Fix: Update SG Rules]
        H --> K[Fix: Correct API Endpoint]
        I --> L[Fix: Update Connection String]
        
        J --> M[✅ Traffic Flows]
        K --> M
        L --> M
        
        M --> N[Application Working]
    end
    
    style C fill:#339af0
    style D fill:#339af0
    style E fill:#f08c00
    style G fill:#ff6b6b
    style H fill:#ff6b6b
    style I fill:#ff6b6b
    style N fill:#51cf66
```

</details>

<details>
<summary>📸 Implementation Screenshots</summary>

#### Multi-Tier Application Architecture
![Architecture](https://raw.githubusercontent.com/charles-bucher/charles-bucher/main/screenshots/MultiTier_01_Architecture.png)
*Three-tier application deployed across frontend, backend, and database layers*

---

#### Troubleshooting Workflow
![Troubleshooting](https://raw.githubusercontent.com/charles-bucher/charles-bucher/main/screenshots/MultiTier_02_Troubleshooting.png)
*Systematic approach to identifying root cause across application tiers*

---

#### Resolution Applied
![Resolution](https://raw.githubusercontent.com/charles-bucher/charles-bucher/main/screenshots/MultiTier_03_Resolution.png)
*Application restored to working state after fixing misconfigurations*

</details>

---

## 📊 GitHub Stats

![Charles's GitHub stats](https://github-readme-stats.vercel.app/api?username=charles-bucher&show_icons=true&theme=dark)

---

## 🎯 Current Goals

**Short-term (Next 3 months):**
- Complete AWS Solutions Architect Associate certification
- Build automated cost optimization tool
- Add CI/CD pipeline with GitHub Actions
- Contribute to open-source AWS projects

**Medium-term (6-12 months):**
- Land first Cloud Support Engineer or Junior DevOps role
- Build production-ready monitoring solutions
- Implement disaster recovery automation
- Expand portfolio with serverless projects (Lambda, API Gateway)

---

## 📚 Learning Journey

I'm documenting everything I learn through practical projects. Each repository includes:
- Working code with clear documentation
- Screenshots proving implementations work
- Architecture diagrams showing system design
- Setup instructions for reproducibility
- Real troubleshooting scenarios

**Current Study Plan:**
- AWS Solutions Architect Associate prep (Adrian Cantrill course)
- Python automation for AWS (Boto3 SDK)
- Terraform infrastructure patterns
- Cloud security best practices

---

## 🤝 Let's Connect

I'm actively looking for opportunities in:
- Cloud Support Engineering
- Junior DevOps Engineering  
- IT Infrastructure roles
- AWS technical support

**Open to:** Entry-level positions, apprenticeships, contract work, remote opportunities

📧 **Email:** quietopscb@gmail.com  
💼 **LinkedIn:** [charles-bucher-cloud](https://linkedin.com/in/charles-bucher-cloud)  
🐙 **GitHub:** [charles-bucher](https://github.com/charles-bucher)

---

## 📝 Recent Activity

- 🔨 Building GuardDuty automated security monitoring
- 📖 Studying for AWS Solutions Architect certification
- 🐍 Writing Python scripts for AWS automation
- 📚 Learning Terraform infrastructure patterns
- 💻 Documenting troubleshooting scenarios with screenshots

---

## 💡 Philosophy

**Learning by doing.** Every project is hands-on, reproducible, and documented. I focus on building practical solutions that demonstrate real-world cloud support skills. No fluff, just working code and clear documentation.

**Why I'm different:** I'm not coming from a traditional CS background. I'm bringing problem-solving skills, self-motivation, and the ability to learn quickly. Every commit represents something I've actually built and tested.

---

*"The best way to learn cloud engineering is to break things, fix them, and document the process."*

---

![Visitor Count](https://komarev.com/ghpvc/?username=charles-bucher&color=blue&style=flat-square)