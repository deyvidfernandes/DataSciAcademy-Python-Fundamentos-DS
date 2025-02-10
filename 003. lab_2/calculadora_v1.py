menu = """******************* Calculadora em Python *******************
   
   Selecione o número da operação desejada:

   (1) - Soma
   (2) - Subtração
   (3) - Multiplicação
   (4) - Divisão

   Digite sua opção: \n"""


def calc(firstNum, secondNum, operation):
   signal, result = "", 0
   
   match operation:
      case 1:
         signal = "+"
         result = firstNum + secondNum
      case 2:
         signal = "-"
         result = firstNum - secondNum
      case 3:
         signal = "*"
         result = firstNum * secondNum
      case 4:
         signal = "/"
         result = firstNum / secondNum
   
   return f"{firstNum} {signal} {secondNum} = {result}"
      

while True:
   print(menu)
   option = input()
   
   firstNum = input("\nDigite o 1° número: ")
   secondNum = input("Digite o 2° número: ")
   operation = calc(int(firstNum), int(secondNum), int(option))

   print ("\nResolução:" + operation)
   print ("\nNovo cálculo? (s/n)\n")
   if input() == "n":
      break






