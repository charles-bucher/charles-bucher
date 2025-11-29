graph LR
    START[Recruiter Visits Profile] --> READ[Read Headline]
    READ --> SCAN[Scan Skills Section]
    
    SCAN --> MATCH{Skills<br/>Match Role?}
    MATCH -->|No| LEAVE[Leave Profile]
    MATCH -->|Yes| REPOS[View Pinned Repos]
    
    REPOS --> CLICK1[Click Repo 1]
    REPOS --> CLICK2[Click Repo 2]
    REPOS --> CLICK3[Click Repo 3]
    
    CLICK1 --> README1[Read README]
    CLICK2 --> README2[Read README]
    CLICK3 --> README3[Read README]
    
    README1 --> TECH1{Technical<br/>Skills Valid?}
    README2 --> TECH2{Technical<br/>Skills Valid?}
    README3 --> TECH3{Technical<br/>Skills Valid?}
    
    TECH1 -->|Yes| IMPRESS[Building Impression]
    TECH2 -->|Yes| IMPRESS
    TECH3 -->|Yes| IMPRESS
    
    TECH1 -->|No| LEAVE
    TECH2 -->|No| LEAVE
    TECH3 -->|No| LEAVE
    
    IMPRESS --> CERTS[Check Certifications]
    CERTS --> STATS[View GitHub Stats]
    STATS --> CONTRIB[Review Contributions]
    
    CONTRIB --> DECIDE{Qualified?}
    DECIDE -->|No| LEAVE
    DECIDE -->|Yes| CONTACT[View Contact Info]
    
    CONTACT --> LINKEDIN[Visit LinkedIn]
    CONTACT --> EMAIL[Copy Email]
    CONTACT --> PORTFOLIO[Visit Portfolio]
    
    LINKEDIN --> VERIFY[Verify Experience]
    PORTFOLIO --> VERIFY
    
    VERIFY --> REACH[Reach Out for Interview]
    REACH --> END[Potential Job Opportunity]
    
    style START fill:#569A31
    style IMPRESS fill:#FF9900
    style DECIDE fill:#DD344C
    style REACH fill:#0A66C2
    style END fill:#232F3E