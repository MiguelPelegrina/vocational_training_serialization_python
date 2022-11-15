import pickle
from tkinter import *
from Alumno import *

'Generador que devuelve un numero autoincremental de tal forma que la gestion de la variable identificadora para ' \
'borrar y modificar no depende del usuario'
def codigoAutoincremental():
    num = 1
    while True:
        yield num
        num += 1

'Cargamos el fichero guardado desde el principio'
'abrimos un puntero: r para leer, b para binario'
fichero_binario = open("fichero", "rb")
'cargamos en la lista los objetos serialiables del fichero'
lista = pickle.load(fichero_binario)
'cerramos el fichero'
fichero_binario.close()
'borramos el puntero'
del fichero_binario
'hacerlo autoincremental'
codigo = codigoAutoincremental()
nombre = ""
apellido = ""

'Funcion que guarda la lista en un fichero'
def crearFichero():
    'abrimos un puntero: w para escribir, b para binario'
    fichero_binario = open("fichero", "wb")
    'escribimos en el fichero la lista'
    pickle.dump(lista, fichero_binario)
    'cerramos el fichero'
    fichero_binario.close()
    'borramos el puntero'
    del fichero_binario


'Funcion que carga el fichero de un sesion previa'
def cargarFichero():
    'abrimos un puntero: r para leer, b para binario'
    fichero_binario = open("fichero", "rb")
    'cargamos en la lista los objetos serialiables del fichero'
    lista = pickle.load(fichero_binario)
    'cerramos el fichero'
    fichero_binario.close()
    'borramos el puntero'
    del fichero_binario


'Funcion que lista todos los elementos de la lista en un campo de texto'
def listar():
    txtLista.delete(1.0, END)
    for alumno in lista:
        txtLista.insert(END, str(alumno.codigo) + ": " + alumno.nombre + ", " + alumno.apellido + "\n")


'Funcion de permite al usuario anadir un alumno a la lista, utiliza los valores dentro de los Entry Nombre y Apellido'
def anadir():
    alumno = Alumno(next(codigo), txtNombre.get(), txtApellido.get())
    lista.append(alumno)

'Funcion que permite al usuario borrar un alumno de la lista, utiliza el valor dentro del Entry Codigo'
def borrar():
    for alumno in lista:
        if int(alumno.codigo) == int(txtCodigo.get()):
            lista.remove(alumno)

'Funcion que permite al usuario modificar un alumno de la lista, utiliza el valor dentro del Entry Codigo para' \
'identificar el elemento de la lista y los valores de los Entry Nombre y Apellido para modificar los datos'
def modificar():
    for alumno in lista:
        if int(alumno.codigo) == int(txtCodigo.get()):
            alumno.nombre = txtNombre.get()
            alumno.apellido = txtApellido.get()

'Funcion que permite buscar en funcion de uno o varios campos en funcion de que si estan vacios o no'
def buscar():
    txtLista.delete(1.0, END)
    for alumno in lista:
        if txtCodigo.get() != '' and txtNombre.get() == '' and txtApellido.get() == '':
            if int(alumno.codigo) == int(txtCodigo.get()):
                txtLista.insert(END, str(alumno.codigo) + ": " + alumno.nombre + ", " + alumno.apellido + "\n")
        elif txtCodigo.get() == '' and txtNombre.get() != '' and txtApellido.get() == '':
            if alumno.nombre == txtNombre.get():
                txtLista.insert(END, str(alumno.codigo) + ": " + alumno.nombre + ", " + alumno.apellido + "\n")
        elif txtCodigo.get() == '' and txtNombre.get() == '' and txtApellido.get() != '':
            if alumno.apellido == txtApellido.get():
                txtLista.insert(END, str(alumno.codigo) + ": " + alumno.nombre + ", " + alumno.apellido + "\n")
        elif txtCodigo.get() != '' and txtNombre.get() != '' and txtApellido.get() == '':
            if int(alumno.codigo) == int(txtCodigo.get()) and alumno.nombre == txtNombre.get():
                txtLista.insert(END, str(alumno.codigo) + ": " + alumno.nombre + ", " + alumno.apellido + "\n")
        elif txtCodigo.get() != '' and txtNombre.get() == '' and txtApellido.get() != '':
            if int(alumno.codigo) == int(txtCodigo.get()) and alumno.apellido == txtApellido.get():
                txtLista.insert(END, str(alumno.codigo) + ": " + alumno.nombre + ", " + alumno.apellido + "\n")
        elif txtCodigo.get() == '' and txtNombre.get() != '' and txtApellido.get() != '':
            if alumno.nombre == txtNombre.get() and alumno.apellido == txtApellido.get():
                txtLista.insert(END, str(alumno.codigo) + ": " + alumno.nombre + ", " + alumno.apellido + "\n")
        elif txtCodigo.get() != '' and txtNombre.get() != '' and txtApellido.get() != '':
            if int(alumno.codigo) == int(txtCodigo.get()) and alumno.nombre == txtNombre.get() and alumno.apellido == txtApellido.get():
                txtLista.insert(END, str(alumno.codigo) + ": " + alumno.nombre + ", " + alumno.apellido + "\n")


'Creamos la ventana'
win = Tk()
win.title('Mantenimiento')
win.geometry('1000x600')
'Creamos las etiquetas'
lblCodigo = Label(win, text="Codigo")
lblCodigo.grid(column=0, row=0)
lblNombre = Label(win, text="Nombre")
lblNombre.grid(column=0, row=1)
lblApellido = Label(win, text="Apellido")
lblApellido.grid(column=0, row=2)
lblLista = Label(win, text="Lista alumnos")
lblLista.grid(column=0, row=3)
'Creamos los campos de texto'
txtCodigo = Entry(win, width=10)
txtCodigo.grid(column=1, row=0)
txtNombre = Entry(win, width=10)
txtNombre.grid(column=1, row=1)
txtApellido = Entry(win, width=10)
txtApellido.grid(column=1, row=2)
txtLista = Text(win, width=30)
txtLista.grid(column=0, row=3)
'Colocamos los botones'
'Para listar'
btnListar = Button(win, text="Listar", width=15, height=1, command=listar)
btnListar.grid(column=3, row=0)
'Para dar de alta'
btnAlta = Button(win, text="Añadir a la lista", width=15, height=1, command=anadir)
btnAlta.grid(column=2, row=0)
'Para dar de baja'
btnBorrar = Button(win, text="Borrar de la lista", width=15, height=1, command=borrar)
btnBorrar.grid(column=2, row=1)
'Para modificar el alumno'
btnModificar = Button(win, text="Modificar datos", width=15, height=1, command=modificar)
btnModificar.grid(column=2, row=2)
'Para guardar los datos en un fichero'
btnGuardar = Button(win, text="Escribir fichero", width=15, height=1, command=crearFichero)
btnGuardar.grid(column=3, row=1)
'Para cargar los datos del fichero'
btnCargar = Button(win, text="Cargar fichero", width=15, height=1, command=cargarFichero)
btnCargar.grid(column=3, row=2)
btnBuscar = Button(win, text="Buscar", width=15, height=1, command=buscar)
btnBuscar.grid(column=4, row=0)
win.mainloop()
