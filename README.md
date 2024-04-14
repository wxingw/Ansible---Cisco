[200~
# Ansible Management for Cisco Nexus Switches

This repository contains Ansible playbooks and scripts designed to manage Cisco Nexus switches. It includes automation for tasks such as configuration backups, retrieving running configurations, and basic troubleshooting. The setup utilizes Ansible's capabilities to work with dynamic inventories and provides a robust framework for network automation.

## Features

- **Dynamic Inventory**: Utilizes an Ansible dynamic inventory script to automatically discover and define switches in the network.
- **Automated Backups**: Scheduled backups of switch configurations to a remote server.
- **Show Running Configuration**: Playbook to fetch and display the current running configuration from the switches.
- **Basic Troubleshooting**: Includes playbooks for basic network diagnostics.
- **Expandable Framework**: Easily extendable to include more advanced networking tasks and configurations.

## Prerequisites

- **Ansible**: Version 2.9 or later.
- **Python**: Version 3.6 or later.
- **Access to Cisco Nexus switches**: SSH access enabled.
- **FTP or SCP server**: For storing configuration backups.

## Setup

### 1. Install Ansible

Ensure that Ansible is installed on your control machine. You can install Ansible with pip:

```bash
pip install ansible
```

### 2. Configure Dynamic Inventory

- Modify the `inventory/dynamic_inventory.py` script to suit your network topology and authentication methods.
- Ensure that the script is executable and returns inventory in a JSON format that Ansible can parse.

### 3. Setup Credentials

- Use Ansible Vault to encrypt credentials. Create a `secrets.yml` file to store sensitive data:

```bash
ansible-vault create secrets.yml
```

Include credentials like SSH passwords, enable passwords, and FTP/SCP credentials.

### 4. Configure Playbooks

- Edit the playbooks to match your network requirements and paths to the dynamic inventory and secrets file.

## Usage

### Running Backups

To run a configuration backup across all your Nexus switches:

```bash
ansible-playbook -i inventory/dynamic_inventory.py playbooks/backup.yml --ask-vault-pass
```

### Display Running Configuration

To display the running configuration of the switches:

```bash
ansible-playbook -i inventory/dynamic_inventory.py playbooks/show_run.yml --ask-vault-pass
```

### Basic Troubleshooting

Execute troubleshooting playbooks:

```bash
ansible-playbook -i inventory/dynamic_inventory.py playbooks/troubleshoot.yml --ask-vault-pass
```

## Troubleshooting Common Issues

- **Authentication Failures**: Ensure that the credentials in `secrets.yml` are correct and that Ansible Vault is unlocked correctly during playbook runs.
- **Dynamic Inventory Errors**: Verify that the dynamic inventory script is up-to-date with network changes and correctly configured.
- **Connection Issues**: Check network connectivity, SSH configurations, and the availability of the FTP/SCP servers.

## Contributing

Contributions to improve the playbooks or add new features are welcome. Please fork the project and submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

