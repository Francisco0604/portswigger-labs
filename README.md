# PortSwigger Web Security Academy Labs & Writeups

Welcome to the **PortSwigger Web Security Academy Solutions & Documentation** repository. This repository contains structured lab notes, practical walkthroughs, HTTP traffic analysis, and vulnerability writeups as part of practical web security training.

---

## 🎯 Purpose & Methodology

The goal of this repository is to systematically document web application security testing methodology using **Burp Suite** and industry-standard security concepts.

### Standard Testing Methodology
```text
  Target Reconnaissance & HTTP Interception
                    ↓
   Identify Controllable Input Parameters
                    ↓
 Send Request to Burp Repeater (Single Variable Edits)
                    ↓
  Analyze HTTP Response Delta (Status, Length, Body)
                    ↓
  Exploit & Verify Security Vulnerability
```

---

## 📂 Repository Structure

```text
portswigger-labs/
├── 01-information-gathering-and-burp/
│   └── lab-01-basic-burp-repeater-workflow.md
├── 02-authentication/
├── 03-access-control/
├── 04-sql-injection/
├── 05-cross-site-scripting-xss/
└── README.md
```

---

## 🔬 Lab Categories Overview

| Category | Description | Status |
| :--- | :--- | :---: |
| **01. Information Gathering & Burp Suite** | Proxy setup, request manipulation, and HTTP Repeater workflow | 🟢 In Progress |
| **02. Authentication** | Broken authentication, brute-force testing, and session management | 🟡 Planned |
| **03. Access Control** | IDOR, privilege escalation, and broken authorization checks | 🟡 Planned |
| **04. SQL Injection (SQLi)** | In-band, blind, and error-based database exploitation | 🟡 Planned |
| **05. Cross-Site Scripting (XSS)** | Reflected, stored, and DOM-based script injection | 🟡 Planned |

---

## 🚀 Quick Start Guide

### Prerequisites
* [Burp Suite Community / Professional](https://portswigger.net/burp)
* Burp's pre-configured embedded browser or FoxyProxy extension
* Free account at [PortSwigger Web Security Academy](https://portswigger.net/web-security)

---

## 📄 License & Usage

This repository is maintained for educational and security research purposes only. All lab writeups and testing procedures are performed in authorized sandbox environments provided by PortSwigger.
