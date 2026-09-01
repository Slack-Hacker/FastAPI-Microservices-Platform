# ⚡ Modular Async Microservices Platform

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100%2B-009688.svg)](https://fastapi.tiangolo.com/)
[![Pydantic](https://img.shields.io/badge/Pydantic-v2-E92063.svg)](https://docs.pydantic.dev/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A production-ready **Asynchronous Microservices & REST API Framework** built with **FastAPI**, **Pydantic v2**, and **JWT Authentication**.

Designed by **Slack-Hacker** for building modular, enterprise-grade backend services with automated OpenAPI documentation and health monitoring.

---

## 🌟 Key Capabilities

- **⚡ Asynchronous FastAPI Routing**: High-concurrency REST API handlers (`app/main.py`).
- **🔐 JWT Authentication Router**: Modular registration and login handlers (`app/routers/auth.py`).
- **🛡️ Strict Data Validation**: Request & response DTO validation using Pydantic v2 schemas (`app/schemas/user.py`).
- **⚙️ Environment Configuration**: Automated Pydantic BaseSettings management (`app/config.py`).

---

## 📁 Repository Structure

```
project_ankit/
├── app/
│   ├── main.py             # FastAPI entrypoint, CORS & middleware
│   ├── config.py           # Pydantic BaseSettings configuration
│   ├── routers/            # Modular API endpoints (Auth, Tasks)
│   └── schemas/            # Request & response data validation DTOs
├── requirements.txt        # Project dependencies
├── .gitignore              # Git ignore rules
└── README.md               # Project documentation
```

---

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/Slack-Hacker/project_ankit.git
cd project_ankit
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run FastAPI Application

```bash
python -m uvicorn app.main:app --reload
```

Navigate to **`http://localhost:8000/docs`** for interactive Swagger API documentation.

---

## 📜 License

Distributed under the MIT License. See `LICENSE` for details.
