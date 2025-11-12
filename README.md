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

### 📊 AWS Monitoring & Observability
Folder: `assets/aws_monitoring_observability_screenshots/`


---

### 📊 AWS Monitoring & Observability
Path: `assets/aws_monitoring_observability_assets/`

### 📊 AWS Monitoring & Observability
Folder: `assets/aws_monitoring_observability_screenshots/`

![01](assets/aws_monitoring_observability_screenshots/01.PNG)
![02](assets/aws_monitoring_observability_screenshots/02.png)
![03](assets/aws_monitoring_observability_screenshots/03.png)
![04](assets/aws_monitoring_observability_screenshots/04.png)
![05](assets/aws_monitoring_observability_screenshots/05.png)

---

### 🏗️ Multi-Tier VPC Cloud Architecture
Path: `assets/aws_mult_itier_vpc_cloud_assets/`

ls assets/aws_mult_itier_vpc_cloud_screenshots

---

### 🛡️ CloudOps GuardDuty Automation
Path: `assets/cloudOps-guardDuty-automation-assets/`

ls assets/cloudops-guardduty-automation-screenshots
---
### 🛡️ CloudOps GuardDuty Automation
Folder: `assets/cloudops-guardduty-automation-screenshots/`

![01](assets/cloudops-guardduty-automation-screenshots/01.png)  
![02](assets/cloudops-guardduty-automation-screenshots/02.png)
![03](assets/cloudops-guardduty-automation-screenshots/03.png)
![04](assets/cloudops-guardduty-automation-screenshots/04.png)
![05](assets/cloudops-guardduty-automation-screenshots/05.png)
![06](assets/cloudops-guardduty-automation-screenshots/06.png)
![07](assets/cloudops-guardduty-automation-screenshots/07.png)
![08](assets/cloudops-guardduty-automation-screenshots/08.png)
![09](assets/cloudops-guardduty-automation-screenshots/09.png)
![10](assets/cloudops-guardduty-automation-screenshots/10.png)
![11](assets/cloudops-guardduty-automation-screenshots/11.png)
![12](assets/cloudops-guardduty-automation-screenshots/12.png)


### 🧰 Cloud Support Troubleshooting
Path: `assets/Cloud-Support-Troubleshooting-assets/`

![04_install_dependencies_terminal](assets/Cloud_Support-Troubleshooting_Knowledge_screenshots/04_install_dependencies_terminal.PNG)
![05_config_editing](assets/Cloud_Support-Troubleshooting_Knowledge_screenshots/05_config_editing.PNG)
![06_run_project_terminal](assets/Cloud_Support-Troubleshooting_Knowledge_screenshots/06_run_project_terminal.PNG)
![08_app_running](assets/Cloud_Support-Troubleshooting_Knowledge_screenshots/08_app_running.PNG)


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
