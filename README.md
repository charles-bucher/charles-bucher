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
Path: `assets/Automated-Multi-Service-assets/`

![Multi-Service Screenshot 1](assets/Automated-Multi-Service-assets/screenshot1.png)
![Multi-Service Screenshot 2](assets/Automated-Multi-Service-assets/screenshot2.png)
<!-- Add more screenshots as needed -->

---

### 📊 AWS Monitoring & Observability
Path: `assets/aws_monitoring_observability_assets/`

![Observability Screenshot 1](assets/aws_monitoring_observability_assets/screenshot1.png)
![Observability Screenshot 2](assets/aws_monitoring_observability_assets/screenshot2.png)

---

### 🏗️ Multi-Tier VPC Cloud Architecture
Path: `assets/aws_mult_itier_vpc_cloud_assets/`

![VPC Screenshot 1](assets/aws_mult_itier_vpc_cloud_assets/screenshot1.png)
![VPC Screenshot 2](assets/aws_mult_itier_vpc_cloud_assets/screenshot2.png)

---

### 🛡️ CloudOps GuardDuty Automation
Path: `assets/cloudOps-guardDuty-automation-assets/`

![GuardDuty Screenshot 1](assets/cloudOps-guardDuty-automation-assets/screenshot1.png)
![GuardDuty Screenshot 2](assets/cloudOps-guardDuty-automation-assets/screenshot2.png)

---

### 🧰 Cloud Support Troubleshooting
Path: `assets/Cloud-Support-Troubleshooting-assets/`

![Support Screenshot 1](assets/Cloud-Support-Troubleshooting-assets/screenshot1.png)
![Support Screenshot 2](assets/Cloud-Support-Troubleshooting-assets/screenshot2.png)

---

## ⚙️ How to Update Screenshots Automatically

You can generate all Markdown image links for every folder with this script:

```bash
#!/bin/bash
echo "# 📸 Project Screenshots" > SCREENSHOTS.md
for dir in assets/*; do
  [ -d "$dir" ] || continue
  dirname=$(basename "$dir")
  echo -e "\n## ${dirname}" >> SCREENSHOTS.md
  find "$dir" -type f \( -iname "*.png" -o -iname "*.jpg" -o -iname "*.jpeg" \) | while read img; do
    echo "![${img##*/}](${img})" >> SCREENSHOTS.md
  done
done
<!-- Auto-generated gallery -->
{% include_relative SCREENSHOTS.md %}
