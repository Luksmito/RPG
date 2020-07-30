from tkinter import *
from functools import partial
from AddCriatura import *
import json


class Batalha():
    """classe que retorna a janela de batalha, listaCriaturas recebe um dict: listaCriaturas = {"nome": string, "hp": int, "iniciativa": int}"""
    def __init__(self):
        self.janela = Tk()
        self.botaoOrdenar = Button(self.janela,width=20,text="Ordenar",bg="green")
        self.botaoAdicionado = 0
        #Carregando o arquivo com as criaturas salvas
        with open('criaturas.json', 'r') as json_file:
            self.listaCriaturas = json.load(json_file)
        #listaBotoes retorna um dict que contem o objeto tkinter.Button e os dados da criatura
        #que aquele botão representa
        self.listaBotoes = [
        {"botao": Button(self.janela, width=20, text=x["nome"])
        , "nome": x["nome"], 
        "hp": x["hp"], 
        "iniciativa": x["iniciativa"]}for x in self.listaCriaturas
        ]
        #lista de criaturas adicionadas a batalha
        self.lutadores = []
        self.botaoAdicionarCriatura = Button(self.janela, width=15, bg="green", text="Adicionar criatura")
        self.atualizar()
        self.janela.mainloop()
        self.janela.geometry("500x500+300+300") 
        
        
        
        
    def criar_lista_criaturas(self):
        """cria os botões de criaturas na janela de batalha"""
        y1=100
        for botao in self.listaBotoes:
            botao["botao"].pack(anchor=E)
            y1 = y1+30
        self.botaoAdicionarCriatura.pack(anchor=E)  
      
    def adicionar_criatura(self):
        """chama a janela de adição de criaturas"""
        self.janela.destroy()
        tela = AddCriatura()
        return tela

    def ordenar_batalha(self):
        tamanho = len(self.lutadores)
        for x in range(0,tamanho):
            for y in range(x+1,tamanho):
                if self.lutadores[x]["dados"]["iniciativa"] < self.lutadores[y]["dados"]["iniciativa"]:
                    aux = self.lutadores[x]
                    self.lutadores[x] = self.lutadores[y] 
                    self.lutadores[y] = aux
        self.atualizar()

    def adicionar_a_batalha(self,botaoWidget,nome,hp,iniciativa, botao):
        """Adiciona a criatura do botão de criatura a batalha"""
        if self.botaoAdicionado == 0:
            self.botaoOrdenar = Button(self.janela, width=20, text="Ordenar", bg="green")
            self.botaoOrdenar.pack(anchor=W)
            self.botaoAdicionado = 1
        texto = f"{nome} \n hp: {hp} iniciativa: {iniciativa}"
        label = Label(self.janela, text=texto)
        botaoDano = Button(self.janela, width=8, text="dano", bg="red")
        botaoCura = Button(self.janela, width=8, text="cura", bg="green")
        botaoIniciativa = Button(self.janela, width=8, text="iniciativa", bg="yellow")
        entrada = Entry(self.janela, width=20)
        lutador = {"label": label,"botaoIniciativa": botaoIniciativa, "botaoDano": botaoDano, "botaoCura": botaoCura, "entrada": entrada, "dados": botao}
        self.lutadores.append(lutador)
        self.parcial()
        self.atualizar()
    
    def atualizar(self):
        """posiciona os widgets criados na tela"""
        self.parcial()
        self.criar_lista_criaturas()
        if len(self.lutadores) != 0:
            for lutador in self.lutadores:
                lutador["label"]["text"] = str(lutador["dados"]["nome"]) + "\n hp: " + str(lutador["dados"]["hp"]) + " iniciativa: " + str(lutador["dados"]["iniciativa"])
                lutador["label"].pack(anchor=W)
                lutador["botaoDano"].pack(anchor=W)
                lutador["botaoCura"].pack(anchor=W)
                lutador["botaoIniciativa"].pack(anchor=W)
                lutador["entrada"].pack(anchor=W)
            

    def dano(self, lutador):
        """dá o dano a criatura passada como parâmetro"""
        self.lutadores[lutador]["dados"]["hp"] = self.lutadores[lutador]["dados"]["hp"] - int(self.lutadores[lutador]["entrada"].get())
        self.atualizar()
    
    def cura(self, lutador):
        """adiciona o numero dado no input ao hp da criatura"""
        self.lutadores[lutador]["dados"]["hp"] = self.lutadores[lutador]["dados"]["hp"] + int(self.lutadores[lutador]["entrada"].get())
        self.atualizar()
    
    def iniciativa(self, lutador):
        """atribui a iniciativa escrita no input à criatura"""
        self.lutadores[lutador]["dados"]["iniciativa"] = self.lutadores[lutador]["dados"]["iniciativa"] + int(self.lutadores[lutador]["entrada"].get())
        self.atualizar()

    
    def parcial(self):
        """cria as funções dos botoes do Tkinter"""
        for botao in self.listaBotoes:
            botao["botao"]["command"] = partial(self.adicionar_a_batalha, botao["botao"],botao["nome"],botao["hp"], botao["iniciativa"], botao)
        if len(self.lutadores) != 0:
            for x in range(0,len(self.lutadores)):
                self.lutadores[x]["botaoDano"]["command"] = partial(self.dano, x) 
                self.lutadores[x]["botaoCura"]["command"] = partial(self.cura, x)
                self.lutadores[x]["botaoIniciativa"]["command"] = partial(self.iniciativa, x)
        self.botaoAdicionarCriatura["command"] = partial(self.adicionar_criatura)    
        self.botaoOrdenar["command"] = partial(self.ordenar_batalha)
