# DevOps Module 1 Assignment

**Student:** Bhabotos Kumar  
**Module:** DevOps Module 1  
**Assignment:** Assignment 1  

---

# Part A: Theoretical Questions

## A1. What is DevOps Engineering?

DevOps Engineering is a technical discipline that combines software development, IT operations, automation, infrastructure, security, monitoring, and collaboration to deliver software and services faster and more reliably.

A DevOps Engineer works to automate and improve the software delivery lifecycle. This includes source code management, continuous integration, continuous delivery, infrastructure provisioning, application deployment, monitoring, logging, incident response, and system reliability.

The main goal of DevOps is not simply to deploy applications faster. It is to create a reliable and repeatable process where development and operations teams can work together effectively while maintaining system stability and security.

### Difference Between DevOps and Traditional Development and Operations

In a traditional organization, development and operations often work as separate teams.

The development team mainly focuses on:

- Writing application code
- Developing new features
- Fixing application bugs
- Testing software

The operations team mainly focuses on:

- Managing servers and infrastructure
- Deploying applications
- Monitoring systems
- Managing incidents
- Maintaining availability

This separation can create communication gaps and manual handoffs.

DevOps brings these responsibilities closer together through collaboration, automation, shared ownership, and continuous feedback.

For example, instead of a developer manually handing an application to an operations engineer for deployment, a DevOps process can use Git, CI/CD pipelines, automated testing, infrastructure as code, and automated deployment to move changes from source code to a production environment in a controlled and repeatable way.

Therefore, traditional roles often focus on individual responsibilities, while DevOps Engineering focuses on the complete software delivery lifecycle and improving collaboration, automation, reliability, and delivery speed.

---

## A2. How DevOps Fits into the Software Development Life Cycle

DevOps supports the entire Software Development Life Cycle (SDLC) rather than being limited to only the deployment phase. It introduces automation, collaboration, continuous feedback, monitoring, and reliability practices throughout the lifecycle.

DevOps adds significant value to the following SDLC phases:

### 1. Planning

DevOps encourages collaboration between development, operations, security, and other stakeholders during planning.

Operational requirements such as scalability, availability, monitoring, security, and deployment requirements can be considered early.

### 2. Development

Developers use version control systems such as Git to manage source code.

DevOps practices also encourage coding standards, peer review, automated testing, and integration of code changes into shared repositories.

### 3. Testing

Automated testing can be integrated into CI pipelines.

Whenever developers push changes, automated unit tests, integration tests, and other validation checks can run automatically.

This helps identify problems earlier.

### 4. Deployment

DevOps introduces Continuous Delivery and Continuous Deployment practices.

CI/CD pipelines can automatically build, test, package, and deploy applications to different environments.

### 5. Operations and Monitoring

After deployment, DevOps practices continue through monitoring, logging, alerting, incident response, and performance analysis.

Feedback from production systems can be used to improve future releases.

### Example

For example, when a developer pushes code to GitHub, a CI/CD pipeline can automatically build the application, run tests, create an artifact or container image, and deploy the application to a staging environment.

Monitoring tools can then detect application errors after deployment.

Therefore, DevOps connects different SDLC phases through automation and continuous feedback, helping organizations deliver software faster while maintaining reliability and quality.

---

## A3. What Values Does a DevOps Engineer Bring to an Organization?

A DevOps Engineer brings several important values to an organization. Four major values are automation, faster and reliable delivery, system reliability, and improved collaboration.

### 1. Automation

DevOps Engineers automate repetitive manual tasks such as application deployment, infrastructure provisioning, testing, backups, and monitoring.

For example, instead of manually deploying an application to a server after every code change, a CI/CD pipeline can automatically build, test, and deploy the application.

This reduces human error and saves time.

### 2. Faster and Reliable Software Delivery

DevOps practices help organizations release software more frequently while maintaining quality.

For example, automated testing and CI/CD pipelines can validate code changes before deployment.

This allows teams to deliver new features faster without depending on lengthy manual deployment processes.

### 3. Reliability and Stability

DevOps Engineers improve system reliability through monitoring, logging, alerting, health checks, backup strategies, automated recovery, and controlled deployment processes.

For example, if a production application becomes unavailable, monitoring can generate an alert immediately so the team can investigate and restore the service quickly.

### 4. Better Collaboration

DevOps promotes collaboration between development, operations, security, and other technical teams.

For example, developers can work with operations engineers to understand deployment requirements, infrastructure limitations, monitoring requirements, and production issues.

This reduces communication gaps and improves shared ownership.

Overall, a DevOps Engineer helps an organization reduce manual work, improve reliability, accelerate software delivery, and create better collaboration between technical teams.

---

## A4. Why Prior Software Engineering Experience Is Helpful for a DevOps Engineer

