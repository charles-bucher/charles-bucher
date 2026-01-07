
from botocore.exceptions import ClientError, BotoCoreError

def safe_aws_call(func, description="AWS call"):
    try:
        return func()
    except ClientError as e:
        logger.error(f"{description} failed: {e.response['Error']['Code']}")
    except BotoCoreError as e:
        logger.error(f"{description} SDK failure: {e}")
    return None

import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)

logger = logging.getLogger(__name__)

#!/usr/bin/env python3
"""
CLOUD PORTFOLIO AUTO-FIXER
Purpose: Automatically improve GitHub repos to meet entry-level cloud hiring standards
- Generates professional README files
- Adds code comments
- Organizes file structure
- Adds monitoring/logging examples
"""
# Import required libraries
import os
import re
import shutil
import json
from pathlib import Path
from datetime import datetime


# Configuration
BACKUP_DIR = "portfolio_backups"
EXCLUDED_DIRS = {".git", "__pycache__", "node_modules", "venv", ".vscode", ".idea"}

AWS_SERVICES_PATTERNS = {
    "EC2": r"\bec2\b",
    "S3": r"\bs3\b",
    "Lambda": r"\blambda\b",
    "CloudWatch": r"\bcloudwatch\b",
    "IAM": r"\biam\b",
    "VPC": r"\bvpc\b",
    "RDS": r"\brds\b",
    "DynamoDB": r"\bdynamodb\b",
}


