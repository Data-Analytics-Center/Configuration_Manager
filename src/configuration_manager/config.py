"""Configuration class and Singleton Abstract class that comprise the Configuration Manager."""

import abc
import os

from dotenv import load_dotenv


class Singleton(abc.ABCMeta, type):
    """Singleton metaclass for ensuring only one instance of a class."""

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """Call method for the singleton metaclass."""
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class Config(metaclass=Singleton):
    """Configuration class to store the state of enviroment variables for different scripts access."""

    def __init__(self, environment_keys: list[str]):
        """Create a new Config instance and sets the environment variables as attributes dynamically.

        Arguments:
            environment_keys (list[str]): The environment variables keys used to read environment variables from the environment into the configuration class.
        """
        load_dotenv()

        self._set_dynamic_attributes(environment_keys=environment_keys)

    def _set_dynamic_attributes(self, environment_keys: list[str]):
        """Dynamically set the environment variables as attributes of the Config class.

        Arguments:
            environment_keys (list[str]): The environment variables keys used to read environment variables from the environment into the configuration class.
        """
        for environment_key in environment_keys:
            value = os.getenv(environment_key)

            if not environment_key.isupper():
                raise ValueError(
                    f"Environment key '{environment_key}' must be in uppercase."
                )

            if not value:
                raise ValueError(f"Environment variable '{environment_key}' not found.")

            attribute_name = environment_key.upper()
            setattr(self, attribute_name, value)

    def __repr__(self):
        """Representation of the Config class."""
        attrs = "\n".join(
            f"{attr}='{getattr(self, attr)}'"
            for attr in dir(self)
            if not attr.startswith("_") and not callable(getattr(self, attr))
        )

        return f"Config:\n{attrs}"
