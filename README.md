# Python Yaml Task RUNner (pytrun).

Simple tool to run tasks defined in a Yaml file.

## Usage

First of all you need to create a `tasks.yaml` or `tasks.yml` to define which tasks should run.

```yaml
setup:
    - pip install -e .[dev]


build:
  - python setup.py sdist

```

```bash
pytrun setup build
```

Also you can specify another file to pytrun:

```sh
pytrun setup build -c ./my-tasks.yml
```
