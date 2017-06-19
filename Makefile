install.requirements:
	pip install -r requirements.txt

start: install.requirements
	python manage.py test && python manage.py runserver

test.api.get.employee:
	curl -H "Content-Type: application/javascript" http://localhost:8000/employee/ 
