contador = 1
while contador < 21:
       
       print ("Menu_de_opcoes:  1-IMC  2-Hidratação diária  3-Gasto calórico de um exercício  4-Meta diária de exercício 5-Gasto calórico diário  6-Resumo diário ") 
       opção = int(input("O que voce deseja consultar?" )) 

       ##Programa de IMC
       if opção == 1: 
              print("Bem-vindo ao programa de IMC")
              nome=(input('Digite seu nome: '))
              peso=float(input('Digite seu peso, em kg: '))
              altura=float(input('Digite sua altura, em metros: '))
              genero=int(input('Qual seu gênero? 1-Feminino; 2-Masculino'))
              imc= peso / (altura ** 2)
              print(f'O seu índice de massa corporal é de: {imc: .2f}' )
              if imc < 18.5:
                     print('O seu IMC indica que você está abaixo do peso normal')
              elif imc > 18.5 and imc < 24.9:
                     print('O seu IMC indica que você está com o peso ideal')
              elif imc > 24.9 and imc < 29.9:
                     print('O seu IMC indica sobrepeso')
              elif imc > 29.9 and imc < 34.9:
                     print('O seu IMC indica obesidade I')
              elif imc > 34.9 and imc < 39.9:
                     print('O seu IMC indica obesidade II')
              else:
                     print('O seu IMC indica obesidade III')

       ##Programa hidratação diaria 
       elif opção == 2: 
              peso = float(input("Qual o seu peso em kg? ")) 
              qtd_agua= peso * 35
              print('A sua meta diária de água é de: ' , qtd_agua , 'ml')

       ##Programa de gasto calórico de um exercicio
       elif opção == 3: 
              print("escolha qual atividade praticou")
              print("1 = musculação")
              print("2 = futebol")
              print("3 = corrida")
              print("4 = bicicleta")
              print("5 = junp")
              print("6 = muay thay")
              print("7 = funcional")
              print("8 = pilates")
              print("9 =  yoga")
              numero = (int(input("qual ativida praticou?")))
              tempo = (int(input ("quanto tempo praticou a atividade?")))
              if numero == 1:
                     calculo = tempo * 5.8
                     print("gasto calorico de : ", calculo)
              elif numero == 2:
                     ca2 = tempo * 8.5
                     print("gasto caorico de :" , ca2)
              elif numero == 3:
                     ca3 = tempo * 9.2
                     print("gasto caorico de :" , ca3)
              elif numero == 4:
                     ca4 = tempo * 6.0
                     print("gasto caorico de :" , ca4)
              elif numero == 5:
                     ca5 = tempo * 12.0
                     print("gasto caorico de :" , ca5)
              elif numero == 6:
                     ca6 = numero * 14.0
                     print("gasto caorico de :" , ca6)
              elif numero == 7:
                     ca7 = tempo * 8.5
                     print("gasto caorico de :" , ca7)
              elif numero == 8:
                     ca8 = tempo * 4.2
                     print("gasto caorico de :" , ca8)
              elif numero == 9:
                     ca9 = numero * 3.3
                     print("gasto caorico de :" , ca9)
              else:
                     print("escolha uma categoria valida")

       ##meta diaria de exercicio 
       elif opção == 4: 
              objetivo = input("Qual a sua meta atual? (emagrecer / manter / ganhar) ")  
              if objetivo == "emagrecer": 
                     minutos = 45
              elif objetivo == "manter":
                     minutos = 30 
              elif objetivo == "ganhar": 
                     minutos = 25 
              else:
                     print("Opção inválida")
              tempo_diario_de_exercicio = int(input("Quantos minutos de exercício você realizou hoje? ")) 
              meta = minutos - tempo_diario_de_exercicio 
              if tempo_diario_de_exercicio >= minutos: 
                     print("Parabéns, seu tempo de exercício diário é de", tempo_diario_de_exercicio, "minutos hoje, meta atingida!")
              else:
                     print("Você não alcançou a meta diária necessária, realize mais", meta, "minutos hoje")  

       ##Gasto calórico do dia inteiro
       elif opção == 5: 
              sexo = input("Qual o seu sexo? (homem / mulher)" )
              peso = float(input("Qual o seu peso atual em kg "))
              altura = float(input("Qual a sua altura atual em cm")) 
              idade = int(input("Quantos anos voce tem? ")) 
              atvd_fisica = int(input("Quantas vezes por semana voce faz atividade fisica? ")) 
              homem = 66 + (13.7 * peso) + (5 * altura) - (6.8 * idade) 
              mulher = 655 + (9.6 * peso) + (1.8 * altura) - (4.7 * idade) 
              if sexo == "mulher" and atvd_fisica == 0:
                     TMB = mulher * 1.2
                     print("Seu gasto calórico diario é de", TMB, "e voce é sedentário") 
              elif sexo == "homem" and atvd_fisica == 0:
                     TMB = homem * 1.2 
                     print("Seu gasto calorico é de", TMB, "kcal/dia, e voce é sedentario") 
              elif sexo == "mulher" and atvd_fisica >= 1 and atvd_fisica <= 3:
                     TMB = mulher * 1.375 
                     print("Seu gasto calorico é de", TMB, "kcal/dia, e voce é levemente ativo") 
              elif sexo == "homem" and atvd_fisica >= 1 and atvd_fisica <=3:
                     TMB = homem *1.375 
                     print("Seu gasto calorico é de", TMB, "kcal/dia e voce é levemente ativo") 
              elif sexo == mulher and atvd_fisica >= 3 and atvd_fisica <= 5:
                     TMB = mulher * 1.55 
                     print("Seu gasto calorico é de", TMB, "kcal/dia e voce é moderadamente ativo") 
              elif sexo == homem and atvd_fisica >= 3 and atvd_fisica <= 5:
                     TMB = homem * 1.55 
                     print("Seu gasto calorico é de", TMB, "kcal/dia e voce é moderadamente ativo") 
              elif sexo == "mulher" and atvd_fisica >= 6 and atvd_fisica <= 7: 
                     TMB = mulher * 1.725 
                     print("Seu gasto calorico é de", TMB, "kcal/dia e voce é muito ativo") 
              elif sexo == "homem" and atvd_fisica >= 6 and atvd_fisica <= 7: 
                     TMB = homem * 1.725 
                     print("Seu gasto calorico é de", TMB, "kcal/dia e voce é muito ativo") 
              elif sexo == "mulher" and atvd_fisica > 7: 
                     TMB = mulher * 1.9 
                     print("Seu gasto calorico é de ", TMB, "kcal/dia e voce é extremamente ativo") 
              else:
                     TMB = homem * 1.9
                     print("Seu gasto calorico é de ", TMB, "kcal/dia e voce é extremamente ativo")    

       elif opção == 6:
              print("Esse é o seu resumo diário:")


       else: 
              print("Opção inválida") 

       contador = contador + 1 
