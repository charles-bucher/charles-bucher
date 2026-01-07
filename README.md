# Charles Bucher

<div align="center">

![AWS Cloud Support](https://img.shields.io/badge/AWS-Cloud_Support_Engineer-FF9900?style=for-the-badge&logo=amazon-aws&logoColor=white)
![Entry Level](https://img.shields.io/badge/Level-Entry--Level_(Ready)-brightgreen?style=for-the-badge)
![Remote](https://img.shields.io/badge/Work-Remote_Ready-blue?style=for-the-badge)

[![Open to Work](https://img.shields.io/badge/🟢_OPEN_TO_WORK-AWS_Cloud_Support-brightgreen?style=for-the-badge)](https://linkedin.com/in/charles-bucher-cloud)

[![LinkedIn](https://img.shields.io/badge/LinkedIn-charles--bucher--cloud-0077B5?style=flat-square&logo=linkedin)](https://linkedin.com/in/charles-bucher-cloud)
[![Email](https://img.shields.io/badge/Email-quietopscb%40gmail.com-EA4335?style=flat-square&logo=gmail)](mailto:quietopscb@gmail.com)
[![Portfolio](https://img.shields.io/badge/Portfolio-View_Projects-4A90E2?style=flat-square&logo=google-chrome)](https://charles-bucher.github.io)

![Profile Views](https://komarev.com/ghpvc/?username=charles-bucher&color=blueviolet&style=flat-square&label=Views)

</div>

---

## 🎯 Target Role: AWS Cloud Support Associate

**Entry-level cloud support engineer seeking first opportunity in AWS customer support**

### Quick Facts
- 📍 **Location:** Florida (Remote preferred, Tampa Bay hybrid OK)
- 💰 **Target Salary:** $50k-$65k
- 📅 **Availability:** Immediate (2-week notice)
- 🕐 **Shift:** Flexible (can work evenings/weekends if needed)

---

## 💼 What I Can Do (Day One Skills)

### Core Cloud Support Skills

**Troubleshooting (My Strongest Skill)**
```
✅ Read CloudWatch Logs and identify error patterns
✅ Debug EC2 connectivity issues (Security Groups, NACLs, routing)
✅ Troubleshoot S3 permission errors (IAM vs bucket policies)
✅ Analyze Lambda timeout/permission issues
✅ Follow systematic troubleshooting methodology
✅ Document root cause and resolution steps
```

**AWS Services I Can Support**
| Service | Comfort Level | Can I Take Tickets? |
|---------|---------------|---------------------|
| **EC2** | ⭐⭐⭐⭐ Comfortable | ✅ Yes - connectivity, instance issues |
| **S3** | ⭐⭐⭐⭐ Comfortable | ✅ Yes - permissions, access errors |
| **VPC** | ⭐⭐⭐ Learning | ✅ Yes - basic networking, Security Groups |
| **CloudWatch** | ⭐⭐⭐⭐ Comfortable | ✅ Yes - log analysis, metrics |
| **IAM** | ⭐⭐⭐ Learning | ⚠️ With guidance - policy debugging |
| **Lambda** | ⭐⭐⭐ Learning | ⚠️ With guidance - timeouts, permissions |
| **RDS** | ⭐⭐ Beginner | ❌ Not yet - would need training |
| **ECS/EKS** | ⭐ Beginner | ❌ Not yet - would need training |

**Translation for Hiring Managers:**
- I can handle 70% of common EC2/S3/VPC/CloudWatch tickets independently
- I need guidance on complex IAM/Lambda issues (but learning fast)
- I'm honest about what I don't know yet (RDS, containers)

### Customer Service Skills (10+ Years)

**Why This Matters for Cloud Support:**
```
✅ Stay calm when customers are frustrated
✅ Ask clarifying questions before troubleshooting
✅ Explain technical issues in plain English
✅ Follow up until issue is fully resolved
✅ Document everything for next time
```

**Real-World Example:**
> Customer: "My website is down!"
> 
> Bad response: "Check your Security Groups and Route53 records"
> 
> My response: "I understand this is urgent. Let me check a few things. 
> First, can you confirm if you're seeing an error message or is the page just not loading?"
>
> [Investigation in CloudWatch Logs]
> 
> "I found the issue - your EC2 instance isn't receiving traffic because 
> of a Security Group setting. I can explain what happened and walk you 
> through the fix. This should take about 5 minutes."

**This is cloud support.** 50% technical, 50% communication.

---

## 🛠️ What I've Actually Built (Proof)

### Why These Projects Matter for Cloud Support

Most entry-level candidates say "I took a course."

I say "I intentionally broke AWS infrastructure and practiced fixing it like a real support engineer."

<table>
<tr>
<td width="50%" valign="top">

### [AWS Cloud Support Simulator](https://github.com/charles-bucher/AWS_Cloud_Support_Sim)

**What This Proves:**
- ✅ Can troubleshoot EC2 connectivity systematically
- ✅ Can debug S3 permission errors (IAM + bucket policies)
- ✅ Can analyze Lambda timeouts in CloudWatch
- ✅ Can respond to GuardDuty security alerts
- ✅ Can document solutions professionally

**Relevant for:** L1/L2 AWS Cloud Support tickets

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python)
![Terraform](https://img.shields.io/badge/Terraform-7B42BC?style=flat-square&logo=terraform)
![CloudWatch](https://img.shields.io/badge/CloudWatch-FF4F8B?style=flat-square&logo=amazon-cloudwatch)

</td>
<td width="50%" valign="top">

### [Error-Driven Troubleshooting Lab](https://github.com/charles-bucher/AWS_Error_Driven_Troubleshooting_Lab)

**What This Proves:**
- ✅ Can read CloudWatch Logs and find root cause
- ✅ Can create professional runbooks
- ✅ Can document incident timelines
- ✅ Can implement prevention strategies
- ✅ Can follow systematic investigation process

**Relevant for:** RCA documentation, runbook creation

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python)
![CloudWatch](https://img.shields.io/badge/CloudWatch-FF4F8B?style=flat-square&logo=amazon-cloudwatch)
![IAM](https://img.shields.io/badge/IAM-DD344C?style=flat-square&logo=amazon-aws)

</td>
</tr>
</table>

**Key Point:** These aren't tutorial projects. These are **troubleshooting practice labs** that directly translate to cloud support work.

### Projects Mapped to Real Support Scenarios

| My Project | Real Cloud Support Ticket |
|------------|---------------------------|
| EC2 connectivity scenario | "Can't SSH to my instance" |
| S3 access denied scenario | "Getting 403 errors on S3" |
| Lambda timeout scenario | "Lambda function keeps timing out" |
| IAM permission scenario | "Service can't access CloudWatch" |
| GuardDuty alerts scenario | "Got security alert, what do I do?" |

**I practiced the exact scenarios I'll support as a cloud support engineer.**

---

## 📊 My Stats (Honest Assessment)

### CloudWatch Log Analysis (My Best Skill)

**What I Can Do:**
```bash
# Search CloudWatch Logs for specific errors
aws logs filter-log-events \
  --log-group-name /aws/lambda/my-function \
  --filter-pattern "ERROR"

# Analyze patterns in Lambda execution
aws logs tail /aws/lambda/my-function --follow

# Use Logs Insights for complex queries
fields @timestamp, @message
| filter @message like /timeout/
| stats count() by bin(5m)
```

**Why This Matters:** 90% of cloud support tickets start with "check the logs."

### Troubleshooting Methodology

**My Systematic Approach:**
```
1. UNDERSTAND: What is the customer trying to do?
2. REPRODUCE: Can I reproduce the issue?
3. INVESTIGATE: What do CloudWatch Logs show?
4. DIAGNOSE: What's the root cause?
5. FIX: Implement solution
6. VERIFY: Confirm resolution with customer
7. DOCUMENT: Create runbook for next time
```

**This is exactly how AWS Cloud Support handles tickets.**

### Documentation Skills

**I've Created:**
- 📝 10+ professional runbooks (RB-001 through RB-010)
- 📊 13 incident reports with full RCA
- 📚 Detailed troubleshooting guides
- 🔧 Step-by-step resolution procedures
- ✅ Before/After comparison metrics

**Sample Runbook Structure:**
```markdown
## RB-001: EC2 SSH Connectivity Issues

### Problem Statement
Customer cannot SSH to EC2 instance

### Investigation Steps
1. Check instance state (running?)
2. Check Security Group rules (port 22 open?)
3. Check NACL rules (allow inbound/outbound?)
4. Check route table (route to IGW?)
5. Check VPC Flow Logs (traffic rejected?)

### Common Root Causes
- Security Group missing SSH rule (70%)
- Wrong key pair (15%)
- Instance stopped/terminated (10%)
- NACL blocking traffic (5%)

### Resolution
[Detailed fix steps with AWS CLI commands]

### Prevention
- Use Infrastructure as Code
- Document Security Group standards
- Enable VPC Flow Logs
```

**This is production-quality documentation.**

---

## 🎓 Certifications & Study

### Current Status

![AWS SAA](https://img.shields.io/badge/AWS_Solutions_Architect_Associate-Studying-informational?style=flat-square&logo=amazon-aws)
![AWS SysOps](https://img.shields.io/badge/AWS_SysOps_Administrator-Next_Goal-lightgrey?style=flat-square&logo=amazon-aws)

**Studying:** AWS Solutions Architect Associate
- Following Stephane Maarek Udemy course
- Doing Tutorials Dojo practice exams
- Building hands-on labs for every service
- **No exam scheduled yet** - learning thoroughly first

**Why I'm not certified yet:**
- I'm prioritizing hands-on skills over exam cramming
- Certifications don't prove you can troubleshoot
- I'd rather show real projects than a badge
- **But I will get certified** once I truly understand the material

**For Cloud Support roles:** AWS recommends Cloud Practitioner. I'm studying SAA because I want deeper knowledge.

---

## 💪 Why I'm Ready for Entry-Level Cloud Support

### What Entry-Level Means to Me

**I'm NOT claiming:**
- ❌ "5+ years experience" (I have months of hands-on)
- ❌ "Expert in cloud architecture" (I'm a beginner)
- ❌ "Can handle any AWS service" (I'm learning)

**I AM claiming:**
- ✅ I can troubleshoot common EC2/S3/VPC issues
- ✅ I can read CloudWatch Logs and find errors
- ✅ I can communicate with non-technical customers
- ✅ I can document solutions professionally
- ✅ I can learn quickly with guidance

**That's what entry-level means: coachable, eager, willing to learn.**

### Why Cloud Support Specifically?

**Perfect fit for my skills:**
```
Cloud Support Role Requires:
✅ Troubleshooting skills → I practice this daily
✅ Customer communication → 10+ years experience
✅ Documentation → All my repos show this
✅ Learning quickly → Self-taught everything here
✅ Following procedures → I create runbooks
✅ Working independently → Built this entire portfolio solo
```

**What I bring that other candidates don't:**

1. **Real Customer Service Background**
   - Most candidates have technical skills but no customer experience
   - I have 10+ years of handling frustrated customers
   - I can explain technical issues in plain English
   - I know how to de-escalate and follow up

2. **Systematic Troubleshooting**
   - I don't guess randomly
   - I follow a methodology (documented in my repos)
   - I check logs first, not last
   - I document root cause, not just symptoms

3. **Honest About Knowledge Gaps**
   - I admit when I don't know something
   - I ask good questions
   - I learn from mistakes
   - I won't BS customers or escalate unnecessarily

4. **Extreme Reliability**
   - I'm 40 with three kids—I take work seriously
   - I show up even when it's hard
   - I'm looking for a career, not just a job

---

## 🎯 What I'm Looking For

### Ideal Cloud Support Role

**Job Title:**
- AWS Cloud Support Associate (L1/L2)
- Technical Support Engineer - Cloud
- Cloud Operations Support Engineer
- Junior SysOps Administrator

**Responsibilities I Want:**
```
✅ Respond to customer tickets via chat/email/phone
✅ Troubleshoot AWS service issues (EC2, S3, VPC, Lambda)
✅ Analyze CloudWatch Logs to diagnose problems
✅ Document solutions in knowledge base/runbooks
✅ Escalate complex issues to L3/engineering
✅ Follow AWS troubleshooting best practices
✅ Learn from senior engineers and feedback
```

**What I DON'T Want:**
```
❌ Senior/lead positions (I'm not qualified)
❌ On-call rotation immediately (willing after training)
❌ Unrealistic salary expectations (I know entry-level pay)
❌ Roles requiring 3-5 years experience (I'm entry-level)
```

### Compensation & Logistics

**Target Salary:** $50,000 - $65,000

**Why this is realistic:**
- AWS Cloud Support Associate avg: $55k-$65k (Glassdoor)
- Entry-level SysOps: $50k-$60k
- Industry standard for entry-level cloud support
- Room to grow to $70k-$90k in 2-3 years

**Location:**
- ✅ **Remote preferred** (Florida-based)
- ✅ **Hybrid OK** if Tampa Bay area
- ✅ **Contract-to-hire** via staffing agencies OK
- ✅ **Flexible on shift** (can work evenings/weekends)

**Start Date:** Immediate (2-week notice to current employer)

---

## 📈 My 90-Day Plan (If You Hire Me)

### First 30 Days: Learn Your Systems

**Week 1-2: Onboarding**
```
✅ Complete all training modules
✅ Shadow senior support engineers
✅ Learn your ticket system and workflows
✅ Familiarize with common customer issues
✅ Study internal runbooks and documentation
```

**Week 3-4: Start Taking Tickets**
```
✅ Handle simple tickets with supervision
✅ Ask questions and learn from feedback
✅ Document new knowledge in personal notes
✅ Start contributing to team knowledge base
```

**Goal:** By day 30, handle 5-10 simple tickets independently per day

---

### Days 31-60: Build Competence

**Taking Tickets Independently**
```
✅ Handle EC2/S3/VPC tickets without constant supervision
✅ Properly escalate complex issues to L3
✅ Maintain 90%+ customer satisfaction
✅ Meet ticket SLA targets
✅ Start recognizing patterns in common issues
```

**Contributing to Team**
```
✅ Create 2-3 new runbooks for common issues
✅ Improve existing documentation
✅ Help newer hires if any join
✅ Participate in team knowledge sharing
```

**Goal:** By day 60, be a reliable team member handling 15-20 tickets/day

---

### Days 61-90: Prove My Value

**Performance Metrics**
```
✅ Handle full ticket load independently
✅ Become go-to person for specific services (EC2, S3)
✅ Reduce average resolution time through better troubleshooting
✅ Zero customer escalations due to poor service
✅ Contribute significantly to team knowledge base
```

**Going Above & Beyond**
```
✅ Identify gaps in documentation and fill them
✅ Create troubleshooting tools/scripts to help team
✅ Volunteer for less desirable shifts if needed
✅ Start studying for AWS certification on own time
```

**Goal:** By day 90, be one of your most reliable L1 engineers

---

## 💼 What I'll Give You

### In the First Year

**Month 1-3: Prove I Can Do the Job**
- Learn your systems faster than typical new hires
- Take ownership of tickets without handholding
- Ask smart questions that show I'm learning
- Show up every day, on time, ready to work

**Month 4-6: Become Reliable**
- Handle tickets independently with 90%+ CSAT
- Create runbooks for recurring issues
- Help train newer hires
- Take on increasingly complex tickets

**Month 7-9: Add Value Beyond Tickets**
- Identify process improvements
- Build tools to make team more efficient
- Become subject matter expert on specific services
- Reduce team's average resolution time

**Month 10-12: Prove You Made the Right Call**
- Be your best L1/L2 engineer
- Have deep knowledge of common issues
- Be the person customers ask for by name
- Make you glad you took a chance on me

### Long-Term (Years 2-3)

**I'm looking for growth, not quick jumps:**
- Stay minimum 18-24 months (prove loyalty)
- Earn AWS certifications (SysOps, then others)
- Move to L3 when ready (not rush it)
- Eventually mentor junior engineers
- Grow with your company

**Why you can trust this:**
- I'm 40 with three kids—I value stability
- I'm serious about building a career in cloud
- I understand this is a long-term investment
- I won't leave for a small pay bump elsewhere

---

## 📞 Let's Talk

<div align="center">

### Ready to Give Me a Shot?

**Here's what I'm asking:**
- Give me an entry-level cloud support role
- Train me on your systems (I'll learn fast)
- Judge me on my performance in 90 days

**Here's what you get:**
- Someone who shows up and works hard
- Someone with real customer service skills
- Someone with proven troubleshooting ability
- Someone who will stay and grow with you

[![Email Me](https://img.shields.io/badge/📧_Email-quietopscb%40gmail.com-EA4335?style=for-the-badge&logo=gmail)](mailto:quietopscb@gmail.com)

[![LinkedIn](https://img.shields.io/badge/💼_LinkedIn-Connect_on_LinkedIn-0077B5?style=for-the-badge&logo=linkedin)](https://linkedin.com/in/charles-bucher-cloud)

[![Portfolio](https://img.shields.io/badge/🌐_Portfolio-View_My_Projects-4A90E2?style=for-the-badge&logo=google-chrome)](https://charles-bucher.github.io)

</div>

---

## 📊 GitHub Activity

<div align="center">

![GitHub Stats](https://github-readme-stats.vercel.app/api?username=charles-bucher&show_icons=true&theme=react&hide_border=true&bg_color=0D1117&title_color=58A6FF&icon_color=1F6FEB)

![GitHub Streak](https://github-readme-streak-stats.herokuapp.com/?user=charles-bucher&theme=react&hide_border=true&background=0D1117&ring=58A6FF&fire=1F6FEB&currStreakLabel=58A6FF)

**397 contributions this year** • **All built through consistent daily practice**

![AWS Account](https://img.shields.io/badge/AWS_Account-722631436033-FF9900?style=flat-square&logo=amazon-aws) *← Real infrastructure, real work*

</div>

---

## 👋 About My Journey

### Career Transition to Cloud

I'm 40 years old, married with three kids (ages 12, 11, and 2), transitioning to cloud operations from non-technical work.

**Why I'm doing this:**
- I want a stable career with growth potential
- Cloud support roles value skills over degrees
- I can work remotely (important with three kids)
- AWS is hiring and growing
- I'm willing to start at entry-level and prove myself

**What makes me different:**
- I'm not a 22-year-old fresh from college
- I have 10+ years of real-world customer service
- I've handled pressure and difficult situations
- I understand accountability and follow-through
- I'm looking for a career, not just a job

**My approach:**
- Self-taught through hands-on AWS labs
- Practice troubleshooting by intentionally breaking things
- Document everything professionally
- Study systematically (currently AWS SAA)
- Build real projects, not just watch videos

**What I'm proving:**
- I can learn technical skills without a degree
- I can troubleshoot systematically
- I can communicate clearly
- I can work independently
- I'm serious about this career change

---

## ⭐ Final Thought

I know what you might be thinking:

*"40 years old, career changer, self-taught... why should I take a chance?"*

**Here's why:**

Look at my GitHub. Look at my projects. Look at my documentation.

This isn't someone who watched a few videos and called it learning.

This is someone who:
- ✅ Built real AWS infrastructure (account 722631436033)
- ✅ Created professional runbooks and RCAs
- ✅ Practiced systematic troubleshooting
- ✅ Documented everything like a real engineer
- ✅ Showed up every day and did the work

**I'm not asking you to take a risk on potential.**

**I'm asking you to look at proof.**

Give me 90 days to show you I'm one of your best entry-level hires.

---

<div align="center">

### ⭐ Star my repos if you find them useful

**"I can't fake experience — so I build it."**

**Charles Bucher** • Self-Taught Cloud Engineer • Open to Work

*Built with consistency, determination, and real AWS infrastructure*

</div>