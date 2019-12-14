import pika
import json

def consumer_callback(ch, method, properties, body):
    cartoes = json.loads(body)
    print('tam',len(cartoes))
    print(cartoes)
    # for cartao in cartoes:
    #     print(cartao)
    #     # print('Numero:', cartao[0], 'Nome do Portador:', cartao[1], 'Validade:', cartao[2], 'Codigo de Seguranca:', cartao[4])


connection = pika.BlockingConnection(pika.ConnectionParameters())

nome_fila = 'analiseCartao'
channel = connection.channel()
channel.queue_declare(queue=nome_fila, durable=True)
channel.basic_consume(on_message_callback=consumer_callback, queue=nome_fila, auto_ack=True)

channel.start_consuming()