import hmac
import hashlib

import requests


class GravelApi():
    def __init__(self, address, shared_secret):
        self.address = address
        self.shared_secret = shared_secret

        self.tokens = []

    def get_problem(self, problemid):
        pass

    def get_user(self, userid):
        pass

    def get_tokens(self, number=1):
        pass

    def _call_api_with_token(self):
        pass

    def _call_api_without_token(self):
        pass


class GravelProblem():
    def __init__(self, api, id, data={}):
        self.api = api
        self.id = id

    def get_replies(self):
        pass

    def post_reply(self):
        pass


class GravelReply():
    def __init__(self, api, id, data={}):
        self.api = api
        self.id = id


class GravelUser():
    def __init__(self, api, id, data={}):
        self.api = api
        self.id = id
