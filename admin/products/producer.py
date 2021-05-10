import pika 

params = pika.URLParameters('amqps://sxwxkysy:mgoDmNss1pIdcPwDeu1K1B6RwHA_xwTt@fly.rmq.cloudamqp.com/sxwxkysy')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish(method, body):
    channel.basic_publish(exchange="", routing_key="main", body='hello')
