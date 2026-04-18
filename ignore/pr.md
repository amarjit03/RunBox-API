# 🚀 Piston-like Code Execution Engine (Python) — Development Roadmap

This document outlines a **phase-by-phase plan** to build a secure, scalable code execution engine similar to Piston using Python.

---

# 📌 Project Goal

Build a system that:

* Executes user-submitted code safely
* Supports multiple languages
* Uses sandboxing (Isolate)
* Scales via worker queues
* Provides API + CLI interface

---

# 🧱 Phase 1: Project Setup & Basic API

## 🎯 Objective

Create a working FastAPI server.

## 🛠 Tasks

* Initialize project structure
* Setup virtual environment (Poetry / venv)
* Install dependencies (`fastapi`, `uvicorn`)
* Create `/health` endpoint

## 📂 Key Files

* `api/app/main.py`
* `config.py`

## ✅ Output

* Server runs successfully
* `GET /health → {"status": "ok"}`

---

# 🧩 Phase 2: Runtime Registry

## 🎯 Objective

Load and manage available runtimes dynamically.

## 🛠 Tasks

* Parse `packages/*/metadata.json`
* Create runtime class
* Store runtimes in memory

## 📂 Key Files

* `runtime.py`
* `packages/*/metadata.json`

## ✅ Output

* `GET /runtimes` returns available languages

---

# ⚙️ Phase 3: Basic Code Execution (Unsafe)

## 🎯 Objective

Execute code locally for testing.

## 🛠 Tasks

* Accept code input via API
* Write code to temp file
* Execute via `subprocess`

## 📂 Key Files

* `job.py`
* `executor.py`

## ✅ Output

```json
POST /execute
{
  "language": "python",
  "code": "print('hello')"
}

Response:
{
  "output": "hello\n"
}
```

---

# 🔒 Phase 4: Sandbox Integration (Isolate)

## 🎯 Objective

Run code securely in isolation.

## 🛠 Tasks

* Integrate `isolate --init`
* Execute code with `isolate --run`
* Cleanup using `isolate --cleanup`

## 📂 Key Files

* `sandbox.py`
* Update `job.py`

## ✅ Output

* Code runs in isolated environment
* No system access
* No network access

---

# ⏱️ Phase 5: Resource Limits & Status Handling

## 🎯 Objective

Enforce execution constraints.

## 🛠 Tasks

* Add limits:

  * CPU time
  * Wall time
  * Output size
* Parse isolate metadata
* Map status codes (RE, TO, SG, etc.)

## ✅ Output

```json
{
  "status": "TO",
  "output": ""
}
```

---

# 🌐 Phase 6: Multi-language Support

## 🎯 Objective

Support compiled & interpreted languages.

## 🛠 Tasks

* Add compile step support
* Use runtime scripts (`compile`, `run`)
* Handle different languages (Python, C++, Rust)

## 📂 Key Files

* `packages/*`
* `runtime.py`

## ✅ Output

* Execute multiple languages successfully

---

# 🔄 Phase 7: Worker Queue (Scalability)

## 🎯 Objective

Decouple execution from API.

## 🛠 Tasks

* Integrate Redis
* Setup worker (Celery / RQ)
* Push jobs to queue

## 📂 Key Files

* `workers/worker.py`

## ✅ Output

Flow:

```
API → Queue → Worker → Sandbox → Result
```

---

# 📦 Phase 8: Package Manager

## 🎯 Objective

Install/remove runtimes dynamically.

## 🛠 Tasks

* Extract `.pkg.tar.gz`
* Maintain runtime directory
* Update runtime registry

## 📂 Key Files

* `package_manager.py`

## ✅ Output

* Install new language versions dynamically

---

# 💻 Phase 9: CLI Tool

## 🎯 Objective

Provide developer interface.

## 🛠 Tasks

* Build CLI using Typer/Click
* Add commands:

  * execute
  * runtimes
  * packages

## 📂 Key Files

* `cli/main.py`

## ✅ Output

```bash
piston-py execute -l python -c "print(123)"
```

---

# 🐳 Phase 10: Dockerization & Deployment

## 🎯 Objective

Prepare for production deployment.

## 🛠 Tasks

* Create Dockerfile
* Add docker-compose
* Setup isolate in container

## 📂 Key Files

* `Dockerfile`
* `docker-compose.yaml`

## ✅ Output

```bash
docker-compose up
```

---

# 🧪 Phase 11: Testing & Security

## 🎯 Objective

Ensure robustness.

## 🛠 Tasks

* Add unit tests
* Add adversarial tests:

  * fork bomb
  * memory abuse
  * network attempts

## 📂 Key Files

* `tests/`

## ✅ Output

* System resists malicious code

---

# 🚀 Final Architecture

```
Client (CLI / HTTP)
        ↓
     FastAPI
        ↓
   Job Queue (Redis)
        ↓
     Worker
        ↓
   Sandbox (Isolate)
        ↓
   Runtime (Python/C++)
```

---

# 📊 Summary

| Phase | Result            |
| ----- | ----------------- |
| 1     | API running       |
| 2     | Runtime detection |
| 3     | Code execution    |
| 4     | Secure sandbox    |
| 5     | Limits & status   |
| 6     | Multi-language    |
| 7     | Scalable workers  |
| 8     | Package manager   |
| 9     | CLI tool          |
| 10    | Dockerized        |
| 11    | Tested & secure   |

---

# 💡 Notes

* Phase 4 (sandboxing) is the most critical
* Phase 7 (workers) enables scalability
* Always keep execution isolated from API

---

# 🎯 Next Steps

Start with:

```
Phase 1 → Phase 2 → Phase 3
```

Then move to:

```
Phase 4 (Security Core)
```

---

**End of Roadmap**
