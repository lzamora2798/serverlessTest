# serverlessTest

**Serverless Test** is a set of function that works with the framework serverless, each of them uses different programming algorithm

# Run project

1. Install Serveless by `npm install -g serverless`
2. Run `npm install`
3. Create a virtual env with python 
4. `virtualenv venv`
5. Activate the venv with `source venv/bin/activate`
6. Install all requirements by `pip3 install -r requirements.txt`
7. Execute the project in localhost with `sls offline`

# Run All test

2. execute `python -m unittest discover src/tests`

# Run Unitary test

on the `src` folder execute depending on the function

1. `python -m unittest src/tests/test_ExcerciseOne.py`
2. `python -m unittest src/tests/test_ExcerciseTwor.py`
3. `python -m unittest src/tests/test_handlerFilter.py`
4. `python -m unittest src/tests/test_handlerMail.py`