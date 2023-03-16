FROM python:3.11.2-alpine3.16
WORKDIR /app
COPY __init__.py /app/
COPY main.py /app/
COPY models /app/models/
COPY ./dummy-data.json /app/
COPY requirements.txt /app/
RUN pip install wheel setuptools
RUN pip install --no-cache-dir --upgrade -r requirements.txt
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]