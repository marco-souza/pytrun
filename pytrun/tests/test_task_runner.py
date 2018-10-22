"""Tests for TaskRunner."""
from unittest import TestCase, mock, main as unittest_main

import yaml

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

    @mock.patch('yaml', autospec=True)
    def test_task_runner_init(self, mock_yaml):
        file = self._args['config']
        TaskRunner._get_config = mock.Mock()

        runner = TaskRunner(file)

        TaskRunner._get_config.assert_called_with(file)
        assert runner.config == self._config
        mock_yaml.load.assert_called_with()


if __name__ == '__main__':
    unittest_main()
