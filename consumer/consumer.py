import pika
import os

amqp_url = os.environ["AMQP_URL"]


def fibonacci(n: int) -> int:
    """
    Рассчитывает число фибоначи для переданного числа.
    """
    a = 0
    b = 1

    # Check is n is less
    # than 0
    if n < 0:
        print("Incorrect input")

    # Check is n is equal
    # to 0
    elif n == 0:
        return 0

    # Check if n is equal to 1
    elif n == 1:
        return b
    else:
        for i in range(1, n):
            c = a + b
            a = b
            b = c
        return b


# Создаем функцию-обработчик сообщений из очереди
def callback(ch, method, properties, body):
    print(
        f"Received and calculated fibonacci number from {int(body)} to {fibonacci(int(body))}"
    )


# Устанавливаем соединение с RabbitMQ
connection = pika.BlockingConnection(pika.URLParameters(amqp_url))
channel = connection.channel()

# Создаем очередь, в которую будут помещаться сообщения
channel.queue_declare(queue="fibonacci_queue")

# Подписываемся на очередь и начинаем получать сообщения
channel.basic_consume(
    queue="fibonacci_queue", on_message_callback=callback, auto_ack=True
)

print(" [*] Waiting for messages. To exit press CTRL+C")
channel.start_consuming()
