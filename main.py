import os
from http.server import HTTPServer, BaseHTTPRequestHandler
import json

class DirectPaymentHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        response = {
            "status": "success",
            "message": "Adastra Sovereign Direct Payout System Active",
            "payment": "Direct to Personal Account (Stripe Removed)"
        }
        self.wfile.write(json.dumps(response).encode('utf-8'))

def run(server_class=HTTPServer, handler_class=DirectPaymentHandler, port=8080):
    port_env = int(os.environ.get("PORT", port))
    server_address = ('0.0.0.0', port_env)
    httpd = server_class(server_address, handler_class)
    print(f"Direct payment server started on port {port_env}")
    httpd.serve_forever()

if __name__ == '__main__':
    run()


