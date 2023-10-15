def exit():
    root.destroy()
 
def bmi():
    #bmi calculation
    h = int(height_entry.get())
    w = int(weight_entry.get())
    b = 703 * (w / ( h ** 2))

fina   
    #gets label with what their BMI corresponds to 
    if b < 18.5:
        under = Label(window, text = "According to Your BMI you are underweight", bg = 'black', fg = 'red')
        under.pack()
    elif b > 18.5 and b < 24.9:
        healthy = Label(window, text = "According to your BMI you are at a healthy weight", bg = 'black', fg = 'green')
        healthy.pack()
    elif b > 24.9 and b < 29.9:
        over = Label(window, text = "According to your BMI you are overweight", bg = 'black', fg = 'orange')
        over.pack()
    else:
        obese = Label(window,text = "According to your BMI you are obese", bg = 'black', fg = 'red')
        obese.pack()


        
    #brings results window up
    window.state('normal')
    #printing results
    label= Label(window,text="",font=("Arial",22))
    label.configure(text=b)
    label.pack()
    #go back button
    goback = tk.Button(window, text='Go Back', font=("Arial",18), bg = 'white', fg = 'black',command = clear_all)
    goback.pack()
    return b


def valid(h,w):
    h = len(height_entry.get())
    w = len(weight_entry.get())

    if h or w == 0:
        nogood = Label(window, text = "Enter something in both fields")
        goback = tk.Button(window, text='Go Back', font=("Arial",18), bg = 'white', fg = 'black',command = clear_all)
        goback.pack()
    else:
        return
        
def clear_all():
    #resets app
    window.state('withdrawn')
    height_entry.delete(0,100)
    weight_entry.delete(0,400)
    height_entry.focus_set()

def get_info():
    #getting person info
    import pickle
    
    name = name_entry.get()
    bmi = bmi.get()
    List = [[name, bmi]]

    #write list to pickle
    with open('file','wb') as fp:
        pickle.dump(names, fp)
    
    


import tkinter as tk
from tkinter import *

root=tk.Tk()
root.configure(background = 'sky blue')
root.geometry("500x500")
root.title("The BMI Calculator App")

#configuring results window
window = Toplevel(root)
window.title("Results")
window.state('withdrawn')
window.configure(background = 'red')

resultslabel = tk.Label(window, text = "Results: ", bg = 'white', fg = 'black')
resultslabel.pack()

result = tk.Label(window, print(bmi), bg = 'white', fg = 'black')
result.pack()

#Setting up Title frame

page1 = tk.Frame(root)
page1.grid(row=0, column=0)
lb1 = tk.Label(page1, text="The magnificent BMI calculator")
lb1.grid(row = 10, column = 1, pady=10)







#Create height label
label1 = tk.Label(root, text = "Height in inches: ", fg = 'black', bg = 'white')

#Create weight label
label2 = tk.Label(root, text = "Weight in pounds: ", fg = 'black', bg = 'white')

#Create calculate label
#label3 = tk.Label(root, text = "CALCULATE", fg = 'red', bg = 'white

#Setting up label location
label1.grid(row = 1, column = 0, padx = 10, pady = 10)
label2.grid(row = 2, column = 0, padx = 10, pady = 10)

#Create entry boxes
height_entry = tk.Entry(root)
weight_entry = tk.Entry(root)

#setting up entry box locations
height_entry.grid(row = 1, column = 1, padx = 10, pady = 10)
weight_entry.grid(row = 2, column = 1, padx = 10, pady = 10)

#create calculate button
btn1 = tk.Button(root, text = "CALCULATE", fg = 'red', bg = 'black', command = bmi) 
btn2 = tk.Button(root, text = "Exit", fg = 'black', bg = 'white', command = exit)

#button locations
btn1.grid(row = 4, column = 1, pady = 10)
btn2.grid(row = 12, column = 3, pady = 10)




root.mainloop()
