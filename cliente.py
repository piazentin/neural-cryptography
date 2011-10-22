from twisted.internet.protocol import Protocol
from twisted.internet.protocol import Factory
from twisted.internet.endpoints import TCP4ClientEndpoint
from twisted.internet import reactor
from tpm import *
import json

TIPO_DE_MENSAGEM = 0
VALOR = 1
ENTRADA = 0
SAIDA = 1
ACK = 2
LIMITE_SINCRONIZACAO = 5

class CriptografiaNeural(Protocol):

    def __init__(self):
        self.A = Cripto(4,3);
        self.contador_sincronizacao = 0

    def connectionMade(self):
        self.A.gerar_entradas()
        self.A.calcular_saida(self.A.entradas)
        self.transport.write(json.dumps([ENTRADA, self.A.entradas]))

    def dataReceived(self, data):
        data = json.loads(data)
        print data

        if self.sincronizado():
            print "Sincronizado"
            self.transport.write(json.dumps([ACK, 0]))
            return;

        if data[TIPO_DE_MENSAGEM] == ACK:
            self.A.gerar_entradas()
            self.A.calcular_saida(self.A.entradas)
            self.transport.write(json.dumps([ENTRADA, self.A.entradas]))

        if data[TIPO_DE_MENSAGEM] == SAIDA:
            self.transport.write(json.dumps([SAIDA, self.A.saida]))
            if self.A.saida == data[VALOR]:
                self.incremenda_sincronizacao()
                self.A.treinar()
            else:
                self.decremenda_sincronizacao()


    def sincronizado(self):
        return self.contador_sincronizacao == LIMITE_SINCRONIZACAO

    def incremenda_sincronizacao(self):
        self.contador_sincronizacao = self.contador_sincronizacao + 1

    def decremenda_sincronizacao(self):
        self.contador_sincronizacao = 0


# Inicializa classe
factory = Factory()
factory.protocol = CriptografiaNeural
endpoint = TCP4ClientEndpoint(reactor, "localhost",1984)
endpoint.connect(factory)
reactor.run()
