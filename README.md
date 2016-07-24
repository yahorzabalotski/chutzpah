# chutzpah
Chutzpah service.

# Running in development
```
git clone https://github.com/yahorzabolotsky/chutzpah
cd chutzpah
virtualenv venv
. venv/bin/activate
pip install -r requirements/dev.txt
python manage.py migrate
python manage.py runserver
```
