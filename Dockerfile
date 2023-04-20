FROM python:3.10.9

ADD main.py .

RUN pip install scikit-learn

CMD ["python", "./main.py"]