FROM python:3.11
EXPOSE 8081

WORKDIR /app
COPY . /app
RUN python3 -m pip install -r requirements.txt

# CMD ["sleep", "1000"]
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8081"]