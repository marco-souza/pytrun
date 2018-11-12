"""Define TaskRunner."""
import yaml
import os


class TaskRunner(object):
    """Define TaskRunner."""

    def __init__(self, file):
        """Load tasks definition."""
        # parse file to config
        self.config = self._get_config(file)

    def run(self, tasks, args=""):
        for task in tasks:
            self._run_task(task, args)

    def _run_task(self, task, args=""):
        """Run a task."""
        cmds = self.config[task]

        if isinstance(args, list):
            if args:
                args = " ".join(args)
            else:
                args = ""

        if isinstance(cmds, dict):
            tasks = cmds.get('tasks')
            if tasks:
                return self._run_subtasks(tasks)
            else:
                raise ValueError('Wrong description for task {}.'.format(task))

        elif isinstance(cmds, list):
            for cmd in cmds:
                print("--- [start:{}] - {}".format(task, cmd))
                if args:
                    command = "{} {}".format(cmd, args)
                else:
                    command = "{}".format(cmd)
                os.system(command)
                print("--- [finished:{}] - {}".format(task, cmd))

    def _run_subtasks(self, tasks):
        for task in tasks:
            self._run_task(task)

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
