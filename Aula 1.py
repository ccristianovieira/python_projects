'BASICS (USAR SPYDER QUE FUNCIONA INPUT)'

#Tipos de variáveis type()
ALGO = 'ALGUMACOISA'
x = 1
y = 1.32
m = 'Boa tarde'
n = "Boa tarde"

#%%
#Tipo lógica (Boolean)

w = True
y = False

z = ''
Z = 0
#bool(z), bool(m), bool(Z)



B = x>y
B = x<y
#%%
#Calculadora 

X = (x + 2*y)**x-y
#%%
#Exibir texto em console

print(x,'\n','\nx',y-x)
print(type(x),type(y))

#%%
#Entrada de dados com input
i = input()
I = input('Escreva um valor:\n')
V = float(input('Inserir número:'))
#Erros no input desta versão no Spyder (5.1.5) a 5.3.5 já arrumou
#%%
'Estruturas de Decisão'

nota = float(input('Quanto você tirou?'))

if nota >= 7:
    print('Aprovado')
    print('Parabéns')
else:
    print('Reprovado')
    
#%% Elif
#==
nota = float(input('Quanto você tirou?'))

if nota <= 4:
    print('Reprovado')
elif nota > 4 and nota <=6:
    print('Exame')
else:
    print('Aprovado')

#%% if com Boolean

if bool(z) == False:
    print('Possui algum texto')
else:
    print('Está vazio')    
    

#%% Loopings

x = 1
while x <= 5:
    print(x)
    x += 1
    #x = x + 1

#%%
usuario = ''
p = 'p'

while(usuario != 's'):
    print('a. Pagar')
    print('b. Receber')         
    print('c. Consultar')
    print('s. sair')
    usuario = input('Digite a opção desejada:')
    if usuario == p:
        break
print('Deslogado')    

#%% Looping for

for i in range(10):
#    print(i)
    print(i+1)
    if i == 4:
        break
print('Fim do looping')    

#%% Looping for com string

palavra = 'Física'
for i in palavra:
    print(i)
    
#%% Looping com lista

lista = [1,4,67,8,5,3,52]

for i in lista:
    print(i)    
    
#%% Listas
import numpy as np

L = [1,2,3,4,6] 
L2 = [1,2,'3',4,'Olá',True]
L3 = [1,[4,3,2,1],4,'a']
L4 = [2,5,9,6,12,43,76,34,8,0,43]

len(L)
np.max(L)
np.argmax(L)
np.argmin(L)
np.mean(L4)
np.var(L4)
np.std(L4)
np.array(L4) #l4.shape()
np.sum(L4)
np.exp(L4)
np.sqrt(L)

#Mostraar slices
L[1:-3]

B = [] #type(B)
for i in range(0,len(L)):
    A = L[i]**2
    B.append(A)

C =[]
I = []    
for i in range(0,len(L4)):
    if L4[i]%2 != 0 and L4[i] != 0:
        I.append(L4[i])

D = []
for i in L:
    D.append(i**2)

#Criar matrizes com numpy com valores iniciais

zeros = np.zeros([4,3])
um = np.ones([5,7])
diagonal = np.eye(5)

#valores aleatórios entre zero e um
ale = np.random.random((5))
print(ale)
print("-------")
#valores aleatórios distr. normal contendo negativos
ale2= np.random.randn((5))
print(ale2)
print("-------")
#valores aleatórios 3 x 4
ale3 = (10*np.random.random((3,4)))
print(ale3)

#gerar inteiros
#ale6 = gnr.integers(10, size=(3, 4))
#print(ale6)

#outra forma de fazer, mesmo resultado
r = np.arange(15).reshape((3, 5))
print(r)
print("-------")
# rearranja um conjunto de 15 elementos 
# mostra a matrizes transposta entre linha e coluna
s = r.transpose((1,0))
print(s)

#expressões lógicas
#usando where
# criando matriz com valores aleatórios positivos e negativos
v = np.random.randn(4, 4)
print(v)
# criando matriz com valores booleanos baseado no array v
x = (v > 0)
print(x)
# criando matriz com valores -1 e 1 baseado nos valores do array x
z = np.where(x > 0, 1, -1)
print(z)

