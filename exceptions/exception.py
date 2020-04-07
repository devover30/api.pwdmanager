from werkzeug.exceptions import BadRequest, InternalServerError, UnprocessableEntity
import json

class JsonBadRequest(BadRequest):

    def get_body(self, environ=None):
        return json.dumps(self.description)

    def get_headers(self, environ=None):
        return [('Content-Type', 'application/json')]

class JsonInternalError(InternalServerError):

    def get_body(self, environ=None):
        return json.dumps(self.description)

    def get_headers(self, environ=None):
        return [('Content-Type', 'application/json')]


class JsonUnprocessable(UnprocessableEntity):
    def get_body(self, environ=None):
        return json.dumps(self.description)

    def get_headers(self, environ=None):
        return [('Content-Type', 'application/json')]
