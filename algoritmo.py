# Faça
# 	A.gerar_entradas
# 	A.transmitir_entradas
# 	A.calcular_saida
# 	B.calcular_saida
# 	A.transmitir_saida
# 	Se A.saida = B.saida
# 		A.treinar
# 		B.treinar
# Até sincronizar


# Formato de mensagens:
# [tipo_de_mensagem, valor]

# Transmição de entradas:
# ["in", [1,0,1,1,1,1,1,1,0,0,0,1,1,1,1,0,0]]

# Transmição de saída:
# ["out", 1]

# Transmição de saída:
# ["ack", 0]

# Para sincronizar as mensagens, usaremos uma mensagem especial de acknowledgment
# informando ao parceiro que a mensagem anterior foi processada


# Para efeito de simplificação do algoritmo, 
# o ultimo vetor de entrada recebido é salvo em B

# Lado A (cliente)
# Inicio da conexão
A.gerar_entradas()
A.calcular_saida(A.entradas)
A.transmitir_entradas()

# Depois de iniciar a conexão, o lado A se torna reativo
if self.sincronizado():
	A.encerrar_sincronizacao

if data[TIPO_DE_MENSAGEM] = ACK:
	A.gerar_entradas()
	A.calcular_saida(A.entradas)
	A.transmitir_entradas()

if data[TIPO_DE_MENSAGEM] = SAIDA:
	A.transmitir_saida()
	if A.saida == data[VALOR]:
		self.incrementa_sincronizacao()
		A.treinar()
	else:
		self.decrementa_sincronizacao()

# Lado B (servidor)
# O servidor é reativo
# O servidor detecta a sincronização
if self.sincronizado():
	B.encerrar_sincronizacao()

if data[TIPO_DE_MENSAGEM] == ENTRADA:
	B.calcular_saida(data[VALOR])
	B.transmitir_saida()

if data[TIPO_DE_MENSAGEM] = SAIDA:
	if B.saida == data[VALOR]:
		self.incrementa_sincronizacao()
		B.treinar()
	else:
		self.decrementa_sincronizacao()