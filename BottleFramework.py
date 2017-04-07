from bottle import run, get, post, request, delete, Bottle, response
import json
from plugins.cors_plugin import RequestPreflightPlugin

request_preflight_plugin = RequestPreflightPlugin( allow_origin = '*',
                                                   preflight_methods = [ 'GET', 'POST', 'PUT', 'DELETE' ],
                                                   ttl = 3600 )
#request_handler.install( request_preflight_plugin )

app = Bottle()

@app.hook('after_request')
def enable_cors():
	"""
	You need to add some headers to each request.
	Don't use the wildcard '*' for Access-Control-Allow-Origin in production.
	"""
	response.headers['Access-Control-Allow-Origin'] = '*'
	response.headers['Access-Control-Allow-Methods'] = 'PUT, GET, POST, DELETE, OPTIONS'
	response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'
	
	# response.headers['Content-type'] = 'application/json'

@app.get('/', skip = [ request_preflight_plugin ])
def getNome():
	return 'diego'

@app.post('/ordena', skip = [ request_preflight_plugin ])
def addOne():
	#numbers = []
	#new_number = {'number' : request.json.get('number')}
	#numbers.append(new_number['number'])
	#print(request.json.get('number'))
	#a =  {'numbers' : numbers}
	#return json.dumps(a)
	return json.dumps(True)

run(app, host='127.0.0.1', port=8080)
