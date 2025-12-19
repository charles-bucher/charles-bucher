# 🔧 How to Fix Broken Screenshot Links in Your README

## Problem
The collapsible screenshot sections have **placeholder paths** that don't exist yet. They won't show images until you add the actual screenshots to your repositories.

## Solution Options

### Option 1: Add Real Screenshots (RECOMMENDED)
This makes your README look professional and proves your projects work.

#### Steps:

**1. Take Screenshots**

For **AWS_Error_Driven_Troubleshooting_Lab**:
- `ec2-unreachable.png` - Screenshot of EC2 connection timeout error
- `vpc-routing.png` - Screenshot of VPC route table showing missing IGW route
- `s3-access-denied.png` - Screenshot of S3 access denied error in AWS console

For **cloud-support-simulation**:
- `architecture-diagram.png` - Simple flowchart of your support workflow
- OR delete the architecture image line if you don't have one

For **AWS_Cloudops_Suite**:
- `monitoring-pipeline.png` - CloudWatch dashboard or architecture diagram
- OR delete the architecture image line

**2. Create Screenshots Folder in Each Repo**
```bash
# In AWS_Error_Driven_Troubleshooting_Lab repo
mkdir screenshots
# Add your 3 screenshots here

# In cloud-support-simulation repo
mkdir docs
# Add architecture diagram here (if you have one)

# In AWS_Cloudops_Suite repo
mkdir architecture
# Add monitoring pipeline diagram here (if you have one)
```

**3. Upload to GitHub**
```bash
git add screenshots/
git commit -m "Add troubleshooting screenshots"
git push
```

**4. Screenshots Will Auto-Display**
Once uploaded to GitHub, the README will automatically show them because the paths are correct:
```
https://raw.githubusercontent.com/charles-bucher/REPO_NAME/main/screenshots/FILENAME.png
```

---

### Option 2: Remove Screenshot Sections (QUICK FIX)
If you don't have screenshots ready, remove the collapsible sections to avoid broken links.

Use this version instead:

```markdown
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

**IAM Troubleshooting Tool Output:**
```bash
🔍 Starting IAM diagnosis for user: john-doe

✅ User 'john-doe' exists
⚠️  Permission boundary detected
❌ Action 's3:GetObject' is DENIED

💡 RECOMMENDATIONS:
   1. Remove or update permission boundary
   2. Check for explicit DENY in bucket policy
```

**VPC Network Diagnostic Output:**
```bash
🔍 Diagnosing connectivity: i-abc123 → i-def456:3306/tcp

✅ Instances found and running
⚠️  Security group does NOT allow inbound tcp/3306
❌ NACL DENIES inbound traffic on port 3306

❌ CONNECTIVITY BLOCKED - 2 blocking issues found
```

**What I Learned:** How to translate technical errors into customer-friendly explanations  
**Tech Used:** Python, IAM, VPC, S3, GuardDuty, Security Groups, Network ACLs

---

### 3️⃣ [AWS CloudOps Suite](https://github.com/charles-bucher/AWS_Cloudops_Suite)
**Automated monitoring practice** - built alert pipeline using CloudWatch and Lambda

**Monitoring Flow:**
```
CloudWatch Metrics → Alarms → Lambda → SNS → Email Alert
```

**Sample Alert Output:**
```json
{
  "AlarmName": "high-cpu-alert-web-server-01",
  "MetricValue": 87.5,
  "Threshold": 80.0,
  "Action": "Investigate high CPU usage"
}
```

**What I Learned:** Event-driven architecture, Lambda functions, Infrastructure as Code basics  
**Tech Used:** Lambda, CloudWatch, SNS, Terraform, Python

---

### 4️⃣ [AWS Cost Optimization Dashboard](https://github.com/charles-bucher/AWS_Cost_Optimization_Dashboard)
**Practice project** - built tool to find wasteful AWS spending

**Sample Report Output:**
```
💰 COST SAVINGS OPPORTUNITIES FOUND:

1. Stopped EC2 Instances → Save $78/month
2. Unattached EBS Volumes → Save $15/month  
3. Idle RDS Instances → Save $180/month
4. Old EBS Snapshots → Save $45/month

TOTAL MONTHLY SAVINGS: $318/month ($3,816/year)
```

**What I Learned:** Working with multiple AWS APIs, data analysis, presenting findings clearly  
**Tech Used:** Python, Boto3, Cost Explorer, CloudWatch
```

---

## Recommended Approach

**For NOW (to fix immediately):**
1. Use **Option 2** - Remove the collapsible screenshot sections
2. The code output examples are still there and look professional
3. No broken image links

**For LATER (when you have time):**
1. Take actual screenshots from AWS console
2. Create simple architecture diagrams (use draw.io or PowerPoint)
3. Upload to your repos
4. Add back the collapsible sections

---

## Quick Screenshots You Can Take Right Now

**EC2 Unreachable:**
1. Launch EC2 instance
2. Don't add SSH rule to security group
3. Try to SSH → Screenshot the timeout error
4. Add rule → Screenshot it working

**VPC Routing:**
1. Create VPC and subnet
2. Don't add route to IGW
3. Screenshot route table showing only local route
4. Add IGW route → Screenshot working

**S3 Access Denied:**
1. Create S3 bucket
2. Try to access without permissions
3. Screenshot the 403 Forbidden error
4. Add permissions → Screenshot it working

---

## Which Should You Do?

**If you're applying THIS WEEK:**
→ Use Option 2 (remove screenshots, keep code output)

**If you have 2-3 hours:**
→ Take the 3 screenshots above and use Option 1

**If you have a full day:**
→ Take screenshots + create simple diagrams in PowerPoint

---

## Need Help Creating Diagrams?

Use these free tools:
- **Draw.io** (diagrams.net) - Free, easy
- **Canva** - Has AWS icon templates
- **PowerPoint** - Built-in shapes
- **Lucidchart** - Professional but has free tier

Or just use ASCII diagrams like the ones already in your README - they work great!

---

**Bottom Line:** Your README still looks professional without the screenshots. The code output examples are enough to prove your work. Add real screenshots later when you have time.