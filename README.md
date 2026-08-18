# PortSwigger Web Security Academy Labs

A structured collection of hands-on, authorized PortSwigger Web Security Academy lab reports. Each report records the methodology, evidence, impact, and remediation for one specific lab.

General reusable concepts are maintained separately in the [Cybersecurity Knowledge Base](https://github.com/Francisco0604/cybersecurity-knowledge-base).

---

## Progress

| Category | Completed labs | Status |
| :--- | :--- | :--- |
| Access Control | 13 | Completed |
| Authentication | 12 | In progress |

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
- [Lab 01 — Username Enumeration via Different Responses](Authentication/01-username-enumeration-via-different-responses.md)
  - **Vulnerability**: Username Enumeration and Password Brute Force
  - **Concepts**: Burp Intruder (Sniper), Burp Repeater, Response Analysis, Credential Testing
- [Lab 02 — 2FA Simple Bypass](Authentication/02-2fa-simple-bypass.md)
  - **Vulnerability**: Two-Factor Authentication Bypass
  - **Concepts**: Authentication State Analysis, Direct Navigation Bypass, MFA Workflow Flaws
- [Lab 03 — Password Reset Broken Logic](Authentication/03-password-reset-broken-logic.md)
  - **Vulnerability**: Broken Password-Reset Logic
  - **Concepts**: Parameter Tampering, Token-to-Account Binding Flaws, Account Takeover
- [Lab 04 — Username Enumeration via Subtly Different Responses](Authentication/04-username-enumeration-via-subtly-different-responses.md)
  - **Vulnerability**: Username Enumeration and Password Brute Force
  - **Concepts**: Burp Intruder (Grep - Extract), Burp Comparer, Response Analysis, Credential Testing
- [Lab 05 — Username Enumeration via Response Timing](Authentication/05-username-enumeration-via-response-timing.md)
  - **Vulnerability**: Username Enumeration via Response Timing, IP-Based Rate-Limit Bypass, Password Brute Force
  - **Concepts**: Response Timing Analysis, `X-Forwarded-For` Header Spoofing, Burp Intruder (Pitchfork), Rate Limiting Bypass
- [Lab 06 — Broken Brute-Force Protection, IP Block](Authentication/06-broken-brute-force-protection-ip-block.md)
  - **Vulnerability**: Flawed Brute-Force Protection Logic / Cross-Account Reset
  - **Concepts**: Burp Intruder (Pitchfork), Grep - Match, Payload Generation, Counter Reset Logic Flaw
- [Lab 07 — Username Enumeration via Account Lock](Authentication/07-username-enumeration-via-account-lock.md)
  - **Vulnerability**: Username Enumeration via Account-Lock Behavior
  - **Concepts**: Account Lock Oracle, Burp Intruder (Sniper), Grep - Extract, Credential Testing
- [Lab 08 — 2FA Broken Logic](Authentication/08-2fa-broken-logic.md)
  - **Vulnerability**: Broken 2FA Logic / Improper User Binding
  - **Concepts**: Authentication State Analysis, Cookie Manipulation (`verify=carlos`), Session Independence, ffuf MFA Brute Force
- [Lab 09 — Brute-forcing a Stay-Logged-In Cookie](Authentication/09-brute-forcing-stay-logged-in-cookie.md)
  - **Vulnerability**: Weak / Predictable Persistent Authentication Cookie
  - **Concepts**: Cookie Reverse-Engineering, Base64 Decoding, MD5 Hashing, Python Payload Generation, Burp Intruder (Sniper)
- [Lab 10 — Offline Password Cracking](Authentication/10-offline-password-cracking.md)
  - **Vulnerability**: Stored Cross-Site Scripting (XSS) / Sensitive Cookie Disclosure / Predictable Persistent Authentication Cookie
  - **Concepts**: Stored XSS, JavaScript Cookie Exfiltration (`document.cookie`), Exploit Server, Base64 Decoding, Offline MD5 Cracking, Account Takeover
- [Lab 11 — Password Reset Poisoning via Middleware](Authentication/11-password-reset-poisoning-via-middleware.md)
  - **Vulnerability**: Password Reset Poisoning via Attacker-Controlled `X-Forwarded-Host`
  - **Concepts**: Reverse Proxy / Middleware Headers, `X-Forwarded-Host` Manipulation, Password Reset Poisoning, Token Exfiltration, Account Takeover
- [Lab 12 — Password Brute-Force via Password Change](Authentication/12-password-brute-force-via-password-change.md)
  - **Vulnerability**: Password Brute-Forcing through Flawed Password-Change Logic / Response Oracle
  - **Concepts**: Password-Change Functionality, Session Cookie Analysis, Username Parameter Manipulation, Response Oracle (`New passwords do not match` vs `Current password is incorrect`), Burp Intruder (Sniper), Credential Verification, Account Takeover

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
│       ├── 02-2fa-simple-bypass/
│       │   ├── 01-authentication-flow.png
│       │   ├── 02-access-without-mfa.png
│       │   └── 03-carlos-account-and-lab-solved.png
│       ├── 03-password-reset-broken-logic/
│       │   ├── 01-password-reset-request.png
│       │   ├── 02-modified-reset-request.png
│       │   └── 03-carlos-account-and-lab-solved.png
│       ├── 04-username-enumeration-subtly-different-responses/
│       │   ├── 01-grep-extract-username-results.png
│       │   ├── 02-amarillo-password-intruder-results.png
│       │   └── 03-amarillo-account-and-lab-solved.png
│       ├── 05-username-enumeration-via-response-timing/
│       │   ├── 01-xff-rate-limit-bypass.png
│       │   ├── 02-an-password-intruder-results.png
│       │   └── 03-an-account-and-lab-solved.png
│       ├── 06-broken-brute-force-protection-ip-block/
│       │   ├── 01-lockout-behavior.png
│       │   ├── 02-counter-reset-with-wiener.png
│       │   ├── 03-monkey-intruder-match.png
│       │   └── 04-carlos-account-and-lab-solved.png
│       ├── 07-username-enumeration-via-account-lock/
│       │   ├── 01-account-lock-enumeration.png
│       │   ├── 02-apps-lockout-confirmation.png
│       │   ├── 03-mustang-password-result.png
│       │   └── 04-apps-account-and-lab-solved.png
│       ├── 08-2fa-broken-logic/
│       │   ├── 01-2fa-flow-and-verify-cookie.png
│       │   ├── 02-carlos-verify-manipulation.png
│       │   ├── 03-0300-ffuf-match.png
│       │   └── 04-carlos-account-and-lab-solved.png
│       ├── 09-brute-forcing-stay-logged-in-cookie/
│       │   ├── 01-stay-logged-in-cookie-intercepted.png
│       │   ├── 02-base64-decoded-cookie.png
│       │   ├── 03-md5-hash-verification.png
│       │   ├── 04-carlos-cookie-intruder-result.png
│       │   └── 05-carlos-account-and-lab-solved.png
│       ├── 10-offline-password-cracking/
│       │   ├── 01-stay-logged-in-cookie-analysis.png
│       │   ├── 02-xss-comment-payload.png
│       │   ├── 03-carlos-cookie-stolen.png
│       │   ├── 04-hash-cracked.png
│       │   └── 05-carlos-account-deleted-and-lab-solved.png
│       ├── 11-password-reset-poisoning-via-middleware/
│       │   ├── 01-password-reset-request.png
│       │   ├── 02-poisoned-reset-email.png
│       │   ├── 03-carlos-token-exploit-log.png
│       │   └── 04-carlos-account-and-lab-solved.png
│       └── 12-password-brute-force-via-password-change/
│           ├── 01-password-change-recon.png
│           ├── 02-password-change-intruder-setup.png
│           ├── 03-carlos-password-found.png
│           ├── 03b-incorrect-password-response.png
│           └── 04-carlos-account-and-lab-solved.png
├── Authentication/
│   ├── 01-username-enumeration-via-different-responses.md
│   ├── 02-2fa-simple-bypass.md
│   ├── 03-password-reset-broken-logic.md
│   ├── 04-username-enumeration-via-subtly-different-responses.md
│   ├── 05-username-enumeration-via-response-timing.md
│   ├── 06-broken-brute-force-protection-ip-block.md
│   ├── 07-username-enumeration-via-account-lock.md
│   ├── 08-2fa-broken-logic.md
│   ├── 09-brute-forcing-stay-logged-in-cookie.md
│   ├── 10-offline-password-cracking.md
│   ├── 11-password-reset-poisoning-via-middleware.md
│   └── 12-password-brute-force-via-password-change.md
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
    ├── 12-multi-step-process-with-no-access-control-on-one-step.md
    └── 13-referer-based-access-control.md
```

---

## 👤 Author

**Francisco Elroy Afonso**  
*Aspiring Penetration Tester*
