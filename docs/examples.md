
## Environment File

The package is powered by the `python-dotenv` package which elegantly loads environment variables from a `.env` file into your Python virtual environment.

So for every project using this inlcude a `.env` file in the root of your project.

Environment variables must be in the format `KEY=VALUE` where key is a uppercase string with words separated by underscores as per the Pep 8 style guide.

Here is an example of what a `.env` looks like:

```
SERVER="TEST_SERVER"
DATABASE="TEST_DB"
DRIVER="TEST_DRIVER"
EMAIL_HOST="TEST_EMAIL_HOST"
```

## Usage

Assuming we have a `.env` file that looks like the on declared above, we can use the package like so:

```{.python .annotate}
from configuration_manager import Config

environment_keys = [  #(1)
    "SERVER",
    "DATABASE",
    "DRIVER",
    "EMAIL_HOST"
]

config = Config(environment_keys) #(2)

# Now we can access the environment variables like so:

print(config.SERVER) # "TEST_SERVER"
print(config.DATABASE) # "TEST_DB"
print(config.DRIVER) # "TEST_DRIVER"
print(config.EMAIL_HOST) # "TEST_EMAIL_HOST"
```
{ .annotate }

1.  The environments keys are used to dereference what is in your `.env` file. If is not included here 
    it will be on your config object.

2.  You only need to initialize the config object once per application lifecycle!

## Multiple Modules

Most likely you will have multiple modules in your application. In this case you can initialize the config object in your main module and then import it into your other modules.

Since the config object is a singleton, it will be the same object in all modules.

### main.py

```{.python .annotate}
from configuration_manager import Config

from other_module import print_env_vars


def main():
    environment_keys = ["SERVER", "DATABASE", "DRIVER", "EMAIL_HOST"]  # (1)

    config = Config(environment_keys)  # (2)

    # Now we can access the environment variables like so:

    print(config.SERVER)  # "TEST_SERVER"
    print(config.DATABASE)  # "TEST_DB"
    print(config.DRIVER)  # "TEST_DRIVER"
    print(config.EMAIL_HOST)  # "TEST_EMAIL_HOST"

    print_env_vars()


if __name__ == "__main__":
    main()
```

### other_module.py

```{.python .annotate}
from configuration_manager import Config


def test2():
    config = Config()  # (2)
    print(config.SERVER)  # "TEST_SERVER"
    print(config.DATABASE)  # "TEST_DB"
    print(config.DRIVER)  # "TEST_DRIVER"
    print(config.EMAIL_HOST)  # "TEST_EMAIL_HOST"
```