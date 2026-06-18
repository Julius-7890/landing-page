from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path


ROOT = Path(__file__).resolve().parent
PORT = 8000


class ScholinkHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def do_GET(self):
        if self.path in {"/", "/index", "/index.html"}:
            self.path = "/templates/index.html"
        return super().do_GET()

    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()


def run():
    server_address = ("127.0.0.1", PORT)
    with ThreadingHTTPServer(server_address, ScholinkHandler) as server:
        print(f"wEkO-Scholink landing page running at http://{server_address[0]}:{PORT}")
        server.serve_forever()


if __name__ == "__main__":
    run()
