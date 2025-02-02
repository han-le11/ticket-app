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

    def initialize_rabbitmq(self):
        # To implement - Initialize the RabbitMq connection, channel, exchange and queue here
        xprint("TicketEventProducer initialize_rabbitmq() called")

    def publish_ticket_event(self, ticket_event):
        xprint("TicketEventProducer: Publishing ticket event {}"
               .format(vars(ticket_event)))
        # To implement - publish a message to the Rabbitmq here
        # Use json.dumps(vars(ticket_event)) to convert the shopping_event object to JSON

    def close(self):
        # Do not edit this method
        self.channel.close()
        self.connection.close()
