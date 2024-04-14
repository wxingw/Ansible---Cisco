
# Resolution of Ansible Inventory Configuration Issue

## Background
We encountered a recurring issue where Ansible playbooks were not executing as expected. The core problem was traced to Ansible defaulting to an incorrect inventory source, which was caused by an environment variable (`ANSIBLE_INVENTORY`) improperly directing Ansible to use a Python script as the inventory. This script, located at `/home/ubuntulab/ansible/cisco-git/nxos/ntp-project/inventory/inventory.py`, was failing due to missing files and incorrect output format.

## Issue Description
The erroneous behavior manifested as a series of errors and warnings indicating that Ansible could not parse the inventory due to missing files and format mismatches. This problem prevented Ansible from recognizing any hosts other than localhost, thus skipping all designated tasks for other hosts.

## Resolution Steps

1. **Identified the Source of Error:**  
   The initial clue was the setting of the `ANSIBLE_INVENTORY` environment variable, which was pointing to the problematic Python script.

2. **Unset the Environment Variable:**  
   To isolate the issue, we temporarily unset the `ANSIBLE_INVENTORY` variable using the command `unset ANSIBLE_INVENTORY` in the terminal. This immediately corrected the issue, confirming that the environment variable was the culprit.

3. **Verification of Shell Configuration Files:**  
   We checked the user's `.bashrc` file and other common configuration files for any commands that might have automatically set the `ANSIBLE_INVENTORY` variable. No such commands were found, suggesting that the variable might have been set in another session-specific script or manually.

4. **Ensured Persistent Resolution:**  
   To prevent future sessions from inadvertently resetting the `ANSIBLE_INVENTORY` variable, we added a precautionary `unset ANSIBLE_INVENTORY` command to the `.bashrc` file. This ensures the variable remains unset for all new terminal sessions.

5. **Test and Confirm Configuration:**  
   After making these changes, we reran the Ansible playbooks without specifying an inventory file, ensuring that Ansible defaulted to the correct inventory specified in the `ansible.cfg` file. The playbooks executed successfully, confirming the resolution.

## Conclusion
The issue was resolved by identifying and unsetting an erroneously set environment variable that misdirected Ansible to an incorrect and non-functional inventory source. Ensuring that this variable remains unset in future sessions prevents recurrence of the problem.

## Recommendation
It is advisable for all team members to review their environment settings and shell configuration files to ensure no unintended settings interfere with system operations. Additionally, documenting these kinds of environment dependencies is recommended to facilitate troubleshooting and configurations.

