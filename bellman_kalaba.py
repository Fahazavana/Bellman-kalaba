import tkinter
from tkinter import ttk
import time
from json.encoder import INFINITY as inf

graphe = {}
graphe_arc = {}


def d_sommet(x0, y0):
    rayon = 15
    id_sommet = zone_d.create_oval(
        x0 - rayon, y0 - rayon, x0 + rayon, y0 + rayon, fill="white", activefill="blue"
    )
    zone_d.create_text(
        x0,
        y0,
        text=str(id_sommet),
        justify="center",
        anchor="c",
        font=("courier", 10),
        fill="black",
    )
    graphe[id_sommet] = [id_sommet]
    graphe_arc[(id_sommet, id_sommet)] = [0, None]


def clic_cercle(event):
    clic_x, clic_y = event.x, event.y
    d_sommet(clic_x, clic_y)


def kalaba(*args):
    arr = int(entry_arr.get())
    etape_list = list()
    etape_dist = list()
    dist = {}
    succ = {}

    dist[arr] = 0
    succ[arr] = None

    for key in graphe:
        if key != arr:
            dist[key] = inf
            succ[key] = None
    etape_list.append(succ)
    etape_dist.append(dist)

    toDo = [arr]
    etape = 0
    while toDo != []:
        etape = etape + 1
        x = toDo.pop()
        zone_d.itemconfig(x, fill="yellow")
        for y in graphe[x]:
            if dist[x] + graphe_arc[(y, x)][0] < dist[y]:
                dist[y] = dist[x] + graphe_arc[(y, x)][0]
                succ[y] = x
                toDo.append(y)
        zone_d.itemconfig(x, fill="white")
        etape_list.append(succ)
        etape_dist.append(dist)

    key = 1
    while succ[key] != None:
        zone_d.itemconfig(key, fill="yellow")
        zone_d.itemconfig(graphe_arc[(key, succ[key])][1], fill="red")
        key = succ[key]
    zone_d.itemconfig(arr, fill="yellow")
    print("terminer")

    for k in range(etape):
        print(etape_list[k])
        print(etape_dist[k])


def arc(*arg):
    global v
    dep = int(entr_deb.get())
    arr = int(entr_arr.get())
    pds = eval(entr_poids.get())
    a = zone_d.coords(dep)
    b = zone_d.coords(arr)

    if pds == "":
        pds = 0
    else:
        pds = int(pds)

    dep_x = (a[0] + a[2]) // 2
    dep_y = (a[1] + a[3]) // 2

    arr_x = (b[0] + b[2]) // 2
    arr_y = (b[1] + b[3]) // 2

    arc = zone_d.create_line(
        dep_x, dep_y, arr_x, arr_y, fill="black", width=0.5, smooth=1, arrow="last"
    )
    zone_d.create_text(
        (arr_x + dep_x) // 2,
        (dep_y + arr_y) // 2,
        text=pds,
        justify="center",
        anchor="c",
        fill="white",
    )
    graphe_arc[dep, arr] = [pds, arc]
    graphe[arr].append(dep)


fen_p = tkinter.Tk()  # La fenetre principale

dessin_c = tkinter.LabelFrame(fen_p, text="Sommet")  # Cadre contenant la zone de dessin

zone_d = tkinter.Canvas(
    dessin_c, bg="gray", width=600, height=500
)  # Canvas pour dessiner le graphe
zone_d.bind("<Button-1>", clic_cercle)  # Binding : surveillance des clics

# Cadre permettant de saisir les arcs de la graphe
arc_entry = tkinter.LabelFrame(dessin_c, text="Arc")

entr_deb_l = tkinter.Label(arc_entry, text="Depart")
entr_arr_l = tkinter.Label(arc_entry, text="Arrive")
entr_poids_l = tkinter.Label(arc_entry, text="Poids")
entr_deb = tkinter.Entry(arc_entry, width=5)
entr_arr = tkinter.Entry(arc_entry, width=5)
entr_poids = tkinter.Entry(arc_entry, width=5)
btn_val = tkinter.Button(arc_entry, text="Valider", command=arc)
error_str = tkinter.StringVar()


entr_deb_l.grid(row=1, column=1)
entr_arr_l.grid(row=1, column=2)
entr_poids_l.grid(row=1, column=3)
entr_deb.grid(row=2, column=1)
entr_arr.grid(row=2, column=2)
entr_poids.grid(row=2, column=3)
btn_val.grid(row=2, column=4)


# Cadre pour demarre l'algorithme
debut = tkinter.LabelFrame(fen_p)
msg = tkinter.Label(debut, text="Saisir le but de votre graphe")

entry_arr = tkinter.Entry(debut)
kalaba_btn = tkinter.Button(debut, text="Demmrer l'algorithme", command=kalaba)
msg.pack()
entry_arr.pack()
kalaba_btn.pack()

dessin_c.pack()
zone_d.grid(row=1, column=1, sticky="nw")
arc_entry.grid(row=2, column=1, sticky="nw")

debut.pack()

fen_p.mainloop()
