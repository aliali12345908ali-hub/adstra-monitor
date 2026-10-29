import os
from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain; charset=utf-8")
        self.end_headers()
        self.wfile.write(b"Adastra Sovereign Digital Enterprise - Running & Healthy")

def run(server_class=HTTPServer, handler_class=SimpleHandler, port=8080):
    port_env = int(os.environ.get("PORT", port))
    server_address = ('0.0.0.0', port_env)
    httpd = server_class(server_address, handler_class)
    print(f"Server started on port {port_env}")
    httpd.serve_forever()

if __name__ == '__main__':
    run()
