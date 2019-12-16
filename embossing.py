import pika
import json
import os


def consumer_callback(ch, method, properties, body):
    cartoes = json.loads(body)
    print(cartoes)


connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))

EXCHANGE_NAME = 'embossing'
EXCHANGE_TYPE = 'direct'
ROUTING_KEY = os.getenv('ROUTING_KEY')
print(ROUTING_KEY)
channel = connection.channel()
channel.exchange_declare(
    exchange=EXCHANGE_NAME,
    exchange_type=EXCHANGE_TYPE,
)

result = channel.queue_declare(queue='', durable=True)
queue_name = result.method.queue

channel.queue_bind(
    exchange=EXCHANGE_NAME,
    queue=queue_name,
    routing_key= ROUTING_KEY,
)

if ROUTING_KEY == 'processing':
    print("Entregar o cartão ao cliente logo após o cadastro na loja.")
else:
    print("Enviar cartões na residência após embossing.")
channel.basic_consume(
    queue=queue_name,
    on_message_callback=consumer_callback,
    auto_ack=True
)


channel.start_consuming()
