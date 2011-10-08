from twisted.internet.protocol import Protocol
from twisted.internet.protocol import Factory
from twisted.internet.endpoints import TCP4ClientEndpoint
from twisted.internet import reactor
from threading import Thread
import time

class Chat(Protocol):

	def connectionMade(self):
		th = Thread(target=chatLoop, args=(self))
		th.start()
		self.transport.write("ok")

	def dataReceived(self, data):
		print data

def chatLoop(chat):
	while True:
		chat.transport.write(str(raw_input()))

# Inicializa classe
factory = Factory()
factory.protocol = Chat
endpoint = TCP4ClientEndpoint(reactor, "localhost",1984)
endpoint.connect(factory)
reactor.run()
