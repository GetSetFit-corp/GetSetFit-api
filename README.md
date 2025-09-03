# GetSetFit-API

## Pre-requisite
- Install postgres database

## Starting Project
### Using terminal
- Make sure you are on the root directory of project
- `pip install -r requirements.txt`
- `pip install -r requirements-dev.txt`
- `uvicorn app.main:app --reload`
- Verify in browser `http://localhost:8000/docs`

### Using Docker
- install docker using colima
  - brew install colima
  - colima start
- docker-compose up --build (This will build and start the dev server)

### Using Pycharm
- Go to run.py
- Run the file
