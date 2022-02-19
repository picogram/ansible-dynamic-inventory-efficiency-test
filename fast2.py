#!/usr/bin/python
import argparse
import json
from pprint import pprint
import time


def build_inventory():
    time.sleep(5)

    inventory = {
#        '_meta': {
#            'hostvars': {}
#        },
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

    return inventory


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Dynamic inventory script')
    parser.add_argument('--list', action='store_true')
    parser.add_argument('--host', type=str)

    args = parser.parse_args()

    if args.list or not args.host:
        inventory = build_inventory()
        print(json.dumps(inventory))
        exit(0)
    
    if args.host:
        hostvars = {}
        print(hostvars)
        exit(0)
        



