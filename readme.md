# conda create -p djangoenv python=3.9

# conda activate F:\DataScience\projects\learningDjango\djangoenv

# pip install -r requirements.txt

# django-admin startproject learningdjango - create django project

# python manage.py runserver - runserver.

# python manage.py startapp login # create login app

# after updating urls.py and views.py of loging app check it 
# python manage.py runserver

# python manage.py migrate - after updating html templates and adding in settings.py of loginapp

# after adding table details in models.py of login 
# python manage.py makemigrations login - create model for login and migratingpy manage.py migrate created login/migrations/0001_initial.py

# python manage.py migrate - Django will create and execute an SQL statement for login.oo1_initial.py

# python manage.py sqlmigrate login 0001 # crete table query for login

# python manage.py shell

# from login.models import Login
# Login.objects.all()
# login = Login(login="admin", pwd="hello")
# login.save()
# Login.objects.all().values() - show table values

<!-- member1 = Member(firstname='Tobias', lastname='Refsnes')
>>> member2 = Member(firstname='Linus', lastname='Refsnes')
>>> member3 = Member(firstname='Lene', lastname='Refsnes')
>>> member4 = Member(firstname='Stale', lastname='Refsnes')
>>> member5 = Member(firstname='Jane', lastname='Doe')
>>> members_list = [member1, member2, member3, member4, member5]
>>> for x in members_list:
>>>   x.save() -->

# change/update data of login table..
<!-- x = Login.objects.all()[0] 
x.login
x.login = "admin1"
x.save()
Login.objects.all().values() 


x.delete() -- to delete data...
-->

# updating template file login/templtes/login.html

# updating login/views.py -- setting templte as output...

# python manage.py runserver


# updateing login tables... adding few more columns...
# python manage.py makemigrations login

