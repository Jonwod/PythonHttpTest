from http.server import HTTPServer, BaseHTTPRequestHandler

ListenPort = 8080

class MyServer(BaseHTTPRequestHandler):
    def do_POST(self):
        data_length = int(self.headers['Content-Length'])
        body = self.rfile.read(data_length)
        print(body.decode('UTF-8'))
        newfile = open("serverfile.txt", "w+")
        newfile.write(body.decode('UTF-8'))
        newfile.close()
        self.send_response(200)
        self.end_headers()


httpd = HTTPServer(('0.0.0.0', ListenPort), MyServer)
httpd.serve_forever()
