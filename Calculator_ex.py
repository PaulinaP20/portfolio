from tkinter import *
import ast

root=Tk()
root.title('Calculator')
root.configure(bg='black')

#create module read of number
i=0
def get_number(number):
    global i
    display.insert(i,number)
    i+=1

def get_operation(operator):
    global i
    lenght = len(operator)
    display.insert(i,operator)
    i+=lenght


def clean_all():
    display.delete(0, END)

def calculate():
    entire_string=display.get()
    try:
        node=ast.parse(entire_string, mode='eval')
        result=eval(compile(node,'<string>','eval'))
        clean_all()
        display.insert(0,result)
    except Exception:
        clean_all()
        display.insert(0,'Error')

def undo():
    entire_string=display.get()
    if len(entire_string):
        new_string=entire_string[:-1]
        clean_all()
        display.insert(0,new_string)
    else:
        clean_all()

#create entry
display=Entry(root)
display.grid(row=1, columnspan=9)

#create a button od number

numbers=[1,2,3,4,5,6,7,8,9]
counter=0
for x in range(3):
    for y in range(3):
        button_text=numbers[counter]
        button=Button(root,width=3, height=3, text= button_text,command=lambda text=button_text:get_number(text))
        button.grid(row=x+2, column=y+2)
        counter+=1

#create 0 in calculate

Button(root, text='0',width=3, height=3,command=lambda:get_number(0)).grid(row=x+3, column=3, padx=2, pady=2)

#create operations
count=0
operations=['+','-','*','/','%','**2','**',]
for x in range(4):
    for y in range(2):
        if count<len(operations):
            button=Button(root,text=operations[count], width=3, height=3, command=lambda text=operations[count]:get_operation(text))
            count += 1
            button.grid(row=x+2, column=y+10, padx=3, pady=2)

#create delete and =
button=Button(root, text='=', width=3, height=3,command=calculate).grid(row=5,column=2)
button=Button(root,text='<-',width=3,height=3,command=undo).grid(row=5,column=4)
#create button clear all
button=Button(root,text='AC', width=3, heigh=3, command=clean_all).grid(row=5,column=11)
root.mainloop()