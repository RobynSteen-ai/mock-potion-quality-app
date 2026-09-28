# Mock Potion Quality App

A Flask API created as a mock DevOps coursework project. The application
classifies potion samples using pH and visual clarity.

## Quality classifications

- **Approved:** pH 5.5–7.5 and clear
- **Review Required:** pH 4.0–9.0 but not approved
- **Rejected:** pH outside the review range
- Invalid pH or clarity values return HTTP 400

## Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/` | Application information |
| GET | `/health` | Application health check |
| POST | `/assess` | Assess potion quality |

## Local setup

```bash
python3 -m venv venv
source venv/bin/activate
python -m pip install -r requirements.txt
python app.py
