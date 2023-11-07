import os

from . import deployers
from .deployers.deployer import AbstractDeployer

providers_deployers = {
        'heroku': deployers.HerokuDeployer
}


def get_deployer() -> AbstractDeployer:
    provider = os.getenv(
        'PROVIDER',
        None
    )
    if not provider:
        raise ValueError('Environement variable "PROVIDER" does not exist or is empty !')
    deployer = providers_deployers.get(provider, None)
    if not deployer:
        raise ValueError(f'There is no Deployer for this Provider (\'{provider}\')')
    return deployer
