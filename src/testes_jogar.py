import jogovelha
import sys

erro = False
lin = 1
col = 1
jogador = 'X'

jogovelha.inicializar()
jogovelha.jogar(jogador, lin, col)
jogo = jogovelha.tabuleiro()

if len(jogo) != 3:
  erro = True
else:
  for linha in range(0,3):
    if len(jogo[linha]) != 3:
      erro = True
     else:
        for coluna in range(0,3):
          if linha == lin and coluna == col:
            if jogo[linha][coluna] != jogador:
              erro = True
            elif jogo[linha][coluna] != '.':
                erro = True
if erro:
  print('Erro!')
  sys.exit(1)
else:
  sys.exit(0)
