
## Commands used to develop this application

### Python

  $ py -m venv .env
> **Explanation**: **-m venv** installs virtual environment; **.env** specify in which folder it'll be installed

$ call venv_folder_name/Scripts/activate
> **Explanation**: start virtual environment

### PIP

  $ pip install django -U
> **Explanation**: **-U** installs the lastest version

### Django

#### django-admin

  $ django-admin startproject project_name folder_name
> **Explanation**: **startproject** creates a project in the given folder

## manage.py

  $ py manage.py runserver
> **Explanation**: **runserver** self explanatory

  $ py manage.py startapp app_name
> **Explanation**: **startapp** self explanatory

  $ py manage.py migrate
> **Explanation**: perform migrations, basically executes migrations execute to update the DB

  $ py manage.py makemigrations
> **Explanation**: looks out for the changes into models and creates a scripts to executes the changes with the previous command

  $ py manage.py validate
> **Explanation**: self explanatory

  $ py manage.py shell
> **Explanation**: opens interactive console with django

  $ py manage.py createsuperuser
> **Explanation**: self explanatory


# PDB
  (Pdb) **continue** continue the execution