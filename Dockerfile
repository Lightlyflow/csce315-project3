FROM python:3.11-alpine
EXPOSE 5000/tcp
WORKDIR /root
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY app/. app/.
CMD [ "python", "app/app.py" ]
