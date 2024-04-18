
# Ansible Configuration for Cisco NX-OS Devices Management

This repository includes Ansible playbooks and configuration files for managing Cisco NX-OS network devices across multiple sites in Canada, focusing on dynamic inventory management and group-specific configurations.

## Directory and File Structure

- **ansible.cfg**: Main Ansible configuration file that sets the default inventory directory and other global settings.
- **group_vars/**: Contains variables for specific groups of hosts.
  - `montreal.yml`: Settings for devices in Montreal.
  - `nxos_switches.yml`: Settings for all Cisco NX-OS switches.
  - `toronto.yml`: Settings for devices in Toronto.
- **hosts_vars.yml**: Defines group memberships for hosts, used by the dynamic inventory script.
- **inventory/**: Contains inventory files and scripts.
  - `01hosts.yml`: Static inventory file defining hosts under geographical and functional groupings.
  - `02inventory.py`: Python script for generating a dynamic inventory from `hosts_vars.yml`.
- **playbook.yml**: Main playbook that tests connectivity to Cisco NX-OS devices.
- **README.md**: Documentation file (this file).
- **secrets.yml**: Encrypted file containing sensitive variables (use Ansible Vault).

## Inventory Configuration

### Static Inventory

The `01hosts.yml` file organizes hosts into hierarchical groups by region (`east`, `central`, `west`) with specific host variables like `ansible_host`.

### Dynamic Inventory

The `02inventory.py` script dynamically generates inventory data based on group memberships defined in `hosts_vars.yml`. This allows for flexible inventory management and integration into automated workflows.

### `/etc/ansible/hosts`

This default Ansible inventory file is not actively used in this setup, given our custom inventory scripts. However, it provides a fallback or traditional approach to host management. Example entries:
```plaintext
[toronto]
n7k-1
n9k-a

[montreal]
n9k-b

[nxos_switches]
n7k-1
n9k-a
n9k-b
```

### `ansible.cfg`

This configuration file directs Ansible to use the custom inventory setup and includes other default settings:
```ini
[defaults]
inventory = inventory
```
This setting specifies that Ansible should look for inventory details within the `inventory/` directory, allowing the use of both static and dynamic inventory mechanisms.

## Running the Playbook

To test connectivity using the dynamic inventory:

```bash
ansible-playbook -i inventory/02inventory.py playbook.yml --ask-vault-pass
```

Enter your vault password when prompted to decrypt the `secrets.yml` file.

## Dynamic Inventory Script Usage

The `02inventory.py` script should be invoked with the `--list` argument to generate a JSON formatted inventory that Ansible can understand:

```bash
./inventory/02inventory.py --list
```

## Troubleshooting

If encountering errors related to Ansible collection support or playbook locations, verify that:
- Your Ansible version supports the collections used in tasks.
- The playbook file names are correct in commands.

## Contributing

Contributions to enhance or extend playbook functionalities are welcome. Please fork this repository and submit pull requests for review.

## License

This project is available under the MIT License.



## Contact Information

For more information or support related issues, please contact me.
