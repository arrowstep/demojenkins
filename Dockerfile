FROM python:3.6

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONUNBUFFERED=1


COPY ./healthdemo /app
VOLUME [ "/app" ]
WORKDIR /app

RUN pip install -r requirements.txt
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

