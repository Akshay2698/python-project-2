from Tkinter import*
import tkMessageBox
import Tkinter
rot=Tk()
rot.geometry("1350x600")
canvas=Canvas(width=300,height=200,bg='white')
canvas.pack(expand=YES,fill=BOTH)
gif1=PhotoImage(file="bf.gif")
canvas.create_image(50,10,image=gif1,anchor=NW)
gif2=PhotoImage(file="bird.gif")
canvas.create_image(600,100,image=gif2,anchor=NW)
gif3=PhotoImage(file="fish.gif")
canvas.create_image(1000,10,image=gif3,anchor=NW)
gif4=PhotoImage(file="flower.gif")
canvas.create_image(100,400,image=gif4,anchor=NW)
gif5=PhotoImage(file="minion.gif")
canvas.create_image(1000,300,image=gif5,anchor=NW)

def refresh():
    canvas1=Canvas(width=300,height=200,bg='white')
    canvas1.pack(expand=YES,fill=BOTH)
    giff1=PhotoImage(file="bf.gif")
    canvas1.create_image(50,10,image=giff1,anchor=NW)
    giff2=PhotoImage(file="bird.gif")
    canvas1.create_image(600,100,image=giff2,anchor=NW)
    giff3=PhotoImage(file="fish.gif")
    canvas1.create_image(1000,10,image=giff3,anchor=NW)
    giff4=PhotoImage(file="flower.gif")
    canvas1.create_image(100,400,image=giff4,anchor=NW)
    giff5=PhotoImage(file="minion.gif")
    canvas1.create_image(1000,300,image=giff5,anchor=NW)
    
B=Tkinter.Button(rot,text="refresh",command=refresh)
B.pack(anchor=NW)

def ok():
    t=Toplevel()
    var1=IntVar()
    var2=IntVar()
    var3=IntVar()
    var4=IntVar()
    var5=IntVar()
    var6=IntVar()
    var7=IntVar()
    var8=IntVar()
    var9=IntVar()
    var10=IntVar()
    
    c1=Checkbutton(t,text="flower",variable=var1,onvalue=1,
                   offvalue=0,height=3,width=50)
    c1.pack()
    c2=Checkbutton(t,text="Minion",variable=var2,onvalue=1,
                   offvalue=0,height=3,width=50)
    c2.pack()
    c3=Checkbutton(t,text="butterfly",variable=var3,onvalue=1,
                   offvalue=0,height=3,width=50)
    c3.pack()
    c4=Checkbutton(t,text="Earth",variable=var4,onvalue=1,
                   offvalue=0,height=3,width=50)
    c4.pack()
    c5=Checkbutton(t,text="Bird",variable=var5,onvalue=1,
                   offvalue=0,height=3,width=500)
    c5.pack()
    c6=Checkbutton(t,text="Fish",variable=var6,onvalue=1,
                   offvalue=0,height=3,width=50)
    c6.pack()
    c7=Checkbutton(t,text="Dog",variable=var7,onvalue=1,
                   offvalue=0,height=3,width=50)
    c7.pack()
    c8=Checkbutton(t,text="shoe",variable=var8,onvalue=1,
                   offvalue=0,height=3,width=50)
    c8.pack()
    c9=Checkbutton(t,text="book",variable=var9,onvalue=1,
                   offvalue=0,height=3,width=50)
    c9.pack()
    c10=Checkbutton(t,text="pen",variable=var10,onvalue=1,
                   offvalue=0,height=3,width=50)
    c10.pack()

    def verify():
        x=Toplevel()
        count=0
        
        if((var1.get())==1):
            L1=Label(x).grid(row=0,column=0)
            count=count+1
        
        if((var2.get())==1):
            L2=Label(x).grid(row=1,column=0)
            count=count+1
        
        if((var3.get())==1):
            L3=Label(x).grid(row=2,column=0)
            count=count+1
        
        if((var4.get())==1):
            L4=Label(x).grid(row=3,column=0)
        
        if((var5.get())==1):
            L5=Label(x).grid(row=4,column=0)
            count=count+1
        
        if((var6.get())==1):
            L6=Label(x).grid(row=5,column=0)
            count=count+1
        
        if((var7.get())==1):
            L7=Label(x).grid(row=6,column=0)
        
        if((var8.get())==1):
            L8=Label(x).grid(row=7,column=0)
        
        if((var9.get())==1):
            L9=Label(x).grid(row=8,column=0)
        
        if((var10.get())==1):
            L10=Label(x).grid(row=9,column=0)

        
        L11=Label(x,text="score:",relief=RAISED,width=10).grid(row=3,column=1)
        L11=Label(x,text=count,relief=RAISED,width=6).grid(row=3,column=2)
        
        x.mainloop()
            
    E=Tkinter.Button(t,text="submit",command=verify)
    E.pack()
    
D=Tkinter.Button(rot,text=" ok",command=ok )
D.pack(anchor=NE)

rot.mainloop()
