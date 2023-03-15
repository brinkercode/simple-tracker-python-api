FROM python:3.11.2-alpine3.16
WORKDIR /app
COPY main.py /app/
COPY ./models /app
COPY ./dummy-data.json /app
COPY requirements.txt /app/
RUN pip install wheel setuptools pip --upgrade
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["uvicorn", "main:app","--port", "8000", "--host", ""]