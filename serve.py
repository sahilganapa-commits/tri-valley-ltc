#!/usr/bin/env python3
"""Local preview server for site/.

    python3 serve.py [port]     # default 8000, then open http://localhost:8000

Unlike `python3 -m http.server`, this tells the browser never to reuse a
cached HTML page. Asset URLs already carry a content hash (see
layout.asset_version), so CSS, JS, and images cache properly and still update
the moment they change. Without this, editing a stylesheet and reloading can
show a half-old page, which looks like a rendering bug rather than a stale file.
"""

import sys
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

SITE = Path(__file__).parent / "site"


class Handler(SimpleHTTPRequestHandler):
    def end_headers(self):
        path = self.path.split("?")[0]
        if path.endswith((".html", "/")):
            self.send_header("Cache-Control", "no-cache, must-revalidate")
        else:
            # Hashed URLs, so these are safe to keep for the session.
            self.send_header("Cache-Control", "public, max-age=300")
        super().end_headers()

    def log_message(self, fmt, *args):
        status = args[1] if len(args) > 1 else ""
        if status not in ("200", "304"):
            super().log_message(fmt, *args)


def main():
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
    if not SITE.is_dir():
        sys.exit("site/ not found — run `python3 build.py` first.")
    # Threaded: a single stalled connection (a headless browser that never
    # closes, say) must not be able to block every other request.
    server = ThreadingHTTPServer(("127.0.0.1", port), partial(Handler, directory=str(SITE)))
    server.daemon_threads = True
    print(f"Serving {SITE.name}/ at http://localhost:{port}  (Ctrl-C to stop)")
    server.serve_forever()


if __name__ == "__main__":
    main()
