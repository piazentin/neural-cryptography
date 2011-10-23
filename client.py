from twisted.internet.protocol import Protocol
from twisted.internet.protocol import Factory
from twisted.internet.endpoints import TCP4ClientEndpoint
from twisted.internet import reactor
from protocol import NeuralCryptography
from tpm import TreeParityMachine
import json

class CriptografiaNeural(NeuralCryptography):

    def __init__(self):
       NeuralCryptography.__init__(self)

    def dataReceived(self, data):
        data = json.loads(data)
        print data 
        if not self.synced():
            self.syncronizer(data)

    def connectionMade(self):
        self.receive_ack()

# Inicializa classe
factory = Factory()
factory.protocol = CriptografiaNeural
endpoint = TCP4ClientEndpoint(reactor, "localhost",1984)
endpoint.connect(factory)
reactor.run()
