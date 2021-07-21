from Arvore import Arvore_Binaria
from Tabela_Hash import hash

#Etapa 1
#pegando os caracteres
arq = open('caracteres.txt', 'r')
caracter = arq.readline()
chave = []
for i in caracter:
    chave.append(i)
arq.close()
#criando a tabela hash
arq = open('chave.txt', 'w')
tab_hash = hash(32)
for i in range(len(chave)):
    tab_hash.inserir(ord(chave[i]))
#guardando a tabela
arq.writelines(tab_hash.guardar())
arq.close()

#Etapa 2
#lendo a senha
arq = open('senha.txt', 'r')
senha = arq.readline()
sen = []
for i in range(len(senha)):
    sen.append(senha[i])
arq.close()
#codificando a senha
arq = open('chave.txt', 'r')
cha = arq.readlines()
cod = ''
i = 0
k = 0
while True:
    if cha[i][0] == sen[k]:
        for j in range(5):
            cod += cha[i][j+3]
        k += 1
    i += 1
    if i == 32:
        i = 0
    if k == len(sen):
        break
arq.close()
#guardando senha codificada
arq = open('senhacodificada.txt', 'w')
arq.writelines(cod)
arq.close()

#Etapa 3
#criando a arvore do arquivo chave
arq = open('chave.txt', 'r')
chave = arq.readlines()
arvore_chave = Arvore_Binaria('0')
for i in chave:
    bino = []
    posi = ''
    for k in range(5):
        if len(bino) < 4:
            bino.append(i[k+3])
        else:
            bino.append(i[0])
            posi = i[k+3]
    arvore_chave.inserir(bino, arvore_chave.raiz, posi)
arq.close()
#guardando a pre-ordem da arvore
pre_ord = ''
for i in arvore_chave.pre_ord([], arvore_chave.raiz):
    pre_ord += i
arq = open('preordem.txt', 'w')
arq.writelines(pre_ord)
arq.close()

#Etapa 4
#criando a tabela hash a partir da pre-ordem
arq = open('preordem.txt', 'r')
preordem = arq.readline()
arvore_preord = Arvore_Binaria('0')
pre = '0000'
aux = ''
for i in range(len(preordem)):
    if (preordem[i] != '0') and (preordem[i] != '1'):
        if (preordem[i-1] != '0') and (preordem[i-1] != '1'):
            pre += preordem[i]
            arvore_preord.inserir(pre, arvore_preord.raiz, '1')
            ponte = pre.replace(pre[-1], '')
            pre = ponte
        elif (preordem[i-1] == '0') or (preordem[i-1] == '1'):
            pre += preordem[i]
            arvore_preord.inserir(pre, arvore_preord.raiz, '0')
            ponte = pre.replace(pre[-1], '')
            pre = ponte
    elif ((preordem[i] == '0') or (preordem[i] == '1')) and (i >= 5):
        aux += preordem[i]
        if (preordem[i+1] != '0') and (preordem[i+1] != '1'):
            ponte_2 = ''
            for k in range(len(pre)):
                if (len(aux)) + k == 4:
                    ponte_2 += aux
                elif (len(aux)) + k < 4:
                    ponte_2 += pre[k]
            pre = ponte_2
            aux = ''
arq.close()
#decodificando a senha apartir da arvore da preordem
arq = open('senhacodificada.txt', 'r')
senha_cod = arq.readline()
senha_decod = ''
ordem = ''
for i in senha_cod:
    ordem += i
    if len(ordem) == 5:
        senha_decod += arvore_preord.busca(ordem, arvore_preord.raiz)
        ordem = ''


print('Caracteres:')
print(caracter)
print()
print('Tabela Hash:')
print(tab_hash.guardar())
print()
print('Senha:')
print(senha)
print()
print('Senha Codificada:')
print(cod)
print()
print('Arvore da Tabela Hash:')
arvore_chave.Display()
print()
print('Pre-Ordem da Arvore:')
print(pre_ord)
print()
print('Arvore da Pre-Ordem:')
arvore_preord.Display()
print()
print('Senha Decodificada:')
print(senha_decod)
print()