# PPZ-Project

Оскільки в репозиторії **не містяться** `.mp3` файли з піснями сторонніх авторів (щоб уникнути порушення авторських прав), перед запуском програми створіть обліковий запис адміністратора (`python manage.py createsuperuser`), потім зайдіть у Django-адмінку за адресою `http://127.0.0.1:8000/admin/` і  відредагуйте записи моделі “Пісня”, завантаживши для кожної відповідний `.mp3` файл.```

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver  
