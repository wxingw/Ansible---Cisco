
# NTP Configuration with Ansible

## Overview

This project automates the Network Time Protocol (NTP) configuration across Cisco NX-OS switches using Ansible. It provides a comprehensive approach to manage time synchronization settings effectively, ensuring all network devices are synchronized.

## Project Structure

```
.
├── ansible.conf               # Ansible configuration file
├── dynamic_vars               # Dynamic variables for inventory
│   └── dynamic_inventory.yml  # YAML file with dynamic inventory configurations
├── group_vars                 # Group-specific variables
│   ├── all.yml                # Variables applicable to all groups
│   └── ntp_servers.yml        # NTP-specific variables for NTP servers
├── host_vars                  # Host-specific variables
│   └── specific_host.yml      # Variables specific to a host
├── inventory                  # Inventory files for Ansible
│   ├── hosts                  # Static hosts file (unused)
│   └── inventory.py           # Dynamic inventory script
├── playbooks                  # Directory containing all playbooks
│   ├── ntp-playbook.yml       # Main playbook for NTP configuration
│   └── set_ANSIBLE_INVENTORY.sh  # Script to set the ANSIBLE_INVENTORY environment variable
├── README.md                  # This README file
├── roles                      # Ansible roles for task organization
│   ├── common                 # Common role for shared tasks across all configurations
│   │   ├── files              # Additional files for the role
│   │   ├── handlers           # Handlers for this role
│   │   │   └── main.yml       # Main handlers file
│   │   ├── tasks              # Tasks for the common role
│   │   │   └── main.yml       # Main task file
│   │   └── templates          # Templates used by this role
│   ├── files                  # General files for the project
│   └── ntp                    # Role specifically for NTP configuration
│       ├── handlers           # Handlers for NTP role
│       │   └── main.yml       # Main handlers file
│       ├── tasks              # Tasks specific to the NTP configuration
│       │   └── main.yml       # Main task file for NTP
│       └── templates          # Templates for NTP configuration
│           └── ntp.conf.j2    # Jinja2 template for NTP configuration
└── secrets.yml                # Encrypted secrets for Ansible
```

## Usage

To use this project, you will need to have Ansible installed along with the required roles and collections. Make sure to adjust your `ansible.conf` to point to the correct inventory and adjust the variables in `group_vars` and `host_vars` as necessary.

### Setting Up the Environment

Run the script to set the Ansible inventory environment variable:

```bash
source playbooks/set_ANSIBLE_INVENTORY.sh
```

### Running the Playbook

To apply the NTP configuration to your Cisco NX-OS switches:

```bash
ansible-playbook -i inventory/inventory.py playbooks/ntp-playbook.yml --ask-vault-pass
```

Enter the vault password when prompted to unlock the encrypted `secrets.yml` file, which contains sensitive information such as passwords.

## Customization

You can customize the NTP settings by editing the `ntp_servers.yml` in `group_vars` and the Jinja2 template `ntp.conf.j2` under the `ntp` role's `templates` directory.

## License

Specify your project license here, which dictates how others can use and contribute to your project.

