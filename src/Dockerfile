FROM python:3.6

WORKDIR /app

COPY . /app
RUN pip install pipenv && pipenv install --system

ENV FLASK_APP app.py
EXPOSE 5000

CMD [ "flask", "run", "-h", "0.0.0.0" ]