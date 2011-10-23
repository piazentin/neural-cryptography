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
        self.call(target=chatLoop, args=(self,))
        self.receive(target=printer)

    def dataReceived(self, data):
        if not self.synced():
            self.syncronizer(data)
        else:
            self.received(data)

def chatLoop(chat):
    while True:
        chat.send_message(str(raw_input("Digite sua mensagem: ")))

def printer(message):
    print "Mensagem recebida: ", message

# Inicializa classe
factory = Factory()
factory.protocol = NeuralCryptographyServer
endpoint = TCP4ServerEndpoint(reactor, 1984)
endpoint.listen(factory)
reactor.run()
