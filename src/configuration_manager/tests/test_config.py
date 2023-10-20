"""Configuration Manager Tests.

NOTE: These tests must be ran individually. If ran in a batch, the tests will fail due to the singleton behavior of the Config class.
"""

import os

import pytest

from configuration_manager import Config


def clear_all_environment_variables():
    """Clear all environment variables."""
    for key in list(
        os.environ.keys()
    ):  # Iterating over a copy of the keys since the dictionary will change size during iteration
        del os.environ[key]


def test_config():
    """Basic success test for config."""
    clear_all_environment_variables()
    os.environ["TEST"] = "test"
    os.environ["SERVER"] = "server"

    environment_keys = ["TEST", "SERVER"]

    config = Config(environment_keys=environment_keys)

    assert config.TEST == "test"
    assert config.SERVER == "server"


def test_singleton_behavior():
    """Ensure that the Config class always returns the same instance."""
    clear_all_environment_variables()
    os.environ["TEST"] = "test"

    config1 = Config(environment_keys=["TEST"])
    config2 = Config(environment_keys=["TEST"])

    assert config1 is config2


def test_environment_variable_validation():
    """Test the validation of environment variables that are included as the keys but are not in the environment."""
    clear_all_environment_variables()
    os.environ["TEST"] = "test"

    environment_keys = ["TEST", "SERVER"]

    with pytest.raises(ValueError, match=r"Environment variable 'SERVER' not found."):
        Config(environment_keys=environment_keys)


def test_environment_key_uppercase_validation():
    """Test the validation that ensures all environment keys are uppercase."""
    clear_all_environment_variables()
    os.environ["Test"] = "test"  # noqa: SIM112

    with pytest.raises(
        ValueError, match=r"Environment key 'Test' must be in uppercase."
    ):
        Config(environment_keys=["Test"])


def test_absence_of_extraneous_attributes():
    """Test that only specified environment keys are set as attributes."""
    clear_all_environment_variables()
    os.environ["TEST"] = "test"
    os.environ["EXTRA"] = "extra"

    config = Config(environment_keys=["TEST"])

    assert hasattr(config, "TEST")
    assert not hasattr(config, "EXTRA")


def test_repr_method():
    """Test the representation method of the Config class."""
    clear_all_environment_variables()
    os.environ["TEST"] = "test"

    config = Config(environment_keys=["TEST"])
    expected_repr = "Config:\nTEST='test'"

    assert str(config) == expected_repr
