FROM python:3.11.1

ENV PYTHONUNBUFFERED=1

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

WORKDIR /project1

COPY /my_aiogram_dialogs /project1/

CMD ["python", "project1/main.py"]