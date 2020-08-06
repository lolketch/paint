from tkinter import *
from tkinter import colorchooser

class Painting():
	def __init__(self):
		self.erase = False
		self.draw = True

		self.ellipse_cursor = 0
		self.brush_size = 1

		self.old_x = None
		self.old_y = None

		self.color = "black"
		self.bg_color = "white"
		self.width = 1200
		self.height = 700
		self.screen_resolution = str(self.width)+'x'+str(self.height) + "+300+300"
		#Создание окна
		self.root = Tk()
		self.root.geometry(self.screen_resolution)
		self.root.resizable(width=False, height=False)
		self.root.title("Paint")

		self.root.bind("<Motion>", self.cursor)

		#Создание панели инструментов 
		self.interface()

		#Создание Канвы 
		self.canvas = Canvas(self.root,width=self.width,height=self.height,bg=self.bg_color)
		self.canvas.bind("<B1-Motion>",self.mouse_move)
		self.canvas.bind("<ButtonRelease-1>",self.null)
		self.canvas.pack(side=BOTTOM)

		#Цикл программы
		self.root.mainloop()

	def interface(self): #Создание панели инструментов 
		tool_bar = Frame(self.root,bg="#e0e0e0")
		

		image_eraser = PhotoImage(file='img/eraser.png')
		btn_erase = Button(tool_bar,text="Erase",image=image_eraser)
		btn_erase.image_eraser = image_eraser
		btn_erase.grid(row=0,column=0,padx=4,pady=4)
		btn_erase.bind("<Button-1>", self.btn_erase)

		image_brush = PhotoImage(file='img/brush.png')
		btn_draw = Button(tool_bar,text="Draw",image=image_brush)
		btn_draw.image_brush = image_brush
		btn_draw.grid(row=1,column=0,padx=4,pady=4)
		btn_draw.bind("<Button-1>", self.btn_draw)

		image_color = PhotoImage(file='img/color.png')
		btn_color = Button(tool_bar,text="Color",image=image_color)
		btn_color.image = image_color
		btn_color.grid(row=2,column=0,padx=4,pady=4)
		btn_color.bind("<Button-1>", self.choose_color)

		image_clear = PhotoImage(file='img/drop.png')
		btn_clear = Button(tool_bar,text="Clear",image=image_clear)
		btn_clear.image = image_clear
		btn_clear.grid(row=3,column=0,padx=4,pady=4)
		btn_clear.bind("<Button-1>", self.clear)

		self.spin = Spinbox(tool_bar, from_=1, to=100, width=5, command=self.choose_br_size)  
		self.spin.grid(row=4, column=0)

		tool_bar.pack(side=RIGHT,fill=Y)

	def mouse_move(self,event): #Режимы рисования и старания(ластика)
		if self.draw and self.erase == False:
			if self.old_x and self.old_y:
				self.canvas.create_line(self.old_x,self.old_y,
										event.x,event.y,
										width=self.brush_size,
										fill=self.color,
										capstyle=ROUND,smooth=True)
			self.old_x = event.x
			self.old_y = event.y
		if self.erase and self.draw == False:
			if self.old_x and self.old_y:
				self.canvas.create_line(self.old_x,self.old_y,
										event.x,event.y,
										width=self.brush_size,
										fill=self.bg_color,
										capstyle=ROUND,smooth=True)
			self.old_x = event.x
			self.old_y = event.y

	def choose_br_size(self): #Выбор размера кисти
		self.brush_size = int(self.spin.get())

	def clear(self,event): #Очистка холста
		self.canvas.delete(ALL)

	def btn_draw(self,event): #Выбор режима рисования 
		self.erase = False
		self.draw = True

	def btn_erase(self,event): #Выбор режима ластика
		self.erase = True
		self.draw = False

	def choose_color(self,event): #Выбор цвета кисти
		c = colorchooser.askcolor()
		self.color = c[1]

	def null(self,event): #Сброс координат
		self.old_x = None
		self.old_y = None

	def cursor(self,event): #Создание эллипса, движущегося за курсором 
		x, y = event.x, event.y  

		self.canvas.delete(self.ellipse_cursor)

		radius = self.brush_size/2

		x_max = x + radius
		x_min = x - radius
		y_max = y + radius
		y_min = y - radius

		self.ellipse_cursor = self.canvas.create_oval(x_max, y_max, x_min, y_min, outline="black",fill="white")

def main():
	mainclass = Painting()

main()