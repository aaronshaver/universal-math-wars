# Notes

## Run local dev environment

docker compose up --build

## Run tests + get coverage report

clear && poetry run pytest --cov-report=term-missing

## Config file

/frontend/.env.development

```
VITE_API_BASE_URL=http://localhost:8000
```