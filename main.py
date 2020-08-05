from tkinter import *
from tkinter import colorchooser

class Painting():
	def __init__(self):
		self.eraser = False
		self.oval = 0
		self.brush_size = 1

		self.old_x = None
		self.old_y = None

		self.color = "black"
		self.bg_color = "white"
		self.width = 1200
		self.height = 700
		self.screen_resolution = str(self.width)+'x'+str(self.height) + "+300+300"
		# Создание окна
		self.root = Tk()
		self.root.geometry(self.screen_resolution)
		self.root.resizable(width=False, height=False)
		self.root.title("Paint")

		self.root.bind("<Motion>", self.motion)

		# Создание панели инструментов 
		self.interface()

		# Создание Канвы 
		self.canvas = Canvas(self.root,width=self.width,height=self.height,bg=self.bg_color)
		self.canvas.bind("<B1-Motion>",self.draw)
		self.canvas.bind("<ButtonRelease-1>",self.null)
		self.canvas.pack(side=BOTTOM)

		# Цикл программы
		self.root.mainloop()

	def interface(self):
		tool_bar = Frame(self.root,bg="gray")
		

		image_eraser = PhotoImage(file='img/eraser.png')
		btn_erase = Button(tool_bar,text="Erase",image=image_eraser)
		btn_erase.image_eraser = image_eraser
		btn_erase.grid(row=0,column=0,padx=4,pady=4)
		btn_erase.bind("<Button-1>", self.erase)

		image_brush = PhotoImage(file='img/brush.png')
		btn_draw = Button(tool_bar,text="Draw",image=image_brush)
		btn_draw.image_brush = image_brush
		btn_draw.grid(row=0,column=1,padx=4,pady=4)
		btn_draw.bind("<Button-1>", self.btn_draw)

		image_color = PhotoImage(file='img/color.png')
		btn_color = Button(tool_bar,text="Color",image=image_color)
		btn_color.image = image_color
		btn_color.grid(row=0,column=2,padx=4,pady=4)
		btn_color.bind("<Button-1>", self.choose_color)

		image_clear = PhotoImage(file='img/drop.png')
		btn_clear = Button(tool_bar,text="Clear",image=image_clear)
		btn_clear.image = image_clear
		btn_clear.grid(row=0,column=3,padx=4,pady=4)
		btn_clear.bind("<Button-1>", self.clear)

		self.spin = Spinbox(tool_bar, from_=1, to=100, width=5, command=self.choose_br_size)  
		self.spin.grid(row=0, column=4)

		btn_save = Button(tool_bar,text="Save",height=2,width=5)
		btn_save.grid(row=0,column=5,padx=4,pady=4)
		btn_save.bind("<Button-1>", self.save)
		
		btn_load = Button(tool_bar,text="Load",height=2,width=5)
		btn_load.grid(row=0,column=6,padx=4,pady=4)
		btn_load.bind("<Button-1>", self.load)
		tool_bar.pack(side=TOP,fill=X)

	def save(self,event):
		pass

	def load(self,event):
		pass

	def choose_br_size(self): # Выбор размера кисти
		self.brush_size = int(self.spin.get())

	def clear(self,event): # Очистка холста
		self.canvas.delete(ALL)

	def btn_draw(self,event): # После отмены ластика, вернется прерыдущее значение цвета 
		self.eraser = False
		self.color = self.backup_color

	def erase(self,event): # Реализация ластика
		self.eraser = True
		self.backup_color = self.color
		self.color = self.bg_color

	def choose_color(self,event): # Выбор цвета кисти
		if self.eraser != True:
			c = colorchooser.askcolor()
			self.color = c[1]

	def null(self,event): # Сброс координат
		self.old_x = None
		self.old_y = None

	def draw(self,event): # Рисование
		if self.old_x and self.old_y:
			self.canvas.create_line(self.old_x,self.old_y,
									event.x,event.y,
									width=self.brush_size,
									fill=self.color,
									capstyle=ROUND,smooth=True)
		self.old_x = event.x
		self.old_y = event.y



	def motion(self,event): # Создание движущегося за курсором "овала"
	    x, y = event.x, event.y  

	    self.canvas.delete(self.oval)

	    radius = self.brush_size/2

	    x_max = x + radius
	    x_min = x - radius
	    y_max = y + radius
	    y_min = y - radius

	    self.oval = self.canvas.create_oval(x_max, y_max, x_min, y_min, outline="black",fill="white")

def main():
	mainclass = Painting()

main()