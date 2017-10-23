# Ansible multienvironments template

## Generate project

```bash
./ansibleGen.py
```

## Directories describe

```
.
|-- ansible.cfg                         # ansible configuration file
|-- environments                        # directory for all your environments
|   |-- 000_cross_env_vars.yml          # cross environtments vars
|   |-- 000_cross_env_vault_vars.yml    # cross environtments hashed vars
|   |-- dev                             # environment dev
|   |   |-- group_vars
|   |   |   |-- all
|   |   |   |   |-- 000_cross_env_vars.yml -> ../../../000_cross_env_vars.yml
|   |   |   |   |-- 000_cross_env_vault_vars.yml -> ../../../000_cross_env_vault_vars.yml
|   |   |   |   |-- vars.yml
|   |   |   |   `-- vault.yml
|   |   |   |-- db
|   |   |   |   `-- vars.yml
|   |   |   `-- web
|   |   |       `-- vars.yml
|   |   `-- hosts                       # dev hosts
|   |-- prod                            # environment prod
|   |   |-- group_vars
|   |   |   |-- all
|   |   |   |   |-- 000_cross_env_vars.yml -> ../../../000_cross_env_vars.yml
|   |   |   |   |-- 000_cross_env_vault_vars.yml -> ../../../000_cross_env_vault_vars.yml
|   |   |   |   |-- vars.yml
|   |   |   |   `-- vault.yml
|   |   |   |-- db
|   |   |   |   `-- vars.yml
|   |   |   `-- web
|   |   |       `-- vars.yml
|   |   `-- hosts                       # prod hosts
|   `-- stage                           # environment stage
|       |-- group_vars
|       |   |-- all
|       |   |   |-- 000_cross_env_vars.yml -> ../../../000_cross_env_vars.yml
|       |   |   |-- 000_cross_env_vault_vars.yml -> ../../../000_cross_env_vault_vars.yml
|       |   |   |-- vars.yml
|       |   |   `-- vault.yml
|       |   |-- db
|       |   |   `-- vars.yml
|       |   `-- web
|       |       `-- vars.yml
|       `-- hosts                       # stage hosts
|-- roles                               # roles directory
|   `-- role_1                          # one role
|       |-- defaults                    # default vars
|       |-- files                       # files dir
|       |-- tasks                       # tasks files
|       |   |-- apply.yml
|       |   |-- main.yml                # main file includ other tasks
|       |   `-- purge.yml
|       `-- templates                   # templates dir
|-- tasks                               # simple pre/post tasks dir
|   |-- tasks_post.yml
|   `-- tasks_pre.yml
`-- test-playbook.yml                   # project playbook

```

## Commands to run project

### Development environment (default)
```bash
ansible-playbook test-playbook.yml
```
or
```bash
ansible-playbook -i environments/dev test-playbook.yml

```

### Stage environment
```bash
ansible-playbook -i environments/stage test-playbook.yml

```

### Prod environment
```bash
ansible-playbook -i environments/prod test-playbook.yml

```