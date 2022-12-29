from tkinter import *

def calc():
    index = int(display3.get())
    ans = display2.get()
    display.delete(0,index)
    display2.delete(0,index)
    
    result = str(eval(ans))
    display3.delete(0,len(display3.get()))
    display3.insert(0,'0')
    display.insert(0,result)
    
def numpad1():
    index = int(display3.get())
    display.insert(index,'1')
    display2.insert(len(display2.get(),),'1')
    display3.delete(0,len(display3.get()))
    display3.insert(0,str(index+1))
    print(index)
def numpad2():
    index = int(display3.get())
    display.insert(index,'2')
    display2.insert(len(display2.get(),),'2')
    display3.delete(0,len(display3.get()))
    display3.insert(0,str(index+1))
    print(index)
def numpad3():
    index = int(display3.get())
    display.insert(index,'3')
    display2.insert(len(display2.get(),),'3')
    display3.delete(0,len(display3.get()))
    display3.insert(0,str(index+1))
def numpad4():
    index = int(display3.get())
    display.insert(index,'4')
    display2.insert(len(display2.get(),),'4')
    display3.delete(0,len(display3.get()))
    display3.insert(0,str(index+1))
def numpad5():
    index = int(display3.get())
    display.insert(index,'5')
    display2.insert(len(display2.get(),),'5')    
    display3.delete(0,len(display3.get()))
    display3.insert(0,str(index+1))
def numpad6():
    index = int(display3.get())
    display.insert(index,'6')
    display2.insert(len(display2.get(),),'6')
    display3.delete(0,len(display3.get()))
    display3.insert(0,str(index+1))
def numpad7():
    index = int(display3.get())
    display.insert(index,'7')
    display2.insert(len(display2.get(),),'7')
    display3.delete(0,len(display3.get()))
    display3.insert(0,str(index+1))
def numpad8():
    index = int(display3.get())
    display.insert(index,'8')
    display2.insert(len(display2.get(),),'8')
    display3.delete(0,len(display3.get()))
    display3.insert(0,str(index+1))
def numpad9():
    index = int(display3.get())
    display.insert(index,'9')
    display2.insert(len(display2.get(),),'9')
    display3.delete(0,len(display3.get()))
    display3.insert(0,str(index+1))
def numpad0():
    index = int(display3.get())
    display.insert(index,'0')
    display2.insert(len(display2.get(),),'0')    
    display3.delete(0,len(display3.get()))
    display3.insert(0,str(index+1))
def numpaddot():
    index = int(display3.get())
    display.insert(index,'.')
    display2.insert(len(display2.get(),),'.')   
    display3.delete(0,len(display3.get()))
    display3.insert(0,str(index+1))
def numpadmnp():
    index = int(display3.get())
    display.insert(len(display.get())-index,'(-')
    display3.delete(0,len(display3.get()))
    display3.insert(0,str(index+2))
    index = int(display3.get())
    display.insert(index,')')
    display3.delete(0,len(display3.get()))
    display3.insert(0,str(index+1))
    display2.insert(len(display2.get())-index,'(-1)*')
def oprtps():
    index = int(display3.get())
    display.insert(index,'+')
    display2.insert(len(display2.get(),),'+')
    display3.delete(0,len(display3.get()))
    display3.insert(0,str(index+1))
def oprtmn():
    index = int(display3.get())
    display.insert(index,'-')
    display2.insert(len(display2.get(),),'-') 
    display3.delete(0,len(display3.get()))
    display3.insert(0,str(index+1))
def oprtml():
    index = int(display3.get())
    display.insert(index,'x')
    display2.insert(len(display2.get(),'*'))  
    display3.delete(0,len(display3.get()))
    display3.insert(0,str(index+1))
def oprtdv():
    index = int(display3.get())
    display.insert(index,'÷')
    display2.insert(len(display2.get()),'/')
    display3.delete(0,len(display3.get()))
    display3.insert(0,str(index+1))
def oprtdel():
    index = int(display3.get())
    if index == 0:
        oprtdelall()
    if "sqrt" in display2.get() or "pow" in display2.get():
        oprtdelall()
    else:
        display.delete(index-1,index)
        display2.delete(len(display2.get())-1,len(display2.get()))
        display3.delete(0,len(display3.get()))
        display3.insert(0,str(index-1))

