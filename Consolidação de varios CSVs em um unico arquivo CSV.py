# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 15:49:56 2019

@author: ADAMLINCOLNOLIVEIRAS
"""

import os
import pandas as pd



''' Abre o diretório atual onde estão os arquivos'''
path = os.getcwd()
#path = os.chdir('C:\\Users\\ADAMLINCOLNOLIVEIRAS\\Box Sync\\Diretorio_Camara_de_Retencao')


''' Guarda os arquivos em variável '''
files = os.listdir(path)

''' Abaixo faz um for em todos os arquivos do diretório para verificar se a extensão é CSV
(-3 significa últimos 3 caracteres do nome do arquivo, ou seja, extensão).
Estas condições em python (For e If por exemplo) em uma única linha se chama list
Comprehension '''

files_csv = [file for file in files if file[-3:] == "TXT"]

''' Cria dataframe vazio '''
df = pd.DataFrame()


''' Lê todos os arquivos dentro da variável files_csv e faz o append no df vazio criado
no passo anterior. No caso de csv, é necessário colocar o parâmetro sep=";" que é o separador '''

for file in files_csv:
    data = pd.read_csv(file, sep=";", names=["SITE", "UF", "DATA CONTA", "CICLO","QTE CONTAS","VALOR", "TIPO", "SUB TIPO"], encoding='iso-8859-1', index_col=False) #iso-8859-1
    df = df.append(data)


df.to_csv('C:\\Users\\ADAMLINCOLNOLIVEIRAS\\Box Sync\\Diretorio_Camara_de_Retencao\\Nova pasta\\20191122_Consolidados_camara_de_retencao.csv', sep = ';', index=False)  #atualiação - caminho path+ nome agora é separado por virgula e SEP=
