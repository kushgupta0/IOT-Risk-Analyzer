# IoT Risk Analyzer

A backend tool that helps you **analyze the security risk of any IoT device** (like smart plugs, cameras, routers) using public CVE data.

---

## Features

- Search for public CVEs related to an IoT device
- Calculate a simple risk score based on bug count
- FastAPI-powered API — clean, fast, and testable
- Easy to run locally and test via browser

---

## Tech Stack

- Python 3.9+
- FastAPI
- Requests (for CVE API)
- CVE CIRCL API (https://cve.circl.lu/)

---

## Install & Run

### 1. Clone this repo

```bash
git clone https://github.com/kushgupta0/IOT-Risk-Analyzer.git
cd IOT-Risk-Analyzer/backend
