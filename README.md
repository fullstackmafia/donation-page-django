# Django Project Template

The clean, fast and right way to start a new Django `1.10.1` powered website.

## Getting Started

Setup project environment with [pipenv]https://pypi.org/project/pipenv/).

```bash
$ pipenv install django
$ pipenv shell

(rave-checkout-python) $ django-admin startproject djangorave
(rave-checkout-python) $ python manage.py startapp payments

# You may want to change the name `djangorave`.
$ django-admin startproject --template https://github.com/fullstackmafia/donation-page-django/archive/master.zip projectname

$ cd projectname/
$ cp settings_custom.py.edit settings_custom.py
$ python manage.py migrate
$ python manage.py runserver
```

## Features

* Basic Django scaffolding (commands, templatetags, statics, media files, etc).
* Split settings in two files. `settings_custom.py` for specific environment settings (localhost, production, etc). `projectname/settings.py` for core settings.
* Simple logging setup ready for production envs.


