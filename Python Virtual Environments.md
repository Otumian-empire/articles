## Python Virtual Environments

> Hi, before we dive in, let **VE** stand for **Virtual Environment**, wherever you see or hear **VE** (here, I mean).

## Back story

In one internship, I joined a team to build an e-commerce system, using python. On my PC I was running `python3.6` but the project uses `python3.8`. Does it matter? Sometimes.

In my case, what do you think I should do so that I would work on and test the project locally, using the same version of python as the project?

I could install `python3.8` and have two versions of python running on my system. I have to call `python3.6` and `python3.8` to make use of them. (I already have `python2.7`, I do not need another). A weirder solution would be to use a Virtual Machine. Install Ubuntu (or any OS) in a Virtual Machine that uses the latest version of python at the time. Someone said I should have used a docker.

There is a simple and stress-free solution that encompasses the same idea as a virtual machine called a Virtual Environment. We shall be talking about Virtual environments.

## What is a Virtual Environment and Why Use It?

With a **VE**, we will have a specific version of python. This environment will have separate dependencies for our project. These dependencies will affect only our project. These dependencies would have absolutely nothing to do with the dependencies on the computer we are using. So an upgrade or downgrade on our machine would not affect our project dependencies. The same applies to making changes in the **VE**, such as deleting a dependency, which would not affect the dependencies on the local machine. [python-environment-101] also introduces python **VE**.

We would discuss the python **VE**s, [virtualenv] and [pipenv], knowing what a **VE** is and why to use one.

## Check Python Version

To be on the safer side check the python version you are using, `python --version` or `python3 --version`.

You should get an output similar to `Python x.y.z`. Where _x_ has to be _3_, with _y_, _6_ or above.

## Install pip3

In the case you do not have `pip3`, then install `pip3` with the command below:

```bash
sudo apt-get install python3-pip

```

We would use `pip` to install packages. If you are new to `pip`, [pip-fcc] and [pip-w3schools] have easy to follow tutorial on [pip].

## Create project directory

On the terminal, navigate to your project folder or create one with:

```bash
mkdir PATH_TO_PROJECT_FOLDER && cd PATH_TO_PROJECT_FOLDER

```

If you are good with the GUI, go with it. We want to create a folder for our project, that is it.

## Virtualenv

Before we start using `virtualenv` we need [pip]. If you have multiple python versions like the _python2_ and _python3_, install `pip3` rather or check if you have `pip3`.

> (What about those who are using `python2.7`? Sorry, but try to adjust and use [pip] in place of `pip3` until you install the **VE** and activate it. I can not promise you that it will work or not. So you have to give it a go.)

### Install virtualenv

Then install virtualenv:

```bash
pip3 install virtualenv

```

### Initialize the virtualenv

Initialize the virtualenv:

```bash
virtualenv VIRTUAL_ENV_NAME

```

For the sake of demonstration, let's assume we're creating an API for jokes, then we'd do:

```bash
mkdir jokeapp && cd jokeapp

```

We'd then initialize the virtual environment with,

```bash
virtualenv joke_env

```

This will create a folder called `joke_env` in the project directory. You can choose to hide the folder by prefixing the **VE** name with a dot, `.`. I prefer to make it visible.

### Activate The **VE**

We have to activate the **VE** else installed packages will be installed in the global space or scope (on the local machine).

```bash
source VIRTUAL_ENV_NAME/bin/activate

```

This will activate the **VE** but in our case, we'd do:

```bash
source joke_env/bin/activate

```

The name of the **VE** gets added to the username before the computer name, like this below:

```bash
(joke_env) username@computername:PATH_TO/jokeapp$

```

Sometimes things can be scary like you turn on the light bulb and you'd forget where the switch is or how to switch it off. Entering into vim is scarier when you can not exit. Press: `[esc] [:] [q] [!] [enter]` to exit vim.

### Deactivate the **VE**

In the activated **VE**, we can deactivate the **VE** with, `deactivate`.

Either our terminal will return to `username@computername:PATH_TO/jokeapp$` or we'd get an error output, saying, `deactivate: command not found`. In the latter case, you didn't _activate_ the **VE** in the first place.

