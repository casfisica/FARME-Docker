

# FARME-Docker
https://youtu.be/YGrfexNwsFU

Python FastAPI, React, and MongoDB (FARM) Stack Using Docker Compose
```bash
PYTHONVERSION=$(python3 --version)
python3 -m virtualenv venv
source ./venv/bin/activate
pip install fastapi uvicorn
pip freeze > requirements.txt
docker build -t farmedoc .
docker run -d --name farmecont -p 80:80 farmedoc
```

The other way is using docker-compose
```bash
docker-compose up
```