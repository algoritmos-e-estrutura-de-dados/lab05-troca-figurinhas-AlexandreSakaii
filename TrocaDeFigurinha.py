def trocaFigurinha(figurinhaMaria, figurinhaJoao):

  indice = 0
  qntd = 0

  if len(figurinhaMaria) < len(figurinhaJoao):
    for i in range(len(figurinhaMaria)):
      for j in range(len(figurinhaJoao)):
        if figurinhaMaria[i] == figurinhaJoao[j]:
          indice += 1
    qntd = len(figurinhaMaria) - indice

  elif len(figurinhaJoao) < len(figurinhaMaria):
    for i in range(len(figurinhaJoao)):
      for j in range(len(figurinhaMaria)):
        if figurinhaJoao[i] == figurinhaMaria[j]:
          indice += 1
    qntd = len(figurinhaJoao) - indice

  else:
    for i in range(len(figurinhaMaria)):
      for j in range(len(figurinhaJoao)):
        if figurinhaMaria[i] == figurinhaJoao[j]:
          indice += 1
    qntd = len(figurinhaMaria) - indice

  return qntd