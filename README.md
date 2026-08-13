# PortSwigger Web Security Academy Labs

A structured collection of hands-on, authorized PortSwigger Web Security Academy lab reports. Each report records the methodology, evidence, impact, and remediation for one specific lab.

General reusable concepts are maintained separately in the [Cybersecurity Knowledge Base](https://github.com/Francisco0604/cybersecurity-knowledge-base).

---

## Progress

| Category | Completed labs | Status |
| :--- | :--- | :--- |
| Access Control | 4 | In progress |

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
│   └── 03-user-role-controlled-by-request-parameter/
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
└── access-control/
    ├── 01-unprotected-admin-functionality.md
    ├── 02-unprotected-admin-functionality-with-unpredictable-url.md
    ├── 03-user-role-controlled-by-request-parameter.md
    └── 04-user-role-can-be-modified-in-user-profile.md
```

---

## 👤 Author

**Francisco Elroy Afonso**  
*Aspiring Penetration Tester*
