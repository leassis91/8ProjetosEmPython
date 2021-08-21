#Projeto 3 - criar um algoritmo que gera um valor aleatório e que o usuário tenha que ficar tentando acertar o número gerado


from random import random, choice

'''def gerar_random(valor):
	n = choice(valores)
	if valor > n:
		print ("Digite um valor mais baixo!")
	elif valor < n:
		print ("Digite um valor mais alto!")
	else:
		print("Parabéns! Você acertou em cheio!")
'''
while True:

	print("\n******************* Tente a sorte! *******************")

	tamanho = int(input("\nDigite até que número você deseja acertar: "))
	valores = range(1, tamanho)
	valor = choice(valores)

	n = int(input("\nTente acertar o número aleatório: "))

	while n != valor:
		if n > valor:
			print ("Digite um valor mais baixo!")
			n = int(input("\nTente acertar o número aleatório novamente: "))
		elif n < valor:
			print ("Digite um valor mais alto!")
			n = int(input("\nTente acertar o número aleatório novamente: "))
	else:
		print("Parabéns! Você acertou em cheio! O número era ", valor)
	