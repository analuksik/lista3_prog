# CRIAR A FUNÇÃO AQUI:

def multiplicaNumeros(n: int, opcao:str):

  '''
  multiplicaNumeros serve para calcular a multiplicação dos números pares ou ímpares no intervalo de [1, n]

  n: um número int > 0 escolhido pelo usuário para definir o intervalo em que será
  feito o calculo

  opcao: uma string 'par' ou 'impar' para o usuario escolher se deseja a multiplicação dops numeros pares ou dos numeros ímpares
  '''
  resultado = 1

  if opcao == 'par':
    for i in range (2, n + 1, 2):
      resultado *= i
    
  elif opcao == 'impar':
    for i in range(1, n + 1, 2):
      resultado *= i

  return resultado

for i in range(100):
  try:

    n = int(input("Insira o valor para n: "))
    opcao = str(input("Escolha 'par' ou 'impar' para multiplicar: "))

  except Exception as ERRO_EXCECAO:
    print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}')


  if n > 0 and opcao in ['par', 'impar']:
    resultado = multiplicaNumeros(n, opcao)
    print(f"Resultado da múltiplicação de número {opcao} entre [1, {n}] é de: {resultado}")
  else:
    print('ENTRADA INVÁLIDA')
