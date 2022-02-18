#!/usr/bin/python
import json
from pprint import pprint
import time

time.sleep(5)

inventory = {
    '_meta': {
        'hostvars': {}
    },
    'foo': {
        'hosts': ['192.168.1.1']
        },
    'bar': {
        'hosts': ['192.168.1.2']
    },
    'baz': {
        'hosts': ['192.168.1.3', '192.168.1.4']
    }
}

print(json.dumps(inventory))


