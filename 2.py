# CRIAR A FUNÇÃO AQUI:
def calculadora(n1= int, n2= int, op= str):
  '''
  calculadora serve para fazer operações matemáticas com dois números

  n1 e n2: números inteiros solicitados ao usuário para realizar as operações

  op = operação que o usuário pretende realizar
  '''

  if op == '+':
    soma = n1 + n2
    resultado = soma

  elif op == '-':
    sub = n1 - n2
    resultado = sub
  
  elif op == '*':
    mult = n1 * n2
    resultado = mult
  
  elif op == '/':
    if n2 != 0:
      divisao = n1 / n2
      resultado = divisao
    else:
      print('ERRO: DIVISÃO POR 0')
  
  elif op == '%':
    resultado = n1 % n2

  elif op == '//':
    div = n1 // n2
    resultado = div

  return resultado

# MENU: REUSABILIDADE
print('MENU: CALCULADORA')
print('OPÇÃO: [+] se você quiser realizar uma soma')
print('OPÇÃO: [-] se você quiser realizar uma subtração')
print('OPÇÃO: [*] se você quiser realizar uma multiplicação')
print('OPÇÃO: [/] se você quiser realizar uma divisão')
print('OPÇÃO: [%] se você quiser realizar o mod')
print('OPÇÃO: [//] se você quiser realizar uma divisão inteira')
print()

for i in range(3): 

  try:

    n1 = int(input('Digite o valor do 1° número: '))
    n2 = int(input('Digite o valor do 2° número: '))
    op = str(input("Digite a opção de operação que deseja realizar: "))

    calc = calculadora(n1, n2, op)
    print(f'O resultado do calculo é: {calc}')

  except Exception as ERRO_EXCECAO:
    print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}')

