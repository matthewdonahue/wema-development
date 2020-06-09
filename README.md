prototype

# make virtual env using python 3.5>

# make db migrations
`python manage.py makemigrations`

# apply db migrations (this step creates db tables and applies model changes to those tables)
`python manage.py migrate`

# run in server folder in virtual env
`python manage.py runserver`

# visit site at localhost:8080
# visit django admin page localhost:8000/admin

# create superuser so sign into the site and use the admin page
`python manage.py createsuperuser`

# you can also create a user on the page without admin priviledges
