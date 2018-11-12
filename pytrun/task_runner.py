"""Define TaskRunner."""
import yaml
import os


class TaskRunner(object):
    """Define TaskRunner."""

    def __init__(self, file):
        """Load tasks definition."""
        # parse file to config
        self.config = self._get_config(file)

    def run(self, tasks):
        for task in tasks:
            self._run_task(task)

    def _run_task(self, task):
        """Run a task."""
        cmds = self.config[task]

        if isinstance(cmds, dict):
            tasks = cmds.get('tasks')
            if tasks:
                return self._run_subtasks(tasks)
            else:
                raise ValueError('Wrong description for task {}.'.format(task))

        elif isinstance(cmds[0], str):
            for cmd in cmds:
                print("[start:{}] - {}".format(task, cmd))
                os.system(cmd)
                print("[finished:{}] - {}".format(task, cmd))

    def _run_subtasks(self, tasks):
        for task in tasks:
            self.run(task)

    def _get_config(self, file):
        abs_path = os.path.abspath(file)
        filename = abs_path.split('.')[0]
        ext_list = [
            'yml',
            'yaml',
        ]

        for ext in ext_list:
            pathname = '{}.{}'.format(filename, ext)
            try:
                with open(pathname, 'r') as stream:
                    return yaml.load(stream)
            except FileNotFoundError:
                pass

        raise FileNotFoundError("{} can't be found!".format(file))
