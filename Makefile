# File:    Makefile
# Author:  Nicholas Russo
# Purpose: Phony targets used for Python linting Python and running
#          the unit tests and samples runs for testing. This file is
#          NOT part of the Python Fundamentals training course.
.PHONY: all
all:	lint unit run

.PHONY: setup
setup:
	@echo "Starting  setup"
	python3 -m pip install -r requirements.txt
	rm -rf outputs
	mkdir outputs
	@echo "Completed setup"

.PHONY: lint
lint:
	@echo "Starting  lint"
	python3 -m json.tool < inputs/rectangle.json >> /dev/null
	yamllint -s inputs/circle.yml
	find . -name "*.py" -not -path "./small/*" | xargs pylint
	find . -name "*.py" -not -path "./small/*" | xargs black -l 80 --check
	@echo "Completed lint"

.PHONY: unit
unit:
	@echo "Starting  unit tests"
	python3 shape_unittest.py
	pytest shape_pytest.py
	@echo "Completed unit tests"

.PHONY: run
run:
	@echo "Starting  runs"
	python3 fundamental.py in
	python3 fundamental.py cm
	python3 complete.py IN
	python3 complete.py CM
	@echo "Completed runs"
