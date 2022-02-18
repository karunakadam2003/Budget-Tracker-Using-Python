'''
Created on 19-Dec-2021

@author: Karuna
'''
from tkinter import *
from tkinter import messagebox
# from Expenses import expenses
import pandas as pd
import os
import csv
import datetime
import matplotlib.pyplot as plt


root = Tk()
income=0
def OK():
    uname = e1.get()
    password = e2.get()                                #progress bar
    if(uname == "" and password == ""):
        messagebox.showerror("Error","Blank not allowed")
    elif(uname == "Admin" and password == "123"):
        messagebox.showinfo("login","Login successfully")
        button = Button(root, text="Next Page", bg='White', fg='Black',font=("Arial",10,'bold'),command=lambda: New_Window())
        button.grid(row = 80, column=55)
    else:
        messagebox.showerror("Error","Invalid Username and Password")
       
def add_money():
   deposit =int(input("Enter the amount to deposit: "))
   global income
   income+=deposit
   print("Money Added Successfully!")
    
def enter_data():
  if not os.path.exists('data.csv'):
    with open('data.csv','w', newline = "") as file:
      writer=csv.writer(file)
      writer.writerow(['Date','Label','Expense'])
  
  if os.path.exists('data.csv'):
    read_file_list = list(csv.reader(open('data.csv','r')))
    if len(read_file_list) == 0:
      with open('data.csv','a', newline = "") as file:
        writer=csv.writer(file)
        writer.writerow(['Date','Label','Expense'])
    Running = True
    
    while(Running):
          date = input("Enter the date: ")
          date_obj = datetime.datetime.strptime(date,'%d-%m-%Y')
          label =input("Label your Expense: ")
          expense= int(input("Expenditure:"))
          with open("data.csv",'a', newline="") as file:
              writer=csv.writer(file)
              writer.writerow([date_obj.date(),label,expense])
          print("Expenses are added!")
          ask=input("Do you want to continue:(y/n) ")
          if(ask == 'n' or ask =='N'):
                print("Your expenses has been successfully added..")
                break

def data_insights():
  try:
    with open('data.csv','r') as file:
      read = csv.reader(file)
      read_list=list(read)
      print("------------------------------------------------------------------")
      print(*read_list,sep = '\n')
      # for i in read_list:
      #     print(i)
      print("------------------------------------------------------------------")
      total_expense=0

      if(income <= 0):
        print("!! You don't have any income yet.Add some money first.");
        return

      for each in read_list[1:]:
        total_expense+=int(each[2])
        
      balance=income-total_expense
      print("* Account Balance:",balance)
      print("* Total Expenditure this month:",total_expense)
      percent=(total_expense/income * 100)
      print("* Expediture is {:.4f}%  of income in {} days of this month.\n".format(percent,len(read_list)-1))
  except Exception as e:
     print("It looks like you don't have enough data yet.",e)   
     


def data_visualization():
  try:
    with open('data.csv','r') as file:
      file = pd.read_csv("data.csv")
      x = file["Date"]
      z = file["Label"]
      y = file["Expense"]
      #plt.pie(y,labels= x)
      plt.pie(y,labels= z)
      plt.title("--Monthly Expenditure--")
     # plt.xticks(dates)  
      plt.legend()
      plt.show()
  except Exception as e:
    print("It looks like you don't have enough data yet.",e)



def limited_visualization(start_date,stop_date):
  try:
    with open('data.csv','r') as file:
      dates=[]
      expense=[]
      read=csv.reader(file)
      file_list=list(read)
      if stop_date > (len(file_list)-1):
          print("!! Stop date out of range..")
          return
      
      for each in file_list[start_date:stop_date+1]:
        dates.append(int(each[0]))
        expense.append(int(each[2]))
      total_expense=sum(list(map(int,expense)))
      percent=total_expense/income*100
      print(f"Total expenditure in this period is {total_expense} which is {percent:.4f}% of the monthly income.")
      today=datetime.date.today()
      
      plt.plot(dates,expense,label='per day range')
      plt.title("--Range of days Expenditure--")
      plt.xlabel(f"Date {today.month} {today.year}")
      plt.ylabel("Expense")
      plt.xticks(dates)  
      plt.legend()
      plt.show()
  except Exception:
    print("It looks like you don't have enough data.")


def New_Window():
    #Creates new window on top of the previous windows
    root.destroy()
    Window = Tk()
    dashboard = PhotoImage(file = "dashboard.gif")         
    label1 = Label(Window, image = dashboard)
    label1.place(x=0,y=0,width=1400,height=700)
    Window.title("Dashboard")
    Window.geometry("1400x1400")
    # Window.resizable(0, 0)
    Window.config(bg = 'orange')
    Button(Window,text = "Add Money ", bg='white', fg='black',font = ("times new roman",12,"bold"),command = lambda:add_money()).place(x=200,y=600)
    Button(Window,text = "data_insights ", bg='white', fg='black',font = ("times new roman",12,"bold"),command = lambda: data_insights()).place(x=650,y=600)
    Button(Window,text = "Data_visualization ", bg='white', fg='black',font = ("times new roman",12,"bold"),command = lambda: data_visualization()).place(x=1100,y=600)
    Button(Window,text = "Add expenses ",bg='white', fg='black',font = ("times new roman",12,"bold"),command = lambda: enter_data()).place(x=300,y=600)
    
    Window.mainloop()
  
   # Show image using label        
login = PhotoImage(file = "login.gif")         
label1 = Label(root, image = login)
label1.place(x = 0, y = 0,width=500,height=500)
root.title("Login")
root.geometry("500x500")
root.config(bg = 'white')
         
Label(root,text="Username",anchor="center").grid(row = 60, column = 40, padx = 40, pady = 60)
Label(root,text="Password",anchor="center").grid(row = 70, column = 40, padx = 40,pady =0)
e1 = Entry(root)
e1.grid(row = 60, column = 50)
e2 = Entry(root)
e2.grid(row = 70, column = 50)
e2.config(show ="*")
Button(root,text = "Login",command = lambda: OK() ).grid(row = 80,column = 45, pady = 35)
root.mainloop()


    








