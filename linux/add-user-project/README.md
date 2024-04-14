
# Managing Users with Ansible

This project includes three Ansible playbooks that demonstrate different methods of defining variables when adding and removing a user from a system. Each playbook uses a different approach to manage the user variables, such as `username`, `uid`, and `shell`.

## Overview of Playbooks

### 1. Inline Variables (`add-user-vars.yml`)

This playbook defines variables directly within the playbook under the `vars` section.

```yaml
vars:
  username: tom
```

### 2. Variables from Files (`add-user-vars-files.yml`)

This playbook imports variables from an external file specified under `vars_files`. This allows you to separate variable definitions from the playbook logic, which is useful for managing variables in a centralized manner.

```yaml
vars_files:
  - vars/main.yml
```

### 3. Variables from Group Vars (`add-user-group-vars.yml`)

This playbook relies on variables defined in the `group_vars` directory, which are automatically loaded based on the host's group membership in the inventory. This method is typically used for setting variables that have different values across various groups of hosts.

## Comparison and Priority

- **Inline Variables:** Defined directly within the playbook. Useful for specific overrides or when variables are not going to change frequently.
- **Variables from Files:** Separated into different files under the `vars` directory. This separation is advantageous for reusability and environment-specific configurations.
- **Group Variables:** Automatically loaded if they match the group names in the inventory. Ideal for managing settings that vary between different server environments or deployment stages.

## Variable Priority

Ansible has a specific order of precedence for variables:

1. **Variables directly in the playbook (Inline Variables).**
2. **Variables included from files specified at the playbook level (`vars_files`).**
3. **Variables from inventory (`group_vars` and `host_vars`).**

This means that if the same variable is defined in multiple places, the one defined in the playbook (`vars`) will take precedence over the ones in `vars_files` and `group_vars`.

## Conclusion

Choosing the right method for variable management depends on your project's needs and the complexity of your environments. Inline variables offer simplicity, `vars_files` offer modularity, and group variables offer adaptability to different environments.

