import json
from jsonschema import validate


def validate_request_and_response(response, request_schema=None, response_schema=None):
    if request_schema:
        validate(json.loads(response.request.body), request_schema)
    if response_schema:
        validate(response.json(), response_schema)
