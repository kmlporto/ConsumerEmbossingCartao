FROM python:3-slim

ARG ROUTING_KEY
ENV ROUTING_KEY ${ROUTING_KEY}
WORKDIR /app
COPY ./ /app
RUN pip install -r /app/requirements.txt
CMD ["python", "embossing.py"]