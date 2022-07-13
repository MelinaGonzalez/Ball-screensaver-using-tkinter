#Python Screensaver using tkinter

import tkinter as tk #librería que permite generar interfaces gráficas
from random import randint #librería que permite elecciones aleatorias de entre un grupo de objetos

class RandomBall: #crea la clase de las bolitas y las elige aleatoriamente
	def __init__(self, canvas, scrWidth, scrHight):
		self.canvas = canvas
		self.scrWidth = scrWidth #ancho
		self.scrHight = scrHight #alto
		
		#define entre qué posiciones del ancho de la pantalla puede ubicarse la pelotita
		self.xpos = randint(70, int(self.scrWidth -70)) 
		#define entre qué posiciones del alto de la pantalla puede ubicarse la pelotita
		self.ypos = randint(70, int(self.scrHight -70)) 
		
		#define la velocidad de la pelotita en x, aleatoria entre 6 y 12
		self.dx = randint(6, 12) 
		#define la velocidad de la pelotita en y, aleatoria entre 6 y 12
		self.dy = randint(6, 12) 
		
		#define aleatoriamente el radio de la pelotita, entre 40 y 70
		self.radius = randint(40, 70) 
		
		#elige aleatoriamente el color
		self.color = f"#{randint(0,255):0>2x}{randint(0,255):0>2x}{randint(0,255):0>2x}" 
		
	def createBall(self): #crea la pelotita
		#ubica el centro de la pelotita en x e y y define el color y tamaño
		x1 = self.xpos - self.radius 
		y1 = self.ypos - self.radius 
		x2 = self.xpos + self.radius
		y2 = self.ypos + self.radius		 
		self.item = self.canvas.create_oval(x1, y1, x2, y2, fill=self.color, outline=self.color)
		
	def moveBall(self): #mueve la pelotita
		self.xpos += self.dx #mueve la pelotita en x
		self.ypos += self.dy #mueve la pelotita en y
		
		if (self.xpos > (self.scrWidth - self.radius)) or (self.xpos <= self.radius):
			#hace que la pelotita se devuelva horizontalmente si llegó al límite de la pantalla
			self.dx = -self.dx 
		if (self.ypos > (self.scrHight - self.radius)) or (self.ypos <= self.radius):
			#hace que la pelotita se devuelva verticalmente si llegó al límite de la pantalla
			self.dy = -self.dy 
		
		self.canvas.move(self.item, self.dx, self.dy)


class ScreenSaver:  #crea el programa salvapantallas
	def __init__(self, master, numBalls): #sus atributos son el so y la cantidad de pelotitas
		self.master = master
		#obtiene ancho y alto de la pantalla
		w, h = self.master.winfo_screenwidth(), self.master.winfo_screenheight() 
		self.balls = [] #crea una lista de pelotitas para poder trabajar con varias
		
		self.master.overrideredirect(True)
		self.master.geometry(f"{w}x{h}+0+0") #define el tamaño de la pantalla
		self.master.attributes('-alpha', 0.3)
		#esto hace que el salvapantallas se quite si se toca cualquier tecla
		self.master.bind("<Any-KeyPress>", self.quit)
		#esto hace que el salvapantallas se quite si se toca cualquier botón del mouse 
		self.master.bind("<Any-Button>", self.quit) 
		#esto hace que el salvapantallas se quite si se mueve el mouse
		self.master.bind("<Motion>", self.quit) 
		
		self.canvas = tk.Canvas(self.master, width=w, height=h)
		self.canvas.pack()
		
		for i in range(numBalls): #crea todas las bolitas
			#elige aleatoriamente las características de la bolita y define la pantalla
			ball = RandomBall(self.canvas, scrWidth=w, scrHight=h) 
			ball.createBall() #crea una bolita
			self.balls.append(ball) #agrega la bolita a la lista de bolitas
		
		self.runScreenSaver() #corre o ejecuta el salvapantallas
		
	def runScreenSaver(self): #define el método que corre o ejecuta el salvapantallas
		for ball in self.balls: #trabaja con todas las bolitas
			ball.moveBall() #llama al método que mueve las bolitas
		#luego de 20 minutos el salvapantallas se activa
		self.master.after(20, self.runScreenSaver) 
		
	def quit(self, event): #define el evento que hace que el salvapantallas se quite
		self.master.destroy()


if __name__=="__main__":
	#define la raíz (master), es lo que le da el control del sistema operativo cuando
	#pasa el tiempo necesario para que el programa empiece a ejecutarse
	root = tk.Tk()
	#llama a la clase ScreenSaver y le manda por parámetros la raíz (master)
	#y el número de bolitas con que va a trabajar
	ScreenSaver(root, 8) 
	#finaliza la ejecución y cierra la ventana cuando se cumplieron las condiciones
	#para que el salvapantallas se quite
	root.mainloop() 
