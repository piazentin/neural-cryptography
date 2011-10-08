from twisted.internet.protocol import Protocol
from twisted.internet.protocol import Factory
from twisted.internet.endpoints import TCP4ServerEndpoint
from twisted.internet import reactor
from tpm import *
import json

TIPO_DE_MENSAGEM = 0
VALOR = 1
ENTRADA = 0
SAIDA = 1
ACK = 2
LIMITE_SINCRONIZACAO = 10

class CriptografiaNeural(Protocol):

    def __init__(self):
        self.B = Cripto(4,3);
        self.contador_sincronizacao = 0

    def dataReceived(self, data):
        data = json.loads(data)
        print data 

        if self.sincronizado():
            print "sincronizado"
            return;

        if data[TIPO_DE_MENSAGEM] == ENTRADA:
            self.B.calcular_saida(data[VALOR])
            self.transport.write(json.dumps([SAIDA, self.B.saida]))

        if data[TIPO_DE_MENSAGEM] == SAIDA:
            if self.B.saida == data[VALOR]:
                self.incremenda_sincronizacao()
                self.B.treinar()
            else:
                self.decremenda_sincronizacao()
            self.transport.write(json.dumps([ACK, 0]))


    def sincronizado(self):
        return self.contador_sincronizacao == LIMITE_SINCRONIZACAO

    def incremenda_sincronizacao(self):
        self.contador_sincronizacao = self.contador_sincronizacao + 1

    def decremenda_sincronizacao(self):
        self.contador_sincronizacao = 0

# Inicializa classe
factory = Factory()
factory.protocol = CriptografiaNeural
endpoint = TCP4ServerEndpoint(reactor, 1984)
endpoint.listen(factory)
reactor.run()
