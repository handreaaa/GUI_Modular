# GUI_Modular
from tkinter import *
import csv 

class RootGUI():
    def __init__(self):
        '''Initializing the root GUI and other comps of the program'''
        self.root = Tk()
        self.root.title("Serial communication")
        self.root.geometry("360x120")
        self.root.config(bg="white")

# Class to setup and create the communication manager with MCU
class ComGui():
    def __init__(self, root):
        '''
        Initialize the connexion GUI and initialize the main widgets 
        '''
        # Initializing the Widgets
        self.root = root
        self.frame = LabelFrame(root, text="Com Manager", padx=5, pady=5, bg="white")
        ...
        # Botón para guardar datos en CSV 
        self.btn_save_csv = Button(self.frame, text="Save as CSV", width=10, state="disabled", command=self.save_data_to_csv)
        ...
        # Para asegurar que todos los elementos sean mostrados
        self.publish()

    def publish(self):
        ...
        
        self.btn_save_csv.grid(column=3, row=4)

    def save_data_to_csv(self):
        # Para guardar los datos actuales de la gráfica en CSV
        data = [["Time", "Value"], [1, 100], [2, 200], [3, 300]]  
        with open('data.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)
        print("Data saved to CSV.")  # Confirmación en la consola

    ...

if __name__ == "__main__":
    root = RootGUI()
    com_gui = ComGui(root.root)
    root.root.mainloop()  # Asegúrate de llamar a mainloop para que la GUI se muestre correctamente