TOX=tox

.PHONY: lint
lint:
	$(TOX) -c tox.ini -e lint

.PHONY: coverage
coverage:
	$(TOX) -c tox.ini -e coverage

.PHONY: fmt
fmt:
	black .

.PHONY: fmt-travis
fmt-travis:
	black . --check

.PHONY: test
test:
	$(TOX) -c tox.ini -e test

.PHONY: upload-release
upload-release:
	python setup.py register sdist upload
