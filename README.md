install python3-pip
pip3 install virtualenv
virtualenv djangoenv
source djangoenv/bin/activate
in win case: djangoenv\Scripts\activate

pip install -r requirements.txt

pip install Pillow
pip install django-debug-toolbar
pip install django-ckeditor
pip install django-simple-captcha
pip install django-db-mailer

python manage.py migrate
python manage.py createsuperuser

In file olgaproject/settings.py add EMAIL_HOST_USER, EMAIL_HOST_PASSWORD
Registrate other user for test sending emails

python manage.py crontab add (not in win!)
in win case: python manage.py parse_articles, python manage.py email_sender
