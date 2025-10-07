#!/usr/bin/env python3
"""
Simple HTTP server for Data Visualization Portfolio
Serves the site/ directory while allowing access to visualizations/
"""
import http.server
import socketserver
import os

PORT = 8000

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Add CORS headers if needed
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

    def translate_path(self, path):
        # Serve files from project root, but default to site/
        path = super().translate_path(path)

        # If path points to the project root and it's a directory
        # redirect to site/index.html
        if path.endswith(os.getcwd()) or path == os.path.join(os.getcwd(), ''):
            return os.path.join(os.getcwd(), 'site', 'index.html')

        return path

if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
        print(f"=" * 60)
        print(f"Data Visualization Portfolio Server")
        print(f"=" * 60)
        print(f"Serving at: http://localhost:{PORT}")
        print(f"Main site: http://localhost:{PORT}/site/")
        print(f"Visualizations accessible at /visualizations/")
        print(f"=" * 60)
        print(f"Press CTRL+C to stop")
        print(f"=" * 60)
        httpd.serve_forever()
