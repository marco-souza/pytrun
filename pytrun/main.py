"""Pytrun main script."""
import argparse

from pytrun.task_runner import TaskRunner


def cli():
    """CLI argparse."""
    parser = argparse.ArgumentParser(description='Python Yaml Task RUNner')
    # task
    parser.add_argument('tasks', type=str, default="main", nargs='+',
                        help='Task Name defined on your task file.')
    # config
    parser.add_argument('--config', '-c', type=str, default="./tasks",
                        help='File to get tasks definition.')
    parser.add_argument('--args', '-a', nargs='+',
                        help='Arguments.')
    args = parser.parse_args()
    return args


def main():
    """Run main code."""
    args = cli()
    runner = TaskRunner(args.config)
    runner.run(args.tasks, args.args)


if __name__ == "__main__":
    main()
