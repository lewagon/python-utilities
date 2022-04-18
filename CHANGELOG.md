
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
