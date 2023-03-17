import os 

db_name = 'favoritecolor$colors'
host = 'favoritecolor.mysql.pythonanywhere-services.com'
port = 3306
user = 'favoritecolor'
password = os.environ.get('DB_PASSWORD')