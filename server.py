from http.server import *
import base64
import time

class Handler(BaseHTTPRequestHandler):
   
    def do_GET(self):
        print("Got request")
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(b'{"data" : "It\'s working yay"}')
       

class Server(HTTPServer):
    def __init__(self, server_address:  tuple[str, int], RequestHandlerClass, bind_and_activate=...) -> None:
        super().__init__(server_address, RequestHandlerClass, bind_and_activate)



if __name__ == "__main__":

    print("\n\n")
    server = Server(('0.0.0.0', 1234), Handler)
    print("Starting server %")
    server.serve_forever()
    server.server_close()
