import pika 

params = pika.URLParameters('amqps://sxwxkysy:mgoDmNss1pIdcPwDeu1K1B6RwHA_xwTt@fly.rmq.cloudamqp.com/sxwxkysy')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue="admin")

def callback(ch, method, properties, body):
    print('Receive in admin')
    print(body)

channel.basic_consume(queue='main', on_message_callback=callback)

print("Started Consuming")

channel.start_consuming()

channel.close()
