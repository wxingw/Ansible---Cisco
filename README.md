
# Ansible Automation for Network and System Management

This repository provides a comprehensive suite of Ansible playbooks and scripts designed for robust automation across both Cisco Nexus switches and Linux systems. It focuses on configuration management, system updates, and routine diagnostics, leveraging Ansible's capabilities to handle both network devices and servers.

## Features

- **Dynamic Inventory**: Leverages Ansible's dynamic inventory capabilities to manage diverse environments including network devices and servers.
- **Automated Configuration Management**: Periodic backups of configurations and system settings across Cisco switches and Linux servers.
- **Operational Commands Execution**: Facilitates execution of operational commands, like retrieving running configurations from Cisco Nexus switches and checking system status on Linux.
- **Diagnostics and Troubleshooting**: Provides tools for routine network diagnostics and system health checks.

## Prerequisites

- **Ansible**: Version 2.9 or later is required.
- **Python**: Version 3.6 or later.
- **Device Access**: SSH enabled for Cisco Nexus switches and Linux systems.
- **Remote Storage**: FTP or SCP server access for storing backups.

## Setup

1. **Install Ansible**:
   Install Ansible on your control machine using pip:
   ```bash
   pip install ansible
   ```
2. **Configure Dynamic Inventory**:
   Adapt the `inventory/dynamic_inventory.py` script for your specific environment to dynamically include both Cisco switches and Linux hosts.

3. **Setup Secure Credentials**:
   Securely store credentials using Ansible Vault:
   ```bash
   ansible-vault create secrets.yml
   ```
   Include necessary access credentials such as SSH passwords and remote storage access details.

4. **Playbook Configuration**:
   Customize playbooks according to your network and system requirements. Ensure paths to dynamic inventory and secrets file are correctly set.

## Usage

- **Running Configurations Backups**:
  Execute configuration backups across all managed devices:
  ```bash
  ansible-playbook -i inventory/dynamic_inventory.py playbooks/backup.yml --ask-vault-pass
  ```

- **Displaying Running Configurations**:
  Fetch and display current configurations from devices:
  ```bash
  ansible-playbook -i inventory/dynamic_inventory.py playbooks/show_run.yml --ask-vault-pass
  ```

- **Executing Troubleshooting**:
  Run diagnostic and troubleshooting playbooks:
  ```bash
  ansible-playbook -i inventory/dynamic_inventory.py playbooks/troubleshoot.yml --ask-vault-pass
  ```

## Troubleshooting Common Issues

- **Authentication Failures**: Check the accuracy of credentials in `secrets.yml` and ensure Ansible Vault is unlocked during runs.
- **Dynamic Inventory Challenges**: Keep the dynamic inventory script updated with changes in the network and server topology.
- **Connection Problems**: Verify network connectivity, SSH configurations, and the operational status of FTP/SCP servers.

## Contributing

We welcome contributions to enhance the playbooks or introduce new features. Please fork the project, make your changes, and submit a pull request.

## License

This project is available under the MIT License. See the LICENSE file for more details.

