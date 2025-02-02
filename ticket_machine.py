import json

import pika

from xprint import xprint


class TicketEventProducer:

    def __init__(self):
        # Do not edit the init method.
        # Set the variables appropriately in the methods below.
        self.connection = None
        self.channel = None
        self.exchange = "ticket_events_exchange"
        self.routing_key = "ticket_event"

    # TODO: test this function
    def initialize_rabbitmq(self):
        """
        Initialize the RabbitMq connection, channel, exchange and queue.
        :return:
        """
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host="localhost")
        )
        self.channel = self.connection.channel()
        self.channel.exchange_declare(exchange=self.exchange, exchange_type="fanout")
        xprint("TicketEventProducer initialize_rabbitmq() called")

    # TODO: Use json.dumps(vars(ticket_event)) to convert the ticket_event object to JSON
    def publish_ticket_event(self, ticket_event):
        """
        Publish a message to the Rabbitmq
        :param ticket_event:
        :return:
        """
        xprint("TicketEventProducer: Publishing ticket event {}"
               .format(vars(ticket_event)))


    def close(self):
        self.channel.close()
        self.connection.close()