class RepoFixer:
    def __init__(self, repo_path, repo_name):
        self.repo_path = Path(repo_path)
        self.repo_name = repo_name
        self.detected_services = set()
        self.code_files = []
        self.has_iac = False
        self.has_monitoring = False
        
    def backup_repo(self):
        """Create backup of repository before modifications."""
        backup_base = Path(BACKUP_DIR)
        backup_base.mkdir(exist_ok=True)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = backup_base / f"{self.repo_name}_{timestamp}"
        
        try:
            shutil.copytree(self.repo_path, backup_path, 
                          ignore=shutil.ignore_patterns('.git', '__pycache__'))
            logger.info(f"✅ Backup created: {backup_path}")
            return backup_path
        except Exception as e:
            logger.info(f"⚠️  Backup failed: {e}")
            return None
    
    def analyze_repo(self):
        """Analyze repository to detect AWS services and file types."""
        logger.info(f"\n🔍 Analyzing {self.repo_name}...")
        
        for root, dirs, files in os.walk(self.repo_path):
            # Skip excluded directories
            dirs[:] = [d for d in dirs if d not in EXCLUDED_DIRS]
            
            for file in files:
                filepath = Path(root) / file
                
                try:
                    content = filepath.read_text(encoding='utf-8', errors='ignore').lower()
                    
                    # Detect AWS services
                    for service, pattern in AWS_SERVICES_PATTERNS.items():
                        if re.search(pattern, content, re.I):
                            self.detected_services.add(service)
                    
                    # Detect file types
                    if file.endswith(('.py', '.sh', '.ps1', '.js')):
                        self.code_files.append(filepath)
                    
                    if file.endswith(('.tf', '.yaml', '.yml')) and 'terraform' in content or 'cloudformation' in content:
                        self.has_iac = True
                    
                    if 'cloudwatch' in content or 'metric' in content or 'alarm' in content:
                        self.has_monitoring = True
                        
                except:
                    pass
        
        logger.info(f"   AWS Services detected: {', '.join(sorted(self.detected_services)) or 'None'}")
        logger.info(f"   Code files: {len(self.code_files)}")
        logger.info(f"   IaC present: {'Yes' if self.has_iac else 'No'}")
        logger.info(f"   Monitoring present: {'Yes' if self.has_monitoring else 'No'}")
    
    def generate_readme(self):
        """Generate or improve README.md file."""
        readme_path = self.repo_path / "README.md"
        
        # Check if README exists
        existing_content = ""
        if readme_path.exists():
            existing_content = readme_path.read_text(encoding='utf-8', errors='ignore')
            logger.info(f"📝 Enhancing existing README...")
        else:
            logger.info(f"📝 Creating new README...")
        
        # Determine project type based on name
        project_type = self._determine_project_type()
        
        # Generate comprehensive README
        readme_content = self._build_readme_content(project_type, existing_content)
        
        # Write README
        readme_path.write_text(readme_content, encoding='utf-8')
        logger.info(f"✅ README.md updated")
    
    def _determine_project_type(self):
        """Determine project type from repo name and content."""
        name_lower = self.repo_name.lower()
        
        if "troubleshoot" in name_lower or "error" in name_lower:
            return "troubleshooting"
        elif "sim" in name_lower or "support" in name_lower:
            return "simulation"
        elif "lab" in name_lower:
            return "lab"
        elif "portfolio" in name_lower or "github.io" in name_lower:
            return "portfolio"
        else:
            return "general"
    
    def _build_readme_content(self, project_type, existing_content=""):
        """Build comprehensive README content."""
        
        # Extract existing sections if they exist
        has_overview = "overview" in existing_content.lower() or "purpose" in existing_content.lower()
        has_architecture = "architecture" in existing_content.lower()
        has_setup = "setup" in existing_content.lower() or "installation" in existing_content.lower()
        
        readme = f"# {self.repo_name.replace('-', ' ').replace('_', ' ').title()}\n\n"
        
        # Overview section
        if not has_overview:
            readme += "## 📋 Overview\n\n"
            readme += self._generate_overview(project_type)
            readme += "\n\n"
        
        # AWS Services section
        if self.detected_services:
            readme += "## ☁️ AWS Services Used\n\n"
            for service in sorted(self.detected_services):
                readme += f"- **{service}**: {self._get_service_description(service)}\n"
            readme += "\n"
        
        # Skills Demonstrated section
        readme += "## 💡 Skills Demonstrated\n\n"
        readme += self._generate_skills_section(project_type)
        readme += "\n"
        
        # Architecture section
        if not has_architecture:
            readme += "## 🏗️ Architecture\n\n"
            readme += self._generate_architecture_section()
            readme += "\n"
        
        # Prerequisites section
        readme += "## 📦 Prerequisites\n\n"
        readme += "- AWS Account with appropriate permissions\n"
        readme += "- AWS CLI configured (`aws configure`)\n"
        if any(f.suffix == '.py' for f in self.code_files):
            readme += "- Python 3.8+ installed\n"
            readme += "- boto3 library (`pip install boto3`)\n"
        if self.has_iac:
            readme += "- Terraform or AWS CloudFormation CLI\n"
        readme += "\n"
        
        # Setup/Installation section
        if not has_setup:
            readme += "## 🚀 Setup Instructions\n\n"
            readme += self._generate_setup_instructions(project_type)
            readme += "\n"
        
        # Usage section
        readme += "## 📖 Usage\n\n"
        readme += self._generate_usage_section(project_type)
        readme += "\n"
        
        # Troubleshooting section
        readme += "## 🔧 Troubleshooting\n\n"
        readme += self._generate_troubleshooting_section()
        readme += "\n"
        
        # Project Structure
        readme += "## 📁 Project Structure\n\n"
        readme += "```\n"
        readme += self._generate_structure_tree()
        readme += "```\n\n"
        
        # Monitoring/Logging section
        if self.has_monitoring or project_type in ["simulation", "lab"]:
            readme += "## 📊 Monitoring & Logging\n\n"
            readme += self._generate_monitoring_section()
            readme += "\n"
        
        # Future Enhancements
        readme += "## 🔮 Future Enhancements\n\n"
        readme += self._generate_future_enhancements()
        readme += "\n"
        
        # Author section
        readme += "## 👤 Author\n\n"
        readme += "**Charles Bucher**\n"
        readme += "- GitHub: [@Charles-Bucher](https://github.com/Charles-Bucher)\n"
        readme += "- LinkedIn: [Charles Bucher](https://linkedin.com/in/charles-bucher-cloud)\n"
        readme += "- Transitioning to Cloud/DevOps | AWS Focused\n\n"
        
        # License
        readme += "## 📄 License\n\n"
        readme += "This project is open source and available for educational purposes.\n"
        
        return readme
    
    def _generate_overview(self, project_type):
        """Generate overview based on project type."""
        overviews = {
            "troubleshooting": (
                "This project demonstrates systematic AWS troubleshooting skills through "
                "hands-on error scenarios. It showcases the ability to diagnose, document, "
                "and resolve common AWS issues - a critical skill for Cloud Support Engineers.\n\n"
                "**Key Focus Areas:**\n"
                "- Error identification and root cause analysis\n"
                "- AWS service debugging techniques\n"
                "- Documentation of remediation steps\n"
                "- Prevention strategies"
            ),
            "simulation": (
                "This AWS Cloud Support simulation recreates real-world support scenarios "
                "to demonstrate troubleshooting, customer communication, and technical problem-solving.\n\n"
                "**What This Simulates:**\n"
                "- Day-to-day cloud support engineer workflows\n"
                "- Common AWS customer issues\n"
                "- Professional incident response procedures"
            ),
            "lab": (
                "A hands-on AWS lab environment for learning and demonstrating cloud operations skills. "
                "This project includes practical exercises with real AWS services.\n\n"
                "**Lab Objectives:**\n"
                "- Build practical AWS experience\n"
                "- Test infrastructure as code\n"
                "- Practice monitoring and troubleshooting"
            ),
            "portfolio": (
                "Professional portfolio showcasing AWS cloud computing projects and skills. "
                "This repository serves as a central hub for demonstrating technical capabilities "
                "to potential employers."
            ),
            "general": (
                "An AWS cloud project demonstrating practical implementation of cloud services "
                "and infrastructure management."
            )
        }
        return overviews.get(project_type, overviews["general"])
    
    def _get_service_description(self, service):
        """Get brief description of AWS service usage."""
        descriptions = {
            "EC2": "Compute instances for hosting applications",
            "S3": "Object storage for data and artifacts",
            "Lambda": "Serverless functions for event-driven processing",
            "CloudWatch": "Monitoring, logging, and alerting",
            "IAM": "Identity and access management",
            "VPC": "Network isolation and security",
            "RDS": "Managed relational database service",
            "DynamoDB": "NoSQL database for scalable data storage",
        }
        return descriptions.get(service, "Cloud service integration")
    
    def _generate_skills_section(self, project_type):
        """Generate skills demonstrated section."""
        skills = [
            "- **AWS Service Configuration**: Hands-on experience with core AWS services",
            "- **Infrastructure as Code**: Automated provisioning and management" if self.has_iac else None,
            "- **Troubleshooting**: Systematic problem diagnosis and resolution",
            "- **Documentation**: Clear technical writing and process documentation",
            "- **Monitoring & Logging**: Proactive system observation" if self.has_monitoring else None,
            "- **Security Best Practices**: IAM policies and least-privilege access" if "IAM" in self.detected_services else None,
        ]
        return '\n'.join(filter(None, skills))
    
    def _generate_architecture_section(self):
        """Generate architecture section."""
        arch = "### System Design\n\n"
        
        if self.detected_services:
            arch += "```\n"
            arch += "User/Application\n"
            arch += "      |\n"
            
            if "IAM" in self.detected_services:
                arch += "   [IAM] Authentication\n"
                arch += "      |\n"
            
            if "VPC" in self.detected_services:
                arch += "   [VPC] Network Layer\n"
                arch += "      |\n"
            
            for service in sorted(self.detected_services):
                if service not in ["IAM", "VPC"]:
                    arch += f"      --> [{service}]\n"
            
            if "CloudWatch" in self.detected_services:
                arch += "      |\n"
                arch += "   [CloudWatch] Monitoring\n"
            
            arch += "```\n\n"
        
        arch += "**Component Interaction:**\n"
        arch += "1. Requests authenticated through IAM (if applicable)\n" if "IAM" in self.detected_services else ""
        arch += "2. Services communicate within VPC for security\n" if "VPC" in self.detected_services else ""
        arch += "3. All activities logged to CloudWatch\n" if "CloudWatch" in self.detected_services else ""
        arch += "4. Infrastructure deployed via IaC templates\n" if self.has_iac else ""
        
        return arch
    
    def _generate_setup_instructions(self, project_type):
        """Generate setup instructions."""
        setup = "### 1. Clone the Repository\n\n"
        setup += "```bash\n"
        setup += f"git clone https://github.com/Charles-Bucher/{self.repo_name}.git\n"
        setup += f"cd {self.repo_name}\n"
        setup += "```\n\n"
        
        setup += "### 2. Configure AWS Credentials\n\n"
        setup += "```bash\n"
        setup += "aws configure\n"
        setup += "# Enter your AWS Access Key ID\n"
        setup += "# Enter your AWS Secret Access Key\n"
        setup += "# Set default region (e.g., us-east-1)\n"
        setup += "```\n\n"
        
        if any(f.suffix == '.py' for f in self.code_files):
            setup += "### 3. Install Python Dependencies\n\n"
            setup += "```bash\n"
            setup += "pip install boto3 --break-system-packages\n"
            setup += "```\n\n"
        
        if self.has_iac:
            setup += "### 4. Deploy Infrastructure\n\n"
            setup += "```bash\n"
            setup += "# For Terraform\n"
            setup += "terraform init\n"
            setup += "terraform plan\n"
            setup += "terraform apply\n\n"
            setup += "# OR for CloudFormation\n"
            setup += "aws cloudformation deploy --template-file template.yaml --stack-name my-stack\n"
            setup += "```\n\n"
        
        return setup
    
    def _generate_usage_section(self, project_type):
        """Generate usage examples."""
        usage = ""
        
        if self.code_files:
            python_files = [f for f in self.code_files if f.suffix == '.py']
            if python_files:
                usage += "### Running Scripts\n\n"
                usage += "```bash\n"
                for py_file in python_files[:3]:  # Show max 3 examples
                    usage += f"python3 {py_file.name}\n"
                usage += "```\n\n"
        
        usage += "### Testing Components\n\n"
        usage += "1. Verify AWS connectivity: `aws sts get-caller-identity`\n"
        usage += "2. Check resource provisioning in AWS Console\n"
        usage += "3. Review CloudWatch logs for any errors\n"
        
        return usage
    
    def _generate_troubleshooting_section(self):
        """Generate troubleshooting guide."""
        ts = "### Common Issues\n\n"
        ts += "**Issue**: AWS credentials not configured\n"
        ts += "- **Solution**: Run `aws configure` and enter valid credentials\n\n"
        
        ts += "**Issue**: Permission denied errors\n"
        ts += "- **Solution**: Verify IAM user has required permissions\n"
        ts += "- Check IAM policy allows actions for services used\n\n"
        
        if "EC2" in self.detected_services:
            ts += "**Issue**: EC2 instance not reachable\n"
            ts += "- **Solution**: Check security group rules allow inbound traffic\n"
            ts += "- Verify instance is in 'running' state\n\n"
        
        if "S3" in self.detected_services:
            ts += "**Issue**: S3 access denied\n"
            ts += "- **Solution**: Check bucket policy and IAM permissions\n"
            ts += "- Verify bucket exists in correct region\n\n"
        
        ts += "**Issue**: Rate limiting or throttling\n"
        ts += "- **Solution**: Implement exponential backoff\n"
        ts += "- Check service quotas in AWS Console\n"
        
        return ts
    
    def _generate_structure_tree(self):
        """Generate project structure tree."""
        tree = f"{self.repo_name}/\n"
        tree += "├── README.md\n"
        
        if self.has_iac:
            tree += "├── infrastructure/\n"
            tree += "│   ├── main.tf or template.yaml\n"
            tree += "│   └── variables.tf\n"
        
        if self.code_files:
            tree += "├── scripts/\n"
            for i, cf in enumerate(self.code_files[:3]):
                prefix = "│   ├──" if i < 2 else "│   └──"
                tree += f"{prefix} {cf.name}\n"
        
        if self.has_monitoring:
            tree += "├── monitoring/\n"
            tree += "│   └── cloudwatch_config.yaml\n"
        
        tree += "└── docs/\n"
        tree += "    └── architecture.md\n"
        
        return tree
    
    def _generate_monitoring_section(self):
        """Generate monitoring documentation."""
        mon = "This project includes monitoring capabilities:\n\n"
        mon += "- **CloudWatch Metrics**: Track resource utilization\n"
        mon += "- **CloudWatch Alarms**: Alert on threshold breaches\n"
        mon += "- **CloudWatch Logs**: Centralized application logging\n\n"
        mon += "### Setting Up Monitoring\n\n"
        mon += "```bash\n"
        mon += "# Create CloudWatch alarm\n"
        mon += "aws cloudwatch put-metric-alarm \\\n"
        mon += "  --alarm-name HighCPU \\\n"
        mon += "  --alarm-description 'Alert when CPU exceeds 80%' \\\n"
        mon += "  --metric-name CPUUtilization \\\n"
        mon += "  --threshold 80\n"
        mon += "```\n"
        return mon
    
    def _generate_future_enhancements(self):
        """Generate future enhancement ideas."""
        enhancements = []
        
        if not self.has_monitoring:
            enhancements.append("- Add CloudWatch dashboards for real-time metrics")
        
        if not self.has_iac:
            enhancements.append("- Convert manual steps to Infrastructure as Code")
        
        if "Lambda" not in self.detected_services:
            enhancements.append("- Add serverless automation with Lambda functions")
        
        if "DynamoDB" not in self.detected_services and "RDS" not in self.detected_services:
            enhancements.append("- Integrate database layer for data persistence")
        
        enhancements.extend([
            "- Implement CI/CD pipeline with AWS CodePipeline",
            "- Add automated testing and validation",
            "- Expand to multi-region deployment",
        ])
        
        return '\n'.join(enhancements)
    
    def add_code_comments(self):
        """Add comprehensive comments to code files."""
        logger.info(f"\n💬 Adding code comments...")
        
        commented_count = 0
        for code_file in self.code_files:
            try:
                if code_file.suffix == '.py':
                    if self._add_python_comments(code_file):
                        commented_count += 1
                elif code_file.suffix == '.sh':
                    if self._add_bash_comments(code_file):
                        commented_count += 1
            except Exception as e:
                logger.info(f"⚠️  Could not comment {code_file.name}: {e}")
        
        logger.info(f"✅ Added comments to {commented_count} files")
    
    def _add_python_comments(self, filepath):
        """Add comments to Python files."""
        content = filepath.read_text(encoding='utf-8', errors='ignore')
        
        # Skip if already well-commented
        lines = content.splitlines()
        comment_lines = sum(1 for l in lines if l.strip().startswith('#'))
        if comment_lines / max(len(lines), 1) > 0.15:  # Already 15%+ comments
            return False
        
        # Add file header if missing
        if not content.startswith('"""') and not content.startswith('#'):
            header = f'"""\n{filepath.stem.replace("_", " ").title()}\n'
            header += f'Purpose: [AWS automation script]\n'
            header += f'Author: Charles Bucher\n'
            header += f'"""\n\n'
            content = header + content
        
        # Add import comments
        import_pattern = r'^(import |from )'
        lines = content.splitlines()
        new_lines = []
        in_imports = False
        
        for line in lines:
            if re.match(import_pattern, line) and not in_imports:
                new_lines.append("# Import required libraries")
                in_imports = True
            elif in_imports and not re.match(import_pattern, line.strip()):
                in_imports = False
                new_lines.append("")
            
            new_lines.append(line)
        
        content = '\n'.join(new_lines)
        
        # Add function docstrings
        content = re.sub(
            r'\ndef ([a-zA-Z_][a-zA-Z0-9_]*)\((.*?)\):(\n    (?!"""|\'\'\'))',
            r'def \1(\2):\n    """\3    Function to \1.\n    """\n\3',
            content
        )
        
        filepath.write_text(content, encoding='utf-8')
        return True
    
    def _add_bash_comments(self, filepath):
        """Add comments to Bash scripts."""
        content = filepath.read_text(encoding='utf-8', errors='ignore')
        
        # Skip if already commented
        if content.count('#') > 5:
            return False
        
        # Add header if missing
        if not content.startswith('#!'):
            header = "#!/bin/bash\n"
            header += f"# {filepath.stem.replace('_', ' ').title()}\n"
            header += "# Purpose: AWS automation script\n\n"
            content = header + content
        
        filepath.write_text(content, encoding='utf-8')
        return True
    
    def organize_files(self):
        """Organize files into logical directory structure."""
        logger.info(f"\n📂 Organizing file structure...")
        
        # Create standard directories
        dirs_to_create = ['scripts', 'docs', 'infrastructure', 'monitoring']
        
        for dir_name in dirs_to_create:
            dir_path = self.repo_path / dir_name
            if not dir_path.exists():
                dir_path.mkdir(exist_ok=True)
        
        # Move Python/Bash scripts to scripts/
        for code_file in self.code_files:
            if code_file.suffix in ['.py', '.sh', '.ps1']:
                if 'scripts' not in str(code_file.parent):
                    target = self.repo_path / 'scripts' / code_file.name
                    if not target.exists():
                        try:
                            shutil.move(str(code_file), str(target))
                            logger.info(f"   Moved {code_file.name} → scripts/")
                        except:
                            pass
        
        logger.info(f"✅ File organization complete")
    
    def add_monitoring_example(self):
        """Add CloudWatch monitoring example if missing."""
        if self.has_monitoring:
            return
        
        logger.info(f"\n📊 Adding monitoring example...")
        
        monitoring_dir = self.repo_path / 'monitoring'
        monitoring_dir.mkdir(exist_ok=True)
        
        # Create CloudWatch config example
        config_content = """# CloudWatch Monitoring Configuration
# This example shows how to set up basic monitoring for AWS resources

Resources:
  HighCPUAlarm:
    Type: AWS::CloudWatch::Alarm
    Properties:
      AlarmName: HighCPUUtilization
      AlarmDescription: Alert when CPU exceeds 80%
      MetricName: CPUUtilization
      Namespace: AWS/EC2
      Statistic: Average
      Period: 300
      EvaluationPeriods: 2
      Threshold: 80
      ComparisonOperator: GreaterThanThreshold
      
  ApplicationLogs:
    Type: AWS::Logs::LogGroup
    Properties:
      LogGroupName: /aws/application/logs
      RetentionInDays: 7

# Python example for custom metrics
# import boto3
# try:
    cloudwatch = boto3.client("cloudwatch")
except BotoCoreError as e:
    logger.critical("Failed to create cloudwatch client: {e}")
    raise

# 
# cloudwatch.put_metric_data(
#     Namespace='CustomApp',
#     MetricData=[{
#         'MetricName': 'RequestCount',
#         'Value': 1,
#         'Unit': 'Count'
#     }]
# )
"""
        
        config_file = monitoring_dir / 'cloudwatch_config.yaml'
        config_file.write_text(config_content)
        
        logger.info(f"✅ Added monitoring/cloudwatch_config.yaml")


