import os
import shutil

nome = input("Digite o nome do funcionário: ")
pasta_backup = 'C:/Backup' + nome
os.mkdir(pasta_backup)

desktop = input("Digite o caminho do Desktop:")
downs = input("Digite o caminho dos Downloads: ")
#docs = input("Digite o caminho dos Documentos: ")
imgs = input("Digite o caminho das Imagens: ")



copiaDesktop = pasta_backup + '/Área de Trabalho'
shutil.copytree(src=desktop, dst=copiaDesktop)

copiaDowns = pasta_backup + '/Downloads'
shutil.copytree(src=downs, dst=copiaDowns)


copiaImgs = pasta_backup + '/Imagens'
shutil.copytree(src=imgs, dst=copiaImgs)




#shutil.copytree(src=imgs, dst=pasta_backup)    
      