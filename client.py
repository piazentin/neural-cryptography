from twisted.internet.protocol import Protocol
from twisted.internet.protocol import Factory
from twisted.internet.endpoints import TCP4ClientEndpoint
from twisted.internet import reactor
from protocol import NeuralCryptography
from tpm import TreeParityMachine
import json

class NeuralCryptographyClient(NeuralCryptography):

    def __init__(self):
        NeuralCryptography.__init__(self)
        self.call(target=chatLoop, args=(self,))
        self.receive(target=printer)

    def dataReceived(self, data):
        if not self.synced():
            self.syncronizer(data)
        else:
            self.received(data)

    def connectionMade(self):
        self.receive_ack()


def chatLoop(chat):
    while True:
        chat.send_message(str(raw_input()))

def printer(message):
    print message

# Inicializa classe
factory = Factory()
factory.protocol = NeuralCryptographyClient
endpoint = TCP4ClientEndpoint(reactor, "localhost",1984)
endpoint.connect(factory)
reactor.run()