Prior Software Engineering experience is helpful because DevOps Engineers work closely with application code, development teams, testing processes, version control systems, and software delivery pipelines.

A person with Software Engineering experience usually understands concepts such as programming, application architecture, debugging, Git, testing, dependencies, APIs, and software development workflows.

This knowledge makes it easier to understand what happens before an application reaches the infrastructure and production environment.

For example, if a CI/CD pipeline fails during the build stage, a DevOps Engineer with software development knowledge can inspect the source code, dependency configuration, build commands, and test failures instead of treating the problem only as an infrastructure issue.

Software Engineering experience also helps DevOps Engineers communicate effectively with developers because they understand development challenges and terminology.

However, becoming a DevOps Engineer does not require being an expert software developer.

Strong fundamentals in programming, version control, Linux, networking, cloud platforms, automation, and troubleshooting are also important.

Therefore, prior Software Engineering experience provides a strong foundation for understanding applications and building reliable software delivery processes.

---

## A5. Importance of Networking Knowledge in DevOps

Networking knowledge is important for DevOps Engineers because applications, servers, containers, cloud services, databases, APIs, and monitoring systems communicate with each other over networks.

A DevOps Engineer should understand fundamental networking concepts such as IP addressing, DNS, ports, protocols, routing, HTTP/HTTPS, TCP/IP, and firewalls.

### DNS

DNS translates domain names into IP addresses.

For example, when a user accesses an application using a domain name, DNS helps determine the IP address of the server hosting the application.

### Ports

Ports identify specific network services running on a host.

Examples include:

- Port 22: SSH
- Port 80: HTTP
- Port 443: HTTPS
- Port 5000: Commonly used by Flask development applications

Understanding ports helps DevOps Engineers troubleshoot connectivity problems and firewall rules.

### Protocols

DevOps Engineers need to understand protocols such as TCP/IP, HTTP, HTTPS, SSH, DNS, and TLS.

For example, if an application works through HTTP but fails through HTTPS, the engineer may need to investigate TLS certificates, configuration, ports, reverse proxy settings, or firewall rules.

### IP Addressing

Understanding IPv4, IPv6, private addresses, public addresses, subnetting, and routing helps DevOps Engineers configure servers, cloud networks, containers, and network security.

### Example

Suppose an application server is running correctly, but users cannot access it.

A DevOps Engineer can troubleshoot the issue by checking DNS resolution, IP connectivity, listening ports, firewall rules, routing, and the application service itself.

Therefore, networking knowledge is essential because many application and infrastructure failures are related to network connectivity or configuration.

---

## A6. Essential Soft Skills for a DevOps Engineer

Technical knowledge alone is not enough for a successful DevOps Engineer.

DevOps work requires strong communication, collaboration, problem-solving, documentation, adaptability, and incident management skills.

### 1. Communication

DevOps Engineers frequently communicate with developers, network engineers, system administrators, security teams, managers, and other stakeholders.

During an incident, clear communication helps the team understand the impact, current status, actions being taken, and expected recovery time.

### 2. Collaboration

DevOps is based on shared responsibility.

Engineers need to work effectively with development, operations, security, and other teams.

Good collaboration helps teams solve problems faster and reduces the development-versus-operations mindset.

### 3. Problem-Solving

DevOps Engineers regularly investigate unexpected application, infrastructure, networking, and deployment problems.

A structured problem-solving approach helps engineers identify the actual root cause rather than making random changes.

### 4. Documentation

Good documentation helps teams understand system architecture, deployment procedures, troubleshooting steps, configurations, and incident history.

For example, a documented rollback procedure can help engineers restore a failed production deployment quickly.

### 5. Adaptability

DevOps environments change frequently.

New tools, cloud platforms, automation frameworks, security requirements, and deployment methods may be introduced.

An adaptable engineer can learn new technologies and adjust processes when requirements change.

### Example During an Incident

If a production application goes down, a DevOps Engineer needs to remain calm, communicate the incident status, collaborate with developers and infrastructure teams, investigate logs and monitoring data, and document the final resolution.

These soft skills help technical teams respond to incidents efficiently while reducing confusion and unnecessary delays.

---

## A7. Importance of Patience and Troubleshooting Mindset in DevOps

Patience and a structured troubleshooting mindset are extremely important for DevOps Engineers because production failures are often caused by multiple interacting factors.

A DevOps Engineer should avoid making random changes without understanding the problem.

Instead, the engineer should collect evidence, identify symptoms, form a hypothesis, test the hypothesis, and verify the result.

A useful troubleshooting process is:

