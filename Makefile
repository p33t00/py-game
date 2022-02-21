# if PYTHON env var not defined, use "python"
PYTHON ?= python
VE_DIR=.venv
PY_VENV_PACKAGE = `$(PYTHON) --version | cut -d . -f 1,2 | tr -d ' ' | tr '[:upper:]' '[:lower:]'`-venv
V_PYTHON=$(VE_DIR)/bin/python

installvenv:
	apt install $(PY_VENV_PACKAGE) -y

initdev:
	$(PYTHON) -m venv $(VE_DIR)
	$(V_PYTHON) -m pip install -U pytest flake8 pylint black coverage
	@printf "\nDev environment is ready to use.\n"
	@printf "Run \"source $(VE_DIR)/bin/activate\" to activate virt env\n"

check:
	@printf $(PY_VENV_PACKAGE)

clearall:
	rm -rf .venv __pycache__ .pytest_cache tests/pytests/__pycache__ tests/pytests/.pytest_cache

clearcache:
	rm -rf __pycache__ .pytest_cache tests/pytests/__pycache__ tests/pytests/.pytest_cache