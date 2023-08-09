# HIVseqDB

## Working with the development version

Create a virtual environment and activate it.

```
virtualenv create hivseqdb_env
source hivseqdb_env/bin/activate
```

Clone this repository.

```
git clone https://github.com/AlfredUg/HIVseqDB.git
```

Navigate to the cloned repository

```
cd HIVseqDB
```

Install dependancies

```
pip -m install requirements.txt
```

Make migrations and execute them

```
python manage.py makemigrations
python manage.py migrate
```

Run the server

```
python manage.py runserver
```


Start `redis` on a different shell tab/window

```
redis-server
```

Start `Celery` on a different shell tab/window

```
python -m celery -A hivseqdb worker
```

