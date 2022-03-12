from tkinter import *
from fpdf import FPDF

def print():
    name = str(entryBox1.get())
    basic = int(entryBox2.get())
    da = 0.05 * basic 
    hra = 0.1 * basic 
    gross = basic  + da + hra 
    pf = 0.0833 * (basic + da)
    if(pf>1800):
        pf = 1800
        
    net = gross - pf   

    basic = int(basic)
    da = int(da)
    hra = int(hra)
    gross = int(gross)
    pf = int(pf)
    net = int(net)

    basic = str(basic)
    da = str(da)
    hra = str(hra)
    gross = str(gross)
    pf = str(pf)
    net = str(net)
    
    
    pdf = FPDF()
    pdf.add_page()
    txt1 = "Employee's Name : " + name
    txt2 = "Basic Salary : " + basic
    txt3 = "Dearness Allowance : " + da
    txt4 = "House Rent Allowance : " + hra
    txt4 = "Provident Fund : " + pf
    txt5 = "Gross Salary : " + gross
    txt6 = "Net Salary : " + net
    pdf.set_font("Times",'BIU',size = 35)
    pdf.cell(200,20,txt="Employee Dashboard",ln=1,align="C")
    pdf.set_font("Times",'I',size = 15)
    pdf.cell(200,10,txt=txt1,ln=2,align="L")
    pdf.cell(200,10,txt=txt2,ln=3,align="L")
    pdf.cell(200,10,txt=txt3,ln=4,align="L")
    pdf.cell(200,10,txt=txt4,ln=5,align="L")
    pdf.cell(200,10,txt=txt5,ln=6,align="L")
    pdf.cell(200,10,txt=txt5,ln=7,align="L")
    pdf.cell(200,10,txt=txt6,ln=8,align="L")

    pdf.output("Salary Slip.pdf")

def function():
    name = str(entryBox1.get())
    basic = int(entryBox2.get())
    da = 0.05 * basic 
    hra = 0.1 * basic 
    gross = basic  + da + hra 
    pf = 0.0833 * (basic + da)
    if(pf>1800):
        pf = 1800
        
    net = gross - pf   

    basic = int(basic)
    da = int(da)
    hra = int(hra)
    gross = int(gross)
    pf = int(pf)
    net = int(net)

    
    window2 = Tk()
    window2.geometry("475x310")
    window2.title("Employee Dashboard : Calculated Result")

    #destroying first window here
    window.destroy()
    
    name_label = Label(window2,font=("Times New Roman",20),text="Employee's Name : ")
    name_label.grid(row=0,column=0)

    name_label2 = Label(window2,font=("Times New Roman",20),text=name).grid(row=0,column=2)

    basic_label = Label(window2,font=("Times New Roman",20),text="Basic Salary :")
    basic_label.grid(row=1)
    
    basic_label2 = Label(window2,font=("Times New Roman",20),text=basic).grid(row=1,column=2)

    da_label = Label(window2,font=("Times New Roman",20),text="Dearness Allowance : ")
    da_label.grid(row=2)

    da_label2 = Label(window2,font=("Times New Roman",20),text=da).grid(row=2,column=2)

    hra_label = Label(window2,font=("Times New Roman",20),text="House Rent Allowance : ")
    hra_label.grid(row=3)

    hra_label2 = Label(window2,font=("Times New Roman",20),text=hra).grid(row=3,column=2)

    gross_label = Label(window2,font=("Times New Roman",20),text="Gross Salary : ")
    gross_label.grid(row=4)

    gross_label2 = Label(window2,font=("Times New Roman",20),text=gross).grid(row=4,column=2)

    pf_label = Label(window2,font=("Times New Roman",20),text="Provident Fund : ")
    pf_label.grid(row=5)

    pf_label2 = Label(window2,font=("Times New Roman",20),text=pf).grid(row=5,column=2)

    net_label = Label(window2,font=("Times New Roman",20),text="Net Salary : ")
    net_label.grid(row=6)

    net_label2 = Label(window2,font=("Times New Roman",20),text=net).grid(row=6,column=2)

    #btnPrint = Button(window2,width="20",bg="Yellow",fg="Black",text="Print",font=("Times New Roman",15),command=print).grid(row=8,column=2)    
    #destroy window2 here
    #window2.destroy()


window = Tk()
window.geometry("700x250")
window.title("Employee Dashboard")

heading = Label(window,text="Employee Salary Calculator",font=("Times New Roman",30),fg="Navy")
heading.place(x=125)

label1 = Label(window,text="Enter Employee's name !",font=("Times New Roman",18))
label1.place(x=20,y=70)

label2 = Label(window,text="Enter Employee's basic salary !",font=("Times New Roman",18))
label2.place(x=20,y=110)

entryBox1 = Entry(window,bd="5",width = "22",bg ="Aqua",fg="Black",font=("Times New Roman",13))
entryBox2 = Entry(window,bd="5",width = "22",bg ="Aqua",fg="Black",font=("Times New Roman",13))
entryBox1.place(x=350,y=70)
entryBox2.place(x=350,y=110)

btn = Button(window,width = "10",text = "Submit",bg="Red",fg="White",font=("Times New Roman",15),command=lambda:[print(),function()])
btn.place(x=250,y=180)

mainloop()




