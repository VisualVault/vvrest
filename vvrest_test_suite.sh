#!/bin/bash
echo 'starting vvrest test suite'
coverage run --source vvrest -m unittest tests/vvrest_test_suite.py
coverage report -m
echo 'vvrest test suite complete'
