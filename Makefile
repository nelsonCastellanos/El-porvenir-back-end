local.start:
	rm -f db.sqlite3
	rm -rf images
	rm -rf original_images

	rm -rf wagtail_porvenir/migrations/0001_initial.py
	rm -rf wagtail_porvenir/migrations/__pycache__
	rm -rf wagtail_porvenir/__pycache__

	rm -rf cms/migrations/0001_initial.py
	rm -rf cms/migrations/__pycache__
	rm -rf cms/__pycache__

	rm -rf el_porvenir/migrations/0001_initial.py
	rm -rf el_porvenir/migrations/__pycache__
	rm -rf el_porvenir/__pycache__
	python manage.py makemigrations
	python manage.py migrate
	echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('ncastellanos', '', 'test')" | python manage.py shell
	python manage.py runserver
	