1. Identify the problem and its impact.
2. Collect logs, metrics, alerts, and error messages.
3. Check recent changes or deployments.
4. Reproduce the problem when possible.
5. Form a hypothesis about the root cause.
6. Test the hypothesis using controlled changes.
7. Apply the appropriate fix or rollback.
8. Verify that the service has recovered.
9. Document the incident and root cause.
10. Implement preventive actions if required.

### Real-Life Example

Suppose a production application becomes unavailable immediately after a new deployment.

Instead of restarting servers repeatedly, a DevOps Engineer should first check monitoring alerts, application logs, deployment history, health checks, database connectivity, network connectivity, and recent configuration changes.

If the evidence indicates that the latest deployment caused the outage, the engineer can roll back to the previous stable version.

After service recovery, the team should perform a root cause analysis and improve automated testing or deployment controls to prevent the same issue from happening again.

Patience is important because troubleshooting under pressure can lead to incorrect assumptions and additional failures.

A calm, evidence-based approach helps restore services safely and creates long-term improvements.

---

# Part B: Scenario-Based Questions

## B1. Onboarding a New Student to GitHub and Cloud Platforms

If a new student joins a DevOps course but is unfamiliar with GitHub and cloud platforms, I would onboard the student gradually using a structured approach.

### Step 1: Explain the Basic Concepts

First, I would explain what Git, GitHub, repositories, branches, commits, and pull requests are.

I would also explain the basic concept of cloud computing and introduce common cloud services such as virtual machines, storage, networking, databases, and identity management.

This gives the student a basic understanding before starting practical work.

### Step 2: Set Up the Development Environment

I would help the student install and configure the required tools:

- Git
- Visual Studio Code
- Python
- Docker if required
- Cloud CLI tools if required

I would verify that the tools work correctly on the student's machine.

### Step 3: Create a GitHub Repository

I would guide the student through creating a repository and explain how to clone it locally.

For example:

```bash
git clone <repository-url>
cd project-directory
```
#### Step 4: Use Documentation

I would provide simple documentation containing installation steps, Git commands, troubleshooting information, and common errors.

The documentation should be clear and easy to follow so that the student can solve common problems independently.

#### Step 5: Use Communication Channels

I would use the course communication channel for announcements and general questions.

A dedicated discussion channel or group can be used for technical troubleshooting and peer support.

Clear communication helps students ask questions, share problems, and receive guidance from instructors and other learners.

#### Step 6: Practical Exercises

Finally, I would give the student small hands-on exercises such as creating a repository, making a commit, pushing code, creating a branch, and deploying a simple application to a cloud environment.

This approach allows the student to learn through practice while having documentation and communication support when problems occur.

---

## B2. Troubleshooting an Application Failure During Production Deployment

If an application goes down unexpectedly during a production deployment, I would follow a structured incident response and troubleshooting process.

### Step 1: Confirm the Incident

First, I would confirm that the application is actually unavailable and determine the scope of the problem.

I would check monitoring dashboards, health checks, alerts, logs, and user reports.

### Step 2: Assess the Impact

I would identify which services, users, regions, or features are affected.

This helps determine the severity of the incident and the required response.

### Step 3: Check Recent Changes

Because the failure occurred during a deployment, I would check the deployment history, recent commits, configuration changes, infrastructure changes, and application version.

### Step 4: Check Application and Infrastructure Health

I would inspect:

- Application logs
- System logs
- CPU and memory usage
- Disk usage
- Network connectivity
- Database connectivity
- Container or process status
- Load balancer and reverse proxy status
- Health check results

### Step 5: Form a Hypothesis

Based on the evidence, I would identify the most likely cause.

For example, the new application version may have introduced an application error or configuration problem.

### Step 6: Roll Back if Necessary

If the new deployment is confirmed as the cause and the application is unavailable, I would roll back to the last known stable version according to the organization's deployment procedure.

The primary objective during a production incident is to restore service safely.

### Step 7: Verify Recovery

After rollback or remediation, I would verify application health, logs, monitoring metrics, database connectivity, and user access.

I would also confirm that the application is functioning normally from the user's perspective.

### Step 8: Root Cause Analysis

After service restoration, the team should perform a root cause analysis.

The team should identify what caused the failure and why automated tests or deployment controls did not detect the problem earlier.

### Step 9: Prevent Recurrence

Possible improvements could include:

- Additional automated tests
- Better health checks
- Deployment approval controls
- Canary or blue-green deployment
- Improved monitoring
- Better rollback automation
- Improved documentation

This approach helps restore the service quickly while also reducing the chance of the same incident happening again.

---

## B3. Balancing Frequent Feature Releases with System Stability

When a team releases features frequently but system stability is decreasing, DevOps practices can help balance delivery speed and reliability.

### 1. Implement Continuous Integration

Developers should frequently integrate their code into a shared repository.

Automated tests should run whenever changes are pushed.

