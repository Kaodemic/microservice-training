import pika , json

params = pika.URLParameters('amqps://sxwxkysy:mgoDmNss1pIdcPwDeu1K1B6RwHA_xwTt@fly.rmq.cloudamqp.com/sxwxkysy')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange="", routing_key="main", body=json.dump(body),properties=properties)
