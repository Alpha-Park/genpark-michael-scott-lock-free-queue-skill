"""MCP Server for Michael-Scott Queue Skill."""
import json
import sys
from client import MichaelScottQueue

def main():
    q = MichaelScottQueue()
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            req = json.loads(line)
            req_id = req.get("id")
            method = req.get("method")
            params = req.get("params", {})

            if method == "tools/list":
                res = {
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "result": {
                        "tools": [
                            {
                                "name": "enqueue",
                                "description": "Enqueue item to concurrent FIFO queue",
                                "inputSchema": {
                                    "type": "object",
                                    "properties": {"value": {}},
                                    "required": ["value"]
                                }
                            },
                            {
                                "name": "dequeue",
                                "description": "Dequeue item from concurrent FIFO queue",
                                "inputSchema": {"type": "object"}
                            }
                        ]
                    }
                }
            elif method == "tools/call":
                name = params.get("name")
                args = params.get("arguments", {})
                if name == "enqueue":
                    q.enqueue(args["value"])
                    out = {"status": "enqueued", "length": q.length}
                else:
                    val = q.dequeue()
                    out = {"item": val, "length": q.length}
                res = {
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "result": {"content": [{"type": "text", "text": json.dumps(out)}]}
                }
            else:
                res = {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": "Method not found"}}
            print(json.dumps(res), flush=True)
        except Exception as e:
            err = {"jsonrpc": "2.0", "id": None, "error": {"code": -32000, "message": str(e)}}
            print(json.dumps(err), flush=True)

if __name__ == "__main__":
    main()
