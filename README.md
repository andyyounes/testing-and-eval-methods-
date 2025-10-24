# MTT419a - Math Operations & Pytest

This repository contains simple math operation functions and tests with timing benchmarks using pytest.

## Files

- `operations.py`: Contains sum, mul, and sub functions.
- `test_math.py`: Contains pytest unit tests and timing tests.
- `pytest.ini`: Pytest configuration marking timing tests.

## checks
```bash
# install pytest
pip install pytest
# create a virtual environment
python -m venv venv
# activate
venv\Scripts\activate.bat

```

## How to Run

- Run tests with: `pytest -v -s`
- Run main program with: `python operations.py` or `python test_math.py`
- Run pytest with verbose output and print statements (-s disables output capture):
```bash
pytest -v -s
```
- Run your main program scripts:
```bash
python operations.py
# OR
python test_math.py
```
Deactivate the virtual environment when done
```bash
deactivate
```
output should be in python to run the test environment:
```bash
python -m pytest --durations=0 -v -s
````
### outputs
In python
```bash
====================================== test session starts ======================================
platform win32 -- Python 3.12.10, pytest-8.4.2, pluggy-1.6.0 -- C:\Users\5306-2\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\5306-2\Desktop\MTT419a
configfile: pytest.ini
plugins: durations-1.6.1
collected 4 items

test_math.py::test_mul PASSED
test_math.py::test_sub PASSED
test_math.py::test_execution_time Execution Time for sum: 0.0 seconds
Execution Time for mul: 0.0 seconds
Execution Time for sub: 0.0 seconds
PASSED

===================================== fixture duration top ====================================== 
total          name        num med     min
       0:00:00 grand total   0 0:00:00 0:00:00
==================================== test call duration top ===================================== 
total          name        num med     min
==================================== test setup duration top ==================================== 
total          name        num med     min
       0:00:00 grand total   4 0:00:00 0:00:00
================================== test teardown duration top =================================== 
total          name        num med     min
       0:00:00 grand total   4 0:00:00 0:00:00
======================================= slowest durations ======================================= 

(12 durations < 0.005s hidden.  Use -vv to show these durations.)
======================================= 4 passed in 0.06s ======================================= 
```


In venv
```bash
=============================================== test session starts ================================================
platform win32 -- Python 3.12.10, pytest-8.4.2, pluggy-1.6.0 -- C:\Users\5306-2\Desktop\MTT419a\venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\5306-2\Desktop\MTT419a
configfile: pytest.ini
collected 4 items

test_math.py::test_sum PASSED
test_math.py::test_mul PASSED
test_math.py::test_sub PASSED
test_math.py::test_execution_time Execution Time for sum: 0.0 seconds
Execution Time for mul: 0.0 seconds
Execution Time for sub: 0.0 seconds
PASSED

================================================ 4 passed in 0.04s =================================================
```
