from twisted.internet.protocol import Protocol
from twisted.internet.protocol import Factory
from twisted.internet.endpoints import TCP4ServerEndpoint
from twisted.internet import reactor

class Chat(Protocol):

	def connectionMade(self):
		self.transport.write("ok")

	def dataReceived(self, data):
		print data

# Inicializa classe
factory = Factory()
factory.protocol = Chat
endpoint = TCP4ServerEndpoint(reactor, 1984)
endpoint.listen(factory)
reactor.run()
