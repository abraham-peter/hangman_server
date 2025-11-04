FROM python:3.12

WORKDIR /src

COPY ./requirements.txt /src/requirements.txt

RUN pip install --no cache-dir --upgrade -r /src/requirements.txt

COPY ./app.py /src/

CMD ["fastapi", "run", "app.py", "--port", "80"]
