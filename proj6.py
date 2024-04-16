import tkinter 
import tkinter as Tk
from tkinter import messagebox

def main():
    my_gui = PropertyTaxGUI()

class PropertyTaxGUI():

    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title("Property Tax Calculator")
        self.top_frame = tkinter.Frame()
        self.mid_frame = tkinter.Frame()
        self.third_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()

        #create widgets for the top frame
        self.prompt_label = tkinter.Label(self.top_frame,
                                          text='Enter the property value: $')
        self.prop_value = tkinter.Entry(self.top_frame,
                                        width=10)

        #pack the top frame's widgets
        self.prompt_label.pack(side='left')
        self.prop_value.pack(side='left')

        #create widgets for the middle frame
        self.assess_val = tkinter.Label(self.mid_frame,
                                        text='Assessment Value: $')

        #need a stringvar object to associate with an output label
        self.value = tkinter.StringVar()

        #create a label and associate it with the stringvar object
        self.assess_label = tkinter.Label(self.mid_frame,
                                          textvariable=self.value)

        #pack the middle frame's widgets
        self.assess_val.pack(side='left')
        self.assess_label.pack(side='left')

        #create the widgets for the third frame
        self.prop_tax = tkinter.Label(self.third_frame,
                                      text='Property Tax: $')

        #need a stringvar object to associate witih second output label
        self.value2 = tkinter.StringVar()

        #create a label and associate it with the stringvar object
        self.prop_tax_val = tkinter.Label(self.third_frame,
                                          textvariable=self.value2)

        #pack the third frame's widgets
        self.prop_tax.pack(side='left')
        self.prop_tax_val.pack(side='left')

        #create the button widgets for the bottom frame
        self.calc_button = tkinter.Button(self.bottom_frame,
                                          text='Calculate',
                                          command=self.calc_button_event)
        self.quit_button = tkinter.Button(self.bottom_frame,
                                          text='Quit',
                                          command=self.main_window.destroy)

        #pack the buttons
        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')

        #pack the frames
        self.top_frame.pack()
        self.mid_frame.pack()
        self.third_frame.pack()
        self.bottom_frame.pack()
        
        #enter the tkinter main loop
        tkinter.mainloop()

    def calc_button_event(self):
        self.calculate()
       # self.taxCalc()


    def calculate(self):
       self.propVal = float(self.prop_value.get())

       self.assessVal = self.propVal*0.6

       self.property_tax = self.assessVal * 0.0075
       self.value.set(self.assessVal)
       self.value2.set(self.property_tax)


main()