#!/usr/bin/env python3
"""ArtViSiON showroom server — no-cache headers taaki browser hamesha fresh file le."""
import http.server, socketserver

class NoCacheHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

socketserver.TCPServer.allow_reuse_address = True
with socketserver.TCPServer(('0.0.0.0', 8000), NoCacheHandler) as httpd:
    print('Serving on 0.0.0.0:8000 (no-cache)')
    httpd.serve_forever()
