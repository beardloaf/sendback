#!/usr/bin/env python3
"""
Simple HTTP server for SendBack web interface
"""

import http.server
import socketserver
import os
import sys

PORT = 8000
DIRECTORY = "web"


class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def end_headers(self):
        # Add CORS headers
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()


def main():
    # Check if web directory exists
    if not os.path.exists(DIRECTORY):
        print(f"Error: '{DIRECTORY}' directory not found")
        sys.exit(1)

    # Start server
    with socketserver.TCPServer(("", PORT), CustomHTTPRequestHandler) as httpd:
        print("=" * 60)
        print("SendBack Web Interface")
        print("=" * 60)
        print(f"Server running at: http://localhost:{PORT}")
        print(f"Serving from: {DIRECTORY}/")
        print("\nMake sure the API is running on port 5000:")
        print("  python app.py")
        print("\nPress Ctrl+C to stop")
        print("=" * 60)

        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\nServer stopped")


if __name__ == '__main__':
    main()
