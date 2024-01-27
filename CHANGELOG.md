
# 0.2.15 (2024-01-27)

### Added

- Adds option in `run_command` to print stderror

# 0.2.14 (2023-05-17)

### Added

- Adds `GitRepo` `config_user_name` and `config_user_email` methods

# 0.2.13 (2023-05-11)

### Added

- Adds `GitRepo` `default_remote` and `default_branch` cached properties

# 0.2.12 (2023-03-06)

### Added

- Adds `git_rm_and_clean` function to wipe git repository content (everything but `.git` dir)

# 0.2.11 (2022-12-02)

### Added

- Adds `GhRepo` `delete_ref` method

# 0.2.10 (2022-11-25)

### Added

- Adds `GitRepo`, `GhOrg`, `GhOrgSecret` and `GhRepo` helper classes
- Adds tests for the `GhRepo` class
- Adds `subblack`, `subred`, `subgreen`, `subyellow`, `subblue`, `submagenta`, `subcyan`, and `subwhite` helpers for `colorama`

### Updated

- Updates `GitHubRepo` constructor params (`username` removed)

# 0.2.9 (2022-11-25)

### Added

- Adds `manage_command` command subprocess helper handling output for `run_command`
- Adds `black`, `red`, `green`, `yellow`, `blue`, `magenta`, `cyan` and `white` helpers for print with `colorama`

### Updated

- Update `run_command` to print command output progressively (used in order to display remote command output when calling `gcloud compute ssh ...`)

# 0.2.8 (2022-11-25)

### Updated

- Updates `are_directories_identical` to add a parameter to ignore a list of patterns
- Updates `resolve_scope` to add a parameter to return the list of inexisting sources passed as parameter

# 0.2.7 (2022-10-20)

### Added

- Adds `rename_branch` git helper

# 0.2.6 (2022-04-17)

### Added

- Adds `PublicationCommand`, `GitRepo` and `Scope` classes with tests
- Adds `are_directories_identical` test helper and `TestBaseDirectoryEquality` test base class + tests for both

# 0.2.5 (2022-04-01)

### Updated

- Updates `git_remote_get_probable_url` to return ssh clone address format

# 0.2.4 (2022-03-25)

### Added

- Adds `git_remote_get_probable_url` allowing to list repo remotes matching a github nickname

# 0.2.3 (2022-01-19)

### Added

- Adds `AliasedGroup` in order to enable the use of prefixes when calling click script commands (i.e. `challengify ite` instead of `challengify iterate`)
