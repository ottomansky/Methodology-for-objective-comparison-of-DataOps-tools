# INTERVIEW TRANSCRIPT - RESPONDENT 02
**Date:** October 2025  
**Platform:** Video Conference  
**Duration:** 25 minutes  
**Language:** English  
## Participants
- **Interviewer:** Researcher (Master's thesis, University of Economics Prague)
- **Respondent 02:** Anonymized industry expert
## Respondent Demographics
**Role:** Analytics Engineer  
**Years of Experience:** 10 years (started as Data Engineer, moved closer to business)  
**Geographic Focus:** United States  
**Organization Scale:** Enterprise  
**Technology Stack:** Google Cloud Platform, BigQuery, Keboola, Python, DBT, Looker  
**Platform Experience:** Extensive Keboola experience, basic Databricks (POC evaluation), awareness of Microsoft Fabric
## INTERVIEW
### Introduction and Informed Consent
**Interviewer:** Hello. Thank you for taking the time for this interview. I'd like to discuss some questions for my thesis research. The interview will be recorded for transcription purposes, which will be part of my master's thesis. All data will be anonymized. Do you consent to recording and processing your responses for academic purposes?
**Respondent 02:** Yes, I consent.
**Interviewer:** Excellent. If you could introduce yourself - tell me about your role, how long you've been in it, and anything that might be helpful for context.
**Respondent 02:** Sure. I'm currently an analytics engineer. I started out as a data engineer. I've been in data for probably 10 years now and have been moving closer to the business side, getting away from the technical problems and into really making an impact as the analyst for my company. I mainly work at an enterprise scale.
**Interviewer:** What stacks are you using in your current role or have you used before?
**Respondent 02:** Google Cloud Platform, of course - that includes BigQuery for the data warehouse. I've used Keboola quite extensively. And then Python, DBT, Looker for the BI side of things. I'm well familiar with all of those.
**Interviewer:** Perfect. We'll jump into the main questions. The structure will be that I'll ask you for some specific things, and at the end of each segment I'll ask you to rate certain aspects from one to five, where five is critically important for you and one is nice to have but not that important. Does that make sense?
**Respondent 02:** Yes, understood.

### C0. Definition of Success in DataOps Implementation
**Interviewer:** First question: What is the definition of success for you in a DataOps implementation? What does successful implementation mean to you?
**Respondent 02:** Success is when operations teams and executives make daily decisions from trustworthy data without needing to ask the data team, "Is this number right?" That's the ultimate measure - when the business trusts the data enough to act on it independently.

### C1. Technical Efficiency and Reliability
**Interviewer:** What metrics do you usually capture regarding the speed and reliability of DataOps systems?
**Respondent 02:** That's a good question. For us, the most practical metrics are:
Pipeline completion time - end to end from source refresh to BI availability. 
The number of failed runs per week is something we watch very closely. We aim for less than 2% failure rate. 
Data freshness lag - the time between when an event occurs and when it's actually available in reporting. That's important to make sure we're not working with stale numbers.
In practice, I care more about whether the morning revenue report loaded before 9 AM than abstract throughput numbers. There are typical bottlenecks like rate limits of our APIs, incremental logic failures, and similar issues.
**Interviewer:** How do you measure and address these bottlenecks?
**Respondent 02:** For Keboola specifically, we use built-in retry logic and incremental loads in the configurations. We cache slow APIs and break big transformations into smaller, more maintainable and testable pieces.
**Interviewer:** Now for the rating part. I need you to rate from one to five where five is critically important and one is nice to have. First: how important is speed, low latency?
**Respondent 02:** Four out of five.
**Interviewer:** Stability, uptime.
**Respondent 02:** Five out of five.
**Interviewer:** Scalability.
**Respondent 02:** Three out of five.
**Interviewer:** And observability.
**Respondent 02:** Five out of five.

### C2. Data Quality and Governance
**Interviewer:** What do you consider the minimum built-in quality and lineage features for a platform to pass an audit or compliance review?
**Respondent 02:** Column-level lineage is absolutely part of the minimum - showing from source through transformations all the way to consumption. 
Another minimum is documented business logic associated with all of the calculated metrics that we have. 
Data freshness indicators that are visible to our end users.
And access logs showing who has viewed what sensitive data.
**Interviewer:** I don't have follow-up questions on this, so we can move to the ratings. First: data lineage, how important is it to you?
**Respondent 02:** Four out of five.
**Interviewer:** Quality tests.
**Respondent 02:** Five out of five.
**Interviewer:** Access control.
**Respondent 02:** Three out of five.
**Interviewer:** And metadata catalog or discoverability.
**Respondent 02:** Four out of five.

### C3. Automation, Versioning, and CI/CD
**Interviewer:** What does the perfect state of CI/CD for data look like? Branches, environments, rollbacks - anything you can think of.
**Respondent 02:** Absolutely. First is git-backed configurations. Everything in git - all the transformations, all of our components. That makes it easy to roll things back and monitor how things have changed over time.
We definitely care about dev, staging, and prod environments that we can use with automatic promotions between them. Being able to quickly promote those things with reviews in between, making rollbacks as seamless as possible when an incident arises.
Automated testing of our transformations on synthetic data is really important for this full automated promotion and CI/CD. That means data diffs on top of everything, so that we know how the data itself and the numbers are changing, not just the code.
**Interviewer:** Have you ever used rollback on versions of your configurations or anything in the data pipelines?
**Respondent 02:** Yes, absolutely. Being able to know how those rollbacks actually affected the numbers over time and making sure that we don't lose anything in the meantime - that's really important.
**Interviewer:** Rating. First is git integration.
**Respondent 02:** Four out of five.
**Interviewer:** API or CLI.
**Respondent 02:** Five out of five.
**Interviewer:** Automated tests.
**Respondent 02:** Four out of five.
**Interviewer:** And deterministic execution.
**Respondent 02:** Five out of five.

### C4. User Experience and Team Collaboration
**Interviewer:** Where do you see the value of no-code versus pro-code approaches and how do they affect team productivity?
**Respondent 02:** No-code wins when it comes to rapid prototyping of simple ETL for new data sources, empowering business analysts to build basic reports without waiting for engineering, and especially reducing the maintenance burden of all of these things.
One example I can give: our operations manager building their own occupancy dashboard for our locations freed up my time very significantly.
Pro-code wins when the business logic is complex or especially when there's something like forecasting involved where you really need to be able to use Python packages and things like that. It makes reusability much easier when you're using code instead of no-code. Version control and all of those automated testings become easier when you're using code. And typically we see better performance when we're using code versus no-code.
**Interviewer:** Do you prefer hybrid or purely one approach for working with data?
**Respondent 02:** Hybrid is best. Start visual for exploration, graduate to code for production. The platform should support both and make transitions easy.
**Interviewer:** Rating. How important is ease of learning?
**Respondent 02:** Four out of five. The team's small, so we can't afford them to waste time just learning how to get set up.
**Interviewer:** Documentation.
**Respondent 02:** Same - four out of five. It's critical when we have a small team.
**Interviewer:** Debugging tools.
**Respondent 02:** Five out of five. 80% of my time is maintenance, not new development.
**Interviewer:** And artifact sharing.
**Respondent 02:** Three out of five. It's nice to have but definitely not essential for our size.

### C5. Business Impact and Costs
**Interviewer:** How do you assess the total cost of ownership in practice - license, compute, management, team skills, whatever?
**Respondent 02:** For TCO, license costs are straightforward - monthly platform fees. 
For compute costs, it's quite variable. Our BigQuery spend ranges 10x based on query optimization. 
Then there are the hidden costs that we're also taking into account. That's the learning curve time, the effort for integration, and the maintenance overhead. 
So we always ask ourselves: what's the opportunity cost? Could we deliver faster with a different stack? 
The real calculation we use: total monthly spend - platform plus compute plus the FTEs needed - versus business value, meaning better pricing decisions equal X in revenue, reduced manual work equals Y in savings.
**Interviewer:** You were talking about hidden costs. Can you elaborate on any unexpected costs you've encountered?
**Respondent 02:** The hidden costs we see most often relate to the learning curve when adopting new platforms, integration effort when connecting to existing systems, and ongoing maintenance overhead. Sometimes platforms require additional tools to complete the picture - for example, you might need to add a separate data catalog or lineage tool if it's not built into the platform.
**Interviewer:** Rating. How important is delivery speed to you?
**Respondent 02:** Five out of five.
**Interviewer:** Total cost of ownership.
**Respondent 02:** Four out of five. We're willing to pay more for productivity.
**Interviewer:** Vendor lock-in risk.
**Respondent 02:** Two out of five. It's not a concern for us.
**Interviewer:** Can you clarify - do you mean you're willing to stay with one vendor or that you're not scared of being locked in?
**Respondent 02:** We're not that scared. As long as our platform provides what we need, we have no interest in switching. And at the same time, we've found that in the past, switching has not been as much of a lock-in as we usually thought it would be at first.
**Interviewer:** And compliance readiness.
**Respondent 02:** Three out of five. It matters for financing and our investors, but it doesn't matter for our daily operations.

### C6. Comparative View (Keboola × Fabric × Databricks)
**Interviewer:** You mentioned working with Keboola, but do you also have experience with Fabric and Databricks?
**Respondent 02:** Yes. I have advanced experience with Keboola. With Databricks, I'd call it basic - I've evaluated it with proof of concepts to understand what that would look like. And with Fabric, it's more awareness. I've seen the webinars, listened to people use it and talk about it, but haven't been as hands-on with it.
**Interviewer:** Can you tell me strengths and weaknesses of all three platforms separately, going one by one?
**Respondent 02:** Sure.
**Keboola:**
Strength - complete orchestration out of the box. It's really good for heterogeneous sources - APIs, databases, flat files. It comes out on top with fast time to value for standard analytics use cases. The pricing is predictable, and their support team is amazing.
Limitations - it's less flexible for ML and data science workflows. We're occasionally fighting with abstraction layers when we need custom low-level control. And there's a much smaller community than the other two.
I wouldn't recommend it for heavy ML or data science workloads. It has no great real-time streaming capabilities either. That hasn't been a problem for us thus far, but it's something we continue to look into. And it's hard to optimize on a low level.
**Databricks:**
Really powerful for data science and ML workflows. Their notebook environment is the best I've ever seen. It has strong performance for large-scale transformations, and the Unity Catalog makes governance super straightforward.
Limitations - it has a much steeper learning curve. It requires much more infrastructure knowledge. The pricing to me is more complex, and it's really just overkill for straightforward ETL.
I wouldn't recommend that one for small teams who don't have the data engineering resources or if you're really just doing BI reporting use cases. It's not necessary.
**Microsoft Fabric:**
The strengths are that it's all unified in the same Microsoft ecosystem. That makes it really appealing for Power BI shops. I like the integrated SaaS approach - in that way it's similar to Keboola.
Limitations - I don't like the Microsoft stack that much, so the lock-in there makes it uncomfortable. There's a lot of uncertainty to me in the pricing model, and it's still very new, so in some ways unproven.
I wouldn't recommend it for organizations who have a presence on AWS or GCP or teams who want a best-of-breed approach.
**Interviewer:** Can you very briefly explain from your experience who each platform is ideal for - the ideal persona like data analyst or something?
**Respondent 02:** Keboola is more ideal for small teams who want to have an outsized impact - one or two people who kind of have to do everything. They have to be the engineer, the analyst, and everything in between.
Databricks is ideal for people who have stronger technical skills and experience.
And Fabric is great for typically the end BI analysts who just care about getting the numbers to their leadership.

### C7. Experimental Scenario and Objective Comparison
**Interviewer:** My thesis is about comparing the tools as objectively as possible. I understand now that it's not completely possible to do fully objectively, but there are also some things that can be measured - for example, TPC-H workloads and runtime or pricing. If you were in my place measuring these things objectively, what would you measure? Do you have some things that I can input into my thesis?
**Respondent 02:** Absolutely. I've thought about this quite deeply actually. What I'd measure comes into a few different categories.
First is **setup and configuration time**. I'd look at the time from when you create the account to when you first successfully have an end-to-end run. I'd also look at the number of clicks or lines of code required to do it, and then the dependency setup required - all the different connectors, libraries, everything else.
Then there's **runtime performance**. That's end-to-end pipeline execution time taking into account consistent data volumes. That's where you're totally right to call out something like TPC-H, which is an industry standard. Very importantly, the cost per run - what are the compute charges across the different platforms? And how efficiently can it be parallelized?
The other area I'd look at is **maintainability**. That means time to modify transformation logic, whether that's adding a column or changing an aggregation. I would look at the effort to add incremental loading. And I'd really look at the clarity of the error messages within the platform when something breaks.
Then there's **operational metrics**, which is the setup required for scheduling, monitoring, alerting, and the ease of setting up the dev, prod, and staging environments.

### C8. Anything Important I Missed?
**Interviewer:** Is there something I missed or didn't ask you about, or something you want to add to the interview from your side?
**Respondent 02:** Technical platform comparisons are good, but they miss the human factor. The best platform technically may fail if business users don't trust it or can't understand it.
I would consider: how comfortable are stakeholders with verifying the data correctness? What would happen if a key person left? What knowledge transfer actually can occur?
Ecosystem maturity is absolutely critical. That means the community size for troubleshooting, the third-party tool integrations, and the availability of talent on the market. If you're trying to hire somebody to do this, are you going to be able to get somebody to apply who actually knows the platform?
I would also be looking at the evolution of the platform and its roadmap. How quickly does it adopt new patterns like LLMs and things like that? And then what's the stability of it? What's the acquisition risk? What's the runway of that company?
For another specific thing, I would highly recommend validating this methodology by looking at one failure scenario at least - what happens when source API changes schema unexpectedly or when a transformation breaks? What's the recovery time and what's the debugging experience?

### C9. Calibration Exercise (100 Points)
**Interviewer:** The last phase is about a calibration exercise. If you imagine you have 100 points and you need to split them however you want between the five dimensions we were talking about - technical efficiency, data quality, CI/CD, user experience, and business impact - how would you split those 100 points based on their importance?
**Respondent 02:** Maybe evenly.
**Interviewer:** Really?
**Respondent 02:** Yeah. I think you can't discount any one thing. To get a really holistic view of the platform, they're all equally important.
**Interviewer:** So 20 points each across all five dimensions?
**Respondent 02:** Yes, exactly. Each dimension plays a critical role, and I don't think we can truly optimize for one at the expense of the others.
### Conclusion
**Interviewer:** Thank you. That's everything from my side. Thank you for your time and insights. I will send you the transcript for review and will reach out again after I prepare the methodology to discuss if it makes sense. Is that okay with you?
**Respondent 02:** Absolutely. I'll be more than happy to help you out any way that I can.
**Interviewer:** Thank you very much.
**Respondent 02:** Good luck with your research.
## SCALES AND CALIBRATION - SUMMARY
### Scales 1-5 (1 = nice to have, 5 = critically important)
**C1. Technical Efficiency:**
- Speed/Low Latency: 4
- Stability/Uptime: 5
- Scalability: 3
- Observability: 5
**C2. Data Quality and Governance:**
- Data Lineage: 4
- Quality Tests: 5
- Access Control (RBAC): 3
- Metadata Catalog: 4
**C3. CI/CD:**
- Git Integration: 4
- API/CLI: 5
- Automated Tests: 4
- Deterministic Execution: 5
**C4. UX and Collaboration:**
- Ease of Learning/Onboarding: 4
- Documentation: 4
- Debugging Tools: 5
- Artifact Sharing: 3
**C5. Business Impact:**
- Time to Value: 5
- Total Cost of Ownership: 4
- Vendor Lock-in Risk: 2
- Compliance Readiness: 3
### Calibration 100 Points (C9)
**Distribution of importance across 5 dimensions:**
- **Technical Efficiency:** 20 points
- **Data Quality:** 20 points
- **CI/CD:** 20 points
- **User Experience:** 20 points
- **Business Impact:** 20 points
*(Note: Respondent emphasized that all five dimensions are equally critical for a holistic platform evaluation and cannot be meaningfully prioritized over one another.)*
**END OF TRANSCRIPT**