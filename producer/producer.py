import pika
import os

amqp_url = os.environ["AMQP_URL"]

# Устанавливаем соединение с RabbitMQ
connection = pika.BlockingConnection(pika.URLParameters(amqp_url))
channel = connection.channel()

# Создаем очередь, в которую будут помещаться сообщения
channel.queue_declare(queue="fibonacci_queue")

# Отправляем сообщение в очередь
print(" [x] Sending number 10")
channel.basic_publish(exchange="", routing_key="fibonacci_queue", body="10")
print(" [x] Sending number 100")
channel.basic_publish(exchange="", routing_key="fibonacci_queue", body="100")
print(" [x] Sending number 56")
channel.basic_publish(exchange="", routing_key="fibonacci_queue", body="56")
print(" [x] All numbers sent. Closing connection.")
# Закрываем соединение
connection.close()
