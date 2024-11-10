import tkinter as tk

app=tk.Tk()
app.title("TO-DO LIST")
app.geometry("352x352")

task_input=tk.Entry(app,text="enter task",width=20,bg="blue")
task_input.pack()
listbox=tk.Listbox(app)
listbox.pack()   

tasks=[]
#default list
#tasks =["meet a friend for a lunch","learn a musical instrument","eat sushi"]

def update():
    for task in tasks:
        listbox.insert("end",task)
    
def view_tasks():
    tasks = listbox.get(0,tk.END)
    print('current to-do-list:')
    for task in tasks:
        print(task)
    
def add_tasks():
    task =task_input.get()
    if tasks != "":
      listbox.insert(tk.END,task)
    update()
    print(f"{task} added successfully!")

def remove_task():
    task_index = listbox.curselection()
    listbox.delete(task_index)
    update() 
    
add_button = tk.Button(app,text="Add task",width=20,bg="yellow",command=add_tasks)
add_button.pack()
remove_button = tk.Button(app,text="Remove task",width=20,bg="yellow",command=remove_task)
remove_button.pack()
view_button = tk.Button(app,text="view list",width=20,bg="yellow",command= view_tasks)
view_button.pack()

app.mainloop()



