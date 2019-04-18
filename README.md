# mynewsdiary
**Python** 3.6.8  
**Django** 2.2  
**Postgresql** 10.2  
15/04/2019 ~  
  
## Before you start...
```bash
pip install psycopg2
pip install django-polymorphic
pip install Markdown
pip install faker
pip install libsass django-compressor django-sass-processor
```
  
## Seeding
> 실행시 현재 갖고 있는 모든 데이터를 지운 후, 새롭게 seed 데이터를 생성합니다. (superuser 1명 포함)
```bash
python manage.py seed --mode=refresh
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'abababab')" | python manage.py shell
```
  
## Migration 파일 정리
```bash
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc"  -delete
python manage.py makemigrations
python manage.py migrate
```