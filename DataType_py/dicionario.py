dicionario = {}
fatec = {}
fatec['casemiro'] = ['DW3', 'ALUNO']
fatec['orlando'] = ['DW2', 'DW3','PROFESSOR']
fatec['nilton'] = 'ALGORITIMO'
fatec['thiago'] = ('BANCO NoSQL', "COORDENAÇÃO")


print(fatec)
print(fatec.keys())
for key in fatec.keys():
    print(fatec[key])