FROM python:3.7-alpine3.10
RUN mkdir /code
COPY requirements.txt /code/
RUN pip install -r /code/requirements.txt
COPY travis_test_script.py /code/
CMD ["python","/code/travis_test_script.py"]