VENV = .venv
VENV_PYTHON = $(VENV)/Scripts/python.exe
VENV_PIP = $(VENV)/Scripts/pip.exe

.PHONY: setup run test

$(VENV_PYTHON):
	python -m venv $(VENV)

setup: $(VENV_PYTHON)
	$(VENV_PIP) install -r requirements.txt

run:
	$(VENV_PYTHON) src/api.py

test:
	$(VENV_PYTHON) run_api/run.py
