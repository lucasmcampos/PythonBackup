import os
import shutil
import time
from tqdm import tqdm


nome = input("Digite o nome do funcionário: ")
pasta_backup = 'C:/Backup' + nome
os.mkdir(pasta_backup)



desktop = input("Digite o caminho do Desktop:")
downs = input("Digite o caminho dos Downloads: ")
docs = input("Digite o caminho dos Documentos: ")
imgs = input("Digite o caminho das Imagens: ")




copiaDesktop = pasta_backup + '/Área de Trabalho'
shutil.copytree(src=desktop, dst=copiaDesktop)

copiaDowns = pasta_backup + '/Downloads'
shutil.copytree(src=downs, dst=copiaDowns)

copiaDocs = pasta_backup + '/Documentos'
shutil.copytree(src=docs, dst=copiaDocs)

copiaImgs = pasta_backup + '/Imagens'
shutil.copytree(src=imgs, dst=copiaImgs)

 
print("FINALIZADO!")

   
      