FROM python:3.11.2-alpine3.16
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
COPY ./data.json /code/data.json
COPY ./app /code/app
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
