[![Python package](https://github.com/kylebascomb/Bascomb-Project-Templates/actions/workflows/pytests.yml/badge.svg)](https://github.com/kylebascomb/Bascomb-Project-Templates/actions/workflows/pytests.yml)

# Project Overview
This repo is a simple collection of commands and templates for creating projects. Currently, it includes a template for:
* Poetry package manage for python
* Pytest for testing python projects
* Github Actions for CI

# Starting a Standalone Virtual Enviroment

If not installed:
``pip install virtualenv``

Once Installed:
``python3 -m venv project-name-env``

My personal practice is to keep the env in the project root folder and prepend the project-name before env.

To activate the virtual env:
``source project-name-env/bin/activate``

To stop the virtual env:
``deactivate``


# Creating a Git Repo
``git init template-project``

This create a folder named template-project. If you already have a folder (from Poetry for example), you can omit the template-project arg.

template-project above is the name of the git project


# Using Poetry

## Installing Poetry
Poetry should be installed globally on the system. This is because poetry creates its own virtual environment for package dependencies.
All other package installs should be done through the poetry commands.
``pip install poetry``

If you need to update Poetry:
``poetry self update``

## Creating an intitial project directory using Poetry
``poetry new poetry-template``

## Poetry uses its own virtual env. 
To enable a shell with this virtual enviroment, run the following command in the directory with the pyproject.toml file
``poetry shell`

Once you are in the shell, you can run any of your project files inside the virtual environment. If you are not in the shell, you can instead run
the following command to run something as a one-off:
``poetry run command``

for example, if you want to run main.py:
``poetry run python main.py``

## Adding dependencies to a Poetry Project
To add a dependency to your project, type the following command into your Poetry Shell. This example will install the requests library.
``poetry add requests``

This command adds a line to your **pyproject.toml** file. It adds a line after the [tool.poetry.dependencies] section. For example, the line added for
installing requests is:
``requests = "^2.28.1"``

## Adding Dev / Test dependencies to a Poetry Project
When setting up a development environment, its best to separate your dependencies into the normal build dependencies that are required for running the program, and a separate group for all dependencies needed for your development environment.

This can be done by adding a --group tag and then following it with a group name. This following example shows adding pytest in a group called dev

``poetry add pytest --group dev``


# Adding a main.py
main.py is

# Using Pytest
Pytest is the go to testing library for python.

## Installing Pytest
You can add pytest to your project as detailed in the "Adding Dev / Test dependencies to a Poetry Project" section above:
``poetry add pytest --group dev``

## Writing Tests:

### Using @pytest.mark.parametrize
The @pytest.mark.parametrize is used to parametrize several inputs to a single function. An example is shown below:

``
@pytest.mark.parametrize(
    "test_input, expected",
    [(10, True), (11, False), (0, True), (-1, False), (-2, True)],
)
def test_even_odd(test_input, expected):
    number = EvenOddNumber(test_input)
    assert number.num_is_even() == expected
``

### Using @pytest.mark.skip
Marking a function as skip simply means that the test will be skipped when running the pytest command.

### Using @pytest.mark.xfail
Marking a function as xfail means that is is expected to fail.

### Using Pytest with exceptions
`` with pytest.raises(ValueError): ``

### Using fixtures
Fixtures are a way to duplicate code across tests
TODO

### Coverage Tests

## Using Pytest
While in the Poetry Environment, you can run all your pytests using the ``pytest`` command in the terminal. This will run all functions in the directory that are prepended with 'test_' and located in a file that is prepended with 'test_'

### Using pytest-cov for Coverage tests
We can install a package called pytest-cov to monitor the coverage of the pytests over the source code. First we have to install pytest-cov

poetry add pytest-cov --group dev


To run pytest-cov, you run your pytest script with the --cov="source code folder" and "/tests" to specify your test directory. See example below:

```pytest --cov=poetry_template tests/```





# Setting up Github 

## Connecting the repository to a new github repository via SSH
https://docs.github.com/en/authentication/connecting-to-github-with-ssh


