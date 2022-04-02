politicos = [
	{
		"nome": "Luis Inácio Lula da Silva",
		"partido": "PT",
		"numero": 13,
		"votos": 0
	},
	{
		"nome": "Simone Tebet",
		"partido": "PMDB",
		"numero": 14,
		"votos": 0
	},
	{
		"nome": "João Dória",
		"partido": "PSDB",
		"numero": 15,
		"votos": 0
	},
	{
		"nome": "Jair Bolsonaro",
		"partido": "PL",
		"numero": 22,
		"votos": 0


	},
]

brancos = []
nulos = []


def pegar_voto():
	return input("Digite o número do político que deseja votar(13(PT), 14(PMDB), 15(PSDB), 22(PL), ou 'branco' para votar em branco: ").lower()


def procurar_politico(voto):
	"""
	Precisar varrer a lista de dicionários de políticos
	Precisamos checar o número do político e ver se é igual ao valor digitado no voto
	Caso encontremos um político, devemos retorná-lo
	Caso contrário, não retornamos nada
	"""
	for politico in politicos:
		if str(politico["numero"]) == voto:
			return politico

	return None


def contabilizar_voto(voto, politico):
	"""
	Checar se o voto é branco e contabilizá-lo
	Checar se existe algum político válido e contabilizar o voto para ele
	Caso contrário, o voto é nulo, contabilizar da mesma forma
	Exibir a mensagem de resultado
	"""
	if voto == "branco":
		print("O seu voto em branco foi contabilizado.")
		brancos.append(voto)
	elif politico:
		politico["votos"] += 1
		print("O seu voto para o político '{}' foi contabilizado.".format(politico["nome"]))
	else:
		nulos.append(voto)
		print("O seu voto foi anulado.")


def validar_voto(voto):
	"""
	Essa função verificar se o voto é válido
	Ela pesquisa cada político e vê se o valor do voto é igual ao número dele
	Ela checa se o voto é branco
	Precisar exibir se achou um político ou não e as informações dele
	Depois disso, precisa contabilizar o voto (confirmando, corrigindo ou cancelando)
	"""

	politico = None

	if voto == "branco":
		print("Você votou em branco.")
	else:
		politico = procurar_politico(voto)

		if politico:
			print("O voto '{}' corresponde ao político '{}' do partido '{}'.".format(voto, politico["nome"], politico["partido"]))
		else:
			print("Nenhum político para o voto '{}' foi encontrado. Se prosseguir, seu voto será anulado.".format(voto))

	acao = input("Deseja confirmar, corrigir ou cancelar: ").lower()

	if acao == "confirmar":
		contabilizar_voto(voto, politico)
	elif acao == "corrigir":
		print("Você selecionou a opção de correção do voto. Informe-o novamente.")
	else:
		print("Você cancelou a informação do voto atual. Informe-o novamente.")


def pegar_votos_validos():
	votos_validos = 0

	for politico in politicos:
		votos_validos += politico["votos"]

	return votos_validos


def exibir_votos():
	print("Votos válidos: {}.".format(pegar_votos_validos()))
	print("Votos brancos: {}.".format(len(brancos)))
	print("Votos nulos: {}.".format(len(nulos)))


def pegar_porcentagem(politico):
	"""
	Preciso pegar o total de votos válidos da eleição
	Preciso pegar os votos do político e fazer a regra de 3
	"""
	votos_validos = pegar_votos_validos()
	porcentagem = (100 * politico["votos"]) / votos_validos
	return porcentagem


def exibir_politico(politico):
	porcentagem = pegar_porcentagem(politico)
	plural = "" if politico["votos"] == 1 else "s"
	print("Político '{}' do partido '{}' recebeu '{}' voto{} e ficou com '{:.2f}%' dos votos válidos.".format(politico["nome"], politico["partido"], politico["votos"], plural, porcentagem))


def exibir_resultado_eleicao():
	"""
	O vencedor precisa ter mais de 50% dos votos válidos
	Caso ninguém tenha, precisamos saber quem é o primeiro e o segundo lugar que vão
	para o segundo turno
	"""
	primeiro_lugar = None
	segundo_lugar = None

	for politico in politicos:
		if primeiro_lugar == None or politico["votos"] > primeiro_lugar["votos"]:
			segundo_lugar = primeiro_lugar

			primeiro_lugar = politico
		elif segundo_lugar == None or politico["votos"] > segundo_lugar["votos"]:
			segundo_lugar = politico

	porcentagem = pegar_porcentagem(primeiro_lugar)

	if porcentagem > 50:
		print("O vencedor da eleição é o político '{}' com '{:.2f}%' dos votos válidos.".format(primeiro_lugar["nome"], porcentagem))
	else:
		print("A votação encerrou em segundo turno.")
		print("Os políticos que irão para o segundo turno são:")
		exibir_politico(primeiro_lugar)
		exibir_politico(segundo_lugar)


def exibir_politicos():
	print("Resultado geral da votação")
	for politico in politicos:
		exibir_politico(politico)


while True:
	voto = pegar_voto()

	if voto == "encerrar_votacao":
		print("Votação encerrada com sucesso.")
		break

	validar_voto(voto)


exibir_votos()
exibir_resultado_eleicao()

print("_____________________________")

exibir_politicos()
# VOTE NESSAS ELEIÇÕES SEU VOTO É MUITO IMPORTANTE PARA O FUTURO DO PAÍS.

# Renato Barbosa