#%% Dicionários

#Chave/Valor

Preços = {'Coca':9.90,'Pipoca P':20.0,'Pipoca M':20.0,'Pipoca G':20.0,'Batom':5.0,'Coca':10.90}
Preços.keys()
Preços.values()
Preços['Coca']

#Loopings com valores do dicionario
for i in Preços.values():
    print(i)
    
#Verificar existência    
print('Pepsi' in Preços)

#Deletar algum item
del Preços['Pipoca P']
print(Preços)    

#Adicionar item no dicionario
Preços['Guaraná'] = 9

#Sets (Conjunto não Ordenado e não repetido) Somente valor

animais = {'Gato','Cachorro','Furao','Cachorro'}

#Verificar existência    
print('Pepsi' in animais)

#Adicionar item no Set
animais.add('Calopsita')

#Tuplas (Listas q n podem ser alteradas)
t = (1,3,5,7,9,10)

#%%Criar valores aleatorios

#valores aleatórios entre zero e um
ale = np.random.random((5))
print(ale)
print("-------")
#valores aleatórios distr. normal contendo negativos
ale2= np.random.randn((5))
print(ale2)
print("-------")
#valores aleatórios 3 x 4
ale3 = (10*np.random.random((3,4)))
print(ale3)

#%%
#unique remove repetições
j = np.array([11, 12, 13, 14, 15, 16, 17, 12, 13, 11, 18, 19, 20])
j = np.unique(j)
print(j)

#%% Funções

def soma(oi,eae):
    return oi+eae

#a = 3
#b = 7
#soma = soma + i

def media(x):
    soma = 0
    for i in x:
        soma += i
    media = soma/len(x)
    return media            

#a = [3,6,9,14,17,28,10]

def desv_pad(x):
    soma = []
    for i in x:
        d = (i-media(x))**2
        soma.append(d)
    return np.sum(soma)/(len(x))

    
def trocarpos(valores,pos1,pos2):
    if 0<=pos1<len(valores) and 0<=pos2<len(valores):
        pos1arm = valores[pos1] #armazena o valor do pos1
        valores[pos1] = valores[pos2] #substitui o valor pos 1 em 2 perdendo o valor pos1
        valores[pos2] = pos1arm #substitui o valor do pos 2 no antigo pos1
    return None

#candidatos = ['joão','Maria','Gabriel','Felipe','Júlia']    
    
def fat(n):  #Função Recursiva chama ela mesma
    if n == 0:
        return 1    #condição de parada
    else:
        return n*fat(n-1)   

#%% 
'Utilizando Dados com pandas (USAR O SPYDER DO ANACONDA)' 
import pandas as pd

nome_colunas=['Coluna Vazia','Nome','Notas']
datatxt = pd.read_csv(r'C:\Users\LUCAS\Documents\Aulas Rafaela\Alunos.txt', sep=" ")#,names=nome_colunas, sep=" ")
dataxlsx = pd.read_excel(r'C:\Users\LUCAS\Documents\Aulas Rafaela\Alunos2.xlsx',names=nome_colunas)
#Colocar o r pois da bug ou inverter as barras ou colocar as mesmas aspas porém duplas

datatxt.head()
dataxlsx.head()
#%% PROGRAMA QUE INDENNTIFICA SE ALUNO ESTÁ APROVADO, EXAME OU REPROVADO
#Colocar nome nas colunas 
#df.columns

datatxt.columns=['Nome','Notas']

#dataxlsx.rename(columns = {'Unnamed: 0':'Coluna Vazia'}, inplace = True) #Inplace pra pçersistir a mudança no dataframe

dataxlsx.columns=['Coluna Vazia','Nome','Notas']

#Trocar , por . e vice-versa
#datatxt['Notas'] = datatxt['Notas'].astype(str)
#datatxt['Notas'] = datatxt['Notas'].str.replace('.', ',')

#Descobrir quem esá aprovado, exame ou reprovado

datatxt['Notas']



