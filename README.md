# PortSwigger Web Security Academy Labs

A structured collection of hands-on, authorized PortSwigger Web Security Academy lab reports. Each report records the methodology, evidence, impact, and remediation for one specific lab.

General reusable concepts are maintained separately in the [Cybersecurity Knowledge Base](https://github.com/Francisco0604/cybersecurity-knowledge-base).

---

## Progress

| Category | Completed labs | Status |
| :--- | :--- | :--- |
| Access Control | 2 | In progress |

## 📂 Categories & Lab Reports

### 🛡️ Access Control
- [Lab 01 — Unprotected Admin Functionality](access-control/01-unprotected-admin-functionality.md)
  - **Vulnerability**: Broken Access Control / Unprotected Administrative Functionality
  - **Concepts**: `robots.txt` Reconnaissance, Direct Endpoint Access, Vertical Privilege Escalation
- [Lab 02 — User Role Controlled by Request Parameter](access-control/02-user-role-controlled-by-request-parameter.md)
  - **Vulnerability**: Broken Access Control / Client-Controlled Authorization (Cookie Role Tampering)
  - **Concepts**: Cookie Manipulation (`Admin=true`), Burp Proxy Intercept, Authorization Boundary Testing

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
│   └── 02-user-role-controlled-by-request-parameter/
│       ├── 01-lab-homepage.png
│       ├── 02-admin-false-401.png
│       ├── 03-admin-true-intercept.png
│       ├── 04-admin-panel.png
│       └── 05-lab-solved.png
└── access-control/
    ├── 01-unprotected-admin-functionality.md
    └── 02-user-role-controlled-by-request-parameter.md
```

---

## 👤 Author

**Francisco Elroy Afonso**  
*Aspiring Penetration Tester*