Now we know how to get in and get out of the **VE** smoothly. We can install and uninstall all the packages we want.

Can we use other versions of python if we want (I don't mean `python2.7`) and not just create a **VE** for our project?

Yeah, we can. It is just that we have to install it locally first, to use it (the python version we want must exist before we can use it or create a **VE** for it). It must
exist in /usr/bin/PYTHON_VERSION

We would have to do:

```bash
virtualenv -p python3 venv

```

or

```bash
virtualenv -p /usr/bin/python3.8 venv

```

### Install/Uninstalling packages

We can install and uninstall packages just like we do with [pip].

## pipenv

### install pipenv

Install `pipenv` like you'd install any package, with the command:

```bash
pip3 install pipenv
```

If you look at the logs/output as the installation goes on you see that
virtualenv pops up here and there. So we can say or assume that `pipenv` was built on top of `virtualenv`.

### Activate the Pipenv Shell

Pipenv has a shell that allows you to create a **VE** with the command:

```bash
pipenv shell

```

This will use the project/root directory name as the **VE** name, using the highest version of python you have. It creates a **VE** when there is no **VE** for our project directory.

### Create **VE** For a Specific Version

You can create the **VE** with the command, `pipenv --python VERSION`. Here, _VERSION_ is the version of python you wish to use for your project.

We could have done, `pipenv --three` or `pipenv --two` to create a `python3` or `python2` **VE** respectively.

> Note the python version you want to use must exist locally else you have to install it.
> The [pipenv] docs tell you not to do `pipenv --three --two`, for "things can happen".

### Where Can I Find The **VE**

The **VE** will be installed at, `~/.local/share/virtualenvs/PROJECT_NAME`

Use `pipenv --venv` to output the path to where the packages will be or are installed on your pc for this very **VE**.

We can use `pipenv --where`, to tell us where our project root directory is. Something the `pwd` command.

### Remove/Delete **VE**

We can remove the **VE**, as in, delete it with `pipenv --rm`. This will delete the content and root directory of our **VE** located at the path provided by, `pipenv --venv`.

### Exist **VE**

Use `exit` to exit the **VE** and activate it with `pipenv shell` (we know this already).

### Pipfile

Pipfile is created when a **VE** is created and it holds the names of the packages we'd use in our projects. `cat Pipfile` will display something like this below, on the terminal.

```
[[source]]
url = "https://pypi.org/simple"
verify_ssl = true
name = "pypi"

[packages]

[dev-packages]

[requires]
python_version = "3.6"
```

So what does this even mean?

- I have no packages installed
- I am using is `python3.6`.
- _dev-packages_ refers to packages that your projects need only during development. An example is an `env` package that reads the content of `.env` files. This is will not be needed, say we publish our project on Heroku (a web project).

### Install a Package

Let's install fastAPI, you can install any package you want.

```bash
pipenv install fastapi

```

We could also do, `pip install fastapi` (in the activated environment). A `Pipfile.lock` file will be created and this is the file that has the hashes for the packages installed.

To install a package with pipenv, do, `pipenv install package_name`

### Uninstall a Package

To uninstall a package, use `pipenv uninstall package`. This works like `pip uninstall package`.

### Run a Python Script

To run a python script do, `pipenv run python script.py`. We could do, `python script.py` (in the activated environment).

### Required Packages, Dev Packages and The requirement.txt File

`pip freeze > requirements.txt` or `pipenv run pip freeze > requirements.txt` will write the output of `pip freeze` into a `.txt` file called, `requirement.txt`. The project dependencies are printed on the terminal when we enter the command, `pip freeze`. In this case, we write the output into a file. This is a basic practice, like package.json for Nodejs.

We can install required packages from the `requirement.txt` file with, `pipenv install -r requirement.txt`.

We can also use the `Pipfile.lock` to write our package dependencies into the `requirement.txt` file using any of the commands below:

- `pipenv lock --requirements > requirements.txt`
- `pipenv lock -r > requirements.txt`

### PYENV

Now there was something I did not mention, which was supposed to be one of the purposes of using a **VE**.

Assuming we just have say python 3.6, running `pipenv shell` for the first time will choose the current `python3` that we have. By the assumption made, we'd have a **VE** for `python3.6`.We have a **VE** for separate dependencies, **what if we want a higher version or a version that we
do not have (on our PC)?**

Yeah. We can a version higher or lower than the current version we have and we can install that with [pyenv]. [pyenv] will allow us to install the various version of python we want. Remember that we want to just use this new version in the **VE** so we must install this new version **in** the **VE** else it will install as part of our PC.

### Install PYENV

Follow the guide from [pyenv-github] page to install [pyenv] on your OS. On Ubuntu (I am on ubuntu 16, which explains why my version of python was `3,6`. If you want to call me out on this because maybe, I have said or you have read that I was on PopOS/ubuntu 20.04, yeah, it is true but things happened and I am on 18 now).

With the instruction provided by the [pyenv-github] page, installation should be quite simple.

### Install Python3.9 With PYENV

We know that `pipenv --python VERSION` will install a python version that already exists on our PC, if it does else spit out some error message. After the [pyenv] installation, if their version doesn't exist, `pipenv` will use `pyenv` to install that version. `pipenv --python 3.9`.

And We Are Done Here... No, I am joking... We are not done.

Say you had, `python_version = "3.6"` in the `Pipfile`, you have to change the version to that which you just installed.

### How I Did Mine When It Was Becoming Weird. How Weird?

This is what I did and how I should have rather done it (At this point I already have the project started and there are packages I am working with. How weird? ).

- Get the packages/dependencies into the `requirements.txt` file, `pip freeze > requirements.txt`
- Remove the `3.6` **VE** with, `pipenv --rm` rather than change the version number, from `python_version = "3.6"` to `python_version = "3.9"`
- Exit out of the activate **VE** with, `exit`
- Remove the Pipfiles, `rm Pipfile*`
- Then start a new environment, `pipenv --python 3.9`
- Assuming the latest (on your PC - you used `pyenv` to install) is `3.9` and you want the `3.9`, then you can run, `pipenv shell`.
- Activate the environment with, `pipenv shell` (I didn't have `3.9` on my PC, as the previous step describes)
- Install the packages from the `requirements.txt` file, `pipenv install -r requirement.txt`

### Somethings We Will Know Only When We Have Used a **VE**

- `Virtualenv`, the folder for the packages used will be available in the main directory and you have to git ignore it. For `Pipenv`, the folder at `pipenv --venv`. You have to either delete the packages folder when the project leaves your custody (you don't work on the project anymore). Out of sight out of mind, remember? This means we will have our memory chip away bit by bit as we use `pipenv` when we do not remove the unwanted **VE** (just the `node_modules`) and we'd not know it because we don't see it.

- `Pipenv` creates `Pipfile` and `Pipfile.lock`. This is similar to `package.json` and `package-lock.json`.

- The only drawback I faced was when I wanted to install only `dev-packages`.

  - `pipenv lock -r > requirement.txt`, for requirement packages
  - `pipenv lock -d > dev-requirements.txt`, for both requirement and dev packages
  - `pipenv lock --dev-only > only-dev-requirements.txt`, for only dev packages

- We could exit the `pipenv` **VE** with `deactivate`. We used `exit`before.

- So practically `Pipenv` is suited for your projects. `Virtualenv` is sugar-coated to give us `Pipenv`. I am just saying from a practical point of view.

### The END

Let me know if you run into a weird situation and how you solved it.

#

[pipenv]: https://docs.pipenv.org/
[virtualenv]: https://virtualenv.pypa.io/en/latest/index.html
[pyenv-github]: https://github.com/pyenv/pyenv
[pyenv]: https://pypi.org/project/pipenv/
[python-environment-101]: https://towardsdatascience.com/python-environment-101-1d68bda3094d
[pip-w3schools]: https://www.w3schools.com/python/python_pip.asp
[pip-fcc]: https://www.freecodecamp.org/news/how-to-use-pip-install-in-python/
[pip]: packaging.python.org/tutorials/installing-packages/
