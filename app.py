# app.py

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return [b"Hello, uswgi!"]
