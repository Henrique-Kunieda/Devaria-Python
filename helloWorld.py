def somar ( numero1, numero2 ):
   print(f'Realizando soma de {n1} + {n2}')
   return numero1 + numero2

def subtrair ( numero1, numero2):
   print(f'Realizando subtração de {n1} - {n2}')
   return numero1 - numero2

def dividir ( numero1, numero2):
   print(f'Realizando divisão de {n1} / {n2}')
   return numero1 / numero2

def multiplicar ( numero1, numero2):
   print(f'Realizando multiplicação de {n1} * {n2}')
   return numero1 * numero2 


if __name__ == '__main__': 
   n1 = int(input('Digite o primeiro número:')) 
   n2 = int(input('Digite o segundo número: '))

   operador = input( 'Qual operação matemática vpcê deseja fazer? ( +, -, /, *)')

   if operador == '+':
      resultado = somar(n1,n2)

   elif operador == '-':
      resultado = subtrair(n1, n2)
      
   elif operador == '/':
     resultado = dividir(n1, n2)

   elif operador == '*':
     resultado = multiplicar(n1,n2)
   
else:
    print('Operador inválido')

print(f'O resultado da operação é {resultado}')
    