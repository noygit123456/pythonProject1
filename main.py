from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs


# This class will handle incoming HTTP requests
# and generate responses to send back to the client.

class MyRequestHandler(BaseHTTPRequestHandler):

    # do_GET -will be called whenever a GET request is received by the
    # server.
    def do_GET(self):
        # Extract the query parameters from the URL.
        url_parts = urlparse(self.path)
        print(f"url_parts: {url_parts}")

        # parse_qs function to parse the query parameters from the URL
        # into a dictionary.
        query_params = parse_qs(url_parts.query)
        print(f"query_params: {query_params}")

        # Send a response to the client
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Received your request!")

    # do_POST -will be called whenever a POST request is received by the server.
    def do_POST(self):

        # self.headers is an instance of the HTTPHeaders class which
        # contains the headers of the HTTP request received by the server.

        # The Content-Length header is the length of the request body in bytes.

        # Get the length of the request data
        content_length = int(self.headers.get('Content-Length', 0))

        #  utf-8 - decodes it into a string.
        # rfile - file-like object that contains the request data.

        # Get the data from the request body.
        request_data = self.rfile.read(content_length).decode('utf-8')

        # Print the data
        print(request_data)

        # Send a response to the client
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Received your request!")


if __name__ == '__main__':
    # Create an HTTP server with the MyRequestHandler class as the handler.
    server = HTTPServer(('localhost', 8000), MyRequestHandler)

    # Start the server
    print('Starting server, use <Ctrl-C> to stop')
    server.serve_forever()


