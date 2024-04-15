#!/usr/bin/env python3
import json
import yaml
import sys

def load_yaml_file(filepath):
    try:
        with open(filepath, 'r') as file:
            return yaml.safe_load(file)
    except FileNotFoundError:
        print("File not found: {}".format(filepath), file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print("Error reading file: {}".format(e), file=sys.stderr)
        sys.exit(1)

def main():
    if len(sys.argv) != 2 or sys.argv[1] != '--list':
        print("Usage: {} --list".format(sys.argv[0]), file=sys.stderr)
        sys.exit(1)

    yaml_path = 'hosts_vars.yml'
    data = load_yaml_file(yaml_path)

    inventory = {
        "_meta": {
            "hostvars": {}
        },
        "all": {
            "children": []
        }
    }

    # Dynamically create group structure and assign hosts
    groups = {}
    for group, hosts in data["group_memberships"].items():
        inventory["all"]["children"].append(group)
        groups[group] = {"hosts": hosts}

    inventory.update(groups)

    print(json.dumps(inventory))

if __name__ == "__main__":
    main()

