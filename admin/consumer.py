import pika , json

params = pika.URLParameters('amqps://sxwxkysy:mgoDmNss1pIdcPwDeu1K1B6RwHA_xwTt@fly.rmq.cloudamqp.com/sxwxkysy')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue="admin")

def callback(ch, method, properties, body):
    print('Receive in admin')
    data= json.loads(body)
    print(data)
    product = Product.objects.get(id=data)
    product.likes = product.likes +1 
    product.save()
    print("Product likes increase")

channel.basic_consume(queue='admin', on_message_callback=callback,auto_ack=True)

print("Started Consuming")

channel.start_consuming()

channel.close()
