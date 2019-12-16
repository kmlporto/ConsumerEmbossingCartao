FROM python:3-slim

WORKDIR /app
COPY ./ /app
RUN pip install -r /app/requirements.txt
CMD ["python", "embossing.py"]