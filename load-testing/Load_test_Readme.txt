# JMeter Test Plan – n11.com Search Module

## 📌 Overview
This JMeter test plan demonstrates load and functional testing for the **n11.com search module**, covering **positive, negative, and edge-case scenarios**.

The test is designed to validate search behavior under different input conditions and simulate realistic user interactions.

---

## 🛠️ Tools Used
- **Apache JMeter** – for load and API-level testing
- **HTTP Request Defaults** – defines base URL and protocol
- **HTTP Header Manager** – simulates real browser headers
- **HTTP Cookie Manager** – manages session persistence
- **Regex Extractor** – extracts dynamic values from responses
- **If Controller** – enables conditional execution
- **Assertions** – validates response codes and content
- **Debug Sampler & View Results Tree** – debugging and validation

---

## 📂 Test Scenarios

### 🔹 Search Laptop
- Valid search request
- Validates response content and behavior

### 🔹 Search Special Characters
- Tests invalid/special input handling
- Validates server response stability

### 🔹 Search Without Input
- Tests default behavior when no query is provided

### 🔹 Conditional Scenarios
- Recently Viewed
- Popular Searches
- View All

Implemented using **If Controllers** with extracted response data.

---

## ⚠️ Notes / Limitations
- Some elements (autocomplete, recently viewed, delete all) are **rendered via JavaScript** and are not part of raw HTTP responses.
- These elements **cannot be fully validated using JMeter**.
- **Delete All** is a client-side action and not testable via HTTP requests.
- Multiple samples may appear due to redirects; **final response is used for validation**.

---

## ▶️ How to Run the Test

### 🔹 Option 1: Run via JMeter GUI
1. Open **Apache JMeter**
2. Go to **File → Open**
3. Select: n11_search_test_plan.jmx
4. Click **Start (▶)** to run the test
5. View results using:
- View Results Tree
- Summary Report
- Aggregate Report

---

### 🔹 Option 2: Run via Command Line (Recommended 🚀)

Run the test in non-GUI mode:

```bash
jmeter -n -t n11_search_test_plan.jmx -l results.jtl

###🔹 Generate HTML Report

Run the test in non-GUI mode:

```bash
jmeter -n -t n11_search_test_plan.jmx -l results.jtl -e -o report