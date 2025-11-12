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

![00_before_cleanup](assets/Automated-Multi-Service-screenshots/00_before_cleanup.png)
![01_clone_success](assets/Automated-Multi-Service-screenshots/01_clone_success.png)
![02_venv_created](assets/Automated-Multi-Service-screenshots/02_venv_created.png)
![03_repo_files](assets/Automated-Multi-Service-screenshots/03_repo_files.png)
![04_packages_installed](assets/Automated-Multi-Service-screenshots/04_packages_installed.png)
![05_deploy_placeholder](assets/Automated-Multi-Service-screenshots/05_deploy_placeholder.png)
![06_config_placeholder](assets/Automated-Multi-Service-screenshots/06_config_placeholder.png)
![08_git_status](assets/Automated-Multi-Service-screenshots/08_git_status.png)
![09_teardown](assets/Automated-Multi-Service-screenshots/09_teardown.png)


---

### 📊 AWS Monitoring & Observability
Path: `assets/aws_monitoring_observability_assets/`

![01_Clone](assets/aws_monitoring_observability_screenshots/01_Clone.PNG)
![01_aws_config](assets/aws_monitoring_observability_screenshots/01_aws_config.png)
![02_clone](assets/aws_monitoring_observability_screenshots/02_clone.png)
![02_cloudwatch_alarm](assets/aws_monitoring_observability_screenshots/02_cloudwatch_alarm.PNG)
![03_tf_plan](assets/aws_monitoring_observability_screenshots/03_tf_plan.png)
![04_cloudwatch_alarms](assets/aws_monitoring_observability_screenshots/04_cloudwatch_alarms.PNG)
![05_terraform](assets/aws_monitoring_observability_screenshots/05_terraform.png)
![07_terraform_installed](assets/aws_monitoring_observability_screenshots/07_terraform_installed.PNG)
![08_terraform_made](assets/aws_monitoring_observability_screenshots/08_terraform_made.PNG)
![09_terraform_plan](assets/aws_monitoring_observability_screenshots/09_terraform_plan.PNG)

---

### 🏗️ Multi-Tier VPC Cloud Architecture
Path: `assets/aws_mult_itier_vpc_cloud_assets/`

ls assets/aws_mult_itier_vpc_cloud_screenshots

---

### 🛡️ CloudOps GuardDuty Automation
Path: `assets/cloudOps-guardDuty-automation-assets/`

ls assets/cloudops-guardduty-automation-screenshots
---

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
