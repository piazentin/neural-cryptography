from twisted.internet.protocol import Protocol
from twisted.internet.protocol import Factory
from twisted.internet.endpoints import TCP4ServerEndpoint
from twisted.internet import reactor
from protocol import NeuralCryptography
from tpm import TreeParityMachine
import json

class NeuralCryptographyServer(NeuralCryptography):

    def __init__(self):
       NeuralCryptography.__init__(self)

    def dataReceived(self, data):
        data = json.loads(data)
        print data 
        if not self.synced():
            self.syncronizer(data)

# Inicializa classe
factory = Factory()
factory.protocol = NeuralCryptographyServer
endpoint = TCP4ServerEndpoint(reactor, 1984)
endpoint.listen(factory)
reactor.run()
