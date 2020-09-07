from tkinter import *
from PIL import ImageTk, Image
import os

root = Tk()

bemVindo = Label(root, text="Bem-vindo(a)!")
bemVindo.pack(pady=20)


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
        print(s, end=" ")

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


label = Label(text="Selecione a parada (o nó):")
label.pack()

paradas = Listbox(root, selectmode=BROWSE)
for item in Metrobsb:
    paradas.insert(END, item)
paradas.pack(padx=100)

noDePartida = paradas.get(ANCHOR)
print(noDePartida)


def buscar(G=Metrobsb, s=noDePartida, visited=[]):
    resultBfs = BFS(G, s, visited)
    resultDfs = DFS(G, s, visited)
    result = Label(text=(resultBfs + resultDfs))
    result.pack()


fazerBuscas = Button(root, text="Fazer buscas BFS e DFS", command=buscar)
fazerBuscas.pack(pady=20)

root.mainloop()
