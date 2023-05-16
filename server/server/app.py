import os
from datetime import datetime

from flask import Flask, Response, abort, make_response, request, send_from_directory
from werkzeug.http import generate_etag, parse_etags

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


def get_etag(start):
    unique_str = f"{datetime.now().date()}-{start}"
    return generate_etag(unique_str.encode("utf-8"))


def check_etag(etag):
    if_none_match_header = request.headers.get("If-None-Match")
    return if_none_match_header and etag in parse_etags(if_none_match_header)


def validate_request():
    start = request.args.get("start")
    error_message = validate_start_date(start)
    if error_message is not None:
        abort(400, error_message)

    etag = get_etag(start)
    if check_etag(etag):
        return Response(status=304)

    args = {"start": start} if start is not None else {}
    return args, etag


@app.route("/stocks/performance")
def performance():
    result = validate_request()
    if isinstance(result, Response):
        return result
    args, etag = result
    return make_response((stocks.performance(**args), {"ETag": etag}))


@app.route("/stocks/statistics")
def statistics():
    result = validate_request()
    if isinstance(result, Response):
        return result
    args, etag = result
    return make_response((stocks.statistics(**args), {"ETag": etag}))
