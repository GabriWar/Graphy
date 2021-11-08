from graphics import *
pontos=[]
escolha = 0 
def traducaoX(x):
    x+=400
    return x
def traducaoY(y):
    if y >=400:
        y-=400
    else:
        y-=400
        y=(y*-1)
    return y
def criarponto(janela,interativa= 0, nome=0, nome2=0, x=0, y=0,cor=0):
    pontonum=0
    janelaX = int(input("por favor insira o tamanho X da janela\n (valor recomendado= 800): "))
    janelaY = int(input("por favor insira o tamanho Y da janela\n (valor recomendado= 800): "))
    janela = str(janela)
    janela=GraphWin(janela, janelaX,janelaY)
    if interativa:
        escolha = int(input("deseja separar a janela em quadrantes?\n 1= sim 0= nao: "))
        if escolha == 1:
            Line(Point(round(janelaX/2),0), Point(round(janelaX/2),janelaY)).draw(janela)
            Line(Point(0,round(janelaY/2)), Point(janelaX,round(janelaY/2))).draw(janela)
        while True:
            pontonum +=1
            cordX= traducaoX(int(input("insira a codenada X do ponto {0}: ".format(pontonum))))
            cordY= traducaoY(int(input("insira a codenada Y do ponto {0}: ".format(pontonum))))
            tamanho= int(input("insira o tamanho do ponto: {0} (recomendado=3): ".format(pontonum)))
            cor= input("insira a cor do ponto {0} (ex:red,blue):  ".format(pontonum))
            Point(cordX,cordY).draw(janela)
            Circle((Point(cordX, cordY)), tamanho).draw(janela).setFill(cor)
            pontos.append([int(pontonum),int(cordX),int(cordY)])
            if pontonum >= 2 and 1 == int(input("deseja separar desenhar uma linha entre 2 pontos? \n 1= sim 0= nao: ")):
                print("lista de pontos")
                for each in pontos:
                    print('')
                    trick =0
                    for each2 in each:
                        if trick==0:
                            utilizar="  P"
                        if trick==1:
                            utilizar="  X"
                        if trick==2:
                            utilizar="  Y"
                        print(utilizar,each2,end="")
                        trick+=1
                pontoutilizado = int(input("\nqual ponto deseja usar como primeiro ponto da linha?: "))
                pontoutilizado2 = int(input("\nqual ponto deseja usar como segundo ponto da linha?: "))
                pontoutilizado -=1
                pontoutilizado2-=1
                Line(Point(pontos[pontoutilizado][1],pontos[pontoutilizado][2]), Point(pontos[pontoutilizado2][1],pontos[pontoutilizado2][2])).draw(janela)
criarponto(janela=1,interativa=1)
input()
