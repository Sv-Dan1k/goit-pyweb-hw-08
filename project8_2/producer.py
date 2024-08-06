import pika
import json
from faker import Faker


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()


channel.queue_declare(queue='email_queue')


fake = Faker()

for _ in range(10):
    contact_id = fake.uuid4() 
    contact = {
        'id': contact_id,
        'fullname': fake.name(),
        'email': fake.email()
    }
    

    channel.basic_publish(exchange='',
                          routing_key='email_queue',
                          body=json.dumps(contact))
    print(f"Sent message for contact {contact['fullname']}")


connection.close()
