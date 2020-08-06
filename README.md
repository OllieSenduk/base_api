**Run Tests**
docker-compose run --rm app sh -c "python manage.py test"

**Run Tests & Linter**
docker-compose run app sh -c "python manage.py test && flake8"

**Run Migrations**
docker-compose run app sh -c "python manage.py makemigrations core"

**Create a new app**
<!-- Example for a user app -->
docker-compose run --rm app sh -c "python manage.py startapp user"