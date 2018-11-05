TOX=tox

.PHONY: lint
lint:
	$(TOX) -c tox.ini -e lint

.PHONY: coverage
coverage:
	$(TOX) -c tox.ini -e coverage

.PHONY: fmt
fmt:
	yapf --style pep8 --recursive --in-place check.py setup.py src tests

.PHONY: fmt-travis
fmt-travis:
	yapf --style pep8 --recursive --diff check.py setup.py src tests

.PHONY: test
test:
	$(TOX) -c tox.ini -e test

.PHONY: upload-release
upload-release:
	python setup.py register sdist upload
