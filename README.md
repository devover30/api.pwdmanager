# Flask Password Manger API

### Basic Configuration

1. Install Python Virtual Enviornment

```python
$ python3 -m pip install --upgrade pip

$ pip3 install virtualenv

$ virtualenv -p python3 venv
```

2. Install extensions

```python
$ source venv/bin/activate

(venv) $ pip install -r requirements.txt
```

3. Create sqlite3 database

```python
(venv) $ python

>>> from pwd_manager import create_app
>>> from pwd_manager import db
>>> app = create_app()
>>> app.app_context().push()
>>> db.create_all()
```

4. Create Flask env file

```bash
(venv) $ vim .flaskenv

Add This Lines

FLASK_ENV=development
FLASK_APP=pwd_manager
```

5. Run Flask

```python
(venv) $ flask run
```
