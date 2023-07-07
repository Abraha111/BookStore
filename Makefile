mig:
	python3 manage.py makemigrations
	python3 manage.py migrate

req-i:
	pip3 install -r requirements.txt

req-w:
	pip3 freeze > requirements.txt