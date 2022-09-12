local.start:
	rm -f db.sqlite3
	rm -rf images
	rm -rf original_images

	rm -rf cms/migrations/0001_initial.py
	rm -rf cms/migrations/__pycache__
	rm -rf cms/__pycache__

	rm -rf cms_home_page/migrations/0001_initial.py
	rm -rf cms_home_page/migrations/__pycache__
	rm -rf cms_home_page/__pycache__



	pyenv virtualenv-delete -f wagtail
	pyenv virtualenv wagtail
	python3 -m pip install -r requirements.txt
	python manage.py makemigrations
	python manage.py migrate
	echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('ncastellanos', '', 'test')" | python manage.py shell
	python manage.py collectstatic --noinput
	python manage.py runserver
	