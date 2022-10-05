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

	rm -rf cms_category_page/migrations/0001_initial.py
	rm -rf cms_category_page/migrations/__pycache__
	rm -rf cms_category_page/__pycache__

	rm -rf product/migrations/0001_initial.py
	rm -rf product/migrations/__pycache__
	rm -rf product/__pycache__

	rm -rf category/migrations/0001_initial.py
	rm -rf category/migrations/__pycache__
	rm -rf category/__pycache__
	
	pyenv virtualenv-delete -f porvenir_cms || pyenv virtualenv -f porvenir_cms
	pyenv virtualenv -f porvenir_cms || echo "Salio mal"
	
	source ~/.pyenv/versions/porvenir_cms/bin/activate porvenir_cms && python3 -m pip install --upgrade pip
	source ~/.pyenv/versions/porvenir_cms/bin/activate porvenir_cms && python3 -m pip install --upgrade pillow
	source ~/.pyenv/versions/porvenir_cms/bin/activate porvenir_cms && python3 -m pip install -r requirements.txt
	source ~/.pyenv/versions/porvenir_cms/bin/activate porvenir_cms && python manage.py makemigrations
	source ~/.pyenv/versions/porvenir_cms/bin/activate porvenir_cms && python manage.py migrate
	source ~/.pyenv/versions/porvenir_cms/bin/activate porvenir_cms && echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('ncastellanos', '', 'test')" | python manage.py shell
	source ~/.pyenv/versions/porvenir_cms/bin/activate porvenir_cms && python manage.py collectstatic --noinput	