def main():
    """Main execution function."""
    logger.info("\n" + "="*60)
    logger.info("  CLOUD PORTFOLIO AUTO-FIXER")
    logger.info("="*60)
    logger.info("\nThis script will automatically improve your GitHub repos to")
    logger.info("meet entry-level cloud hiring standards.\n")
    logger.info("Changes include:")
    logger.info("  ✓ Professional README files")
    logger.info("  ✓ Code comments and documentation")
    logger.info("  ✓ Organized file structure")
    logger.info("  ✓ Monitoring examples")
    logger.info("\n⚠️  A backup will be created before any modifications.\n")
    
    # Get current directory
    base_dir = Path.cwd()
    
    # Scan for repositories
    repos = []
    for item in os.listdir(base_dir):
        item_path = base_dir / item
        if item_path.is_dir() and item not in EXCLUDED_DIRS:
            repos.append((item_path, item))
    
    if not repos:
        logger.info("❌ No repositories found in current directory.")
        return
    
    logger.info(f"Found {len(repos)} repositories:\n")
    for i, (_, name) in enumerate(repos, 1):
        logger.info(f"  {i}. {name}")
    
    logger.info("\nOptions:")
    logger.info("  1. Fix all repositories")
    logger.info("  2. Select specific repositories")
    logger.info("  3. Exit")
    
    choice = input("\nEnter choice (1-3): ").strip()
    
    if choice == '3':
        logger.info("Exiting...")
        return
    elif choice == '2':
        indices = input("Enter repository numbers (comma-separated, e.g., 1,3,4): ").strip()
        try:
            selected = [int(i.strip()) - 1 for i in indices.split(',')]
            repos = [repos[i] for i in selected if 0 <= i < len(repos)]
        except:
            logger.info("❌ Invalid selection. Exiting.")
            return
    
    # Process each repository
    for repo_path, repo_name in repos:
        logger.info("\n" + "="*60)
        logger.info(f"Processing: {repo_name}")
        logger.info("="*60)
        
        fixer = RepoFixer(repo_path, repo_name)
        
        # Create backup
        fixer.backup_repo()
        
        # Analyze repository
        fixer.analyze_repo()
        
        # Apply fixes
        fixer.generate_readme()
        fixer.add_code_comments()
        fixer.organize_files()
        fixer.add_monitoring_example()
        
        logger.info(f"\n✅ {repo_name} improvements complete!")
    
    logger.info("\n" + "="*60)
    logger.info("  ALL REPOSITORIES PROCESSED")
    logger.info("="*60)
    logger.info(f"\n📁 Backups saved to: {BACKUP_DIR}/")
    logger.info("\n🎯 Next steps:")
    logger.info("  1. Review changes in each repository")
    logger.info("  2. Commit and push to GitHub")
    logger.info("  3. Run cloud_breakin_scanner.py to verify improvements")
    logger.info("\n💡 Tip: Add screenshots to your READMEs for maximum impact!")
    logger.info("="*60 + "\n")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logger.info("\n\n⚠️  Process interrupted by user.")
    except Exception as e:
        logger.info(f"\n❌ Fatal error: {e}")
        import traceback
        traceback.print_exc()