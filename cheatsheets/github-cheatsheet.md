# Github Overview
Github is an essential resource to sharing your personal projects with other people.

# Setting up Github 

## Connecting the repository to a new github repository via SSH
You can connect your github to your local git via ssh to keep authentication simple. My suggestion is to follow the guidlines at the link below from the official github documentation:

https://docs.github.com/en/authentication/connecting-to-github-with-ssh

## Connecting a local repo to github
One way to connect a local repo to github

One method for linking a local repo to github is to start by creating a local repo on your machine.

You can create a repo using the following command:
`` git init -b main ``

You can then log into github and create a new repository. After this repository is created, you click the green "Code" button and copy the link found in the SSH tab. This link is your REMOTE_URL.

Once the repo is initialized, you issue the following command:
`` git remote add origin <REMOTE_URL>``

After the remote origin is added, you can push any commits to your GitHub repo via the following command:
`` git push origin <BRANCH> ``

More info can be found at the following article from the official github documentation:
https://docs.github.com/en/get-started/importing-your-projects-to-github/importing-source-code-to-github/adding-locally-hosted-code-to-github

### NOTE: -b main initializes the 'main' branch. By default, git will use the 'master' branch, but this naming convention has been pushed out due to the negative connotations associated with the origin of the term. 

# Creating Github Actions for CI/CD
Github actions is an invaluable tool for quick automatic CI / CD pipelines for your project.

An example for running pytest on every push and pull request can be found at 

``../.github/workflows.pytest.yaml``
