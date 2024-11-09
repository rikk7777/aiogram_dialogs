FROM python:3.11.1

ENV PYTHONUNBUFFERED=1

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

WORKDIR /my_aiogram_dialogs

COPY ./my_aiogram_dialogs /my_aiogram_dialogs/

CMD ['python', '/my_aiogram_dialogs/dialog.py']