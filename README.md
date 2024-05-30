# uwsgi-test with flask

## Install uwsgi
```
sudo apt update
sudo apt install uwsgi uwsgi-plugin-python3 -y
```

## Clone
```
git clone https://github.com/AlperenY-cs/uwsgi-test.git
```

## Run
Go project directory

```
sudo uwsgi --http-socket :9090 --plugin python3 --wsgi-file app.py
```
## Run with config file
Create app.ini

```
[uwsgi]
http-socket = :9090
plugin = python3
wsgi-file = /path/to/app.py
callable = application
processes = 4
threads = 2
logto = /tmp/uwsgi.log
```
```
sudo uwsgi --ini app.ini
```

