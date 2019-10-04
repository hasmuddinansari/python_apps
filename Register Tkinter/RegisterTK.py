from tkinter import *
import tkinter.messagebox


#saving all data in csv file...

import csv
filename= 'Userdata.csv'
with open(filename, 'w', newline="") as file:
    writerr = csv.writer(file)
    writerr.writerow(["First", "Last", "DOB", "Gender", "Country", "Code"])
    file.close()


#all calling functions:::
def submited():
    first= f_var.get()
    last=l_var.get()
    dobirth=dob_var.get()
    gender=gender_var.get()
    country = country_var.get()
    code = code_var.get()
    tkinter.messagebox.showinfo("Submited", f'Name: {first} {last},\n Date of year {dobirth}\n Gender: {gender}\n Country: {country}\n Language: {code}')
    filename = "Userdata.csv"
    with open(filename, 'a', encoding="utf-8", newline='') as file:
        writer = csv.writer(file)
        writer.writerow([first, last, dobirth, gender, country, code])


def clear():
    global f_var
    global l_var
    global dob_var
    global gender_var
    global country_var
    global code_var
    l_var.set("")
    f_var.set("")
    dob_var.set("")
    gender_var.set("")
    country_var.set("Select Country")
    code_var.set("")



#setting window..

window = Tk()
window.geometry("400x500")
window.title("Registeration")

#Heading

heading = Label(window, text="Registeration Form", relief="solid",fg="white",bg="black", font= ("arial", 20, "bold")).pack()

#Entry:

f_name = Label(window, text="First Name  :", font= ("arial", 12, "bold"))
f_name.place(x=40, y=60)

l_name = Label(window, text="Last Name   :", font= ("arial", 12, "bold"))
l_name.place(x=40, y=100)

dob = Label(window, text="Date Of Birth   :", font= ("arial", 12, "bold"))
dob.place(x=40, y=140)

country = Label(window, text="Country:", font= ("arial", 12, "bold"))
country.place(x=40, y=180)

Gender = Label(window, text="Gender:", font= ("arial", 12, "bold"))
Gender.place(x=40, y=220)

Language = Label(window, text="Language:", font= ("arial", 12, "bold"))
Language.place(x=40, y=260)


#Radio buton and chekbutton for lang and gender

#input :function to getting values:
f_var = StringVar()
l_var = StringVar()
dob_var= StringVar()
country_var = StringVar()
gender_var= StringVar()
code_var = StringVar()

#input field
f_ent = Entry(window,width=30, textvar=f_var).place(x=200, y=63)
l_ent = Entry(window,width=30, textvar=l_var).place(x=200, y=103)
dob_ent = Entry(window,width=30, textvar=dob_var).place(x=200, y=143)

#list

countries = ["India", "Nepal", "Canada", "America","Kathmandu", "SriLanka"]
droplist = OptionMenu(window,country_var, *countries)
country_var.set("Select Country")
droplist.place(x=200, y=183)


#chekbox:

male = Radiobutton(window, text="Male", variable=gender_var, value="Male").place(x=200, y=223)
female = Radiobutton(window, text="Female", variable=gender_var, value="Female").place(x=260, y=223)

java = Radiobutton(window, text="Java", variable=code_var, value="java").place(x=200, y=263)
python = Radiobutton(window, text="Python", variable=code_var, value="Python").place(x=260, y=263)
JavaScript = Radiobutton(window, text="JavaScript", variable=code_var, value="JavaScript").place(x=320, y=263)

#buttons:

submit = Button(window, text="Submit",width=30, bg="black",fg="white",font=("arial",14, "bold"),relief="groove", command=submited).place(x=20, y=400)
clear = Button(window, text="Clear",width=30, bg="black",fg="white",font=("arial",14, "bold"),relief="groove", command=clear).place(x=20, y=450)


window.mainloop()