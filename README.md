# 🐾 Backend‑SpyCatAgency

A Django REST API for managing **Spy Cats**, **Missions**, and **Targets** in a “Spy Cat Agency”. This application showcases CRUD operations and validation logic to ensure mission assignments and target status constraints are properly enforced.

---

## ✅ Features

### 🐱 Spy Cats
- **Create** a spy cat (fields: name, experience years, breed, salary)
- **List** all spy cats
- **Retrieve** a single spy cat
- **Update** only the spy cat’s salary
- **Delete** a spy cat

### 🎯 Missions & Targets
- **Create** missions along with 1–3 targets in a single request
- **Assign** a spy cat to a mission (only if not already on another mission)
- **List** all missions
- **Retrieve** a single mission with its targets
- **Update** mission—fields allowed:
  - `cat` (forces validation)
  - `is_completed`
- **Mark** targets as completed
- **Update** notes on targets (disallowed if `target` or `mission` is completed)
- **Delete** missions only if **no cat is assigned**

---

## 🔧 Tech Stack
- **Backend**: Django + Django REST Framework
- **Database**: SQLite (default) | Configurable to PostgreSQL, MySQL, etc.
- **Testing**: (Optional) Add tests for endpoint and business rules coverage

---

## 🛠️ Setup Instructions

1. **Clone the repo**
    git clone https://github.com/shabnamadil/Backend-SpyCatAgency.git
    cd Backend-SpyCatAgency

2. **Create & activate virtual environment**
    python3 -m venv venv
    source venv/bin/activate

3. **Install dependencies**
    make install

4. **Apply migrations**
    make migrate-all

5. **Run the server**
    make build

---

## 🚀 API Endpoints Collection

https://.postman.co/workspace/My-Workspace~fd87af34-8156-4a5c-8fda-aef4c1ea92dd/collection/28122193-d90b292e-a1b4-4844-80ca-ec740a5bf499?action=share&creator=28122193

### 🐾 SpyCat Endpoints

| Method | Endpoint             | Description                             |
|--------|----------------------|-----------------------------------------|
| GET    | `/cats/`             | List all spy cats                       |
| POST   | `/cats/`             | Create a spy cat |
| GET    | `/cats/{id}/`        | Retrieve a specific spy cat             |
| PATCH  | `/cats/{id}/`        | Partially update (only `salary`)        |
| DELETE | `/cats/{id}/`        | Delete a spy cat                        |
| GET    | `/spycat/breeds/`    | Get all breeds                          |

### 🎯 Mission & Target Endpoints

| Method | Endpoint                                | Description |
|--------|-----------------------------------------|----------------------------------------------|
| GET    | `/missions/`                            | List all missions                            |
| POST   | `/missions/`                            | Create mission **with targets**              |
| GET    | `/missions/{id}/`                       | Retrieve a specific mission (with targets)   |
| PATCH  | `/missions/{id}/`                       | Update `is_completed` **and/or** assign cat  |
| DELETE | `/missions/{id}/`                       | Delete a mission (only if unassigned)        |
| PATCH  | `/targets/{id}`                         | Mark a target as completed                   |
| PUT/PATCH | `/targets/{id}/`                     | Update target notes **only if not completed**|

---

## ✅ Validation Rules

1. **Breed field**: validated against a predefined list (It is scrapped data via python)
2. **Notes**: cannot be changed after the target and its parent mission is marked completed
3. **Mission deletion**: disallowed if a cat is currently assigned
4. **Single mission per cat**: a cat cannot be assigned to more than one active mission simultaneously


## 🧪 Running Linters & Formatters

To maintain a clean and professional codebase, the project uses several tools for linting, formatting, security, and type checking. You can run them using the following `make` commands:


### ✅ 1. `make enable-pre-commit-hooks`
Installs the pre-commit Git hooks defined in .pre-commit-config.yaml file. These hooks run automatically before every commit to enforce code quality checks (e.g., formatting, linting).
💡 Tip: Run this once after cloning the repo to ensure Git hooks are enabled.

### ✅ 2. `make format`
Auto-formats your Python code using:

- black – for consistent code style
- isort – to sort imports
- autopep8 – to fix PEP8 issues
- autoflake – to remove unused imports and variables

### ✅ 3. `make lint`
Checks the code for common style and complexity issues using:

- flake8 – for style violations and complexity checks
- black and isort – in check mode (does not modify files)

### ✅ 4. `make secure`
Runs a security analysis using bandit, focusing on high-severity and high-confidence vulnerabilities.

### ✅ 5. `make type-check`
Performs static type checking using mypy with support for Django via django-stubs.