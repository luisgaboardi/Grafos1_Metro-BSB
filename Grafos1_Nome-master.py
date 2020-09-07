from tkinter import *

metrobsb = {'102 Sul': ['Galeria', '104 Sul'],
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

root = Tk()

myLabel = Label(root, text="Bem-vindo!")
myLabel.pack()

canvas = Canvas(root, height=700, width=700, bg="#263D42")
canvas.pack()

start = Button(root, text="Iniciar", padx=10, pady=5, fg="white", bg="#263D42")
start.pack()

root.mainloop()
