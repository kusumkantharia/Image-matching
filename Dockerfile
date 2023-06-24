FROM python:3.9.14-slim-bullseye
COPY . /usr/app/
EXPOSE 5000
WORKDIR /usr/app/
RUN pip install --upgrade pip && pip install -r requirements.txt
CMD ["python","app.py"]