import json
from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleAPIHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        # Root endpoint: returns a simple text response
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
        
        # /data endpoint: returns sample JSON data
        elif self.path == '/data':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            self.wfile.write(json.dumps(data).encode('utf-8'))
        
        # /status endpoint: returns the status of the API
        elif self.path == '/status':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            status = {
                "status": "OK"
            }
            self.wfile.write(json.dumps(status).encode('utf-8'))
        
        # Handling undefined endpoints (404 Not Found)
        else:
            self.send_response(404)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            error_message = {
                "error": "Endpoint not found"
            }
            self.wfile.write(json.dumps(error_message).encode('utf-8'))

# Set up the server
def run(server_class=HTTPServer, handler_class=SimpleAPIHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
