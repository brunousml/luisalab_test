install.requirements:


start: install.requirements
	python manage.py test && python manage.py runserver