# PortSwigger Web Security Academy Labs

A structured collection of hands-on, authorized PortSwigger Web Security Academy lab reports. Each report records the methodology, evidence, impact, and remediation for one specific lab.

General reusable concepts are maintained separately in the [Cybersecurity Knowledge Base](https://github.com/Francisco0604/cybersecurity-knowledge-base).

---

## Progress

| Category | Completed labs | Status |
| :--- | :--- | :--- |
| Access Control | 13 | Completed |
| Authentication | 2 | In progress |

## 📂 Categories & Lab Reports

### 🛡️ Access Control
- [Lab 01 — Unprotected Admin Functionality](access-control/01-unprotected-admin-functionality.md)
  - **Vulnerability**: Broken Access Control / Unprotected Administrative Functionality
  - **Concepts**: `robots.txt` Reconnaissance, Direct Endpoint Access, Vertical Privilege Escalation
- [Lab 02 — Unprotected Admin Functionality with Unpredictable URL](access-control/02-unprotected-admin-functionality-with-unpredictable-url.md)
  - **Vulnerability**: Broken Access Control / Unprotected Administrative Functionality
  - **Concepts**: Response Inspection, Hidden Endpoint Discovery, Server-Side Authorization
- [Lab 03 — User Role Controlled by Request Parameter](access-control/03-user-role-controlled-by-request-parameter.md)
  - **Vulnerability**: Broken Access Control / Client-Controlled Authorization (Cookie Role Tampering)
  - **Concepts**: Cookie Manipulation (`Admin=true`), Burp Proxy Intercept, Authorization Boundary Testing
- [Lab 04 — User Role Can Be Modified in User Profile](access-control/04-user-role-can-be-modified-in-user-profile.md)
  - **Vulnerability**: Broken Access Control / Mass Assignment
  - **Concepts**: JSON Request Testing, Mass Assignment, Privilege Escalation
- [Lab 05 — User ID Controlled by Request Parameter](access-control/05-user-id-controlled-by-request-parameter.md)
  - **Vulnerability**: Broken Access Control / IDOR
  - **Concepts**: Object-Level Authorization, Parameter Tampering, Horizontal Privilege Escalation
- [Lab 06 — User ID Controlled by Request Parameter, with Unpredictable User IDs](access-control/06-user-id-controlled-by-request-parameter-with-unpredictable-user-ids.md)
  - **Vulnerability**: Broken Access Control / IDOR
  - **Concepts**: GUID Discovery, Repeater Testing, Horizontal Privilege Escalation
- [Lab 07 — User ID Controlled by Request Parameter with Data Leakage in Redirect](access-control/07-user-id-controlled-by-request-parameter-with-data-leakage-in-redirect.md)
  - **Vulnerability**: Broken Access Control / Sensitive Data Leakage
  - **Concepts**: Redirect Response Inspection, Response-Body Leakage, Horizontal Privilege Escalation
- [Lab 08 — User ID Controlled by Request Parameter with Password Disclosure](access-control/08-user-id-controlled-by-request-parameter-with-password-disclosure.md)
  - **Vulnerability**: Broken Access Control / Sensitive Information Disclosure
  - **Concepts**: Password Disclosure, HTML Response Inspection, Credential Exposure
- [Lab 09 — Insecure Direct Object References](access-control/09-insecure-direct-object-references.md)
  - **Vulnerability**: Broken Access Control / IDOR
  - **Concepts**: Object-Level Authorization, Transcript Access, Sensitive Data Exposure
- [Lab 10 — URL-Based Access Control Can Be Circumvented](access-control/10-url-based-access-control-can-be-circumvented.md)
  - **Vulnerability**: Broken Access Control / Front-End and Back-End Access Control Discrepancy
  - **Concepts**: `X-Original-URL` Header, Front-End Proxy Bypass, Administrative Endpoint Access
- [Lab 11 — Method-Based Access Control Can Be Circumvented](access-control/11-method-based-access-control-can-be-circumvented.md)
  - **Vulnerability**: Broken Access Control / Method-Based Access Control Bypass
  - **Concepts**: HTTP Verb Tampering, `POST` to `GET` Conversion, Vertical Privilege Escalation
- [Lab 12 — Multi-Step Process with No Access Control on One Step](access-control/12-multi-step-process-with-no-access-control-on-one-step.md)
  - **Vulnerability**: Broken Access Control / Missing Authorization on Multi-Step Process
  - **Concepts**: Workflow Sub-Step Bypass, `confirmed=true` Tampering, Vertical Privilege Escalation
- [Lab 13 — Referer-Based Access Control](access-control/13-referer-based-access-control.md)
  - **Vulnerability**: Broken Access Control / Referer-Based Access Control Bypass
  - **Concepts**: Client-Controlled Header Spoofing, `Referer` Validation Bypass, Vertical Privilege Escalation

### 🔑 Authentication
- [Lab 01 — Username Enumeration via Different Responses](labs/Authentication/01-username-enumeration-via-different-responses.md)
  - **Vulnerability**: Username Enumeration and Password Brute Force
  - **Concepts**: Burp Intruder (Sniper), Burp Repeater, Response Analysis, Credential Testing
- [Lab 02 — 2FA Simple Bypass](labs/Authentication/02-2fa-simple-bypass.md)
  - **Vulnerability**: Two-Factor Authentication Bypass
  - **Concepts**: Authentication State Analysis, Direct Navigation Bypass, MFA Workflow Flaws

---

## 🛠️ Repository Structure

```text
portswigger-labs/
│
├── README.md
├── templates/
│   └── lab-report-template.md
├── screenshots/
│   ├── Access_Control/
│   │   ├── 01-unprotected-admin-functionality/
│   │   ├── 02-unprotected-admin-functionality-unpredictable-url/
│   │   ├── 03-user-role-controlled-by-request-parameter/
│   │   ├── 04-user-role-modified-in-profile/
│   │   ├── 05-user-id-controlled-by-request-parameter/
│   │   ├── 06-user-id-controlled-by-request-parameter-unpredictable-ids/
│   │   ├── 07-user-id-controlled-by-request-parameter-data-leakage-redirect/
│   │   ├── 08-user-id-controlled-by-request-parameter-password-disclosure/
│   │   ├── 09-insecure-direct-object-references/
│   │   ├── 10-url-based-access-control-circumvented/
│   │   ├── 11-method-based-access-control-circumvented/
│   │   ├── 12-multi-step-process-no-access-control/
│   │   └── 13-referer-based-access-control/
│   └── Authentication/
│       ├── 01-username-enumeration/
│       │   ├── 01-username-intruder-results.png
│       │   ├── 02-app01-response-confirmation.png
│       │   ├── 03-password-intruder-results.png
│       │   └── 04-account-access-and-lab-solved.png
│       └── 02-2fa-simple-bypass/
│           ├── 01-authentication-flow.png
│           ├── 02-access-without-mfa.png
│           └── 03-carlos-account-and-lab-solved.png
├── access-control/
│   ├── 01-unprotected-admin-functionality.md
│   ├── 02-unprotected-admin-functionality-with-unpredictable-url.md
│   ├── 03-user-role-controlled-by-request-parameter.md
│   ├── 04-user-role-can-be-modified-in-user-profile.md
│   ├── 05-user-id-controlled-by-request-parameter.md
│   ├── 06-user-id-controlled-by-request-parameter-with-unpredictable-user-ids.md
│   ├── 07-user-id-controlled-by-request-parameter-with-data-leakage-in-redirect.md
│   ├── 08-user-id-controlled-by-request-parameter-with-password-disclosure.md
│   ├── 09-insecure-direct-object-references.md
│   ├── 10-url-based-access-control-can-be-circumvented.md
│   ├── 11-method-based-access-control-can-be-circumvented.md
│   ├── 12-multi-step-process-with-no-access-control-on-one-step.md
│   └── 13-referer-based-access-control.md
└── labs/
    └── Authentication/
        ├── 01-username-enumeration-via-different-responses.md
        └── 02-2fa-simple-bypass.md
```

---

## 👤 Author

**Francisco Elroy Afonso**  
*Aspiring Penetration Tester*
