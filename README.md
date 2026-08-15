# PortSwigger Web Security Academy Labs

A structured collection of hands-on, authorized PortSwigger Web Security Academy lab reports. Each report records the methodology, evidence, impact, and remediation for one specific lab.

General reusable concepts are maintained separately in the [Cybersecurity Knowledge Base](https://github.com/Francisco0604/cybersecurity-knowledge-base).

---

## Progress

| Category | Completed labs | Status |
| :--- | :--- | :--- |
| Access Control | 12 | In progress |

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

---

## 🛠️ Repository Structure

```text
portswigger-labs/
│
├── README.md
├── templates/
│   └── lab-report-template.md
├── screenshots/
│   ├── 01-unprotected-admin-functionality/
│   │   ├── 01-lab-homepage.png
│   │   ├── 02-robots-txt.png
│   │   ├── 03-delete-request.png
│   │   └── 04-lab-solved.png
│   ├── 02-unprotected-admin-functionality-unpredictable-url/
│   │   ├── 01-leaked-admin-url.png
│   │   ├── 02-admin-panel.png
│   │   └── 03-lab-solved.png
│   ├── 03-user-role-controlled-by-request-parameter/
│       ├── 01-lab-homepage.png
│       ├── 02-admin-false-401.png
│       ├── 03-admin-true-intercept.png
│       ├── 04-admin-panel.png
│       └── 05-lab-solved.png
│   ├── 04-user-role-modified-in-profile/
│       ├── 01-profile-update-request.png
│       ├── 02-roleid-2-request.png
│       ├── 03-admin-panel.png
│       └── 04-lab-solved.png
│   ├── 05-user-id-controlled-by-request-parameter/
│       ├── 01-wiener-account-request.png
│       ├── 02-carlos-account-request.png
│       ├── 03-carlos-api-key.png
│       └── 04-lab-solved.png
│   └── 06-user-id-controlled-by-request-parameter-unpredictable-ids/
│       ├── 01-wiener-account-guid.png
│       ├── 02-carlos-guid-discovered.png
│       ├── 03-carlos-account-repeater.png
│       ├── 04-carlos-api-key.png
│       └── 05-lab-solved.png
│   └── 07-user-id-controlled-by-request-parameter-data-leakage-redirect/
│       ├── 01-carlos-request.png
│       ├── 02-redirect-response-data-leakage.png
│       └── 03-lab-solved.png
│   └── 08-user-id-controlled-by-request-parameter-password-disclosure/
│       ├── 01-admin-redirect.png
│       ├── 02-administrator-password-response.png
│       ├── 03-admin-access.png
│       └── 04-lab-solved.png
│   ├── 09-insecure-direct-object-references/
│   │   ├── 01-chat-transcript-request.png
│   │   ├── 02-modified-transcript-request.png
│   │   ├── 03-leaked-credentials.png
│   │   └── 04-lab-solved.png
│   ├── 10-url-based-access-control-circumvented/
│   │   ├── 01-direct-admin-blocked.png
│   │   ├── 02-x-original-url-bypass.png
│   │   ├── 03-admin-panel.png
│   │   └── 04-lab-solved.png
│   ├── 11-method-based-access-control-circumvented/
│   │   ├── 01-admin-promotion-request.png
│   │   ├── 02-get-method-bypass.png
│   │   └── 03-wiener-admin-access-and-lab-solved.png
│   └── 12-multi-step-process-no-access-control/
│       ├── 01-admin-multi-step-process.png
│       ├── 02-wiener-direct-step-bypass.png
│       └── 03-wiener-admin-access-and-lab-solved.png
└── access-control/
    ├── 01-unprotected-admin-functionality.md
    ├── 02-unprotected-admin-functionality-with-unpredictable-url.md
    ├── 03-user-role-controlled-by-request-parameter.md
    ├── 04-user-role-can-be-modified-in-user-profile.md
    ├── 05-user-id-controlled-by-request-parameter.md
    ├── 06-user-id-controlled-by-request-parameter-with-unpredictable-user-ids.md
    ├── 07-user-id-controlled-by-request-parameter-with-data-leakage-in-redirect.md
    ├── 08-user-id-controlled-by-request-parameter-with-password-disclosure.md
    ├── 09-insecure-direct-object-references.md
    ├── 10-url-based-access-control-can-be-circumvented.md
    ├── 11-method-based-access-control-can-be-circumvented.md
    └── 12-multi-step-process-with-no-access-control-on-one-step.md
```

---

## 👤 Author

**Francisco Elroy Afonso**  
*Aspiring Penetration Tester*
