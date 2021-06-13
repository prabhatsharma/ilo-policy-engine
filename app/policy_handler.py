import json


def create_update(request_object):
    print("Got new admission policy: ")
    print(json.dumps(request_object))


def resource(request_object):
    print("Got new resource: ")
    print(json.dumps(request_object))
