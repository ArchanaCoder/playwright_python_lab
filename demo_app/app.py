"""Local learning system only: deliberately simple auth, not a production service."""

import io
import secrets
from threading import Lock
from uuid import uuid4

from flask import Flask, Response, jsonify, redirect, request, send_file

DEMO_USER = {"username": "archana", "password": "practice123"}


def create_app():
    app = Flask(__name__)
    items, sessions = {}, set()
    lock = Lock()

    def authorized():
        token = request.headers.get("Authorization", "").removeprefix("Bearer ")
        token = token or request.cookies.get("session", "")
        with lock:
            return token in sessions

    @app.get("/")
    def home():
        return app.send_static_file("index.html")

    @app.get("/lab")
    def lab():
        return app.send_static_file("lab.html")

    @app.get("/frame")
    def frame():
        return '<label>Card number<input aria-label="Card number"></label>'

    @app.get("/health")
    def health():
        return jsonify(status="ok")

    @app.route("/api/login", methods=["POST"])
    def login():
        data = request.get_json(silent=True) or request.form.to_dict()
        if data != DEMO_USER:
            return jsonify(error="Invalid credentials"), 401
        token = secrets.token_urlsafe(24)
        with lock:
            sessions.add(token)
        response = jsonify(token=token, username=data["username"])
        response.set_cookie("session", token, httponly=True, samesite="Lax")
        return response

    @app.post("/api/logout")
    def logout():
        token = request.cookies.get("session")
        with lock:
            sessions.discard(token)
        response = jsonify(status="logged out")
        response.delete_cookie("session")
        return response

    @app.get("/api/me")
    def me():
        if not authorized():
            return jsonify(error="Unauthorized"), 401
        return jsonify(username="archana")

    @app.route("/api/items", methods=["GET", "POST"])
    def collection():
        if not authorized():
            return jsonify(error="Unauthorized"), 401
        if request.method == "GET":
            query = request.args.get("q", "").lower()
            with lock:
                result = [dict(item) for item in items.values() if query in item["name"].lower()]
            return jsonify(items=result, count=len(result))
        data = request.get_json(silent=True)
        if (
            not isinstance(data, dict)
            or not isinstance(data.get("name"), str)
            or not data["name"].strip()
        ):
            return jsonify(error="name is required"), 422
        item = {"id": uuid4().hex, "name": data["name"], "amount": data.get("amount", 0)}
        with lock:
            items[item["id"]] = item
        return jsonify(item), 201, {"Location": "/api/items/" + item["id"]}

    @app.route("/api/items/<item_id>", methods=["GET", "PUT", "PATCH", "DELETE"])
    def resource(item_id):
        if not authorized():
            return jsonify(error="Unauthorized"), 401
        with lock:
            if item_id not in items:
                return jsonify(error="Not found"), 404
            if request.method == "DELETE":
                del items[item_id]
                return "", 204
            if request.method in ("PUT", "PATCH"):
                data = request.get_json(silent=True)
                if not isinstance(data, dict):
                    return jsonify(error="JSON object required"), 422
                if request.method == "PUT" and not data.get("name"):
                    return jsonify(error="name is required"), 422
                if "name" in data and (
                    not isinstance(data["name"], str) or not data["name"].strip()
                ):
                    return jsonify(error="name is required"), 422
                if request.method == "PUT":
                    items[item_id] = {
                        "id": item_id,
                        "name": data["name"],
                        "amount": data.get("amount", 0),
                    }
                else:
                    items[item_id].update(
                        {k: v for k, v in data.items() if k in ("name", "amount")}
                    )
            return jsonify(dict(items[item_id]))

    @app.route("/api/echo", methods=["GET", "POST", "PUT", "PATCH", "DELETE", "HEAD", "OPTIONS"])
    def echo():
        return (
            jsonify(
                method=request.method,
                query=request.args.to_dict(),
                json=request.get_json(silent=True),
                form=request.form.to_dict(),
                body=request.get_data(as_text=True),
                custom_header=request.headers.get("X-Learning"),
            ),
            200,
            {"X-Demo": "playwright"},
        )

    @app.post("/api/upload")
    def upload():
        file = request.files.get("file")
        if file is None:
            return jsonify(error="file required"), 422
        content = file.read()
        return jsonify(
            filename=file.filename, size=len(content), description=request.form.get("description")
        )

    @app.get("/api/status/<int:status>")
    def status_code(status):
        if status not in {200, 400, 401, 403, 404, 409, 422, 429, 500, 503}:
            return jsonify(error="Unsupported practice status"), 400
        return jsonify(status=status), status

    @app.get("/api/redirect")
    def redirect_example():
        return redirect("/health", code=302)

    @app.get("/download")
    def download():
        return send_file(
            io.BytesIO(b"name,amount\nPractice transfer,100\n"),
            mimetype="text/csv",
            as_attachment=True,
            download_name="payments.csv",
        )

    @app.get("/api/text")
    def text():
        return Response("Playwright practice", mimetype="text/plain")

    return app


if __name__ == "__main__":
    # Bind only to loopback. Pytest starts an isolated app automatically on a free port.
    create_app().run(host="127.0.0.1", port=8765, debug=False)
