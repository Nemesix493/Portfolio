import abc


class AbstractDeployer(abc.ABC):
    @abc.abstractclassmethod
    def get_deploying_info(cls) -> dict:
        return {}

    @abc.abstractclassmethod
    def init_deploying(cls, deploying_info: dict) -> None:
        pass

    @abc.abstractclassmethod
    def deploy(cls, deploying_info: dict) -> None:
        pass

    @abc.abstractclassmethod
    def finalize_deploying(cls, deploying_info: dict) -> None:
        pass

    @abc.abstractstaticmethod
    def init_message(deploying_info: dict) -> str:
        pass

    @abc.abstractstaticmethod
    def success_message() -> str:
        pass

    def run_deployement(cls) -> None:
        deploying_info = cls.get_deploying_info()
        print(cls.init_message())
        cls.init_deploying(
            deploying_info=deploying_info
        )
        cls.deploy(
            deploying_info=deploying_info
        )
        cls.finalize_deploying(
            deploying_info=deploying_info
        )
        print(cls.success_message())
