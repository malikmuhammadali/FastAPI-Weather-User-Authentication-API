
# FastAPI Task Project

# Project Overview
This project is built using **FastAPI**. It includes user registration, login with JWT authentication, and a weather forecast feature.

**Features:**
- `POST /signup` → Register a new user
- `POST /login` → Login a user and get JWT token
- `GET /weather?city=CityName` → Get 7-day weather forecast for a city
- `GET /` → Root endpoint for a welcome message


## Project Structure

FastAPI Weather & User Authentication API/           ← Root folder 
│
├─ main.py                  ← FastAPI main application
├─ auth.py                  ← User signup/login endpoints
├─ weather.py               ← Weather endpoint
├─ models.py                ← SQLAlchemy models
├─ database.py              ← Database connection setup
├─ create_tables.py         ← Script to create database tables
├─ config.json              ← Database credentials & API key
├─ requirements.txt         ← Python dependencies
└─ README.md   

## Setup Instructions

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Configure Database
Update `config.json` with your database credentials and API key:
```json
{
    "db_host": "localhost",
    "db_port": 5432,
    "db_name": "fastapi_users",
    "db_user": "postgres",
    "db_password": "YourPasswordHere",
    "weather_api_key": "YourOpenWeatherMapAPIKey"
}
```

### 3. Create Database Tables
```bash
python create_tables.py
```

### 4. Run FastAPI Server
```bash
uvicorn main:app --reload
```

- Server runs at `http://127.0.0.1:8000`

## Testing Endpoints

### Signup a User
```bash
curl -X POST "http://127.0.0.1:8000/signup?username=ali&email=ali@test.com&password=123"
```

### Login User
```bash
curl -X POST "http://127.0.0.1:8000/login?email=ali@test.com&password=123"
```

### Get Weather Forecast
```bash
curl -X GET "http://127.0.0.1:8000/weather?city=Lahore"
```

## Verify Database Records
```sql
SELECT * FROM users;
```

## Notes
- Passwords are hashed.
- Internet connection required for weather API.
- Use the same email for login as used during signup.

   "# FastAPI-Weather-User-Authentication-API" 
