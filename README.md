# Python Yaml Task RUNner (pytrun).

Simple tool to run tasks defined in a Yaml file.

## Usage

First of all you need to create a `tasks.yaml` or `tasks.yml` to define which tasks should run.

```yaml
setup:
    - pip install -e .[dev]

```

```bash
pytrun setup
```

Also you can specify another file to pytrun:

```sh
pytrun setup -c ./my-tasks.yml
```