This helps identify defects early.

### 2. Strengthen Automated Testing

The CI/CD pipeline should include appropriate unit, integration, API, security, and end-to-end tests depending on the application.

Automated testing reduces the risk of releasing defective changes.

### 3. Use CI/CD Pipelines

A controlled CI/CD pipeline can automatically build, test, and deploy applications using repeatable steps.

This reduces manual errors and creates consistency between deployments.

### 4. Use Staging Environments

New features should be tested in a staging environment that is as similar as possible to production before they are released to users.

### 5. Use Safer Deployment Strategies

Techniques such as:

- Rolling deployments
- Blue-green deployments
- Canary releases

can reduce the impact of problematic releases.

For example, a canary release can initially expose a new version to a small percentage of users.

If monitoring shows that the new version is stable, the rollout can continue.

### 6. Implement Monitoring and Alerting

Application performance, error rates, response time, infrastructure health, and business metrics should be monitored.

Alerts should notify the team when important thresholds are exceeded.

### 7. Maintain Fast Rollback

Every deployment should have a reliable rollback strategy.

If a release causes problems, the team should be able to quickly return to the previous stable version.

### 8. Learn from Incidents

When failures occur, the team should perform root cause analysis and use the findings to improve testing, monitoring, deployment procedures, and architecture.

Therefore, DevOps does not mean releasing as quickly as possible.

It means creating an automated and controlled delivery process that allows teams to release frequently while maintaining reliability, security, and system stability.
---

# Part C: Technical / Practical Tasks

## Task 1: Local DevOps Demo Application

### Objective

The objective of this task was to run a simple application locally and verify that it was running successfully.

### Technology Used

- Python 3.14.5
- Flask 3.1.3
- Python Virtual Environment
- Windows PowerShell
- Visual Studio Code

### Project Structure

```text
devops-module-1-assignment/
├── app/
│   ├── app.py
│   └── requirements.txt
├── docs/
│   └── assignment-answers.md
└── screenshots/
### Step 1: Create Python Virtual Environment

A Python virtual environment was created using:

```powershell
python -m venv .venv
```

The virtual environment was activated using:

```powershell
.\.venv\Scripts\Activate.ps1
```

The environment was verified using:

```powershell
python --version
```

The Python version used for this assignment was Python 3.14.5.

### Step 2: Install Flask

The application dependency was added to:

`app/requirements.txt`

The file contains:

```text
Flask
```

Flask was installed using:

```powershell
pip install -r requirements.txt
```

The installation completed successfully.
### Step 3: Run the Application

The Flask application was started using:

```powershell
python app.py
```

The application was configured to run on port 5000.

The application was successfully accessed locally using:

```text
http://127.0.0.1:5000
```

The application displayed:

**DevOps Module 1 Assignment**

**Application Running Successfully**

Environment: Local Development

Technology: Python Flask

Port: 5000

### Evidence

The local Flask application and terminal execution screenshots are included in the `screenshots` directory.

### How Running Applications Locally Helps in DevOps

Running an application locally allows engineers to test application functionality before deploying it to a remote or production environment.

It helps verify application functionality, dependencies, configuration, port availability, application errors, and basic connectivity.

This reduces the risk of discovering basic application problems during deployment.
---

## Task 2: Exposing Local Application Using ngrok

### Objective

The objective of this task was to expose the local Flask application to the internet using ngrok.

The Flask application was running locally on:

```text
http://localhost:5000

### Step 1: Verify ngrok

The installed ngrok version was checked using:

```powershell
ngrok version
```

The installed version was:

```text
ngrok version 3.39.9-msix-stable
```

The ngrok configuration was verified using:

```powershell
ngrok config check
```

The configuration check completed successfully.
### Step 2: Create ngrok Tunnel

The ngrok tunnel was configured to forward public traffic to the local Flask application running on port 5000.

The forwarding configuration was:

```text
https://asleep-maximum-cesspool.ngrok-free.dev -> http://localhost:5000
```

### Public URL

The public URL generated during the assignment was:

```text
https://asleep-maximum-cesspool.ngrok-free.dev
```

The public URL successfully displayed the Flask application running on the local machine.

### Evidence

A screenshot showing the active ngrok tunnel and the public application URL is included in the `screenshots` directory.
### Real-World Use Case

Exposing a local application through ngrok is useful when a developer needs to test an application from an external network without deploying it to a production server.

For example, a developer can share a temporary public URL with a teammate or use it to test webhook integrations, external API callbacks, or mobile application connectivity with a locally running backend.

This provides a quick way to test external connectivity during development while keeping the actual application running on the local machine.

### Conclusion

The local Flask application was successfully exposed to the internet using ngrok.

The public ngrok URL successfully accessed the application running on the local machine.