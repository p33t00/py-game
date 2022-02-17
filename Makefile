# if PYTHON env var not defined, use "python"
PYTHON ?= python
PY_VENV_PACKAGE = `$(PYTHON) --version | cut -d . -f 1,2 | tr -d ' ' | tr '[:upper:]' '[:lower:]'`-venv
BIN=.venv/bin/
# SHELL:=/bin/bash
# .ONESHELL:
# .PHONY: initdev

initdev:
	: # apt install $(PY_VENV_PACKAGE) -y
	: # $(PYTHON) -m venv .venv
	: # $(BIN)python -m pip install flake8 pylint
	@printf "\nDev environment is ready.\n"
	@printf "Run \"source $(BIN)activate\" to activate virt env\n"

check:
	@printf $(PY_VENV_PACKAGE)

test:
	source .venv/bin/activate


clean:
	rm -rf .venv