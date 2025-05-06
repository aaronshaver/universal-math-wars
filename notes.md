# Notes

## Run tests + get coverage report

clear && pytest --cov=registration --cov-report=term-missing

## Run database

docker run --name mysql-dev -e MYSQL_ROOT_PASSWORD=root_password -e MYSQL_DATABASE=mathwars_db -e MYSQL_USER=dev_user -e MYSQL_PASSWORD=dev_password -p 3306:3306 -d mysql:8.0

## Config file

/frontend/.env.development

```
VITE_API_BASE_URL=http://localhost:8000
```

/backend/.env

```
DB_USER=dev_user
DB_PASSWORD=dev_password
DB_HOST=localhost # Or your MySQL host
DB_PORT=3306
DB_NAME=mathwars_db
```