# Lab 01: Basic Burp Repeater Workflow & Parameter Analysis

## 📌 Lab Overview
* **Platform**: PortSwigger Web Security Academy
* **Category**: Information Gathering & Burp Suite Basics
* **Objective**: Capture an active HTTP request in Burp Proxy, isolate controllable input parameters, re-issue the request in Burp Repeater with single-variable modifications, and analyze the response behavior.

---

## 🛠️ Requirements & Tools Used
* **Tool**: Burp Suite (Community / Professional Edition)
* **Client**: Embedded Chromium Browser
* **Feature Scope**: Burp Proxy, HTTP History, Burp Repeater

---

## 📋 Step-by-Step Walkthrough

### 1. Launch & Target Navigation
1. Open Burp Suite and navigate to **Proxy** -> **Intercept**.
2. Click **Open Browser** to launch Burp's embedded Chromium browser.
3. Access the target lab URL.

### 2. Traffic Capture & Selection
1. Browse to a functional page on the target website (e.g., viewing a product detail page or profile page).
2. Open **Proxy** -> **HTTP History** in Burp Suite.
3. Locate the target request (e.g., `GET /product?productId=1 HTTP/2`).

### 3. Send Request to Repeater
1. Right-click the request in the HTTP History log.
2. Select **Send to Repeater** (Keyboard shortcut: `Ctrl + R`).
3. Switch to the **Repeater** tab.

### 4. Establish Baseline Response
1. In Repeater, click **Send** without modifying any headers or parameters.
2. Record the baseline HTTP response details:
   * **Status Code**: `200 OK`
   * **Content Length**: Record original byte size
   * **Body**: Standard page output for `productId=1`

### 5. Parameter Manipulation & Delta Analysis
1. Change `productId=1` to `productId=2` in the request pane.
2. Click **Send**.
3. Compare response parameters against baseline:

```http
GET /product?productId=2 HTTP/2
Host: target-lab.web-security-academy.net
Cookie: session=sample_session_id
```

---

## 🔍 Key Findings & Takeaways
* **Single Variable Rule**: Modifying one parameter at a time provides clear visibility into backend logic changes.
* **Repeater Utility**: Repeater allows rapid request replaying without interfering with active browser state or re-authenticating repeatedly.
