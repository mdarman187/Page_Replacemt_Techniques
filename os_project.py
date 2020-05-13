from tkinter import *

def fifo_pgf():
        frames=int(entry_1.get())
        a=entry_2.get()
        s=[]
        s=a.split(" ")
        f,st,page_fault,top = [],[],0,0
        for i in s:
              if i not in f:
                   if len(f)<frames:
                         f.append(i)
                   else:
                         f[top] = i
                         top = (top+1)%frames
                   page_fault+= 1
              else:
                   pass
        label_4.configure(text=len(s))
        label_6.configure(text=page_fault)

def lru_pgf():
        frames=int(entry_1.get())
        a=entry_2.get()
        s=[]
        s=a.split(" ")
        f,st,page_fault= [],[],0
        for i in s:
                if i not in f:
                    if len(f)<frames:
                         f.append(i)
                         st.append(len(f)-1)
                    else:
                         ind = st.pop(0)
                         f[ind] = i
                         st.append(ind)
                    page_fault+= 1
                else:
                    st.append(st.pop(st.index(f.index(i))))
        label_4.configure(text=len(s))
        label_6.configure(text=page_fault)
        
def optimal_pgf():
        frames=int(entry_1.get())
        a=entry_2.get()
        s=[]
        s=a.split(" ")
        f,st,page_fault= [],[],0
        occurance = [None for i in range(frames)]
        for i in range(len(s)):
              if s[i] not in f:
                      if len(f)<frames:
                             f.append(s[i])
                      else:
                             for x in range(len(f)):
                                   if f[x] not in s[i+1:]:
                                           f[x] = s[i]
                                           break
                                   else:
                                           occurance[x] = s[i+1:].index(f[x])
                             else:
                                   f[occurance.index(max(occurance))] = s[i]
                      page_fault += 1
                      
              else:
                      pass
        label_4.configure(text=len(s))
        label_6.configure(text=page_fault)







root = Tk()
root.geometry('500x500')
root.title("PAGE REPLACEMENT TECHNIQUES")

label_0 = Label(root, text="PAGE REPLACEMENT TECHNIQUES",fg ='black',bg='skyblue',font=("bold", 20))
label_0.place(x=10,y=53)


label_1 = Label(root, text="FRAME SIZE",width=20,fg='red',font=("bold", 10))
label_1.place(x=80,y=130)
entry_1 = Entry(root)
entry_1.place(x=240,y=130)

label_2 = Label(root, text="REFERENCE STRING",width=20,fg='red',font=("bold", 10))
label_2.place(x=80,y=165)
entry_2 = Entry(root)
entry_2.place(x=240,y=165)

Button(root, text='FIFO',width=15,bg='orange',fg='white',command=fifo_pgf).place(x=180,y=220)
Button(root, text='LRU',width=15,bg='white',fg='blue',command=lru_pgf).place(x=180,y=250)
Button(root, text='OPTIMAL',width=15,bg='GREEN',fg='white',command=optimal_pgf).place(x=180,y=280)

label_3 = Label(root, text="TOTAL REQUEST ->",width=20,fg='red',font=("bold", 10))
label_3.place(x=80,y=350)
label_4 =Label(root, text="______________",font=("bold",10))
label_4.place(x=225,y=350)

label_5 = Label(root, text="PAGE FAULT    -->>",width=20,fg='red',font=("bold", 10))
label_5.place(x=80,y=380)
label_6 =Label(root, text="______________",font=("bold",10))
label_6.place(x=225,y=380)

Button(root, text='EXIT',width=15,bg='grey',fg='white',command=root.destroy).place(x=180,y=430)



