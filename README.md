**Run Tests**
docker-compose run app sh -c "python manage.py test"

**Run Migrations**
docker-compose run app sh -c "python manage.py makemigrations core"