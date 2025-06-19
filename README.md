# CST8919 Lab 2: Building a Web App with Threat Detection using Azure Monitor and KQL


## Objective

In this lab, we will:
- Create a simple Demo Python Flask app
- Deploy a the app to Azure App Service
- Enable diagnostic logging with Azure Monitor
- Use Kusto Query Language (KQL) to analyze logs
- Create an alert rule to detect suspicious activity and send it to your email
---
## Scenario
As a cloud security engineer, you're tasked with securing a simple web application. The app logs login attempts. You must detect brute-force login behavior and configure an automatic alert when it occurs.

## Tasks

### Part 1: Deploy the Flask App to Azure
1. Develop a Python Flask app with a `/login` route that logs both successful and failed login attempts.
2. Deploy the app using **Azure Web App**.

### Part 2: Enable Monitoring
1. Create a **Log Analytics Workspace** in the same region.
2. In your Web App, go to **Monitoring > Diagnostic settings**:
   - Enable:
     - `AppServiceConsoleLogs`
     - `AppServiceHTTPLogs` (optional)
   - Send to the Log Analytics workspace.
3. Interact with the app to generate logs (e.g., failed `/login` attempts).


You must test your app using a .http file (compatible with VS Code + REST Client) and include that file in your GitHub repo as test-app.http.

![image](https://github.com/user-attachments/assets/b2ed0b06-86a4-45b6-ba32-ba8f7ca50802)

![image](https://github.com/user-attachments/assets/66b8ecdd-ce09-4c90-bad6-a519c19cfda0)



### Part 3: Query Logs with KQL
1. Create a KQL query to find failed login attempts.
2. Test it

### Part 4: Create an Alert Rule
1. Go to Azure Monitor > Alerts > + Create > Alert Rule.
2. Scope: Select your Log Analytics Workspace.
3. Condition: Use the query you created in the last step.
4. Set:
    - Measure: Table rows
    - Threshold: Greater than 5
    - Aggregation granularity: 5 minutes
    - Frequency of evaluation: 1 minute
    - Add an Action Group to send an email notification.
    - Name the rule and set Severity (2 or 3).
    - Save the alert.
  
    - ![image](https://github.com/user-attachments/assets/ba114217-f918-4a76-b3b3-a140b6ebb129)


## Submission
### GitHub Repository
- Initialize a Git repository for your project.
- Make **frequent commits** with meaningful commit messages.
- Push your code to a **public GitHub repository**.
- Include  **YouTube demo link in the README.md**.

Include a `README.md` with:
  - Briefly describe what you learned during this lab, challenges you faced, and how you’d improve the detection logic in a real-world scenario.
  - Your KQL query with explanation
``` kql
    AppServiceConsoleLogs
| where TimeGenerated > ago(5m)
| where ResultDescription has "Failed login attempt"

```
## Create Alert Rule:

```
Signal Type: Custom log search

Query: Used the KQL from Part 3

Evaluation settings:

Aggregation: Count of table rows

Threshold: > 5 failed attempts

Granularity: 5 minutes

Frequency: 1 minute

Action Group: sendfailedloginalert

Type: Email (to chha0038@algonquinlive.com)

Tested: Manual test email received

Severity: Set to 0 – Critical

Alert Rule Name: failedalertrule

```

Scope: Set correctly to flaskapplogs (Log Analytics Workspace)

## Challenges Faced
- URL Not Found (404) Errors

App Service didn't properly serve the /login endpoint after deployment.

Cause: Incomplete deployment, route mismatch, or inactive app.py.

- Log Analytics Delay / No Logs

Queries didn’t return results even though logging code was present.

Cause: Time range mismatch, improper message filters, or logs not being streamed.

- Deployment Conflict (409)

GitHub Actions failed to push code to App Service.

Cause: App may have been in a running state or not correctly reset before deployment.

- Email Alerts Not Received

Despite correct action group, email wasn't received.

Cause: Alert rule condition may never have evaluated to true.
-  Time-Sensitive Conditions

Filtering logs for ago(5m) missed real log entries.

Cause: Latency in log ingestion or misalignment with real-time tests.

 ## Real-World Improvement
In a real-world scenario:
- Log Full Request Metadata, Instead of logging only usernames and login status, I would also log: IP addresses, user-agent strings, and timestamps. This helps identify bots, crawlers, or targeted brute-force attacks from specific clients.
- Enable Rate Limiting and Lockout Logic, I would integrate a rate limiter (e.g., Flask-Limiter) to: Block excessive login attempts from the same IP (e.g., 5 attempts in 10 minutes). Temporarily lock the user account or throttle the client after repeated failures.

- Store Login Attempts in Persistent Storage, Rather than console-only logs: Save login attempts (username, IP, time, success/failure) to a secure database or blob storage. This enables historical audits, anomaly detection, and compliance reviews.



- **A link to a 5-minute YouTube video demo** showing:
  - App deployed
  - Log generation and inspection in Azure Monitor
  - KQL query usage
  - Alert configuration and triggering
  - 
  https://youtu.be/NrBCyVk6PJ0

You must test your app using a .http file (compatible with VS Code + REST Client) and include that file in your GitHub repo as test-app.http.


---


