#!/usr/bin/env python3
"""
Simple HTTP Server for Frontend Testing
Serves the frontend on http://localhost:5000
Run this in the frontend directory
"""

import http.server
import socketserver
import os
from pathlib import Path

# Change to script directory
os.chdir(Path(__file__).parent)

PORT = 5000
Handler = http.server.SimpleHTTPRequestHandler

print(f"""
╔════════════════════════════════════════════════════════════════╗
║          Frontend Web Server - Started                         ║
╚════════════════════════════════════════════════════════════════╝

📍 URL: http://localhost:5000
📁 Serving: {os.getcwd()}

Available pages:
  • http://localhost:5000/index.html        (Main app)
  • http://localhost:5000/VOICE_TEST.html   (Voice testing)
  • http://localhost:5000/DEBUG.html        (Debug console)
  • http://localhost:5000/TEST.html         (System tests)

🛑 Stop server: Press CTRL+C

═════════════════════════════════════════════════════════════════
""")

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n\n✅ Server stopped")
