
# Publishing the pydvkbiology package
#   http://peterdowns.com/posts/first-time-with-pypi.html
#
# Note: Advance 'version' in setup.py before doing 'upload_PyPI'
upload_PyPI:
	python setup.py register -r pypi
	python setup.py sdist upload -r pypi

install_pydvkbiology:
	pip install --ignore-installed --upgrade pydvkbiology

upload_PyPI_test:
	python setup.py register -r pypitest
	python setup.py sdist upload -r pypitest

pylint_all:
	find src -name \*.py | grep -v __init__ | xargs pylint --reports=n

clean_pyc:
	find . -name \*.pyc | xargs rm -f

