# conda create -p djangoenv python=3.9


# conda activate F:\DataScience\projects\learningDjango\djangoenv

# django-admin startproject learningdjango - create django project

# python manage.py runserver - runserver.

# python manage.py startapp login # create login app

# python manage.py runserver

# python manage.py migrate - after updating html templates and adding in settings.py

# python manage.py makemigrations login - create model for login and migratingpy manage.py migrate created login/migrations/0001_initial.py

# python manage.py migrate - Django will create and execute an SQL statement for login.oo1_initial.py

# python manage.py sqlmigrate login 0001 # crete table query for login

# python manage.py shell

# from login.models import Login
# Login.objects.all()
# login = Login(login="admin", pwd="hello")
# login.save()
