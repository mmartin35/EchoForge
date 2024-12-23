FROM python:3.9-slim
WORKDIR /code
COPY ./requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt
COPY ./ /code/
ENV PYTHONUNBUFFERED 1
EXPOSE 8082
CMD ["python", "manage.py", "runserver", "0.0.0.0:8082"]
