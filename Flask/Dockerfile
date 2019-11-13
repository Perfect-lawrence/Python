FROM python:3.6.8
WORKDIR /app
ADD . /app
RUN pip install -r requirements.txt
EXPOSE 10080
ENV NAME World
CMD ["python","app.py"]