def oprtsqrt():
    index = int(display3.get())
    display.insert(len(display.get())-index,'√(')
    display2.insert(len(display2.get())-index,'math.sqrt(')
    display3.delete(0,len(display3.get()))
    display3.insert(0,str(index+2))
    index = int(display3.get())
    display.insert(index,')')
    display2.insert(display2.get().find('math.sqrt')+index+8,')')
    display3.delete(0,len(display3.get()))
    display3.insert(0,str(index+1))
    

def numpadbkl():
    index = int(display3.get())
    display.insert(index,'(')
    display2.insert(len(display2.get()),'(')
    display3.delete(0,len(display3.get()))
    display3.insert(0,str(index+1))
def numpadbkr():
    index = int(display3.get())
    display.insert(index,')')
    display2.insert(len(display2.get()),')')
    display3.delete(0,len(display3.get()))
    display3.insert(0,str(index+1))
def oprtdelall():
    display.delete(0,len(display.get()))
    display2.delete(0,len(display2.get()))
    display3.delete(0,len(display3.get()))
    display3.insert(len(display3.get()),'0')

def oprtpow2():
    index = int(display3.get())
    display.insert(index,'²')
    display2.insert(len(display2.get())-index,'pow(')
    display2.insert(len(display2.get()),',2)')
    display3.delete(0,len(display3.get()))
    display3.insert(0,str(index+1))
    


window = Tk()
window.title('pyCalc')
icon = PhotoImage(file=("Assets/icon.png"))
window.iconphoto(True,icon)
canvas = Canvas(window,width=300, height=500)
canvas.pack()

#display
display = Entry(window,width=10,font=('OCR A Extended',30))
canvas.create_window(150,35,window=display)
display2 = Entry(window,width=10,font=('OCR A Extended',30))
canvas.create_window(150,600,window=display2)
display3 = Entry(window,width=10,font=('OCR A Extended',30))
canvas.create_window(150,600,window=display3)


#opirators
divis = Button(text='÷',width='5',height='2',command=oprtdv)
canvas.create_window(260,260,window=divis)
mines = Button(text='-',width='5',height='2',command=oprtmn)
canvas.create_window(260,310,window=mines)
plus = Button(text='+',width='5',height='2',command=oprtps)
canvas.create_window(260,360,window=plus)
mlt = Button(text='*',width='5',height='2',command=oprtml)
canvas.create_window(190,260,window=mlt)
quar = Button(text='X²',width='5',height='2',command=oprtpow2)
canvas.create_window(120,210,window=quar)
sqr = Button(text='√',width='5',height='2',command=oprtsqrt)
canvas.create_window(50,210,window=sqr)

#numpad
nm9 = Button(text='9',width='5',height='2',command=numpad9)
canvas.create_window(190,310,window=nm9)
nm6 = Button(text='6',width='5',height='2',command=numpad6)
canvas.create_window(190,360,window=nm6)
nm3 = Button(text='3',width='5',height='2',command=numpad3)
canvas.create_window(190,410,window=nm3)
nm8 = Button(text='6',width='5',height='2',command=numpad8)
canvas.create_window(120,310,window=nm8)
nm5 = Button(text='5',width='5',height='2',command=numpad5)
canvas.create_window(120,360,window=nm5)
nm2 = Button(text='2',width='5',height='2',command=numpad2)
canvas.create_window(120,410,window=nm2)
nm7 = Button(text='7',width='5',height='2',command=numpad7)
canvas.create_window(50,310,window=nm7)
nm4 = Button(text='4',width='5',height='2',command=numpad4)
canvas.create_window(50,360,window=nm4)
nm1 = Button(text='1',width='5',height='2',command=numpad1)
canvas.create_window(50,410,window=nm1)
nm0 = Button(text='0',width='5',height='2',command=numpad0)
canvas.create_window(120,460,window=nm0)
nmdot = Button(text='.',width='5',height='2',command=numpaddot)
canvas.create_window(190,460,window=nmdot)
nmmp = Button(text='±',width='5',height='2',command=numpadmnp)
canvas.create_window(50,460,window=nmmp)
bkr = Button(text=')',width='5',height='2',command=numpadbkr)
canvas.create_window(120,260,window=bkr)
bkl = Button(text='(',width='5',height='2',command=numpadbkl)
canvas.create_window(50,260,window=bkl)

#sys
dlt = Button(text='del',width='5',height='2',command=oprtdel)
canvas.create_window(260,210,window=dlt)
dltall = Button(text='C',width='5',height='2',command=oprtdelall)
canvas.create_window(190,210,window=dltall)
equal = Button(text='=',width='5',height='5',command=calc)
canvas.create_window(260,435,window=equal)

display3.insert(0,str('0'))

window.mainloop()