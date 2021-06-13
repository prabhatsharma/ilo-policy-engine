import json

policies = []


def create_update(request_object):
    # print("Got new admission policy: ")
    # print(json.dumps(request_object))

    print("Got new admission policy. Rules are: ")

    rules = request_object["spec"]["rules"]

    # print(json.dumps(rules))

    for rule in rules:
        print(rule)
        policies.append(rule)


def resource(resource):
    print("Policies are: ", policies)
    print("Got new resource: ")
    # print(json.dumps(resource))

    rule1 = policies[0]["rule"]
    print(rule1)

    rule1_result = eval(rule1, {}, { "resource": resource})

    print("Result is: ", rule1_result)


