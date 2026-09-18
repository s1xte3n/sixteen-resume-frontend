// PROJECT-OVERVIEW.md

# Azure Cloud Resume Challenge

## 1. Project Purpose

Build and deploy a personal cloud resume and portfolio website that demonstrates practical Azure cloud, backend development, serverless architecture, infrastructure-as-code, testing, and CI/CD skills.

The project is based on the Azure edition of the Cloud Resume Challenge and will implement all challenge requirements, with one documented certification deviation: **AI-901 is used instead of AZ-900** because AI-901 is the Azure certification currently held.

The website will initially serve as a portfolio and learning project and is intended to become a production personal website.

## 2. Target Users

The website has two primary audiences:

1. **Recruiters and hiring managers**

   * Quickly understand professional background, technical skills, certifications, education, and projects.
   * Access GitHub and blog content.

2. **Technical reviewers**

   * Inspect the implementation and GitHub repositories.
   * Evaluate Azure architecture, Python, serverless development, IaC, testing, security, and CI/CD practices.

## 3. MVP

The MVP consists of the complete Azure Cloud Resume Challenge:

1. Azure certification displayed on the resume.
2. Resume written in HTML.
3. Resume styled with CSS.
4. Website hosted using Azure Storage static website hosting.
5. HTTPS using Azure CDN.
6. Custom DNS hostname pointing to the Azure CDN endpoint.
7. JavaScript visitor counter.
8. Visitor count stored in Azure Cosmos DB Table API using serverless capacity.
9. Azure Function HTTP API between the browser and Cosmos DB.
10. Azure Function implemented in Python.
11. Automated tests for the Python code.
12. Azure Resource Manager template for infrastructure as code.
13. Separate GitHub repository for backend code.
14. GitHub Actions CI/CD for backend testing and deployment.
15. Separate GitHub repository for frontend code and GitHub Actions deployment.
16. Blog content documenting lessons learned and the project journey, linked from the resume.

## 4. Resume Positioning

The resume will describe the user as having:

> **4+ years of hands-on software development experience**

This experience includes substantial personal and technical projects beginning in 2022.

Professional employment will remain separately represented as:

**IT Operator — Gijima Holdings | June 2022–Present**

The resume will not imply that the entire four-plus-year period represents professional software-engineering employment.

## 5. Existing Resume Source

A complete current CV has been supplied as the source material.

The CV contains experience in:

* Backend development
* Cloud-native development
* Serverless architecture
* JavaScript
* Python
* C#
* SQL
* REST APIs
* AWS
* Microsoft Azure
* GitHub Actions
* Jenkins
* Infrastructure as Code
* Docker
* Enterprise IT operations

Existing technical projects include:

* Enterprise E-Commerce Platform
* Contoso MediaOps Azure Cloud-Native Media Platform
* Multi-Cloud CI/CD Platform
* AWS Cloud Resume Challenge
* Python Log Analysis Application
* Python Automation/API Integration Tool

The CV still requires editorial updating and conversion into the project's HTML resume.

## 6. Technology Stack

### Frontend

* HTML
* CSS
* JavaScript

### Hosting and Delivery

* Azure Storage static website
* Azure CDN
* FreeDNS for the initial free DNS/hostname requirement

### Backend

* Azure Functions
* Python
* HTTP trigger

### Database

* Azure Cosmos DB
* Table API
* Serverless capacity

### Infrastructure as Code

* Azure Resource Manager (ARM) template
* Azure Functions Consumption plan

### Source Control and CI/CD

* GitHub
* GitHub Actions
* Python testing

### Documentation and Publishing

* Dev.to
* Hashnode

## 7. Azure Environment

* Cloud provider: Microsoft Azure
* Region: East US
* Deployment environments: one
* Azure subscription: existing subscription
* Target cost: R0 where possible
* Paid services: lowest-cost option where a genuinely free implementation is not possible

The Azure subscription identifier is intentionally not stored in project documentation.

## 8. Repository Structure

Two separate GitHub repositories will be used.

### Frontend

`	sixteen-resume-frontend`

Contains:

* HTML resume
* CSS
* JavaScript
* frontend deployment workflow

### Backend

`	sixteen-resume-backend`

Contains:

* Azure Function
* Python application code
* Python tests
* ARM infrastructure template
* backend deployment workflow

## 9. Git Workflow

The intended development workflow is:

```text
develop
   ↓
feature/*
   ↓
Pull Request
   ↓
CI
   ↓
Merge
   ↓
develop
   ↓
main
```

`main` represents the production version.

Protected branches and CI checks are part of the intended workflow.

## 10. Security Baseline

The project will follow a standard security baseline:

* No Azure credentials committed to Git.
* No secrets committed to source control.
* GitHub Actions secrets used for deployment credentials where required.
* Least-privilege access wherever practical.
* HTTPS for the public website.
* Browser JavaScript must not connect directly to Cosmos DB.
* Cosmos DB access remains behind the Azure Function API.
* Infrastructure and deployment configuration should be reproducible through source-controlled IaC and CI/CD.

## 11. Cost Strategy

The project prioritizes:

1. Free services and free allowances.
2. Serverless/pay-per-use options.
3. Minimal resource consumption.
4. Lowest-cost paid alternatives where a free implementation is unavailable.

The project is not intended to optimize for high-scale production workloads.

## 12. Timeline

Target completion date:

**30 September 2026**

## 13. Blog Requirement

The project will produce blog content on both:

* Dev.to
* Hashnode

The blog content will cover:

* Technical lessons learned.
* Project implementation.
* Problems encountered.
* Solutions and decisions.
* The broader project journey.

The resume will link to the published blog content.

## 14. Scope Boundaries

The project will remain strictly aligned with the Cloud Resume Challenge.

The following are outside the MVP:

* Authentication
* Admin dashboards
* Contact forms
* CMS functionality
* E-commerce
* Payments
* Additional analytics
* Additional APIs
* Custom blogging platform
* Multiple deployment environments
* Additional cloud providers
* Additional application frameworks
* Features not required by the challenge

## 15. Certification Deviation

The challenge specification calls for **AZ-900**.

The user currently holds:

**Microsoft Certified: Azure AI Fundamentals (AI-901)**

Therefore:

> The project intentionally uses AI-901 as the displayed Azure certification rather than AZ-900.

This is a documented deviation from the literal challenge requirement. The project must not claim full AZ-900 compliance unless AZ-900 is subsequently obtained.
