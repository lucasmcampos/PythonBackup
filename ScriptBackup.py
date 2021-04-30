import os
import shutil

print("************************************************")
print("*******SCRPIT DE BACKUP MANUAL COM PYTHON*******")
print("* [Autor:] Lucas Martins                       *")
print("* [Versão:] 0.2                                *")
print("* [Status:] Em desenvolvimento                 *")
print("************************************************")

input("Press Enter to continue...")


nome = input("Digite o nome do funcionário: ")
pasta_backup = 'C:/Backup' + nome

#Função para Criar a pasta do Backup e mostrar a onde ela está.
def inicio ():
    os.mkdir(pasta_backup)
    return print("PASTA CRIADA: " + pasta_backup)   

#Função de copiar os diretórios para pasta do Backup.
def criacaoPastas():
    
    desktop = input("Digite o caminho do Desktop:")
    copiaDesktop = pasta_backup + '/Área de Trabalho'
    shutil.copytree(src=desktop, dst=copiaDesktop)
    
    downs = input("Digite o caminho dos Downloads: ")
    copiaDowns = pasta_backup + '/Downloads'
    shutil.copytree(src=downs, dst=copiaDowns)
        
    docs = input("Digite o caminho dos Documentos: ")
    copiaDocs = pasta_backup + '/Documentos'
    shutil.copytree(src=docs, dst=copiaDocs)
        
    imgs = input("Digite o caminho das Imagens: ")
    copiaImgs = pasta_backup + '/Imagens'
    shutil.copytree(src=imgs, dst=copiaImgs)

    return print("FINALIZADO!")

#Execução das funções
inicio() 
criacaoPastas()
   
      