#! /bin/bash
set -ex

until mysqladmin ping -h ${MYSQL_HOST} --silent; do
    echo 'waiting for mysqld to be connectable...'
    sleep 3
done

python -m bin.create_database
cd automan/
python manage.py makemigrations
python manage.py migrate

exec "$@"
