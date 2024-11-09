FROM python:3.11.1
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache -r /app/requirements.txt
COPY . /app/
CMD ["python", "my_dialog.py"]