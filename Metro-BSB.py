from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import os

root = Tk()
root.title("BFS e DFS no metrô de Brasília")

bemVindo = Label(root, text="\nBem-vindo(a)!\n")
bemVindo.pack()

imagem = Image.open("metro.jpg").resize((600, 383), Image.ANTIALIAS)
imagem = ImageTk.PhotoImage(imagem)
imgLabel = Label(image=imagem)
imgLabel.pack()


Metrobsb = {'102 Sul': ['Galeria', '108 Sul'],
            '108 Sul': ['102 Sul', '112 Sul'],
            '112 Sul': ['108 Sul', '114 Sul'],
            '114 Sul': ['112 Sul', 'Terminal Asa Sul'],
            'Águas Claras': ['Arniqueiras', 'Concessionárias', 'Taguatinga Sul'],
            'Arniqueiras': ['Águas Claras', 'Guará'],
            'Ceilândia': ['Ceilândia Norte'],
            'Ceilândia Centro': ['Ceilândia Norte', 'Guariroba'],
            'Ceilândia Norte': ['Ceilândia', 'Ceilândia Centro'],
            'Ceilândia Sul': ['Guariroba', 'Centro Metropolitano'],
            'Central': ['Galeria'],
            'Centro Metropolitano': ['Ceilândia Sul', 'Praça do Relógio'],
            'Concessionárias': ['Águas Claras', 'Praça do Relógio'],
            'Feira': ['Guará', 'Shopping'],
            'Furnas': ['Taguatinga Sul', 'Samambaia Sul'],
            'Galeria': ['Central', '102 Sul'],
            'Guará': ['Feira', 'Arniqueiras'],
            'Guariroba': ['Ceilândia Centro', 'Ceilândia Sul'],
            'Praça do Relógio': ['Concessionárias', 'Centro Metropolitano'],
            'Samambaia': ['Samambaia Sul'],
            'Samambaia Sul': ['Samambaia', 'Furnas'],
            'Shopping': ['Terminal Asa Sul', 'Feira'],
            'Taguatinga Sul': ['Furnas', 'Águas Claras'],
            'Terminal Asa Sul': ['114 Sul', 'Shopping']
            }


def BFS(G, s, visited):
    queue = []
    visited.append(s)
    queue.append(s)

    while queue:
        s = queue.pop(0)

        for neighbour in G[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

    return visited


def DFS(G, s, visited):
    if s not in visited:
        visited.append(s)
        for neighbour in G[s]:
            DFS(G, neighbour, visited)
    return visited


def buscar():
    noDePartida = clicked.get()
    print(noDePartida)
    bfs = str(BFS(Metrobsb, noDePartida, []))
    dfs = str(DFS(Metrobsb, noDePartida, []))
    resultBfs.config(text=bfs)
    resultDfs.config(text=dfs)


label = Label(text="\nSelecione a parada (o nó):\n")
label.pack()

options = []
for item in Metrobsb:
    options.append(item)
clicked = StringVar()
clicked.set(options[0])

paradas = OptionMenu(root, clicked, *options)
paradas.pack(padx=100)

fazerBuscas = Button(root, text="Fazer buscas BFS e DFS", command=buscar)
fazerBuscas.pack(pady=20)

bfsLabel = Label(root, text="BFS:", pady=5)
bfsLabel.pack()
global resultBfs
resultBfs = Label(root, text="", wraplength=600, pady=5, padx=20)
resultBfs.pack()

dfsLabel = Label(root, text="DFS:", pady=5)
dfsLabel.pack()
global resultDfs
resultDfs = Label(root, text="\n\n", wraplength=600, pady=5, padx=20)
resultDfs.pack()

root.mainloop()
