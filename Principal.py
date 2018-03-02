                                ############ Função de entrada #############
    #ADICIONAR ENTRADA COMO FUNÇÂO DE X
    #Pedir as dimensões do plano a ser modulado

#funcao = input('Digite sua função com variável x, usando '**' como expoente e '*' como multiplicação: ')
#comprimento = int(input('Digite o comprimento do seu plano a ser modulado: '))
#largura = int(input('Digite a largura do seu plano a ser modulado: '))
#dobras = int(input('Digite a quantidade de desdobramentos a ser computado: '))
  ## ADICIONAR CONDIÇÕES COMO A FUNÇÃO TER VARIÁVEL X E O COMPRIMENTO E A LARGURA SEREM INTEIROS ##

dobras = 3
#####################################
                                #  aqui diz que se a quantidade de dobras for ímpar
                                #  será feitos "N" nobras em y e "N-1" dobras em x


if dobras % 2 !=0:
    dobra_y = dobras
    x = 0
    fim = 10*dobra_y
    coord_y = []
    coord_x = []

    desdobras = 0
    while desdobras <= dobras:
        desdobras += 1

    ############### essa parte se dedica a pegar os valores num intervalo 'x' e aplica na função y ###############
        while x <= fim :

            x += 1
            coordenada_x=coord_x.append(x)
            y = -x ** 1.76 + 2 * x * 2 - 10  #### Adicionar a função aqui como sendo y = - funcao    #####

            coordenada_y=coord_y.append(y)

#################### Essa parte se dedica a salvar num arquivo os pontos x ##########################

            arquivo_coord = open('coordenadas_x.txt', 'a', encoding='utf8')
            arquivo_coord.write(str(x) + '\n')
            arquivo_coord.close()
            #################### Essa parte se dedica a salvar num arquivo os pontos f(x) ##########################
                                # for y in coord_y:

            arquivo_coord = open('coordenadas_y.txt', 'a', encoding='utf8')
            arquivo_coord.write(str(y) + '\n')

            arquivo_coord.close()



