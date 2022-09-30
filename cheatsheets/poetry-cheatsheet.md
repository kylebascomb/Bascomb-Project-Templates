# Poetry Overview

Poetry is a fantastic tool for both package management and virtual environment management in your python projects. 


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

This command adds a line to your **pyproject.toml** file. It adds a line after the [tool.poetry.dependencies] section. For example, the line added for installing requests is:
``requests = "^2.28.1"``

## Adding Dev / Test dependencies to a Poetry Project
When setting up a development environment, its best to separate your dependencies into the normal build dependencies that are required for running the program, and a separate group for all dependencies needed for your development environment.

This can be done by adding a --group tag and then following it with a group name. This following example shows adding pytest in a group called dev

``poetry add pytest --group dev``