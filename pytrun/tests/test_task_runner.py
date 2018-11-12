"""Tests for TaskRunner."""
from unittest import TestCase, mock, main as unittest_main

from pytrun.task_runner import TaskRunner


class TaskRunnerTests(TestCase):
    """Tests for TaskRunner."""

    # TODO: test config load
    # TODO: test os calls

    def setUp(self):
        self._args = {
            'config': 'some/file',
            'task': 'any',
        }
        self._config = {
            "main": ["echo hello pytrun"]
        }

    def test_error_file_dont_exists(self):
        file = self._args['config']

        try:
            TaskRunner(file)
        except FileNotFoundError as err:
            assert str(err) == "some/file can't be found!"

    def test_run_task_bundle(self):
        file = self._args['config']
        TaskRunner._run_task = mock.Mock()
        TaskRunner._get_config = mock.MagicMock(return_value=self._config)

        runner = TaskRunner(file)
        tasks = ['task1',
                 'task2']
        runner._run_subtasks(tasks)

        # Asserts
        assert runner._run_task.call_count == 2
        runner._run_task.assert_has_calls([mock.call(i) for i in tasks])

    @mock.patch('os.system')
    def test_run_task(self, system):
        file = self._args['config']
        # TaskRunner.run = mock.Mock()
        TaskRunner._get_config = mock.MagicMock(return_value=self._config)
        # system = mock.MagicMock(return_value=True)

        task = ['main']
        item = self._config[task[0]][0]
        # import pdb; pdb.set_trace()
        runner = TaskRunner(file)
        runner.run(task)

        # Asserts

        system.assert_called_with(item)


if __name__ == '__main__':
    unittest_main()
