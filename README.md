# Charles Bucher

**AWS Cloud Engineer | Infrastructure Automation Specialist**

Building cost-effective cloud solutions that prevent downtime & save money.  
🧠 AWS | Terraform | Python | Bash | DevOps Automation

---

## 📸 Project Screenshots

Below are visual examples from each of my key cloud engineering projects.  
Each folder inside `/screenshots` corresponds to one project.

---

### 🚀 Automated Multi-Service Deployment
Path: `screenshots/Automated-Multi-Service-screenshots/`

![Multi-Service Screenshot 1](screenshots/Automated-Multi-Service-screenshots/screenshot1.png)
![Multi-Service Screenshot 2](screenshots/Automated-Multi-Service-screenshots/screenshot2.png)
<!-- Add more screenshots as needed -->

---

### 📊 AWS Monitoring & Observability
Path: `screenshots/aws_monitoring_observability_screenshots/`

![Observability Screenshot 1](screenshots/aws_monitoring_observability_screenshots/screenshot1.png)
![Observability Screenshot 2](screenshots/aws_monitoring_observability_screenshots/screenshot2.png)

---

### 🏗️ Multi-Tier VPC Cloud Architecture
Path: `screenshots/aws_mult_itier_vpc_cloud_screenshots/`

![VPC Screenshot 1](screenshots/aws_mult_itier_vpc_cloud_screenshots/screenshot1.png)
![VPC Screenshot 2](screenshots/aws_mult_itier_vpc_cloud_screenshots/screenshot2.png)

---

### 🛡️ CloudOps GuardDuty Automation
Path: `screenshots/cloudOps-guardDuty-automation-screenshots/`

![GuardDuty Screenshot 1](screenshots/cloudOps-guardDuty-automation-screenshots/screenshot1.png)
![GuardDuty Screenshot 2](screenshots/cloudOps-guardDuty-automation-screenshots/screenshot2.png)

---

### 🧰 Cloud Support Troubleshooting
Path: `screenshots/Cloud-Support-Troubleshooting-screenshots/`

![Support Screenshot 1](screenshots/Cloud-Support-Troubleshooting-screenshots/screenshot1.png)
![Support Screenshot 2](screenshots/Cloud-Support-Troubleshooting-screenshots/screenshot2.png)

---

## ⚙️ How to Update Screenshots Automatically

You can generate all Markdown image links for every folder with this script:

```bash
#!/bin/bash
echo "# 📸 Project Screenshots" > SCREENSHOTS.md
for dir in screenshots/*; do
  [ -d "$dir" ] || continue
  dirname=$(basename "$dir")
  echo -e "\n## ${dirname}" >> SCREENSHOTS.md
  find "$dir" -type f \( -iname "*.png" -o -iname "*.jpg" -o -iname "*.jpeg" \) | while read img; do
    echo "![${img##*/}](${img})" >> SCREENSHOTS.md
  done
done
<!-- Auto-generated gallery -->
{% include_relative SCREENSHOTS.md %}
