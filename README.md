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


# Adding a main.py
main.py is 


# Setting up Github 

## Connecting the repository to a new github repository via SSH
https://docs.github.com/en/authentication/connecting-to-github-with-ssh


