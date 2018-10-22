"""Define TaskRunner."""
import yaml
from os import path, system


class TaskRunner(object):
    """Define TaskRunner."""

    def __init__(self, file):
        """Load tasks definition."""
        # parse file to config
        self.config = self._get_config(file)

    def run(self, task):
        """Run a task."""
        cmds = self.config[task]

        if isinstance(cmds, dict):
            tasks = cmds.get('tasks')
            if tasks:
                return self._run_tasks(tasks)
            else:
                raise ValueError('Wrong description for task {}.'.format(task))

        elif isinstance(cmds[0], str):
            for cmd in cmds:
                print("[start:{}] - {}".format(task, cmd))
                system(cmd)
                print("[finished:{}] - {}".format(task, cmd))

    def _run_tasks(self, tasks):
        for task in tasks:
            self.run(task)

    def _get_config(self, file):
        abs_path = path.abspath(file)
        filename = abs_path.split('.')[0]
        ext_list = [
            'yml',
            'yaml',
        ]

        for ext in ext_list:
            pathname = '{}.{}'.format(filename, ext)
            if path.exists(pathname):
                stream = open(pathname, 'r')
                return yaml.load(stream=stream)

        raise FileNotFoundError("{} can't be found!".format(file))
