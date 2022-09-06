#Starting a Virtual Enviroment

If not installed:
``pip install virtualenv``

Once Installed:
``python3 -m venv project-name-env``

My personal practice is to keep the env in the project root folder and prepend the project-name before env.

To activate the virtual env:
``source project-name-env/bin/activate``

To stop the virtual env:
``deactivate``


#Creating a Git Repo
``git init template-project``

template-project above is the name of the git project


#Using Poetry

## Installing Poetry
Poetry should be installed globally on the system. This is because poetry creates its own virtual environment for package dependencies.
All other package installs should be done through the poetry commands.
``pip install poetry``

If you need to update Poetry:
``poetry self update``

##Creating an intitial project directory using Poetry
``poetry new poetry-template``

##Note: Poetry uses its own virtual env.
