# Zmienne
PYTHON = python
PIP = pip
PROJECT_NAME = WMS-Django

# Cele
.PHONY: install run test lint format

install:
	$(PIP) install --upgrade $(PIP) &&\
		$(PIP) install -r requirements.txt

migrate:
	python manage.py makemigrations
	python manage.py migrate

run:
	$(PYTHON) manage.py runserver

test:
	$(PYTHON) manage.py test

lint:
	pylint *.py --exit-zero

format:
	black *.py

all: lint format install test
