FROM python:3.10-slim

WORKDIR /code
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt
COPY data data
COPY app app
COPY exceptions exceptions
COPY log log
COPY static static
COPY tests tests
COPY uploads uploads
COPY config.py .
COPY config_logger.py .
COPY run.py .
COPY wsgi.py .

CMD flask run -h 0.0.0.0 -p 5000