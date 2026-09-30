class Alumno:
    def __init__(
        self,
        nombre:str,
        edad:int,
        tieneMatricula:bool,
        bloqueado:bool,
        precioCurso:float,
        descuento:float,
        nota:float,
    ):
        self.nombre = nombre
        self.edad = edad
        self.tieneMatricula = tieneMatricula
        self.bloqueado = bloqueado
        self.precioCurso = precioCurso
        self.descuento = descuento
        self.nota = nota

    def calcularPrecioFinal(self):
        if self.bloqueado:  
            print("Alumno bloqueado, no puede inscribirse al curso.")
            return 0

    def puedeAcceder(self):
        if self.edad >= 18 and self.tieneMatricula and not self.bloqueado:
            return True
        else:
            return False

    #Creacion de un alumno

    alumno1 = Alumno("Juan, 21, True, False, 1000, 7, 8.5")

    def obtenerCalificacion(self):
        if self.nota < 0 or self.nota > 10:
            print("Nota no valida")
        elif self.nota <5:
            print("suficiente")
        elif self.nota <7:
            print("notable")
        elif self.nota <9:
            print("Excelente")
        

#Informacion del alumno
print("----- INFORMACIÓN DEL ALUMNO -----") 
print("Nombre:", alumno1.nombre) 
print("Edad:", alumno1.edad)
print("Tiene matrícula:", alumno1.tieneMatricula) 
print("Bloqueado:", alumno1.bloqueado) 
print("Precio del curso:", alumno1.precioCurso, "€") 
print("Descuento:", alumno1.descuento, "%") 
print("Precio final:", alumno1.calcularPrecioFinal(), "€") 
print("Puede acceder:", alumno1.puedeAcceder()) 
print("Nota:", alumno1.nota) 
print("Calificación:", alumno1.obtenerCalificacion())


    