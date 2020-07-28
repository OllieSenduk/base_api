**Run Tests**
docker-compose run app sh -c "python manage.py test"

**Run Tests & Linter**
docker-compose run app sh -c "python manage.py test && flake8"

**Run Migrations**
docker-compose run app sh -c "python manage.py makemigrations core"