# if PYTHON env var not defined, use "python"
PYTHON ?= python
VE_DIR=.venv
PY_VENV_PACKAGE = `$(PYTHON) --version | cut -d . -f 1,2 | tr -d ' ' | tr '[:upper:]' '[:lower:]'`-venv
V_PYTHON=$(VE_DIR)/bin/python
# SHELL:=/bin/bash
# .ONESHELL:
# .PHONY: initdev

initdev:
	apt install $(PY_VENV_PACKAGE) -y
	apt install python-pytest -y
	$(PYTHON) -m venv $(VE_DIR)
	$(V_PYTHON) -m pip install flake8 pylint
	@printf "\nDev environment is ready.\n"
	@printf "Run \"source $(VE_DIR)/bin/activate\" to activate virt env\n"

check:
	@printf $(PY_VENV_PACKAGE)

clean:
	rm -rf .venv