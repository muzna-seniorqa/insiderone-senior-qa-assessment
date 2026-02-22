# API Automation – Swagger Petstore

## 📌 Overview
This project demonstrates API automation for the **Swagger Petstore API**, focusing on the **pet endpoints**.

The test suite covers CRUD operations with comprehensive **positive, negative, and edge case scenarios**.  
Tests are implemented using **Postman** and can be executed via **Newman CLI** for automation and CI/CD integration.

---

## 🛠️ Tools & Technologies
- Postman (API test creation and validation)
- Newman (CLI execution for automation)
- Swagger Petstore API

---

## 📂 Test Coverage

### 1. Create Pet (`POST /pet`)
- ✅ Positive:
  - Add a new pet with valid data
- ❌ Negative:
  - Missing fields
  - Empty name
  - Invalid data types
  - Invalid status
  - Negative ID
  - Duplicate ID
  - Unsupported media type

---

### 2. Get Pet (`GET /pet/{petId}`)
- ✅ Positive:
  - Fetch existing pet
- ❌ Negative:
  - Non-existent pet
  - Invalid ID
  - Decimal ID
  - Negative ID
- ⚠️ Edge Case:
  - SQL Injection attempt

---

### 3. Update Pet (`PUT /pet`)
- ✅ Positive:
  - Update existing pet with valid data
- ❌ Negative:
  - Missing fields
  - Invalid ID types
  - Non-integer ID
  - Negative ID
  - Empty body
  - Invalid status
  - Malformed JSON

---

### 4. Delete Pet (`DELETE /pet/{petId}`)
- ✅ Positive:
  - Delete existing pet
- ❌ Negative:
  - Non-existent pet
  - Invalid ID
  - Negative/zero ID
  - Missing path parameter

---

## ✅ Assertions Strategy
- Folder-level assertions used for reusable validations across similar requests
- Request-level assertions applied for specific response validation
- Status codes, response structure, and error handling validated

---

## ⚙️ Setup & Execution

### 🔹 Option 1: Run using Postman (Manual)
1. Import the collection:
   - `insiderone-petstore-api-automation.postman_collection.json`
2. Import the environment:
   - `insiderone-petstore-api-automation.postman_environment.json`
3. Select environment: **Swagger Petstore Environment**
4. Click **Run Collection**

---

### 🔹 Option 2: Run using Newman (Recommended 🚀)

#### Install Newman:
```bash
npm install -g newman


### Run collection:
```bash
newman run insiderone-petstore-api-automation.postman_collection.json -e insiderone-petstore-api-automation.postman_environment.json


### Generate HTML Report:
```bash
npm install -g newman-reporter-htmlextra

newman run insiderone-petstore-api-automation.postman_collection.json \
-e insiderone-petstore-api-automation.postman_environment.json \
-r cli,htmlextra \
--reporter-htmlextra-export "Petstore API report.html"
