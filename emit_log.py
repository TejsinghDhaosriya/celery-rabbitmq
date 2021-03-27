import sys
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.exchange_declare(exchange='logs',
                         exchange_type='fanout')
# channel.queue_declare(queue='', durable=True, exclusive=True)
message = ' '.join(sys.argv[1:]) or "Hello World!"

# channel.queue_bind(exchange='logs',
#                    queue=result.method.queue)
channel.basic_publish(exchange='logs',
                      routing_key='',
                      body=message
                      )
print(" [x] Sent %r" % message)


connection.close()
