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
    # Handle the special arguments from Ansible
    if len(sys.argv) == 2 and sys.argv[1] == '--list':
        yaml_path = 'dynamic_vars/dynamic_inventory.yml'  # Adjusted path to the YAML file
    else:
        print("Usage: {} --list".format(sys.argv[0]), file=sys.stderr)
        sys.exit(1)

    data = load_yaml_file(yaml_path)

    # Construct the inventory dynamically based on the YAML file
    inventory = {
        "_meta": {
            "hostvars": {}
        },
        "all": {
            "children": ["nxos_switches", "ungrouped"]
        },
        "nxos_switches": {
            "hosts": list(data["hosts_list"]["hosts"].keys()),
            "vars": data["hosts_list"]["group_vars"]
        }
    }

    # Print the inventory in JSON format
    print(json.dumps(inventory))

if __name__ == "__main__":
    main()

