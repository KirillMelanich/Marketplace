# Marketplace

## Overview:
The "Marketplace" is a fully-fledged online store built on Django. Users can browse and purchase a variety of products, facilitated by the secure online payment system, Stripe. The entire functionality is implemented following the best programming practices of the Django framework.

## Technologies used
- Python3
- Django
- Django Rest Framework
- Docker
- Nginx
- Postgres
- HTML
- CSS
- JavaScript
- Stripe
- Celery
- Redis Broker
- Gunicorn
- Ajax
- Swagger
- Webhook
- Faker
- HTMX
- Djoser
- Redoc
- Google fonts
- Signals
- and many others

## Installation 
1. Clone the repository:
   ```shell
   https://github.com/KirillMelanich/Marketplace.git
2. Run Docker Desktop 
   
3. Build the project locally using Docker Compose:
   ```shell
   sudo docker-compose build
4. Run the project:
   ```shell
   sudo docker-compose build
5. After running project create superuser:
   ```shell
   sudo docker exec -it marketplace-backend python manage.py createsuperuser
   
6. Fill empty shop with fake categories and products to visualize how the project works:
   ```shell
   sudo docker exec -it marketplace-backend python manage.py fakeproducts

7. Enjoy the Marketplace!

## Future Improvements
    This project is a work in progress and will be improved further.