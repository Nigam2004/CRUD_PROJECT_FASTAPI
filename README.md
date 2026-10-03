# Project Setup

## Steps to Start the Project

### 1. Create Virtual Environment

```bash
python -m venv venv
```

### 2. Activate Virtual Environment

For **Windows (Git Bash):**

```bash
source venv/Scripts/activate
```

For **Windows CMD:**

```cmd
venv\Scripts\activate
```

For **Windows PowerShell:**

```powershell
venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Start the FastAPI Server

```bash
uvicorn main:app --reload
```

The API will run at:

```text
http://127.0.0.1:8000
```

### 5. Open API Documentation

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

ReDoc:

```text
http://127.0.0.1:8000/redoc
```
