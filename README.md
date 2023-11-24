# HIVseqDB

## Working with the development version

Clone this repository.

```
git clone https://github.com/AlfredUg/HIVseqDB.git
```

Navigate to the cloned repository

```
cd HIVseqDB
```

Switch over to the development branch

```
git checkout dev
```

Create a virtual environment and activate it.

```
python3 -m venv venv    
source venv/bin/activate
```

Install dependancies

```
pip -m install requirements.txt
```

In addition, have a working version of sierralocal and quasitools.

```
pip install sierralocal
conda install -c bioconda quasitools
```

Setting up the `SECRET_KEY`. To set this manually, open the settings file (located at `$(PWD/hivseqdb/settings.py`), and add a value for the `SECRET_KEY` or export it to the system `PATH` as indicated below.

```
export SECRET_KEY='some-hash-string'
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

