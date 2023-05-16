import os
from datetime import datetime

from flask import Flask, request, send_from_directory

from . import stocks

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


def validate_start_date(start):
    if start is not None:
        try:
            datetime.strptime(start, "%Y-%m-%d")
        except ValueError:
            return (
                "Invalid start date format. "
                'Please provide a date in the format "YYYY-MM-DD".'
            )


@app.route("/stocks/performance")
def performance():
    start = request.args.get("start")
    error_message = validate_start_date(start)
    if error_message is None:
        args = {"start": start} if start is not None else {}
        return stocks.performance(**args)
    else:
        return {"error": error_message}, 400


@app.route("/stocks/statistics")
def statistics():
    start = request.args.get("start")
    error_message = validate_start_date(start)
    if error_message is None:
        args = {"start": start} if start is not None else {}
        return stocks.statistics(**args)
    else:
        return {"error": error_message}, 400
