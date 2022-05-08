# -*- coding: utf-8 -*-
# Python3 program for demonstrating
# coroutine execution
import asyncio, time

# Files to read and write 
arq_leitura = open("leitura_nomes.txt", "r")
arq_escrita = open("escrita_nomes.txt", "w")

#-------------------------------------------------------------------------------------------        
# READ NAMES IN FILE 
def ler_nome(arq_leitura):
    nome = arq_leitura.readline()
    print(nome, end="")
    return nome
#------------------------------------------------------------------------------------------- 

#-------------------------------------------------------------------------------------------        
# WRITE NAMES IN EMPTY FILE
async def escrever_nome(arq_escrita):
    flag = True
    while flag:
        nome = ler_nome(arq_leitura)
        if nome:
            arq_escrita.write(nome)
        else:
            flag=False
#-------------------------------------------------------------------------------------------        

async def main():
    print("Coroutines using Python")

    print(f"Start execution at : {time.strftime('%X')}")

    task = asyncio.create_task(escrever_nome(arq_escrita))
    await task

    print(f"Execution finished at : {time.strftime('%X')}")
    
if __name__ == "__main__":
    asyncio.run(main())