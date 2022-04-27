import tkinter
from tkinter import ttk
import time
from json.encoder import INFINITY as inf

#Graph={ (id,num):[(id,num,poids)]}
class Sommet():
	_nbr_sommet = 0
	_rayon = 15
	_rayonMax=50

	def __init__(self,x0,y0):
		self.x = x0
		self.y = y0
		Sommet._nbr_sommet+=1
		self.numero = Sommet._nbr_sommet
	def addSommet(self, zone, listAdj ):
		a = self.x-Sommet._rayon
		b = self.y-Sommet._rayon
		c = self.x+Sommet._rayon
		d = self.y+Sommet._rayon
		e = self.x-Sommet._rayonMax
		f = self.y-Sommet._rayonMax
		g = self.x+Sommet._rayonMax
		h = self.y+Sommet._rayonMax
		#print(help(zone.find_enclosed))
		#print(zone.find_closest(self.x,self.y))
		if (zone.find_enclosed(e,f,g,h))==() and self.x>30 and self.x<430 and self.y>30 and self.y<370 and Sommet._nbr_sommet < 21 :
			id_sommet = zone.create_oval(a, b, c, d, fill = "white", activefill = "blue")
			zone.create_text(self.x,self.y,text=str(self.numero), justify="center",anchor="c", font= ("courier", 5, "bold"), fill="black")
			listAdj[(self.numero, id_sommet)] = [[self.numero, id_sommet, inf]]
		else:
			Sommet._nbr_sommet-=1
		
class Graph():
	def __init__(self):
		self.listAdj = {}
	
		
		
class Dessin(tkinter.Frame):
	def __init__(self, principale):
		super().__init__(principale)
		self.zone = tkinter.Canvas(self,bg="green",width=460,height=400)# Canvas pour dessiner le graphe
		self.pack()
		self.zone.bind("<Button-1>",self.createSommet)
		self.zone.grid(row=0, column=0)
		
		self.data = Graph()
		
	def createSommet(self,event):
		print(self.data.listAdj)
		Sommet(event.x,event.y).addSommet(self.zone, self.data.listAdj)
		print(self.data.listAdj)
	
class Command(tkinter.Frame):
	def __init__(self,principale):
		super().__init__(principale)
		self.root=principale
		self.logs = tkinter.StringVar()
		self.logs.set("")
		self.ecran = tkinter.Message(self, text=self.logs.get(), width=300,justify="left",bg="white")
		self.depId = tkinter.Entry(self, width = 5)
		self.arrId = tkinter.Entry(self, width = 5)
		self.pdsDA = tkinter.Entry(self, width = 5)
		self.btn = tkinter.Button(self,text="Ok",command = self.addArc)
		
		self.pack(side="left")
		
		tkinter.Label(self, text="Depart (D").grid(row=0, column=0)
		tkinter.Label(self, text="Arrivé (A)").grid(row=1, column=0)
		tkinter.Label(self, text="Poids (P)").grid(row=2, column=0)
		
		
		self.depId.grid(row=0,column=1)
		self.arrId.grid(row=1, column=1)
		self.pdsDA.grid(row=2, column=1)
		self.btn.grid(row=3, columnspan=2)
		self.ecran.grid(column=3, row = 0,rowspan=4, columnspan=7)
	def printMsg(self, msg):
		print("call")
		self.ecran["text"]= msg
		
	def addArc(self):
		test=[False, False, False]
		erreur=""
		try:
			x = int(self.depId.get())
		except ValueError as xError:
			erreur+="Sommet D invalide"+"\n"
		else:
			test[0]=True
		try:
			y = int(self.arrId.get())
		except ValueError as yError:
			erreur+="Sommet A invalide"+"\n"
		else:
			test[1]=True
		try:
			p = self.pdsDA.get()
			if p == 'inf':
				p = inf
			else:
				p = int(p)
				
		except ValueError as pError :
			erreur+="Poid P invalude"
		else:
			test[2]=True
			
		if not test:
			print(test, erreur)
		else:
			self.printMsg(erreur)
			print(erreur, test)

fenPrincipale = tkinter.Tk()
fenPrincipale.geometry("480x800")
Dessin(fenPrincipale)
Command(fenPrincipale)
fenPrincipale.mainloop()