"""One-screen authorization surface: the agent's entire authority transition is
VISIBLE — never buried in logs. Run: python server.py [port]"""
from __future__ import annotations

import json
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

from app.agent import StopAndAskFlow
from app.receipts import ReceiptChain

ROOT = Path(__file__).resolve().parent
flow: StopAndAskFlow | None = None
chain = ReceiptChain(ROOT / "data" / "strands_spike_001_receipts.jsonl")


class Handler(BaseHTTPRequestHandler):
    def _send(self, code: int, body: bytes, ctype: str = "application/json"):
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if self.path in ("/", "/index.html"):
            self._send(200, (ROOT / "ui" / "index.html").read_bytes(), "text/html")
        elif self.path == "/state":
            snap = flow.snapshot() if flow else {"stage": "IDLE"}
            self._send(200, json.dumps(snap).encode())
        elif self.path == "/api/replay":
            ok, why = ReceiptChain(ROOT / "data" / "strands_spike_001_receipts.jsonl").verify()
            self._send(200, json.dumps({"ok": ok, "why": why}).encode())
        else:
            self._send(404, b'{"error":"not found"}')

    def do_POST(self):
        global flow, chain
        length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(length) if length else b"{}"
        if self.path == "/start":
            flow = StopAndAskFlow()
            chain = flow.chain
            threading.Thread(target=flow.run, daemon=True).start()
            self._send(200, json.dumps({"started": True}).encode())
        elif self.path in ("/approve", "/deny") and flow:
            flow.human_decision = "APPROVE" if self.path == "/approve" else "DENY"
            flow.decision_event.set()
            self._send(200, json.dumps({"decision": flow.human_decision}).encode())
        else:
            self._send(404, b'{"error":"not found"}')

    def log_message(self, *a):  # quiet
        pass


if __name__ == "__main__":
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8474
    print(f"stop-and-ask agent on http://127.0.0.1:{port} (loopback only)")
    ThreadingHTTPServer(("127.0.0.1", port), Handler).serve_forever()
