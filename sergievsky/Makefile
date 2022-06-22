run:
	./manage.py runserver
migrate:
	./manage.py makemigrations && ./manage.py migrate
col-static:
	./manage.py collectstatic
fixture-dump-post:
	./manage.py dumpdata blog.post --format yaml --output dump.db.yaml
fixture-dump-all:
	./manage.py dumpdata --format yaml --output dump.db.yaml
fixture-load-dump:
	./manage.py loaddata dump.db.yaml