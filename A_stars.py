from celulas import celula
from math import sqrt
from math import pow

def RetiraEspaço():  #Retira os espaços e preenche a lista com a classe
	mapa = open("hyrule.txt", 'r', encoding="utf8")
	linha = mapa.readline()
	linha = mapa.readline() # Pular comentários
	aux = []
	x=0
	y=0
	while linha:
		Retira_espaço = []
		y=0
		for i in linha:
			if i==" ":   # Retira espacos em branco do arquivo
				continue
			else :
				celulas = celula(i,x,y)	 #preenche a celula, com o valor e as coordenadas
				if i != "\n":
					Retira_espaço.append(celulas)
				y = y + 1
		x = x + 1		
		aux.append(Retira_espaço)
		linha = mapa.readline()
	#print(aux[9][41].x)
	#print(aux[1][41].y)
	#print(aux[1][41].valor)
	mapa.close()
	return aux

def calcula_distancia(estado_atual, estado_final):
	a = abs(estado_atual.x - estado_final.x) + abs((estado_atual.y - estado_final.y))
	return D * a
	#soma = pow((estado_final.x - estado_atual.x), 2) + pow((estado_final.y - estado_atual.y), 2)
	#distancia = sqrt(soma)
	#return distancia


def melhor_filho(lista_Aberta , lista_heuristica):
	
	melhor_valor = 999999999
	melhor_estado = None
	melhor_indice = 0
	indice = 0

	for estado in lista_Aberta:
		if(melhor_valor > lista_heuristica[estado]):
			melhor_estado = estado
			melhor_valor = lista_heuristica[estado]
			melhor_indice = indice
		indice = indice + 1
	return melhor_indice

def procura_filhos(matriz, estado): #Apenas na vertical e horizontal

	x = estado.x
	y = estado.y
	filhos = []
	if( x+1 < 42 ):   #move pra baixo
		filhos.append(matriz[x+1][y])
	if( x-1 > 0 ):   #move pra cima 
		filhos.append(matriz[x-1][y])
	if( y-1 > 0): 	#move pra esquerda
		filhos.append(matriz[x][y-1]) 
	if( y+1 < 42):		#move pra direita
		filhos.append(matriz[x][y+1])

	return filhos

def peso_do_caminho(estado):
	if (estado.valor == "G"):
		return 10
	if (estado.valor == "D"):
		return 20
	if (estado.valor == "F"):
		return 100
	if (estado.valor == "M"):
		return 150
	if (estado.valor == "A"):
		return 180
	if (estado.valor == "L"):
		return 0
	if (estado.valor == "S"):
		return 0
	if (estado.valor == "REB"):
		return 0
	else: 
		return 0

def mostra_solucao(estado,predecessores,repeticao):
	custo_total = 0
	caminho = []
	caminho.append(estado)					# Faz o caminho de volta até o estado inicial
	while(predecessores[estado]!=None) :
		caminho.append(predecessores[estado])
		estado = predecessores[estado]
	caminho = caminho[::-1]  #Inverte a lista
	for no in caminho:
		print('x = ',no.x,'y =',no.y, 'valor:',no.valor)
		custo_total = custo_total + peso_do_caminho(no)
	print(custo_total)

def retorna_solucao(estado,predecessores,repeticao):
	path =[]
	custo_total = 0
	caminho = []
	caminho.append(estado)					# Faz o caminho de volta até o estado inicial
	while(predecessores[estado]!=None) :
		caminho.append(predecessores[estado])
		estado = predecessores[estado]
	caminho = caminho[::-1]  #Inverte a lista
	for no in caminho:
		custo_total = custo_total + peso_do_caminho(no)
		path.append((no.x,no.y,custo_total))
		
	return path


def busca_a_estrela( matriz , estado_inicial, estado_final):

	d_linha_reta = {}	#Distância em linha reta
	d_percorrida = {}	#Distância Percorrida
	heuristica = {}
	predecessores = {}
	nos_expandidos = [] #  append
	auxiliar = []   #	append
	solucao = False

	auxiliar.append(estado_inicial)
	predecessores[estado_inicial] = None 
	d_percorrida[estado_inicial] = 0
	d_linha_reta[estado_inicial] =  calcula_distancia(estado_inicial,estado_final)
	heuristica[estado_inicial] =  d_percorrida[estado_inicial] + d_linha_reta[estado_inicial]

	
	repeticao = 1

	while len(auxiliar) != 0:
		melhor_indice = melhor_filho(auxiliar,heuristica)   
		estadoPai = auxiliar.pop(melhor_indice)  #retira o melhor indice da lista
		if estadoPai == estado_final:
			solucao = True
			break
		estados_filhos = procura_filhos(matriz,estadoPai)
		nos_expandidos.append(estadoPai) # E o adiciona como nó expandido

		#GUI feedback
		yield (estadoPai.x,estadoPai.y)

		for i in range(0, len(estados_filhos)):
			sucessor = estados_filhos[i]
			if(sucessor not in nos_expandidos and sucessor not in auxiliar) : #Verifica se o nó já foi expandido ou se já esta para ser avaliado
				auxiliar.append(sucessor)

				if(sucessor not in heuristica.keys()): # metodo que retorna chaves do dicionario
					d_linha_reta[sucessor] = calcula_distancia(sucessor, estado_final)
					teste = (peso_do_caminho(sucessor))
					d_percorrida[sucessor] = d_percorrida[estadoPai] + (peso_do_caminho(sucessor))
					heuristica[sucessor] = d_linha_reta[sucessor] + d_percorrida[sucessor]   #Calculo da Func heuristica
					predecessores[sucessor] = estadoPai 

		repeticao = repeticao + 1


	#Checar se encontrou uma solucao através da variável booleana

	if (solucao == True):
		return retorna_solucao(estadoPai,predecessores,repeticao)
		mostra_solucao(estadoPai,predecessores,repeticao)
	else:
		print("Não foi possivel achar uma solução")


def main():


	matriz = RetiraEspaço()
	#print(matriz[6][4].x)
	estado_inicial = matriz[23][27]
	estado_final = matriz[2][1]
	print(estado_final.x)
	print(estado_inicial.x)
	sol = busca_a_estrela(matriz,estado_inicial,estado_final)
	return sol
	

if __name__ == "__main__":
    main()