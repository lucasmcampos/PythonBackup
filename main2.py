import backup2 as bkp

# posição 0 = pasta windows 
# posição 1 = pasta destino bakcup

folders = \
[
    ['Documents', 'Documentos'],
    ['Downloads', 'Downloads'],
    ['Pictures', 'Imagens'],
    ['Desktop', 'Área de Trabalho']
]

#loop em cada item da tupla folders
for folder in folders:
    bkp.backup_folder(folder[0], folder[1])
    print("\n Backup "+folder[0]+" finalizado")


print("Backup Finalizado")
