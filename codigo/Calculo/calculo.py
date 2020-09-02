from math import sqrt

''' Função que calcula a distância entre dois pontos
    Entrada: pontoA = (x, y) coordenasdas x e y do ponto A 
             pontoB = (x, y) coordenasdas x e y do ponto A 
    Saida: distancia = distância entre os pontos A e B'''
def distanciaPontos(pontoA, pontoB):
    distancia = sqrt((pontoB[0] - pontoA[0]) ** 2 + (pontoB[1] - pontoA[1]) ** 2)
    return distancia