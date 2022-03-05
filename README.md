### Game Manual:
================
# Run App:
The only requirement for running the game is python.
Than in order to start the app, run:
```
python main.py
```

# Start:
Initial command is ```start```
It is used to initialize game values and setup Player and Bot

```r``` is used to restart game scores.

Player can refer to help manual in the game by typing 'help' command.


# Roll/Stop:
Player shall roll the dice by using ``` z``` command.
When Player decides to stop the turn and score points, ```x``` command is used.


# Player Statistics:
Players can view their statistics anytime, using the command
```stats```
It will display the statistics for the Player.


# Cheat:
Player can set a value by which his/her roll score will be multiplied.
```
cheat 10
```
This way every time Player rolls the dice, result will be multiplied by 10


# Change Name:
A Player can change their name, whenver they wish to, using ```c``` command, which will let the player to enter a new name.
Doing this, all the tracks of their old name will be replaced with the new name.


# Bot (Robot):
Intelligence of Bot is being selected on game initialization (start command)
Also it is possible to change Bot intelect level anytime by using command:
```
b
```
This will let Player change Bot intelligence level and will restart game.


# Exit:
In order to exit the game, ```exit``` command can be used.



### Unit Testing
================
Our project uses unittests and pytests to cover different functionality.
Each is executed and presents statitstics separately.
That means, when you run pytests, unittests are not executed and not included in the stats.

# Setup Testing env:
1. Run ```make venv PYTHON={your_python_command}``` to install python virtual environment and follow the 
    instructions on the screen.
2. Run ```make install``` to install dev environment
    Can Run ```make installed``` to view installed packages


# App testing
1. Run unit tests:
    - (pytest): Run ```pytest```
    - (unittests): Run ```unittest```


2. Coverage statistic:
    2.1. Run ```make coverage_pytest``` to view pytest results
    2.2. Run ```make coverage_unittest``` to view unittest reults
    2.3. Run ```make coverage``` to view both pytest and unittest results
    4.2. Run ```make report``` to view unit test statistics
    By now unit test statistics should be avilable in html format in
        htmlcov/index.html


# Checking code compliance
```make pylint``` in order to run pylint.
```make flake8``` to let flake8 check code compliance.
```make lint``` to run both above



# Generating Documentation
```make pdoc``` will generate code documentation in doc/ directory.
```make pyreverse``` will generate UML documentation of the code
```make doc``` will run both pdoc and pyreverse and generate the documents.





### Development Environment (detailed):
=======================================
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)


# Check version of Python

Check what version of Python you have. The Makefile uses `PYTHON=python` as default.

```
# Check Python installation
make version
```

If you have another naming of the Python executable then you can solve that using an environment variable. This is common on Mac and Linux.

```
# Set the environment variable to be your python executable
export PYTHON=python3
make version
```

Read more on [GNU make](https://www.gnu.org/software/make/manual/make.html).



# Python virtual environment

Install a Python virtual environment and activate it.

```
# Create the virtual environment
make venv

# Activate on Windows
. .venv/Scripts/activate

# Activate on Linx/Mac
. .venv/bin/activate
```

When you are done you can leave the venv using the command `deactivate`.

Read more on [Python venv](https://docs.python.org/3/library/venv.html).



### Install the dependencies

Install the PIP packages that are dependencies to the project and/or the development environment. The dependencies are documented in the `requirements.txt`.

Do not forget to check that you have an active venv.

```
# Do install them
make install

# Check what is installed
make installed
```

Read more on [Python PIP](https://pypi.org/project/pip/).



### Run the code

The example program can be started like this.

```
# Execute the main program
python main.py
```

All code is stored in directory `src/`.



### Run the validators

You can run the static code validators like this. They check the sourcecode and exclude the testcode.

```
# Run each at a time
make flake8
make pylint

# Run all on the same time
make lint
```

You might need to update the Makefile if you change the name of the source directory currently named `src/`.

Read more on:

* [flake8](https://flake8.pycqa.org/en/latest/)
* [pylint](https://pylint.org/)



### Run the unittests

You can run the unittests like this. The testfiles are stored in the `test/` directory.

```
# Run unttests without coverage
make unittest

# Run unittests with coverage
make coverage

# Run pytests without coverage
pytest

# Run pytests with coverage
make coverage

# Run the linters and the unittests with coverage
make test
```

You can open a web browser to inspect the code coverage as a generated HTML report.

```
firefox htmlcov/index.html
```

Read more on:

* [pytest](https://docs.pytest.org)
* [unittest](https://docs.python.org/3/library/unittest.html)
* [coverage](https://coverage.readthedocs.io/)



### Run parts of the testsuite

You can also run parts of the testsuite, for examples files or methods in files.

You can run all tests from a testfile.

```
# Run a testfile
python -m unittest test.test_game
pytest tests/pytests/Dice_test.py
```

You can also run a single testcase from a file.

```
# Run a test method, in a class, in a testfile
python -m unittest test.test_game.TestGameClass.test_init_default_object
pytest tests/pytests/Dice_test.py::TestDice::test_inc_turn_total_score
```



### Remove generated files

You can remove all generated files by this.

```
# Remove files generated for tests or caching
make clean

# Do also remove all you have installed
make clean-all
```



Optional targets
--------------------------

These targets might be helpful when running your project.



### Codestyle with black

You can unify the codestyle using black. Running black will change your source code to have a codestyle according to black codestyle.

```
# Same same, different names
make black
make codestyle
```

Read more on [black](https://pypi.org/project/black/).



More targets
--------------------------

The Makefile contains more targets, they are however not yet tested on this directory structure.
