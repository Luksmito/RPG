from tkinter import *
from functools import partial
import Batalha
import json

class AddCriatura():
    def __init__(self):
        self.janela = Tk()
        self.janela.geometry("500x500+300+300")
        with open("criaturas.json", "r") as json_file:
            self.listaCriaturas = json.load(json_file)
        self.nomeLabel = Label(self.janela, text="Nome: ")
        self.nomeEntry = Entry(self.janela)   
        self.hpLabel = Label(self.janela, text="Hp: ")
        self.hpEntry = Entry(self.janela) 
        self.iniciativaLabel = Label(self.janela, text="Iniciativa: ")
        self.iniciativaEntry = Entry(self.janela)
        self.botaoAdicionar = Button(self.janela, text="Adicionar criatura", bg="green", width=20)
        self.botaoBatalha = Button(self.janela, text ="Voltar a Batalha", bg="red", width=20)
        self.parcial()
        self.atualizar()
        self.janela.mainloop()
    
    def atualizar(self):
        self.nomeLabel.grid(row=0, column=0)
        self.hpLabel.grid(row=1, column=0)
        self.iniciativaLabel.grid(row=2, column=0)
        self.nomeEntry.grid(row=0,column=1)
        self.hpEntry.grid(row=1,column=1)
        self.iniciativaEntry.grid(row=2,column=1)
        self.botaoAdicionar.grid(row=3,column=1)
        self.botaoBatalha.grid(row=4,column=1)
    
    def parcial(self):
        self.botaoAdicionar["command"] = partial(self.adicionar_criatura) 
        self.botaoBatalha["command"] = partial(self.voltar_batalha)
    
    def adicionar_criatura(self):
        criatura = {"nome":self.nomeEntry.get(), "hp": int(self.hpEntry.get()), "iniciativa": int(self.iniciativaEntry.get())}
        self.listaCriaturas.append(criatura)
        with open("criaturas.json", "w") as json_file:
            json.dump(self.listaCriaturas,json_file, indent=4)
    
    def voltar_batalha(self):
        self.janela.destroy()
        tela = Batalha.Batalha()
        return tela