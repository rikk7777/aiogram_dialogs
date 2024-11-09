FROM python:3.11.1

ENV PYTHONUNBUFFERED=1

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

WORKDIR /project1/bot/

COPY /project1/bot/ /project1/bot/

CMD ["python", "project1/bot/main.py"]