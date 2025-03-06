E-Book API

1-pip install -r requirements.txt

2- python manage.py makemigrations/migrate

3-To ensure the project works correctly, create a .env file and assign values to the keys from the .env sample file.

Sign up on https://dashboard.stripe.com/ as a test account and obtain values for SECRET_KEY and PUBLIC_KEY


docker-compose exec web python manage.py createsuperuser

celery -A config worker -l info --pool=solo docker-compose

docker-compose run web python3 manage.py createsuperuser

NEW CHANGES ✅ Refactoring according to best practises ✅ Added dotenv for security ✅ Custom Permissions ✅ Order Books ✅ replenish and reduce stock of books ✅ Django signals, integration to telegram bot