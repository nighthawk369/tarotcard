

django-admin startproject tarot_project
cd tarot_project/
python manage.py startapp tarot_app
then add the tarot_app in INSTALLED APP inside setting.py

python3 manage.py collectstatic

add in model.py
python manage.py makemigrations tarot_app
python manage.py migrate
python3 manage.py createsuperuser
python3 manage.py runserver

to remove node

node -v
sudo rm -rf /usr/local/bin/npm /usr/local/share/man/man1/node* ~/.npm
sudo rm -rf /usr/local/lib/node*
sudo rm -rf /usr/local/bin/node*
sudo rm -rf /usr/local/include/node*
sudo apt-get purge nodejs npm
sudo apt autoremove

sudo apt install npm
npm cache clean -f 
sudo npm install -g n
sudo n latest 

close terminal and open another

pip install djangorestframework

for rest_framework

python3 manage.py


context to use in views.py and also render the context.

code bootstrap se chaapo

variables in html

<body>
    Your attacted card is <b>{{data}}</b>
    <!-- Display the image -->
    <!-- <img src="{{ my_instance.image.url }}" alt="Image" width="200"> -->
    
    <title>This is a text page</title>
    <!-- Other content -->
<p>Lorem ipsum, dolor sit</p>
