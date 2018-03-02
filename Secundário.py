#from Principal import *
from random import *
import math
import operator


tamanho = 20


coord = open('coordenadas_y.txt', 'r', encoding='utf8')

            ####################### transforma o arquivo de texto em lista de string ###############
lista_string = [linha.strip() for linha in coord]

    ######################### transforma a lista de string em uma lista de inteiros #############

lista_int =[float(elem) for elem in lista_string]
    ############################# desloca a funçao em 'x' tamanhos #####################
deslocador = []

for item in lista_int:
    deslocador = item*(-1) + tamanho
            ###################### Salva a função desloc                                            ada num arquivo de texto #################
    new_coord = open('coordenadas_y.txt', 'a', encoding='utf8')
    new_coord.writelines(str(deslocador) + ' ' +  'aaslkdj' + '\n')
    new_coord.close()
    coord.close()
    print(deslocador)
