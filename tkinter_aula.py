from tkinter import *
import os

framevar = ''
id_meta = 0
id_parcela = 0


def nova_meta():

    def salvar_entradas():
        global id_meta

        try:
            with open('metas.txt', 'r') as arquivo_meta:
                linhas = arquivo_meta.readlines()
                ids_meta = len(linhas)
                id_meta = ids_meta

        except FileNotFoundError:
            id_meta = 0

        entradas_metas = [
            (str(id_meta) + '\t'),
            (str(tipo_scale.get()) + '\t'),
            (nome_entrada.get() + '\t'),
            (str(custo_entrada.get()) + '\t'),
            (str(prazo_entrada.get()) + '\t'),
            (finalidade_entrada.get() + '\n')
            ]

        id_meta += 1

        with open('metas.txt', 'a') as arquivo:
            for valor in entradas_metas:
                arquivo.write(valor)
        for indice, valor in enumerate(entradas_metas):
            Label(colunas_metas[indice], text=valor).pack()

        entrada_meta.destroy()

    entrada_meta = Tk()
    entrada_meta.geometry('250x400+350+150')
    entrada_meta.title('Adicione sua meta')

    tipo = LabelFrame(entrada_meta, text='TIPO', labelanchor='n')
    tipo_scale = Scale(tipo, orient='horizontal', from_=0, to=5, tickinterval=1)
    tipo_scale.pack()
    tipo.pack(side='top')

    nome = LabelFrame(entrada_meta, text='NOME', labelanchor='n')
    nome_entrada = Entry(nome)
    nome_entrada.pack()
    nome.pack(side='top')

    custo = LabelFrame(entrada_meta, text='CUSTO', labelanchor='n')
    custo_entrada = Entry(custo)
    custo_entrada.pack()
    custo.pack(side='top')

    prazo = LabelFrame(entrada_meta, text='PRAZO', labelanchor='n')
    prazo_entrada = Entry(prazo)
    prazo_entrada.pack()
    prazo.pack(side='top')

    finalidade = LabelFrame(entrada_meta, text='FINALIDADE', labelanchor='n')
    finalidade_entrada = Entry(finalidade)
    finalidade_entrada.pack()
    finalidade.pack(side='top')

    salvar = Button(entrada_meta, text='SALVAR', command=salvar_entradas, bd='20', pady='20', relief='groove')
    salvar.pack(side='top')

    entrada_meta.mainloop()


def nova_parcela():
    def salvar_parcela():
        global id_parcela

        try:
            with open('parcelas.txt', 'r') as arquivo_parcela:
                linhas = arquivo_parcela.readlines()
                ids_parcela = len(linhas)
                id_parcela = ids_parcela

        except FileNotFoundError:
            id_parcela = 0

        entradas_parcelas = [
            (str(id_parcela) + '\t'),
            (str(nome_entrada.get()) + '\t'),
            (valor_entrada.get() + '\t'),
            (str(mes_entrada.get() + '\t')),
            (str(duracao_entrada.get() + '\n'))
        ]

        id_parcela += 1

        with open('parcelas.txt', 'a') as arquivo:
            for valores in entradas_parcelas:
                arquivo.write(valores)
        for indice, valores in enumerate(entradas_parcelas):
            Label(colunas_parcelas[indice], text=valores).pack()

        entrada_parcela.destroy()

    entrada_parcela = Tk()
    entrada_parcela.geometry('250x300+350+150')
    entrada_parcela.title('Adicione sua parcela')

    nome = LabelFrame(entrada_parcela, text='Nome', labelanchor='n')
    nome_entrada = Entry(nome)
    nome_entrada.pack()
    nome.pack()

    valor = LabelFrame(entrada_parcela, text='Valor', labelanchor='n')
    valor_entrada = Entry(valor)
    valor_entrada.pack()
    valor.pack()

    mes = LabelFrame(entrada_parcela, text='Mês', labelanchor='n')
    mes_entrada = Entry(mes)
    mes_entrada.pack()
    mes.pack()

    duracao = LabelFrame(entrada_parcela, text='Duração', labelanchor='n')
    duracao_entrada = Entry(duracao)
    duracao_entrada.pack()
    duracao.pack()

    salvar = Button(entrada_parcela, text='SALVAR', command=salvar_parcela, pady='20')
    salvar.pack()
    entrada_parcela.mainloop()


root = Tk()
root.geometry('900x500+200+100')
root.title('PLANEJAMENTO')

metas = LabelFrame(root, text='METAS', bg='white', labelanchor='n')
recebe_metas = Frame(metas)
recebe_parcelas = Frame(metas)


def escreve_metas():
    if os.path.isfile('metas.txt'):
        arquivo = open('metas.txt', 'r')
        linhas = arquivo.readlines()
        for linha in linhas:
            separador = linha.split()
            for indice, valor in enumerate(separador):
                separador[indice] = Label(colunas_metas[indice], text=valor).pack()
        arquivo.close()


def escreve_parcelas():
    if os.path.isfile('parcelas.txt'):
        arquivo = open('parcelas.txt', 'r')
        linhas = arquivo.readlines()
        for linha in linhas:
            separador = linha.split()
            for indice, valor in enumerate(separador):
                separador[indice] = Label(colunas_parcelas[indice], text=valor).pack()

        arquivo.close()


# creating columns of the table
colunas_metas = [
    LabelFrame(recebe_metas, text='Id', labelanchor='n'),
    LabelFrame(recebe_metas, text='Tipo', labelanchor='n'),
    LabelFrame(recebe_metas, text='Nome', labelanchor='n'),
    LabelFrame(recebe_metas, text='Custo', labelanchor='n'),
    LabelFrame(recebe_metas, text='Prazo', labelanchor='n'),
    LabelFrame(recebe_metas, text='Finalidade', labelanchor='n')]

for coluna in colunas_metas:
    coluna.pack(side='left')
recebe_metas.pack(anchor='nw', side='left')


colunas_parcelas = [
    LabelFrame(recebe_parcelas, text='Id', labelanchor='n'),
    LabelFrame(recebe_parcelas, text='Nome', labelanchor='n'),
    LabelFrame(recebe_parcelas, text='Valor', labelanchor='n'),
    LabelFrame(recebe_parcelas, text='Mês', labelanchor='n'),
    LabelFrame(recebe_parcelas, text='Duração', labelanchor='n')
]

for coluna in colunas_parcelas:
    coluna.pack(side='left')
recebe_parcelas.pack(anchor='ne', side='right')

metas.pack(fill='both', expand='true', side='top')

# calling the saved parcelas e metas


escreve_metas()
escreve_parcelas()

menubar = Menu(root)
menu_metas = Menu(menubar, tearoff=0)
menu_metas.add_command(label='Nova', command=nova_meta)
menubar.add_cascade(label='Metas', menu=menu_metas)

menu_parcela = Menu(menubar, tearoff=0)
menu_parcela.add_command(label='Nova', command=nova_parcela)
menubar.add_cascade(label='Parcelas', menu=menu_parcela)


root.config(menu=menubar)
root.mainloop()
