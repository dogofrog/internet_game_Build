import http.server
import os
import socketserver
import mimetypes

mimetypes.add_type('application/wasm', '.wasm')
mimetypes.add_type('application/octet-stream', '.data')

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)

PORT = 8080

with socketserver.TCPServer(("", PORT), http.server.SimpleHTTPRequestHandler) as httpd:
    httpd.allow_reuse_address = True
    print(f"\n  Сервер запущен!")
    print(f"  Открой в браузере:  http://localhost:{PORT}/")
    print(f"  Страница с игрой:   http://localhost:{PORT}/play.html")
    print(f"\n  Остановить: Ctrl+C\n")
    httpd.serve_forever()
