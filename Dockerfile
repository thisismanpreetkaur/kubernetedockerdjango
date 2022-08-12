FROM python:3.9

COPY /mysite/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /code
COPY . /code


EXPOSE 8000


CMD ["runserver", "0.0.0.0:8000"]