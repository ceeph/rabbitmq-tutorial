import pika

# setting up connection with parameter 'localhost'
connection = pika.BlockingConnection(pika.ConnectionParameters(
                'localhost'))
# get channel from connection
channel = connection.channel()

# create queue
channel.queue_declare(queue='hello')

channel.basic_publish(exchange='', #default
                      routing_key='hello', #queue name
                      body='Hello, World!') #message
print(" [x] Sent 'Hello, World!'")

connection.close()

