INICIAR O PROJETO DJANGO

```
python -m venv venv
.venv/scripts/activate
pip install django
django-admin startproject project .

```
GIT
```
  git init
  git commit -m "first commit"
  git branch -M main
  git remote add origin git@github.com:Lucas-menezzes/project-django.git
  git push -u origin main 
  
migrando a base dados

python manage.py makemigrations
python manage.py migrate

criando super user

python manage.py createsuperuser
python manage.py changepassword username