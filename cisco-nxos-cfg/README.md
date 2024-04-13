# Cisco Nexus Configuration Backup

This project includes an Ansible playbook designed to backup the running configurations of Cisco Nexus switches to a remote FTP server. It uses Ansible to automate the backup process, ensuring that configurations are regularly saved and can be restored if necessary.

## Project Structure

- `backup.yml` - The main Ansible playbook that performs the backup.
- `inventory/` - Directory containing the Ansible inventory file `inventory.py`, which lists the Nexus switches.
- `secrets.yml` - An encrypted Ansible Vault file containing sensitive variables like passwords.

## Prerequisites

1. Ansible 2.9 or higher installed on your control machine.
2. Access to Cisco Nexus switches with network automation enabled.
3. A configured FTP server with appropriate permissions.

## Setup Instructions

1. **Configure Inventory:**
   - Edit `inventory/inventory.py` to include the IP addresses of the Cisco Nexus switches you want to backup.

2. **Prepare the Secrets File:**
   - Use `ansible-vault create secrets.yml` to create a new secrets file if not already present.
   - Ensure the following variables are included and correctly encrypted:
     - `ansible_ssh_password`: SSH password for the Nexus switches.
     - `ansible_become_password`: Enable password for the Nexus switches, if applicable.
     - `ftp_pass`: Password for the FTP server.

3. **FTP Server Configuration:**
   - Ensure the FTP server is running and accessible from the Nexus switches.
   - Configure the directory `/backup/nexus` on the FTP server with write permissions for the user `ftpuser`.

4. **Running the Playbook:**
   - Execute the playbook with the following command:
     ```
     ansible-playbook -i inventory/inventory.py backup.yml --ask-vault-pass
     ```
   - Enter the vault password when prompted to decrypt the `secrets.yml` file.

## Usage

To perform a backup, simply run the `backup.yml` playbook as described in the setup instructions. This will trigger the backup process for all configured switches and save their configurations to the specified FTP server directory.

## Troubleshooting

- **Permission Issues on FTP Server:** Make sure the `ftpuser` has the necessary write permissions on the `/backup/nexus` directory.
- **Ansible Vault Password:** If you receive errors related to the vault password, ensure that the correct password is being used and that the `secrets.yml` file is properly formatted.
- **Connectivity Issues:** Verify network connectivity between the Ansible control node and both the Cisco Nexus switches and the FTP server.

## Contributing

Contributions to this project are welcome. Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

