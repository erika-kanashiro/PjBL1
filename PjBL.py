#Programa IMC
repetir='1'

while repetir == '1': 
  print('Seja bem-vindo ao menu de opções. 1-IMC  2-Hidratação diária  3-Gasto calórico  4-Meta diária de exercício  5-Resumo diário')
  opcao= int(input('O que você deseja consultar? '))

  if opcao == 1:
    peso=float(input('Digite seu peso, em kg: '))
    altura=float(input('Digite sua altura, em metros: '))
    imc= peso / (altura ** 2)
    print(f'O seu índice de massa corporal é de: {imc: .2f}' )
    if imc < 18.5:
      print('O seu IMC indica que você está abaixo do peso normal')
    elif imc >= 18.5 and imc <= 24.9:
      print('O seu IMC indica que você está com o peso ideal')
    elif imc >= 24.9 and imc <= 29.9:
      print('O seu IMC indica sobrepeso')
    elif imc >= 29.9 and imc <= 34.9:
      print('O seu IMC indica obesidade I')
    elif imc >= 34.9 and imc <= 39.9:
      print('O seu IMC indica obesidade II')
    else:
      print('O seu IMC indica obesidade III')

  elif opcao == 2:
  #Programa quantidade de água
    peso=float(input('Digite seu peso, em kg: '))
    qtd_agua= peso * 35
    print('A sua meta diária de água é de: ' , qtd_agua , 'ml')

  elif opcao == 3:
    #Programa gasto calórico
    print(' 1-Musculação 2-Futebol 3-Corrida 4-Bicicleta 5-Jump 6-Muay Thay 7-Funcional 8-Pilates 9-Yoga')
    numero=int(input('Selecione a atividade praticada: '))
    tempo=int(input ('Por quanto tempo, em minutos, você costuma pratica-lá?'))
    if numero == 1:
      calculo = tempo * 5.8
      print('Seu gasto calórico é de: ', calculo, 'calorias')
    elif numero == 2:
      calculo = tempo * 8.5
      print('Seu gasto calórico é de:' , calculo ,'calorias')
    elif numero == 3:
      calculo = tempo * 9.2
      print('Seu gasto calórico é de:' , calculo , 'calorias')
    elif numero == 4:
      calculo = tempo * 6.0
      print('Seu gasto calórico é de: ' , calculo , 'calorias')
    elif numero == 5:
      calculo = tempo * 12.0
      print('Seu gasto calórico é de:' , calculo , 'calorias')
    elif numero == 6:
      calculo = tempo * 14.0
      print('Seu gasto calórico é de:' , calculo ,'calorias')
    elif numero == 7:
      calculo = tempo * 8.5
      print('Seu gasto calórico é de:' , calculo , 'calorias')
    elif numero == 8:
      calculo = tempo * 4.2
      print('Seu gasto calórico é de:' , calculo , 'calorias')
    elif numero == 9:
      calculo = tempo * 3.3
      print('Seu gasto calórico é de:' , calculo , 'calorias')
    else:
      print('Escolha uma categoria valida')

  elif opcao == 4:
      #Programa meta de exercício diário
      objetivo = input('Qual a sua meta atual? (emagrecer / manter / ganhar) ')
      if objetivo == 'emagrecer':
        minutos = 45
      elif objetivo == 'manter':
        minutos = 30
      elif objetivo == 'ganhar':
        minutos = 25
      else:
        print('Opção inválida')
        minutos=0
      tempo_diario_de_exercicio = int(input("Quantos minutos de exercício você realizou hoje? "))
      meta = minutos - tempo_diario_de_exercicio
      if tempo_diario_de_exercicio >= minutos:
        print("Parabéns, seu tempo de exercício diário é de", tempo_diario_de_exercicio, "minutos hoje, meta atingida!")
      else:
        print("Você não alcançou a meta diária necessária, realize mais", meta , "minutos hoje")

  elif opcao == 5:
    #Programa resumo
    peso=float(input('Digite seu peso, em kg: '))
    altura=float(input('Digite sua altura, em metros'))
    imc= peso / (altura ** 2)
    meta_agua= peso * 35
    tempo= int(input('Quantos minutos você treinou hoje? '))
    gasto_calorico= tempo * 8
    objetivo=input('Qual seu objetivo? (emagrecer/ manter / ganhar): ')
    if objetivo == "emagrecer":
      minutos=45
    elif objetivo == "manter":
      minutos=30
    elif objetivo == "ganhar":
      minutos=25
    else:
      print('Selecione uma opção disponível.')
      minutos=0
    if tempo >= minutos:
      status='meta diária atingida'
    else:
      status='meta diária não atingida'
    print('Resultados')
    print(f'O seu IMC é de: {imc:.2f}')
    print(f'A sua meta diária de água é de {meta_agua} ml')
    print(f'A meta diária de exercício é de {minutos} minutos')
    print(f'Hoje: {status}')
    print(f'Seu gasto calórico é de {gasto_calorico} calorias') 


  else:
    print('Escolha uma opção válida')

  repetir=input('Deseja continuar novamente? 1-Sim / 2-Não ')

       contador = contador + 1 
