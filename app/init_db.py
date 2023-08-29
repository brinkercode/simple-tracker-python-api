import os

config = {
    'user': os.environ.get('DB_USER'),
    'password': os.environ.get('DB_PASSWORD'),
    'host': os.environ.get('DB_HOST'),
    'database': os.environ.get('DB_DATABASE'),
    'raise_on_warnings': os.environ.get('DB_DATABASE', 'true') == 'true',
}