import pika

# same connection as sender
connection = pika.BlockingConnection(pika.ConnectionParameters(
                   'localhost'))
channel = connection.channel()

# we declare the queue here as well as in
# the sender because we don't know which
# one gets to execute first
channel.queue_declare(queue='hello')

# we define the function we later associate
# to a queue, executing it everytime we
# receive a message on it
def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)

print (' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
