#!/bin/bash

#activate project virtual env
source venv39/bin/activate
#everything lives in the virutal environment (same environment everytime)

#execute test suite
#...test_app.py
pytest
#code 0 
#code 1