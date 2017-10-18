import json

import sys

sys.path.insert(0, '')

class Payload(object):
    def __init__(self, j="{}"):
        self.changed_files = None
        self.deletions = None
        self.additions = None
        self.__dict__ = json.loads(j)

    def __repr__(self):
        return str(self.__dict__)
