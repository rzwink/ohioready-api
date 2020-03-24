![ERD](https://github.com/rzwink/ohioready-api/raw/master/ohioready_logo.png "ERD")


## Install

### Install Python3 + Pip + Virtualenv
```shell script
virtualenv venv -p python3
. ./venv/bin/activate
pip install -r requirements.txt
```
### If you are going to modify this script then take advantage of pre-commit hooks
```shell script
pip install pre-commit
pre-commit install
```

## Run locally
```shell script
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

```
1. To access the admin portal open a web browser and go to http://127.0.0.1:8000/admin/

# Entity Relationship Diagram
![ERD](https://github.com/rzwink/ohioready-api/raw/master/erd.png "ERD")
