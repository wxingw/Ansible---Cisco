
# FTP Server and Client Management with Ansible

This project contains a collection of Ansible playbooks and templates for setting up and managing FTP servers and clients across different environments. The playbooks handle the installation of FTP services, configuration of firewall settings, and file transfers, ensuring a consistent setup across multiple servers.

## Project Structure

```
.
├── ansible.cfg                      # Ansible configuration file with default settings
├── ansible-vsftpd.yml               # Playbook for setting up VSFTPD on servers
├── ansible-vsftp-yum-only.yml       # Playbook for installing VSFTPD using YUM (CentOS specific)
├── create-ftp-users.yml             # Playbook for creating FTP user accounts
├── ftpclients.yml                   # Playbook for setting up FTP clients
├── inventory                        # Inventory file defining the servers
├── README.md                        # This README file
├── secret.yml                       # Encrypted secrets, such as passwords
├── site.yml                         # Main playbook that includes others as needed
├── templates/                       # Templates for configuration files
│   └── vsftpd.conf.j2               # Template for VSFTPD configuration
├── transfer-test-file.yml           # Playbook for testing file transfers via FTP
└── vars/                            # Variable files for playbooks
    ├── defaults-template.yml        # Template for default variables (example)
    └── vars.yml                     # Specific variables for playbooks
```

## Features

- **FTP Server Setup**: Configures VSFTPD on CentOS and Ubuntu servers with custom settings.
- **FTP Client Setup**: Ensures that FTP clients are configured to interact with the FTP servers.
- **Firewall Management**: Handles firewall configurations using `firewalld` on CentOS and `ufw` on Ubuntu to ensure FTP ports are accessible.
- **File Transfer Tests**: Includes a playbook to test file transfers, verifying that the setup works as expected.

## Usage

To run any playbook, use the following command:

```bash
ansible-playbook -i inventory <playbook_name>.yml
```

Replace `<playbook_name>` with the name of the playbook you wish to run. For example, to set up FTP servers, run:

```bash
ansible-playbook -i inventory site.yml
```

## Requirements

- Ansible 2.9 or higher
- Access to the target servers defined in the `inventory` file
- Appropriate permissions to manage services and firewall settings on the target servers

## Configuration

Edit the `vars.yml` and `secret.yml` files to match your environment's requirements. The `secret.yml` file should be encrypted using Ansible Vault for security.

## Contributing

Contributions to this project are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is available under the MIT License. 

---

For more detailed instructions on how to use each playbook, refer to the comments within each playbook file.
