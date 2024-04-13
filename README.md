# Using-dynamic-inventory-to-manage-Cisco-Nexus-Switches
# Dynamic_inventory.py

## Summary

This Python script generates a dynamic inventory for Ansible using data from an external YAML file (`hosts_vars.yml`). It constructs an inventory structure based on the YAML data and outputs it in JSON format.

## Script Overview

## **Importing Modules**:
   ```python
   #!/usr/bin/env python3

   import json
   import sys
   ```
## Reading YAML Data Function:
```python
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
```
## Main Function:
```python
def main():
    # Read YAML data from hosts_vars.yml
    data = load_yaml_file('hosts_vars.yml')

    # Generate the inventory structure
    inventory = {
        "_meta": {
            "hostvars": {}  # Placeholder for host-specific variables
        },
        "all": {
            "children": ["nxos_switches", "ungrouped"]
        },
        "nxos_switches": {
            "hosts": list(data["hosts_list"].keys()),  # List of hosts
            "vars": data.get("group_vars", {})  # Group-level variables
        }
    }

    # Convert inventory to JSON format and print
    print(json.dumps(inventory))
```
## Script Invocation:
```python
if __name__ == "__main__":
    main()
```
## Execution Flow
```python
The script reads the YAML file containing information about hosts and group variables.
It constructs an inventory structure in memory based on the YAML data.
The inventory structure includes group-level variables and a list of hosts under the "nxos_switches" group.
Finally, it converts the inventory structure to JSON format and prints it to standard output.
```
## hosts_vars.yml
```yaml
hosts_list:
  hosts:
    n7k-1:
      ansible_host: 10.10.35.99
    n9k-a:
      ansible_host: 10.10.35.100
    n9k-b:
      ansible_host: 10.10.35.101

  group_vars:
    ansible_become: yes
    ansible_become_method: enable
    ansible_connection: ansible.netcommon.network_cli
    ansible_network_os: nxos
    ansible_user: cisco
```
## Create an Encrypted File:
```bash
ansible-vault create secrets.yml
```
```bash
(myenv) [ubuntulab@workstation-centos8 cisco-nxos-branch1]$ ansible-vault create secrets.yml
New Vault password:
Confirm New Vault password:
```
## Edit the Encrypted File:
```bash
ansible-vault edit secrets.yml
```
```bash
(myenv) [ubuntulab@workstation-centos8 cisco-nxos-branch1]$ ansible-vault view secrets.yml
Vault password:
ansible_ssh_password: cisco
ansible_become_password: cisco
```
## Use the Encrypted File in Playbook:
```yaml
(myenv) [ubuntulab@workstation-centos8 cisco-nxos-branch1]$ cat dynamic_play.yml
---
- name: Test Cisco NX-OS Connection
  hosts: all
  vars_files:
    - secrets.yml
  tasks:
  - name: Check connectivity
    ping:
```

## Test Results
```bash
(myenv) [ubuntulab@workstation-centos8 cisco-nxos-branch1]$ ansible-playbook -i dynamic_inventory-4.py dynamic_play.yml --ask-vault-password 2>/dev/null
Vault password:

PLAY [Test Cisco NX-OS Connection] **********************************************************

TASK [Gathering Facts] **********************************************************************
ok: [n7k-1]
ok: [n9k-a]
ok: [n9k-b]

TASK [Check connectivity] *******************************************************************
ok: [n9k-a]
ok: [n7k-1]
ok: [n9k-b]

PLAY RECAP **********************************************************************************
n7k-1                      : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
n9k-a                      : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
n9k-b                      : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```
