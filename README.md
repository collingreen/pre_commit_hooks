pre-commit-hooks
==========

Hooks for use with [pre-commit](https://github.com/pre-commit/pre-commit)


### Using pre-commit-hooks with pre-commit

Add this to your `.pre-commit-config.yaml`

    -   repo: git://github.com/collingreen/pre-commit-hooks
        sha: ''  # Use the sha you want to point at
        hooks:
        -   id: name-of-hook


### Hooks available

- `do-not-commit` - Looks for strings like '# DONOTCOMMIT'
    - Set flags for places you know you must return to before committing


### Running Tests
`tox`
