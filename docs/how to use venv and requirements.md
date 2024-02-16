# A Friendly Guide to Python Virtual Environments and Requirements Files

## Step 1: Setting Up Your Project

First, open your terminal. Navigate to the directory where you want to create your new Python project. You can do this with the `cd` command. For example:

```bash
cd /path/to/your/project
```

## Step 2: Creating a Virtual Environment

A virtual environment is like an isolated container where you can keep all the dependencies for your specific project. This way, different projects won’t interfere with each other. To create a virtual environment named `env`, use the following command:

```bash
python3 -m venv env
```

## Step 3: Activating the Virtual Environment

`Before` you start installing packages, you need to activate the virtual environment. The command to do this will depend on your operating system:

- On windows:

```bash
.\env\Scripts\activate
```

- On Unix or MacOS:

```bash
source env/bin/activate
```

You’ll know it worked if you see `(env)` at the beginning of your command prompt.

## Step 4: Using a requirements.txt File

The `requirements.txt` file is a list of all Python packages that your project depends on. You can create one manually, but it’s easier to let `pip` do it for you. Just install your packages as you normally would, and then run:

```bash
pip freeze > requirements.txt

```

This will create a `requirements.txt` file with all the currently installed packages and their versions.

## Step 5: Installing Packages from requirements.txt

If you have a `requirements.txt` file, you can install all the packages listed in it with one command:

```bash
pip install -r requirements.txt
```

And that’s it! You now have a separate environment for your Python project with all the necessary packages installed.

Remember, when you’re done working on your project, you can deactivate the virtual environment by simply typing `deactivate` in the terminal.
