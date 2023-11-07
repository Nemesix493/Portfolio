import os

from .deployer import AbstractDeployer
from .utils import run_terminal_command


class HerokuDeployer(AbstractDeployer):
    required_info = [
        'HEROKU_APP_NAME',
        'HEROKU_API_KEY',
        'HEROKU_AUTH_TOKEN',
        'HEROKU_EMAIL'
    ]

    @staticmethod
    def set_heroku_file() -> None:
        commands = [
            'echo "machine api.heroku.com" >> ~/.netrc',
            'echo "login $HEROKU_EMAIL" >> ~/.netrc',
            'echo "password $HEROKU_AUTH_TOKEN" >> ~/.netrc'
        ]
        run_terminal_command(
            command="; ".join(commands),
            command_name='set_heroku_file'
        )

    @staticmethod
    def push_to_git_heroku(deploying_info: dict) -> None:
        command = f'git push https://heroku:{deploying_info["HEROKU_API_KEY"]}'\
            f'@git.heroku.com/{deploying_info["HEROKU_APP_NAME"]}.git master'
        run_terminal_command(
            command=command,
            command_name='Git Push Heroku'
        )

    @classmethod
    def get_deploying_info(cls) -> dict:
        deploying_info = {
            key: os.getenv(key, None)
            for key in cls.required_info
        }
        missing_info = [
            key
            for key, val in deploying_info.items()
            if val is None
        ]
        if missing_info:
            raise Exception(
                f'Missing required informations : [{", ".join(missing_info)}]'
            )
        return deploying_info

    @staticmethod
    def run_remote_commands(deploying_info: dict) -> None:
        remote_commands = [
            'python -m manage migrate',
            'python -m manage init_admin_user'
        ]
        run_terminal_command(
            command=f'heroku run --app={deploying_info["HEROKU_APP_NAME"]} "{"; ".join(remote_commands)}"',
            command_name='set_heroku_file'
        )

    @classmethod
    def init_deploying(cls, deploying_info: dict) -> None:
        cls.set_heroku_file()

    @classmethod
    def deploy(cls, deploying_info: dict) -> None:
        cls.push_to_git_heroku(
            deploying_info=deploying_info
        )

    @classmethod
    def finalize_deploying(cls, deploying_info: dict) -> None:
        cls.run_remote_commands(
            deploying_info=deploying_info
        )

    @staticmethod
    def init_message(deploying_info: dict) -> str:
        return f'Deploy {deploying_info["HEROKU_APP_NAME"]} on heroku !'

    @staticmethod
    def success_message() -> str:
        return 'All Done !'
