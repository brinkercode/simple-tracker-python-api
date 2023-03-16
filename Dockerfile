FROM python:3.11.2-alpine3.16
WORKDIR /app
COPY __init__.py /app/
COPY ./python-env/main.py /app/
COPY ./python-env/models /app/models/
COPY ./python-env/dummy-data.json /app/
COPY ./python-env/requirements.txt /app/
RUN pip install wheel setuptools
RUN pip install --no-cache-dir --upgrade -r requirements.txt
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]