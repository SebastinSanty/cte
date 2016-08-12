# CTE

##Setup Instructions

1. Setup Python Virtual Environment (virtualenv): `virtualenv erp` .
2. Go into the Virtual Enviroment: `cd erp`
3. Activate virtualenv: `source bin/activate`
4. Clone this repository: `git clone <url of repo> cte`
5. Go into the cloned repository: `cd cte`
7. Webserver runs for default on `localhost:8000`. To set the port manually run `python manage.py runserver 8080` for `localhost:8080`

##Login Credentials
1. Admin panel at: `localhost:8000/admin`. Username for admin: `admin`. Password: `123`

##Authors
Developers: Sebastin, Divyansh

##Contribution Guidelines

###For Front-end contributors (HTML, CSS, JS)
To edit the templates, go to the templates folder which has all the templates. Note that direct links \(\<a href\>\) won't work in Django backend. Hence please route it through the urls.py in cte folder.

###For Backend contributors (Python (Django))


##License
Coming soon