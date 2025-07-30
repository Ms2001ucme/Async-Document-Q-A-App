# 📄 Async Document Q&A Backend (FastAPI + PostgreSQL)

This is a backend microservice built using **FastAPI**, **PostgreSQL**, and **async SQLAlchemy**.  
It allows users to:
- Upload documents (title & content)
- Retrieve documents by ID
- Extendable to add async Q&A feature with background tasks

---

## 🚀 Features
- **FastAPI** for high-performance async APIs
- **PostgreSQL** as the database using `asyncpg`
- **SQLAlchemy (Async)** as ORM
- **Pydantic v2** for schema validation

---

## 📂 Project Structure
app/
app/
├── crud.py # CRUD operations
├── database.py # Database connection & session management
├── main.py # FastAPI entrypoint
├── models.py # SQLAlchemy models
├── schemas.py # Pydantic schemas
├── services.py # Async background tasks (future)
│
├── requirements.txt # Dependencies
└── README.md # Documentation

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository
```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>
2️⃣ Create & activate virtual environment
bash
Copy
Edit
# Windows (PowerShell)
python -m venv venv
.\venv\Scripts\Activate.ps1

# macOS/Linux
python3 -m venv venv
source venv/bin/activate

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Configure DATABASE_URL
DATABASE_URL=postgresql+asyncpg://postgres:your_password@127.0.0.1:5432/docqa

5️⃣ Start PostgreSQL (if not running)
# Windows: Use pgAdmin or PostgreSQL service
# Linux/macOS:
sudo service postgresql start

6️⃣ Run the app
uvicorn app.main:app --reload
App → http://127.0.0.1:8000

Swagger Docs → http://127.0.0.1:8000/docs

---

🗂️ API Endpoints
Endpoint	Method	Description
/documents/	POST	Upload a document (title + content)
/documents/{id}	GET	Retrieve a document
/documents/{id}/question	POST	Submit a question related to a document
/questions/{id}	GET	Retrieve status (pending or answered) and the answer

---

🤝 Contributing
Fork the repository

Create a new branch (git checkout -b feature-name)

Commit changes and push

Create a Pull Request

---
