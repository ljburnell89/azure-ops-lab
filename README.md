 # Azure Ops Lab

 > A production-style Azure platform built to demonstrate practical DevOps, cloud engineering, automation, security, and observability skills.

 [](<https://github.com/>)\
 [](<https://azure.microsoft.com/>)\
 [](<https://www.terraform.io/>)\
 [](<https://www.docker.com/>)\

---

 ## 📖 Overview

 **Azure Ops Lab** is a hands-on cloud and DevOps project designed to demonstrate how a modern application can be built, deployed, secured, monitored, and operated on Microsoft Azure.

 Rather than focusing on building a complex application, the project focuses on the **engineering platform and operational practices surrounding it**.

 The platform is being developed incrementally, starting with a containerised API and progressing towards:

 - Infrastructure as Code
- Automated CI/CD
- Azure Container Registry
- Azure Container Apps
- Secure secrets management
- Managed identities
- Automated security scanning
- Application monitoring and observability
- Incident detection and response
- Infrastructure testing
- Kubernetes on Azure
- Helm
- GitOps

 The goal is to create a realistic environment that demonstrates the skills and decision-making expected from a modern Cloud / DevOps / Platform Engineer.

---

 ## 🎯 Project Goals

 The project has four primary goals:

 ### 1\. Infrastructure as Code

 All cloud infrastructure should be reproducible and version controlled using Terraform.

 ### 2\. Automated Delivery

 Changes should progress from source control through automated testing and validation into Azure with minimal manual intervention.

 ### 3\. Security by Design

 Secrets, identities, dependencies, containers, and infrastructure should be treated as security concerns throughout the development lifecycle.

 ### 4\. Observability & Operations

 The platform should provide enough visibility to detect, investigate, and recover from application and infrastructure problems.

---

 # 🏗️ Architecture

 The platform will evolve throughout the project.

 ### Current architecture

```
┌───────────────────────┐
│       Developer       │
│                       │
│  Python / FastAPI     │
└───────────┬───────────┘
            │
            ▼
┌───────────────────────┐
│        Docker         │
│                       │
│   Container Image     │
└───────────────────────┘
```

 ### Target architecture

```
                              ┌─────────────────┐
                              │     GitHub      │
                              │                 │
                              │ Source Control  │
                              └────────┬────────┘
                                       │
                                       ▼
                              ┌─────────────────┐
                              │ GitHub Actions  │
                              │                 │
                              │ Test            │
                              │ Security Scan   │
                              │ Build           │
                              │ Deploy          │
                              └────────┬────────┘
                                       │
                                       ▼
                              ┌─────────────────┐
                              │ Azure Container  │
                              │    Registry      │
                              └────────┬────────┘
                                       │
                         ┌─────────────┴─────────────┐
                         │                           │
                         ▼                           ▼
                ┌─────────────────┐        ┌─────────────────┐
                │ Azure Container │        │       AKS       │
                │      Apps       │        │                 │
                │                 │        │ Kubernetes      │
                │ Application     │        │ Helm / GitOps   │
                └────────┬────────┘        └────────┬────────┘
                         │                          │
                         └────────────┬─────────────┘
                                      │
                                      ▼
                              ┌─────────────────┐
                              │ Azure Monitor   │
                              │                 │
                              │ App Insights    │
                              │ Log Analytics   │
                              │ Alerts          │
                              └─────────────────┘

                 ┌────────────────────────────────────┐
                 │            Azure Platform          │
                 │                                    │
                 │ Terraform │ Key Vault │ Networking │
                 │ Managed Identity │ Monitoring      │
                 └────────────────────────────────────┘
```

---

 # 🛠️ Technology Stack

 ## Application

 | Technology | Purpose |
| --- | --- |
| Python | Application development |
| FastAPI | REST API framework |
| pytest | Automated testing |

## Cloud

 | Azure Service | Purpose |
| --- | --- |
| Azure Container Registry | Container image storage |
| Azure Container Apps | Application hosting |
| Azure Key Vault | Secret management |
| Azure Monitor | Monitoring and alerting |
| Application Insights | Application observability |
| Log Analytics | Centralised logging |
| Azure Kubernetes Service | Kubernetes platform |

## DevOps

 | Technology | Purpose |
| --- | --- |
| Git | Source control |
| GitHub | Repository and collaboration |
| GitHub Actions | CI/CD |
| Terraform | Infrastructure as Code |
| Docker | Containerisation |
| Helm | Kubernetes packaging |
| Argo CD | GitOps |

---

 # 📁 Repository Structure

 The repository will evolve as additional platform capabilities are introduced.

```
azure-ops-lab/
│
├── app/
│   ├── __init__.py
│   └── main.py
│
├── tests/
│   └── test_api.py
│
├── terraform/
│   ├── modules/
│   │   ├── container-app/
│   │   ├── container-registry/
│   │   └── monitoring/
│   │
│   └── environments/
│       ├── dev/
│       └── prod/
│
├── kubernetes/
│   ├── deployment.yaml
│   ├── service.yaml
│   └── ingress.yaml
│
├── helm/
│   └── azure-ops-api/
│
├── docs/
│   ├── architecture/
│   ├── decisions/
│   └── incidents/
│
├── .github/
│   └── workflows/
│       ├── ci.yml
│       ├── terraform.yml
│       └── cd.yml
│
├── Dockerfile
├── requirements.txt
├── .gitignore
└── README.md
```

---

 # 🚀 Getting Started

 ## Prerequisites

 The following tools are required for local development:

 - Python 3.12+
- Docker
- Git
- Terraform
- Azure CLI

 Later stages of the project will also require:

 - kubectl
- Helm
- An Azure subscription

---

 ## 1\. Clone the repository

```
git clone <repository-url>
cd azure-ops-lab
```

---

 ## 2\. Create a Python virtual environment

```
python -m venv .venv
```

 Activate it:

 ### Linux / macOS

```
source .venv/bin/activate
```

 ### Windows PowerShell

```
.venv\Scripts\Activate.ps1
```

---

 ## 3\. Install dependencies

```
pip install -r requirements.txt
```

---

 ## 4\. Run the application

```
uvicorn app.main:app --reload
```

 The API will be available at:

```
http://localhost:8000
```

 Interactive API documentation is available at:

```
http://localhost:8000/docs
```

---

 # 🧪 Testing

 Tests are written using `pytest`.

 Run the test suite:

```
pytest
```

 The test suite should pass before changes are merged.

 The eventual CI pipeline will automatically execute these tests for pull requests.

---

 # 🐳 Docker

 The application is packaged as a Docker container to provide a consistent runtime environment across development and deployment.

 ## Build the image

```
docker build -t azure-ops-api:1.0.0 .
```

 ## Run the container

```
docker run --rm -p 8000:8000 azure-ops-api:1.0.0
```

 The API can then be accessed at:

```
http://localhost:8000
```

---

 # 🔄 CI/CD

 The project will use GitHub Actions to automate validation and deployment.

 The target pipeline is:

```
Pull Request
      │
      ▼
┌─────────────┐
│ Unit Tests  │
└──────┬──────┘
       ▼
┌─────────────┐
│ Code Checks │
└──────┬──────┘
       ▼
┌───────────────┐
│ Security Scan │
└──────┬────────┘
       ▼
┌───────────────┐
│ Docker Build  │
└──────┬────────┘
       ▼
┌─────────────────────┐
│ Terraform Validation│
└──────────┬──────────┘
           ▼
         Merge
           │
           ▼
    Deploy to Dev
           │
           ▼
    Smoke Tests
           │
           ▼
 Production Approval
           │
           ▼
    Deploy Production
```

 The pipeline will aim to ensure that application and infrastructure changes are validated before reaching production.

---

 # 🏗️ Infrastructure as Code

 Azure infrastructure will be managed using Terraform.

 The objective is to make environments reproducible and avoid manually configured infrastructure wherever practical.

 The Terraform configuration will eventually manage:

 - Resource groups
- Container Registry
- Container Apps
- Networking
- Monitoring
- Log Analytics
- Application Insights
- Key Vault
- Managed identities
- AKS

 Terraform changes will be reviewed through pull requests.

 Typical workflow:

```
terraform fmt
terraform validate
terraform plan
terraform apply
```

 Production changes should require appropriate review and approval.

---

 # 🔐 Security

 Security is treated as part of the development lifecycle rather than a separate stage.

 The project will progressively introduce:

 ### Secrets Management

 Application secrets will be stored in Azure Key Vault rather than committed to source control.

 ### Managed Identity

 Where supported, Azure managed identities will be preferred over long-lived credentials.

 ### Dependency Scanning

 Application dependencies will be scanned for known vulnerabilities.

 ### Container Scanning

 Docker images will be scanned before deployment.

 ### Infrastructure Scanning

 Terraform configurations will be checked for common security and configuration issues.

 ### Least Privilege

 Azure identities and permissions will follow the principle of least privilege wherever practical.

---

 # 📊 Monitoring & Observability

 The deployed application will use Azure monitoring services to provide visibility into application and platform behaviour.

 Planned telemetry includes:

 - Request volume
- HTTP status codes
- Error rates
- Response times
- Application exceptions
- Dependency failures
- CPU utilisation
- Memory utilisation
- Application availability

 Target architecture:

```
Application
     │
     ▼
Application Insights
     │
     ├──────────────► Metrics
     │
     ├──────────────► Logs
     │
     └──────────────► Exceptions
                          │
                          ▼
                    Azure Monitor
                          │
                          ▼
                       Alerts
```

---

 # 🚨 Incident Management

 The project will deliberately introduce controlled failures to demonstrate operational practices.

 Example scenarios include:

 - Failed application deployment
- Increased HTTP 500 responses
- Application dependency failure
- Increased response latency
- Resource exhaustion
- Failed health checks

 Each significant incident will be documented under:

```
docs/incidents/
```

 Incident reports will contain:

```
- Impact
- Detection
- Timeline
- Root cause
- Resolution
- Recovery
- Preventative actions
- Lessons learned
```

 Example:

```
docs/incidents/001-api-errors.md
```

 The objective is to demonstrate not only how to deploy software, but also how to **detect, investigate, recover from, and learn from failures**.

---

 # 🧠 Architecture Decisions

 Important technical decisions will be documented as Architecture Decision Records (ADRs).

 Location:

```
docs/decisions/
```

 Examples:

```
001-why-container-apps.md
002-terraform-state-management.md
003-secret-management.md
004-deployment-strategy.md
005-why-aks.md
```

 Each decision will document:

 - Context
- Options considered
- Decision
- Reasoning
- Consequences

 This helps demonstrate the engineering reasoning behind the implementation rather than simply documenting which technologies were used.

---

 # ☸️ Kubernetes & GitOps

 A later stage of the project will deploy the application to Azure Kubernetes Service.

 The target deployment model is:

```
Developer
    │
    ▼
 GitHub
    │
    ▼
GitHub Actions
    │
    ├── Test
    ├── Scan
    └── Build
           │
           ▼
Azure Container Registry
           │
           ▼
     GitOps Repository
           │
           ▼
        Argo CD
           │
           ▼
          AKS
```

 Kubernetes capabilities will include:

 - Deployments
- Services
- Ingress
- ConfigMaps
- Secrets
- Health probes
- Resource requests and limits
- Horizontal Pod Autoscaling
- Rolling deployments
- Rollbacks

 Helm will be used to package the Kubernetes application.

---

 # 📋 Project Roadmap

 ## Phase 1 — Application

 - [x] Create FastAPI application
- [x] Add health endpoint
- [x] Add API endpoints
- [x] Add automated tests
- [x] Containerise application
- [x] Create initial Git repository

 ## Phase 2 — Azure

 - [ ] Create Azure Container Registry
- [ ] Push container image to ACR
- [ ] Deploy application to Azure Container Apps
- [ ] Configure application ingress
- [ ] Configure environment variables

 ## Phase 3 — Infrastructure as Code

 - [ ] Introduce Terraform
- [ ] Terraform Azure resources
- [ ] Create reusable modules
- [ ] Separate development and production environments
- [ ] Configure remote Terraform state
- [ ] Add Terraform validation to CI

 ## Phase 4 — CI/CD

 - [ ] GitHub Actions CI
- [ ] Automated tests
- [ ] Docker image build
- [ ] Container security scanning
- [ ] Push images to ACR
- [ ] Automated development deployment
- [ ] Production approval
- [ ] Deployment rollback

 ## Phase 5 — Security

 - [ ] Azure Key Vault
- [ ] Managed Identity
- [ ] Dependency scanning
- [ ] Container image scanning
- [ ] Terraform security scanning
- [ ] Least-privilege access

 ## Phase 6 — Observability

 - [ ] Application Insights
- [ ] Log Analytics
- [ ] Azure Monitor
- [ ] Application dashboard
- [ ] Availability monitoring
- [ ] Error-rate alerts
- [ ] Performance alerts

 ## Phase 7 — Operations

 - [ ] Simulate application failure
- [ ] Create incident documentation
- [ ] Demonstrate rollback
- [ ] Document recovery procedures
- [ ] Create operational runbook

 ## Phase 8 — Kubernetes & GitOps

 - [ ] Deploy AKS using Terraform
- [ ] Deploy application to AKS
- [ ] Add health probes
- [ ] Add resource limits
- [ ] Configure autoscaling
- [ ] Create Helm chart
- [ ] Install Argo CD
- [ ] Implement GitOps deployment
- [ ] Demonstrate GitOps rollback

---

 # 💰 Cost Considerations

 This project is intended primarily as a learning and portfolio environment.

 Azure resources can incur costs depending on configuration and usage.

 The project will therefore aim to:

 - Use appropriate low-cost development resources
- Avoid unnecessary always-on infrastructure
- Destroy temporary environments when not required
- Monitor Azure spending
- Document production-scale alternatives separately from development configurations

 > **Important:** Always check current Azure pricing before deploying resources. Costs and free-tier eligibility can change.

---

 # 📚 What This Project Demonstrates

 By completion, this project is intended to demonstrate practical experience with:

 ### Cloud Engineering

 - Microsoft Azure
- Azure networking
- Identity and access management
- Managed services
- Container platforms

 ### DevOps

 - CI/CD
- Infrastructure as Code
- Automated testing
- Automated deployments
- Release management
- Rollbacks

 ### Containers

 - Docker
- Container registries
- Container orchestration
- Kubernetes

 ### Security

 - Secret management
- Managed identities
- Vulnerability scanning
- Infrastructure security
- Least privilege

 ### Operations

 - Monitoring
- Logging
- Alerting
- Incident response
- Troubleshooting
- Reliability

 ### Platform Engineering

 - Reusable infrastructure
- Self-service deployment patterns
- GitOps
- Declarative configuration
- Environment management

---

 # 📝 Lessons Learned

 This section will be updated throughout the project.

 The intention is to document practical lessons rather than simply record successful deployments.

 Topics will include:

 - What worked
- What didn't work
- Azure-specific challenges
- Infrastructure decisions
- Deployment failures
- Security considerations
- Operational trade-offs
- Improvements made during the project

---

 # 🚧 Current Status

 **Phase 1 — Application**

 The initial API and containerisation are complete.

 The next milestone is to deploy the container image to **Azure Container Registry** and run the application using **Azure Container Apps**.

---

 ## 📌 Disclaimer

 This is a personal learning and portfolio project designed to demonstrate practical cloud and DevOps engineering concepts.

 Production implementations would require additional considerations around availability, compliance, security, disaster recovery, cost management, and organisational requirements.

 I'd use that as your initial README and **tick the roadmap items off as we build them**. It will become a nice visual record of the project's progression rather than you having to rewrite the README every week.

 One small recommendation: don't tick anything off merely because you've created the resource—only tick it when you've actually **tested and documented** it. That will keep the repository credible when you eventually show it to recruiters or interviewers.
