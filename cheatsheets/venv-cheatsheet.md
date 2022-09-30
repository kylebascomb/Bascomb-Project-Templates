# Venv Overview
Venv is a simple but powerful tool to create virtual environments for you project if you do not want to utilize the poetry virtual environment features.

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