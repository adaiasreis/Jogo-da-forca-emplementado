#Jogo da forca emplementado
import random
import os
import time

def cabecalho():
  os.system('clear')
  print("-="*20)
  print("\t***** BEM VINDO *****")
  print("-="*20)
  print()
  print(" \/\/\/\/ JOGO DA FORCA \/\/\/\/")
  print()
  print("*-"*20)
  print()

def menu():
  cabecalho()
  while(True):
    print("[1]-Nova Partida\n[2]-Ver Pontuação\n[3]-Sair")
    opcao = int(input("\nO que você deseja fazer? "))
    if opcao == 1:
      start()
    elif opcao == 2:
      verPontuacao(jogador, pontos)
    elif opcao == 3:
      sair()
      break
    else:
      print("\nEntrada Inválida, tente novamente.")
      time.sleep(3)
    return(menu)

def painel(palavra_resposta):
  print("\nQual é a palavra?")
  print("A palavra tem",len(palavra_resposta),"letras.")
  #print("Letras acertadas: ",p_certas)
  print("Letras digitadas:")
  print(letras_digitadas)
  print("\n")
  print(palavra_resposta)
  print("\n")

def msgDerrota():
  global jogador
  print("\n\tA palavra era: ",palavra_secreta)
  print("\n\nQue pena, você perdeu! Mas, não desanime, você pode tentar novamente.")
  jogador = input("\nDigite o seu nome: ")

def palavraSecreta():

  lista_palavras = ["computador","instrumento", "desencadeamento","estatuto","triunfo","hospede", "escolaridade","simplicidade","metamorfose","ortopedista","circulo","matrimonio","colateral","implante","verme","escala","farmaceutico","institucionalidade","implementar","pediatria","concordancia","programar","inovar","carne","polir","pedir","insistir","investir","imprimir","cumprimento","intervir","curtir","traumatico","impostor","incidente","invejoso","hospede","primeiro","milionario","helicoptero","helice","sismico","homenagem","entretenimento","felicidade","tipo","hino","vaga","tema","cova","linha","pena","dado","dente","tio","tulipa","rosa","casa","andorinha"]
    
  index = random.randint(0, len(lista_palavras) - 1)
    
  return lista_palavras[index]

def geraPalavraResposta(palavra):

  resposta = []
  for i in range(0, len(palavra)):
    resposta.append('_')

  return resposta

def verificaLetra(palavra, letra):

  acertos = []
 
  for i in range(0, len(palavra)): 
    if palavra[i] == letra:
      acertos.append(i)

  return acertos

def verificaVitoria(p_resposta):
  while(True):
    for i in range(0, len(p_resposta)):
      if p_resposta[i] == "_":
        return False
    print("\nParabéns, você jagou a jogada!")
    time.sleep(3)
    return True

def insereLetra(p_secreta, p_resposta, acertos):
  for i in range(0, len(acertos)):
    index = acertos[i]
    p_resposta[index] = p_secreta[index]

  return p_resposta

def verPontuacao(jogador, pontos):
  os.system('clear')
  print("\n\t\t *** PARABENS!!! ***\n")
  print(jogador,", você obteve",tPontos, "pontos.\n\nVocê foi muito bem!!!")
  time.sleep(5)

def contarLetrasCertas(resposta): #Não encontrei onde usar para contar corretamente ou a função está errado!
  global p_certas

  p_certas = 0

  for i in range(0, len(resposta)):
    if resposta[i] != "_":
      
      p_certas += 1
      
    return p_certas

def chutarPalavra(p_certas, palavra_secreta): #Por não ter conseguido implementar a função anterior, essa também não teve como.

  if (p_certas) >= len(palavra_secreta) // 2:
    print("\nJá sabe a palavra? Deseja chutar valendo 15 pontos?")
    chute = input("[S]-Sim [N]-Não: ")
    if chute == 's':
      palavra_secreta = palavra_resposta
      pontos + 15
      jogar()
    else:
      pontos - 5
    return menu()

def sair():
  os.system('clear')
  print("\nJogo encerrado. Volte sempre!")
  print("")
  time.sleep(3)

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

vida = 5
palavra_secreta = ""
palavra_resposta = ""
letras_digitadas = []
jogador = ""
pontos = 0
jogada = 1
acertos = ""
p_certas = 0
tPontos = 0

def start():

  global palavra_secreta, palavra_resposta, jogada, pontos, letras_digitadas, vida, pontos

  vida = 5
  pontos = 0
  letras_digitadas = []
  palavra_secreta = palavraSecreta()
  palavra_resposta = geraPalavraResposta(palavra_secreta)

  while(True):

    os.system('clear')
    print("Jogada ",jogada)
    print("Chances restantes: ",vida)
    print("Pontos: ",pontos)

    painel(palavra_resposta)
    
    jogar()

    if verificaVitoria(palavra_resposta) == True:
      jogada += 1
      start()
    elif vida == 0:
      msgDerrota()
      break


def jogar():
    
  global vida, palavra_resposta, p_secreta, p_resposta, acertos, pontos, tPontos, letras_digitadas, p_certas, vida
    
  letra = input("Digite uma letra: ")

  if letra in letras_digitadas:
    print("\nLetra já digitada, tente outra!")
    time.sleep(3)

  elif len(letra) == 1:
    letras_digitadas.append(letra)
    acertos = verificaLetra(palavra_secreta, letra)

    pontos += (5 * len(acertos))
  
    if len(acertos) == 0:  
      print("\n****** Letra não encontrada! ****** ")
      time.sleep(2)
      vida -= 1
    else:
      palavra_resposta = insereLetra(palavra_secreta, palavra_resposta, acertos)
      tPontos += pontos  

  else:
    print("\n****** ENTRADA INVÁLIDA! ****** ")
    time.sleep(3)

menu()