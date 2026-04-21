#Programa IMC
repetir='1'

while repetir == '1': 
  print('Seja bem-vindo ao menu de opções. \n1-IMC \n2-Hidratação diária \n3-Gasto calórico \n4-Meta diária de exercício \n5-Gasto calórico no dia \n6-Resumo diário' )
  opcao= int(input('O que você deseja consultar? '))

  if opcao == 1:
    peso=float(input('Digite seu peso, em kg: '))
    altura=float(input('Digite sua altura, em metros (exemplo : 1.55) '))
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
    print('Atividades físicas \n1-Musculação \n2-Futebol \n3-Corrida \n4-Bicicleta \n5-Jump \n6-Muay Thay \n7-Funcional \n8-Pilates \n9-Yoga')
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
      objetivo = input('Qual a sua meta atual? \n1-Emagrecer \n2-Manter \n3-Ganhar ')
      if objetivo == '1':
        minutos = 45
      elif objetivo == '2':
        minutos = 30
      elif objetivo == '3':
        minutos = 25
      else:
        print('Opção inválida')
        minutos=0
      tempo_diario_de_exercicio = int(input("Quantos minutos de exercício você realizou hoje? "))
      meta = minutos - tempo_diario_de_exercicio
      if tempo_diario_de_exercicio >= minutos:
        print("A meta para alcançar o seu objetivo é de", minutos, "minutos. Parabéns seu tempo de exercício diário foi de", tempo_diario_de_exercicio, "minutos hoje, meta atingida!")
      else:
        print("Seu tempo para alcançar o seu objetivo deve ser de", minutos, "minutos, você não alcançou a meta diária necessária, realize mais", meta , "minutos hoje")

  elif opcao == 5:
        #Programa gasto calórico total 
      genero = input("Qual o seu gênero? \n1-Masculino \n2-Feminino" )
      peso = float(input("Digite seu peso atual, em kg: "))
      altura = float(input("Digite a sua altura atual, em cm(exemplo : 155): ")) 
      idade = int(input("Digite sua idade, em anos: ")) 
      atividade_fisica = int(input("Quantas vezes por semana voce faz atividade fisica? ")) 
      if genero == "1":
        TMB = 66 + (13.7 * peso) + (5 * altura) - (6.8 * idade) 
      if genero == "2":
        TMB = 655 + (9.6 * peso) + (1.8 * altura) - (4.7 * idade) 
      if atividade_fisica <1:
        TMB = TMB * 1.2
        print(f"Seu gasto calórico é de {TMB:.2f} kcal/dia e você é sedentário")
      elif atividade_fisica  >= 1 and atividade_fisica <= 3: 
        TMB = TMB * 1.375
        print(f"Seu gasto calórico é de {TMB:.2f} kcal/dia e você é levemente ativo")
      elif atividade_fisica > 3 and atividade_fisica <= 5:
        TMB = TMB * 1.55 
        print(f"Seu gasto calórico é de {TMB:.2f} kcal/dia e você é moderadamente ativo")
      elif atividade_fisica >= 6 and atividade_fisica <= 7:
        TMB = TMB * 1.725
        print(f"Seu gasto calórico é de {TMB:.2f} kcal/dia e você é muito ativo")
      else:
        TMB = TMB * 1.9
        print(f"Seu gasto calórico é de {TMB:.2f} kcal/dia e você é extremamente ativo")
              
      deficit_calorico = input("Deseja calcular seu consumo calórico para emagrecer? \n1-Sim \n2-Não ") 
      if deficit_calorico == "2": 
        print("Siga para o próximo programa") 
      else: 
          deficit = input("Qual ritmo de emagrecimento vocë deseja? \n1-Leve \n2-Moderado \n3-Intenso ") 
          if deficit == "1":
            deficit = 200
            consumo = TMB - deficit 
            perda = (deficit*7) / 7700
            print(f"Seu consumo diário para emagrecer deve ser de {consumo:.2f} kcal e você deverá perder {perda:.3f} kg/semana")
          elif deficit == "2":
            deficit = 400  
            consumo = TMB - deficit 
            perda = (deficit*7) / 7700
            print(f"Seu consumo diário para emagrecer deve ser de {consumo:.2f} kcal e você deverá perder {perda:.3f} kg/semana")
          elif deficit == "3": 
            deficit = 700  
            consumo = TMB - deficit 
            perda = (deficit*7) / 7700
            print(f"Seu consumo diário para emagrecer deve ser de {consumo:.2f} kcal e você deverá perder {perda:.3f} kg/semana")
          else:
            print("Opção inválida") 

  elif opcao == 6:
    #Programa resumo
    peso=float(input('Digite seu peso, em kg: '))
    altura=float(input('Digite sua altura, em metros'))
    idade=int(input("Digite a sua idade" ))
    imc= peso / (altura ** 2)
    meta_agua= peso * 35
    tempo= int(input('Quantos minutos você treinou hoje? '))
    gasto_calorico= tempo * 8
    genero = input("Qual o seu gênero? \n1-Masculino \n2-Feminino" )
    atividade_fisica = int(input("Quantas vezes por semana voce faz atividade fisica? "))
    objetivo=input('Qual seu objetivo? \n1-Emagrecer \n2-Manter \n3-Ganhar: ')
    if objetivo == "1":
      minutos=45
    elif objetivo == "2":
      minutos=30
    elif objetivo == "3":
      minutos=25
    else:
      print('Selecione uma opção disponível.')
      minutos=0
    if tempo >= minutos:
      status='meta diária atingida'
    else:
      status='meta diária não atingida'
    if genero == "1":
        TMB = 66 + (13.7 * peso) + (5 * altura) - (6.8 * idade) 
    elif genero == "2":
        TMB = 655 + (9.6 * peso) + (1.8 * altura) - (4.7 * idade) 
    else:
        print("Selecione uma opção válida") 
    if atividade_fisica <1:
        TMB = TMB * 1.2
    elif atividade_fisica  >= 1 and atividade_fisica <= 3: 
        TMB = TMB * 1.375
    elif atividade_fisica > 3 and atividade_fisica <= 5:
        TMB = TMB * 1.55 
    elif atividade_fisica >= 6 and atividade_fisica <= 7:
        TMB = TMB * 1.725
    else:
        TMB = TMB * 1.9
    deficit_calorico = input("Deseja calcular seu consumo calórico para emagrecer? \n1-Sim \n2-Não ")  
    if deficit_calorico == "sim": 
        deficit = input("Qual ritmo de emagrecimento vocë deseja? \n1-Leve \n2-Moderado \n3-Intenso ") 
        if deficit == "1":
            deficit = 200
            consumo = TMB - deficit 
            perda = (deficit*7) / 7700
        elif deficit == "2":
            deficit = 400  
            consumo = TMB - deficit 
            perda = (deficit*7) / 7700
        elif deficit == "3": 
            deficit = 700  
            consumo = TMB - deficit 
            perda = (deficit*7) / 7700
        else:
            print("Opção inválida") 
    
    print('Resultados')
    print(f'O seu IMC é de: {imc:.2f}')
    print(f'A sua meta diária de água é de {meta_agua} ml')
    print(f'A meta diária de exercício é de {minutos} minutos')
    print(f'Hoje: {status}')
    print(f'Seu gasto calórico no treino de hoje foi de {gasto_calorico} calorias') 
    print(f"Seu gasto calórico total é de {TMB:.2f} kcal/dia")
    print(f"Seu consumo diário de kcal é de {consumo:.2f}")
    print(f"Você deve perder {perda:.3f} kg/dia para emagrecer") 
    
  else:
    print('Escolha uma opção válida')

  repetir=input('Deseja continuar novamente? \n1-Sim \n2-Não ')

else:
    print('Escolha uma opção válida')
       contador = contador + 1 
