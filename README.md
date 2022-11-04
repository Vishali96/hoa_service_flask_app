#db
brew install postgresql
pg_ctl -D /usr/local/var/postgres start && brew services start postgresql
psql postgres
create database api_dev;

python -m venv env
source env/bin/activate
pip install -r requirements.txt
export FLASK_APP=src/__init__.py
export APP_SETTINGS=src.config.DevelopmentConfig
export FLASK_ENV=development
export DATABASE_URL="postgresql:///api_dev"
python3 manage.py recreate_db
python3 manage.py run 

https://bootstrapmade.com/demo/NiceAdmin/