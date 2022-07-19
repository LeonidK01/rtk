import csv
import tkinter
from tkinter import ttk, messagebox
import mysql.connector
from tkinter import *
import tkinter as tk

Type_1=[]
Type_2=[]
Type_3=[]


def new_rule(event):
    new_w=Tk()
    new_w.geometry("800x500")
    row_id = listBox.selection()[0]
    select = listBox.set(row_id)
    print(select)
    root.destroy()
    type_label = ttk.Label(new_w, text="Тип")
    type_label.grid(column=0, row=0, padx=5, pady=5)
    attr_label = ttk.Label(new_w, text="Атрибут")
    attr_label.grid(column=1, row=0, padx=5, pady=5)
    oper_label = ttk.Label(new_w, text="Оператор")
    oper_label.grid(column=2, row=0, padx=5, pady=5)
    value_label = ttk.Label(new_w, text="Значение")
    value_label.grid(column=3, row=0, padx=5, pady=5)
    mysqldb = mysql.connector.connect(host="localhost", user="root", password="root", database="rules")
    mycursor = mysqldb.cursor()
    mycursor.execute("SELECT `type`, `attribute`, `operator`, `value` FROM `rule` WHERE `id_rule`=1")
    records = mycursor.fetchall()
    type_0=ttk.Entry(new_w)
    type_1 = ttk.Entry(new_w)
    type_2 = ttk.Entry(new_w)
    type_3 = ttk.Entry(new_w)
    type_4 = ttk.Entry(new_w)
    type_5 = ttk.Entry(new_w)
    combo_type0 = ttk.Combobox(new_w,
                                values=[
                                    "Тип задания 1",
                                    "Тип задания 2",
                                    "Тип задания 3",
                                    "Тип связи",
                                    "Признак запроса ОГВ",
                                    "Признак соответствия суммы критериям НС"])
    combo_type1 = ttk.Combobox(new_w,
                               values=[
                                   "Тип задания 1",
                                   "Тип задания 2",
                                   "Тип задания 3",
                                   "Тип связи",
                                   "Признак запроса ОГВ",
                                   "Признак соответствия суммы критериям НС"])
    combo_type2 = ttk.Combobox(new_w,
                               values=[
                                   "Тип задания 1",
                                   "Тип задания 2",
                                   "Тип задания 3",
                                   "Тип связи",
                                   "Признак запроса ОГВ",
                                   "Признак соответствия суммы критериям НС"])
    combo_type3 = ttk.Combobox(new_w,
                               values=[
                                   "Тип задания 1",
                                   "Тип задания 2",
                                   "Тип задания 3",
                                   "Тип связи",
                                   "Признак запроса ОГВ",
                                   "Признак соответствия суммы критериям НС"])
    combo_type4 = ttk.Combobox(new_w,
                               values=[
                                   "Тип задания 1",
                                   "Тип задания 2",
                                   "Тип задания 3",
                                   "Тип связи",
                                   "Признак запроса ОГВ",
                                   "Признак соответствия суммы критериям НС"])
    combo_type5 = ttk.Combobox(new_w,
                               values=[
                                   "Тип задания 1",
                                   "Тип задания 2",
                                   "Тип задания 3",
                                   "Тип связи",
                                   "Признак запроса ОГВ",
                                   "Признак соответствия суммы критериям НС"])
    for i, (id, stname, course, fee) in enumerate(records, start=0):
        if(i==0):
            type_0.insert(0,str(id))
            type_0.grid(column=0, row=i+1, padx=5, pady=5)
            combo_type0.insert(0,str(stname))
            combo_type0.grid(column=1, row=i+1, padx=5, pady=5)
            if(combo_type0.get()=="Тип задания 1"):
                combo_value0=ttk.Combobox(new_w, values=Type_1)
                combo_value0.grid(column=3, row=i+1, padx=5, pady=5)
                combo_value0.insert(0,str(fee))
            if (combo_type0.get() == "Тип задания 2"):
                combo_value0 = ttk.Combobox(new_w, values=Type_2)
                combo_value0.grid(column=3, row=i + 1, padx=5, pady=5)
                combo_value0.insert(0, str(fee))

        if(i==1):
            type_1.insert(0,str(id))
            type_1.grid(column=0, row=i + 1, padx=5, pady=5)
            combo_type1.insert(0,str(stname))
            combo_type1.grid(column=1, row=i+1, padx=5, pady=5)
        if (i == 2):
            type_2.insert(0, str(id))
            type_2.grid(column=0, row=i + 1, padx=5, pady=5)
            combo_type2.insert(0,str(stname))
            combo_type2.grid(column=1, row=i+1, padx=5, pady=5)
        if (i == 3):
            type_3.insert(0, str(id))
            type_3.grid(column=0, row=i + 1, padx=5, pady=5)
            combo_type3.insert(0,str(stname))
            combo_type3.grid(column=1, row=i+1, padx=5, pady=5)
        if (i == 4):
            type_4.insert(0, str(id))
            type_4.grid(column=0, row=i + 1, padx=5, pady=5)
            combo_type4.insert(0,str(stname))
            combo_type4.grid(column=1, row=i+1, padx=5, pady=5)
        if (i == 5):
            type_5.insert(0, str(id))
            type_5.grid(column=0, row=i + 1, padx=5, pady=5)
            combo_type5.insert(0,str(stname))
            combo_type5.grid(column=1, row=i+1, padx=5, pady=5)

    new_w.mainloop()


def show():
    mysqldb = mysql.connector.connect(host="localhost", user="root", password="root", database="rules")
    mycursor = mysqldb.cursor()
    mycursor.execute("SELECT * FROM `routing_rule`")
    records = mycursor.fetchall()
    print(records)

    for i, (id, stname, course, fee) in enumerate(records, start=1):
        listBox.insert("", "end", values=(id, stname, course, fee))
        mysqldb.close()

with open('type.csv') as f:
    reader = csv.reader(f,delimiter = ";")
    count=0
    for row in reader:
        if count==0:
            count+=1
        else:
            Type_1.append(row[0])
            Type_2.append(row[1])
            Type_3.append(row[2])
type_1=set(Type_1)
type_2=set(Type_2)
type_3=set(Type_3)
root = Tk()
root.geometry("800x500")

cols = ('id_rule', 'rule_name', 'queue','rank')
listBox = ttk.Treeview(root, columns=cols, show='headings' )

for col in cols:
    listBox.heading(col, text=col)
    listBox.grid(row=1, column=0, columnspan=2)
    # listBox.place(x=10, y=200)

show()
listBox.bind('<Double-Button-1>', new_rule)

root.mainloop()

