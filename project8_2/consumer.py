import pika
import json

def send_email(contact):
    #Заглушка
    print(f"Sending email to {contact['email']}")
    return True

def callback(ch, method, properties, body):
    contact = json.loads(body)
    
    if send_email(contact):
        print(f"Email sent to {contact['fullname']}")


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()


channel.queue_declare(queue='email_queue')
channel.basic_consume(queue='email_queue', on_message_callback=callback, auto_ack=True)

print('Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
