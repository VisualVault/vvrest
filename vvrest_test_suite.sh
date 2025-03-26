echo 'starting vvrest test suite'
coverage run --source vvrest -m unittest tests/vvrest_test_suite.py
coverage report
echo 'vvrest test suite complete'