datatxt.shape
datatxt.tail(2) #e datatxt.tail(datatxt.shape[0]) #(fim-começo)
datatxt[['Notas']] #type(datatxt[['Notas']]) e type(datatxt['Notas']) Data frame conjunto de series
datatxt.loc[1:3]  #(começo-fim)
datatxt.loc[[1,3]] #posicao precisa ter 2 colchetes
datatxt.loc[datatxt['Notas'] > 5]
#dataframe que só tem os alunos no Exame
dataexam = datatxt.loc[(datatxt['Notas'] >= 4) & (datatxt['Notas'] < 7)] #Condições entre parenteses & = and
dataxlsx.isnull() #Onde estao os valores nulos
dataxlsx.isnull().sum() #Soma dos valores nulos
dataxlsx.dropna(axis = 1, how = 'all', inplace = True)
#Axis 0 para tirar index 1 para tirar a coluna, how vc pode escolher deleter se TODOS forem nulos ou se any (qualquer NAN) ja vai excluir
dataxlsx['Coluna Vazia'].fillna(0,inplace = True) #Substitui NAN por algo
#Adicionar Linha
to_append = ['Júlia', 10]
datatxt_tamanho = len(datatxt)
datatxt.loc[datatxt_tamanho] = to_append
#Adicionar coluna
datatxt['Em Exame'] = pd.NaT
datatxt_exames = datatxt.loc[(datatxt['Notas'] >= 4) & (datatxt['Notas'] < 7)]
datatxt['Em Exame'] = datatxt_exames['Nome']
#Coluna que atribui se o aluno está de exame ou nao
datatxt['Em Exame'].fillna(0,inplace = True) #não é possível atribuir nan a um boolean
for i in range(len(datatxt['Em Exame'])):
    if bool(datatxt['Em Exame'][i]) == False:
        datatxt['Em Exame'][i] = 'Não'
    else:
        datatxt['Em Exame'][i] = 'Sim'
        
    
#%% 
'MATPLOT'
import numpy as np
import matplotlib.pyplot as plt

#Plotando barras Quantos exames precisarao de imprimir

exam = (4,3)
Qual = ['Sem exames', 'Exames']
fig = plt.figure(figsize=(5,5))

fig = plt.bar(Qual,exam)
#%%
#Gráfico de linhas

#x = [0,2,4,6,8]
x = np.linspace(0, 300, 100)
y = np.array(x)**2

fig1 = plt.figure(figsize=(5,5))
fig1 = plt.axhline(y=0, color='black', linestyle='dashed', linewidth=1)
fig1 = plt.axvline(x=0, color = 'black', linestyle='dashed', linewidth=1)
fig = plt.grid(linestyle= 'dashed', c = 'black')
fig1 = plt.plot(x,y)
fig1 = plt.xlabel('Ampere (mA)')
fig1 = plt.ylabel('Volt (V)')
fig1 = plt.title('Medidas do circuito com a Pilha')
#%%
'Usando dataframe pra plotar'

df = pd.read_excel(r'C:\Users\LUCAS\Documents\Física experimental 3\Tabelas\Tabela_tratada_AT2.xlsx')

df_y_série = df['V_P']
df_x_série = df['A_P']
df_y_paralelo = df['V_PS']
df_x_paralelo = df['A_R1']

#Calculo precisa colocar .values
x_error = df['P_ERR'].values/120

y_error = df['A_ERR_P'].values/120

#%% PLOT SCATTER

fig2 = plt.figure(figsize=(5,5))

fig2 = plt.scatter(df_x_série.values, df_y_série.values, s= 10, marker= 'o',)
#fig2 = plt.grid(linestyle= 'dashed', c = 'black')
#fig2 = plt.axhline(y=1.26, color='black', linestyle='-', linewidth=1)
#fig2 = plt.axvline(x=0 ,color = 'black', linestyle='-', linewidth=1)

#fig2 = plt.errorbar(df_x_série.values, df_y_série.values, yerr = y_error, xerr = x_error,fmt = 'o', ecolor = 'black'
#            , elinewidth= 1)
fig2 = plt.xlabel('Ampere (mA)')
fig2 = plt.ylabel('Volt (V)')
fig2 = plt.title('Medidas do circuito com a Pilha')





