import os

from flask import Flask, send_from_directory

app = Flask(__name__, static_folder="../../client/dist")


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def serve(path):
    if path != "" and os.path.exists(
        os.path.join(os.path.abspath(app.static_folder), path)
    ):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, "index.html")