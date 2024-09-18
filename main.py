#Project 1 - Hollywood Walk of Fame
import tkinter as tk
import tkinter.font

class Hollywood:
    def __init__(self):
        self.__main_window = tk.Tk()
        self.__main_window.title('Walk of Fame')
        self.create_widget()
        tk.mainloop()
    def create_widget(self):
        #squares
        self.__canvas = tk.Canvas(self.__main_window, width= 612, height= 458)
        self.__canvas.create_rectangle(0, 0, 149, 149, fill= 'light blue', outline= 'light blue')
        self.__canvas.create_rectangle(153, 0, 303, 149, fill= 'SpringGreen4', outline= 'SpringGreen4')
        self.__canvas.create_rectangle(307, 0, 457, 149, fill= 'light pink', outline= 'light pink')
        self.__canvas.create_rectangle(461, 0, 611, 149, fill= 'MediumOrchid2', outline= 'MediumOrchid2')
        self.__canvas.create_rectangle(0, 153, 149, 303, fill= 'khaki', outline= 'khaki')
        self.__canvas.create_rectangle(153, 153, 303, 303, fill='burlywood1', outline= 'burlywood1')
        self.__canvas.create_rectangle(307, 153, 457, 303, fill= 'medium slate blue', outline= 'medium slate blue')
        self.__canvas.create_rectangle(461, 153, 611, 303, fill= 'pale green', outline= 'pale green')
        self.__canvas.create_rectangle(0, 307, 149, 457, fill= 'MediumPurple1', outline= 'MediumPurple1')
        self.__canvas.create_rectangle(153, 307, 303, 457, fill= 'coral1', outline= 'coral1')
        self.__canvas.create_rectangle(307, 307, 457, 457, fill= 'snow3', outline= 'snow3')
        self.__canvas.create_rectangle(461, 307, 611, 457, fill= 'midnight blue', outline= 'midnight blue')

        #stars
        self.__canvas.create_polygon(33, 0, 56, 64, 0, 24, 66, 24, 10, 64, fill= 'DarkGoldenRod2', outline= 'DarkGoldenRod2')
        self.__canvas.create_polygon(186, 0, 209, 64, 153, 24, 219, 24, 163, 64, fill= 'DarkGoldenRod2', outline= 'DarkGoldenRod2')
        self.__canvas.create_polygon(340, 0, 363, 64, 307, 24, 373, 24, 317, 64, fill= 'DarkGoldenRod2', outline= 'DarkGoldenRod2')
        self.__canvas.create_polygon(494, 0, 517, 64, 461, 24, 527, 24, 471, 64, fill= 'DarkGoldenRod2', outline= 'DarkGoldenRod2')
        self.__canvas.create_polygon(33, 153, 56, 217, 0, 177, 66, 177, 10, 217, fill= 'DarkGoldenRod2', outline= 'DarkGoldenRod2')
        self.__canvas.create_polygon(186, 153, 209, 217, 153, 177, 219, 177, 163, 217, fill= 'DarkGoldenRod2', outline= 'DarkGoldenRod2')
        self.__canvas.create_polygon(340, 153, 363, 217, 307, 177, 373, 177, 317, 217, fill= 'DarkGoldenRod2', outline= 'DarkGoldenRod2')
        self.__canvas.create_polygon(494, 153, 517, 217, 461, 177, 527, 177, 471, 217, fill= 'DarkGoldenRod2', outline= 'DarkGoldenRod2')
        self.__canvas.create_polygon(33, 307, 56, 371, 0, 331, 66, 331, 10, 371, fill= 'DarkGoldenRod2', outline= 'DarkGoldenRod2')
        self.__canvas.create_polygon(186, 307, 209, 371, 153, 331, 219, 331, 163, 371 , fill= 'DarkGoldenRod2', outline= 'DarkGoldenRod2')
        self.__canvas.create_polygon(340, 307, 363, 371, 307, 331, 373, 331, 317, 371, fill= 'DarkGoldenRod2', outline= 'DarkGoldenRod2')
        self.__canvas.create_polygon(494, 307, 517, 371, 461, 331, 527, 331, 471, 371, fill= 'DarkGoldenRod2', outline= 'DarkGoldenRod2')

        #text
        self.__font_options = tk.font.Font(family = 'Tekton Pro', size = 11, weight = 'bold')
        self.__canvas.create_text(32, 33, text= 'Aguilera', font= self.__font_options, fill= 'dark slate gray')
        self.__canvas.create_text(187, 33, text= 'Goldberg', font= self.__font_options, fill= 'light pink')
        self.__canvas.create_text(339, 33, text= 'Elliott', font= self.__font_options, fill= 'forest green')
        self.__canvas.create_text(494, 33, text= 'Chestnut', font= self.__font_options, fill= 'aquamarine')
        self.__canvas.create_text(34, 186, text= 'DiCaprio', font= self.__font_options, fill= 'midnight blue')
        self.__canvas.create_text(190, 186, text= 'Quintanilla', font= self.__font_options, fill= 'OrangeRed2')
        self.__canvas.create_text(339, 186, text= 'Marley', font= self.__font_options, fill= 'LightGoldenrod2')
        self.__canvas.create_text(494, 186, text= 'Usher', font= self.__font_options, fill= 'dark green')
        self.__canvas.create_text(32, 340, text= 'Spears', font= self.__font_options, fill='purple4')
        self.__canvas.create_text(185, 340, text= 'Olsen', font= self.__font_options, fill= 'brown4')
        self.__canvas.create_text(339, 340, text= 'Monroe', font= self.__font_options, fill= 'purple4')
        self.__canvas.create_text(494, 340, text= 'LaBelle', font= self.__font_options, fill= 'snow')
        self.__canvas.pack()
obj = Hollywood()
