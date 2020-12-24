import time
import os
def letreiro():
    esp = 50
    time.sleep(0.07)
    print(" "*esp,end='')
    print("███████╗███████╗██╗     ██╗███████╗    ███╗   ██╗ █████╗ ████████╗ █████╗ ██╗     ")
    time.sleep(0.07)
    print(" "*esp,end='')
    print("██╔════╝██╔════╝██║     ██║╚══███╔╝    ████╗  ██║██╔══██╗╚══██╔══╝██╔══██╗██║     ")
    time.sleep(0.07)
    print(" "*esp,end='')
    print("█████╗  █████╗  ██║     ██║  ███╔╝     ██╔██╗ ██║███████║   ██║   ███████║██║     ")
    time.sleep(0.07)
    print(" "*esp,end='')
    print("██╔══╝  ██╔══╝  ██║     ██║ ███╔╝      ██║╚██╗██║██╔══██║   ██║   ██╔══██║██║     ")
    time.sleep(0.07)
    print(" "*esp,end='')
    print("██║     ███████╗███████╗██║███████╗    ██║ ╚████║██║  ██║   ██║   ██║  ██║███████╗")
    time.sleep(0.07)
    print(" "*esp,end='')
    print("╚═╝     ╚══════╝╚══════╝╚═╝╚══════╝    ╚═╝  ╚═══╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚══════╝")
def arvore():
    os.system("clear")
    tamanho = 20
    k = 1
    esp = 65 
    decremento = tamanho-1
    for i in range(tamanho):
        print(" "*esp,end='')
        print(" "*decremento,end='')
        for l in range(k):
            time.sleep(0.005)
            print("* ",end='')
        print('')
        decremento-=1
        k+=1
    tamanho_pezim = tamanho-6
    for m in range(tamanho_pezim-7):
        print(" "*esp,end='')
        print(" "*12, end='')
        for x in range(tamanho_pezim):
            time.sleep(0.005)
            print("*",end='')
        print('')
for n in range(10):
    arvore()
    letreiro()
    time.sleep(0.5)

