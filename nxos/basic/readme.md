
# Ansible Configuration for Nexus Switches

This repository contains Ansible playbooks and configurations for managing Cisco Nexus switches. The structure is organized to easily manage tasks such as checking switch status, displaying configurations, and troubleshooting common issues.

## Directory Structure

Here is the basic layout of the project:

```
basic/
├── ansible.cfg                  # Ansible configuration file.
├── check_nexus_switches.yml     # Playbook for checking the status of Nexus switches.
├── group_vars/
│   └── nxos_switches/
│       └── vault.yml            # Encrypted variables specific to Nexus switches.
├── inventory/
│   └── inventory                # Inventory file with details about the switches.
├── readme.md                    # This README file.
├── show-run.yml                 # Playbook to display the running configuration of switches.
└── troubleshoot.yml             # Playbook for troubleshooting common issues.
```

## Configuration

### Ansible Configuration File

- `ansible.cfg`: Specifies default settings for Ansible, such as the inventory location and defaults that are applicable across all playbooks.

### Inventory

- `inventory/inventory`: Defines the hosts and groups that Ansible will target. Adjust this file to include your Cisco Nexus switches.

### Group Variables

- `group_vars/nxos_switches/vault.yml`: Stores sensitive variables like passwords. This file is encrypted with Ansible Vault.

## Playbooks

- `check_nexus_switches.yml`: Runs diagnostic checks on Nexus switches to ensure they are operating correctly.
- `show-run.yml`: Collects and displays the running configurations from the Nexus switches.
- `troubleshoot.yml`: Contains tasks to troubleshoot common network issues that may arise.

## Usage

To run a playbook, use the following command:

```bash
ansible-playbook -i inventory/inventory playbook_name.yml
```

Replace `playbook_name.yml` with the name of the playbook you wish to run.

## Security

Ensure your `vault.yml` is kept secure and access is restricted to authorized users only.

## Contributions

Contributions to this project are welcome. Please ensure that you update the inventory and variable files as necessary to reflect the configuration of your environment.

## License

Specify the license under which this project is made available.
