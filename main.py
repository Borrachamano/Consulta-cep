try:
        from os import system
	import requests as rq
except:
	system("pip intall requests")
        import requests as rq


def lines():
	print('-' * 40)


def main():
	print('#########################')
	print('Consulta Cep')
	print('#########################')
	cep = input('Informe o cep que deseja consultar: ')
	
	while len(cep) != 8:
		print('Quantidade de digitos invalida. Tente novamente.')
		cep = input('Informe o ceo que deseja consultar: ')
	info = rq.get(f'https://viacep.com.br/ws/{cep}/json/').json()
	
	lines()
	
	if 'erro' not in info:
		print(f'##### Informações do cep #####')
		print(f'Sucess: True')
		print(f'Cep: {info["cep"]}')
		print(f'Logradouro: {info["logradouro"]}')
		print(f'Complemento: {info["complemento"]}')
		print(f'Bairro: {info["bairro"]}')
		print(f'Localidade: {info["localidade"]}')
		print(f'UF: {info["uf"]}')
		print(f'DDD: {info["ddd"]}')
	else:
		print('Resultado: Cep não encontrado')
		print(f'Sucess: False')
	
	lines()
	
	opc = str(input('Deseja continuar? [S/n]: ')).strip().upper()
	
	if opc == 'S':
		system('clear')
		main()

# A funcao onde esta todas as funcionalidade do programa
# Só sera chamada se estiver sendo executada no arquivo principal

if __name__ == '__main__':
	main()
