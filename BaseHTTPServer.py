from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import cgi
from cgi import parse_header, parse_multipart
from urllib.parse import parse_qs

# HTTPRequestHandler class
class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):
	def _set_headers(self):
		self.send_response(200)
		self.send_header('Content-type', 'text/html')
		self.end_headers()
	def do_OPTIONS(self):
		self.send_response(200, "ok")
		self.send_header('Access-Control-Allow-Credentials', 'true')
		self.send_header('Access-Control-Allow-Origin', 'http://localhost:8888')
		self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
		self.send_header("Access-Control-Allow-Headers", "X-Requested-With, Content-type")

  # GET
	def do_GET(self):
		# Send response status code
		self.send_response(200)

		# Send headers
		self.send_header('Content-type','text/html')
		self.end_headers()

		# Send message back to client
		message = "Hello world!"
		# Write content as utf-8 data
		self.wfile.write(bytes(message, "utf8"))
		return

	def do_POST(self):
		global rootnode
		try:
			ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
			if ctype == 'multipart/form-data':
				query=cgi.parse_multipart(self.rfile, pdict)
			self.send_response(301)

			self.end_headers()
			upfilecontent = query.get('upfile')
			#print "filecontent", upfilecontent[0]
			self.wfile.write("<HTML>POST OK.<BR><BR>");
			self.wfile.write(upfilecontent[0]);

		except :
			pass
		
		return

 
def run():
  print('starting server...')
 
  # Server settings
  # Choose port 8080, for port 80, which is normally used for a http server, you need root access
  server_address = ('10.180.93.80', 8080)
  httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
  print('running server...')
  httpd.serve_forever()
 
 
run()