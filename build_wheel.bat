@echo off
python setup.py clean
python setup.py build
python setup.py bdist_wheel
rem python -m pyc_wheel ./dist/*.whl
pause