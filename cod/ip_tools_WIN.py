# cod by rda ,leng cod = python ,cod alpha
 

import socket 
from tkinter import *
import tkinter

print(""" ip_tools vo.o.1 alpha by rda 
...................................................
    in case of error it will be displayed below
        """)
# socket 
hostname = socket.gethostname()
ip_pc = socket.gethostbyname(hostname)

#tk root   
root= Tk()
root.geometry("600x450+444+290")
root.minsize(120, 1)
root.maxsize(1444, 881)
root.resizable(False,False)
root.title("ip_tools")
root.configure(background="#000000")

# frame setting
Frame1 = Frame(root)
Frame1.place(relx=0.067, rely=0.044, relheight=0.744
                                      , relwidth=0.875)
Frame1.configure(relief='groove')
Frame1.configure(borderwidth="3")
Frame1.configure(relief="groove")
Frame1.configure(background="#000000")

# label
t1 = Label(root,text='HOSTNAME_PC: ',bg='black',fg='red')
t1.place(relx=0.229, rely=0.06, height=41, width=224)
t1.configure(font="-family {Segoe UI} -size 21 -weight bold")

t_host =Label(root,text=hostname,bg='black',fg='red')
t_host.place(relx=0.267, rely=0.239, height=41, width=184)
t_host.configure(font="-family {Segoe UI} -size 21 -weight bold")

t2= Label(root,text='     PC_IP:  ',bg='black',fg='red')
t2.place(relx=0.305, rely=0.388, height=41, width=104)
t2.configure(font="-family {Segoe UI} -size 21 -weight bold")

t_ip = Label(root,text=ip_pc,bg='black',fg='red')
t_ip.place(relx=0.248, rely=0.537, height=41, width=204)
t_ip.configure(font="-family {Segoe UI} -size 21 -weight bold")
   
def info1():
    import time
    import webbrowser
    import tkinter as tk
         # var link
    link ='https://github.com/RedAnonymusITA/ip-tools/releases/tag/v0.0.1'
    root3 = tk.Tk()
    root3.geometry('400x400')
    root3.title('info app ')
    root3.resizable(False, False)
    root3.configure(background='black')
    

    
   
    t =tk. Label(root3, text=""" dev nikname:  RDA(REDANONYMUS2)
real name dev is : Pop Mario Denis
leg : en
cod : python 
os:for windows ,mac os and GUI/linux
ver :ip_tools_gui_0.0.1 alpha
req:python 3.0 or new (no python 2.0 no test)
original lenguage ip_tools: italy
--------------------------------------
           more APP
ip_tools_0.0.1 for termux and cmd 
leg : en
Os= windows,Mac and GUI/linux
ip_tools_0.0.2 for termux and cmd
leg= ita and en 
Os= windows,Mac and GUI/linux """, bg='black', fg='red')
    t.place(x=20, y=3) 
       
    def more1():
        import time
          
        t = time.sleep(3)
        web= webbrowser.open(link)

      
        




      
   
          # buttun more
    bt_m = tk.Button(root3, text='github ', command=more1)
    bt_m.place(x=200, y=310)
    bt_m.configure(bg='red',fg='white',activebackground='black',activeforeground='red')
    bt_m.configure(borderwidth='3')
    bt_m.configure(relief='flat')
    if __name__=="__main__" :
         root3.mainloop()
    


# next page, web ip page and cod 
def nextpag1():
    # tk root
    import time
    import socket
    import tkinter as tk
    root2= tk.Tk()
    root2.geometry("600x450+444+290")
    root2.minsize(120, 1)
    root2.maxsize(1444, 881)
    root2.resizable(False,False)
    root2.title("web_ip")
    root2.configure(background="#000000")
    
    # text box
    textbox1 = tk.Entry(root2, bg='white', fg='black',borderwidth='1')
    textbox1.place(relx=0.270, rely=0.190,height=29, width=279)
    textbox1.configure(bg='black',fg='red')
    def help():
        import tkinter as tk
        root6=tk.Tk()
        root6.geometry('300x300')
        root6.title('HELP_WEBIP')
        root6.configure(bg='black')
        root6.resizable(False,False)
        t_h=tk.Label(root6,text=""" write hostname ex:pc99
        write web ip ex:www.webname.com
        and localhost for localhost ip""")
        t_h.configure(fg='red')
        t_h.place(x=50,y=100)
        root.mainloop()
    def go1():
       try :
            time.sleep(2)
            web_ip = socket.gethostbyname(textbox1.get())
            res = tk.Label(root2, text=web_ip)
            res.place(x=260, y=200)
            res.configure(bg='black',fg='red')
            res.configure(font="-family {Segoe UI} -size 21 -weight bold")
       except:
            print('attention website or host not existing :(')
       # label res
            spa = tk.Label(root2, text='             ',bg='black').grid(row=1, column=8)
    bt_go = tk.Button(root2, text='GO', command=go1)
    bt_go.place(x=493, y=90)
    bt_go.configure(bg='red',fg='black',activeforeground='red',activebackground='black')
    bt_go.configure(relief='flat')  
    bt_help=tk.Button(root2,text='HELP',command=help) 
    bt_help.place(x=100,y=200)
    bt_help.configure(bg='red',fg='black',activeforeground='red',activebackground='black')
    bt_help.configure(relief='flat')  
    if __name__=="__main__":
            root2.mainloop()

    

#------------------------------------------------------------------------
    #button root

bt_next = Button(root,text='web_ip',command=nextpag1,bg='red',fg='black',activebackground='black',activeforeground='red',relief='flat',borderwidth='2')
bt_next.place(relx=0.100, rely=0.822, height=44, width=217)

bt_ifo = Button(root,text='INFO',command=info1,bg='red',fg='black',activebackground='black',activeforeground='red',relief='flat',borderwidth='2').place(relx=0.538, rely=0.822, height=44, width=217)

if __name__=='__main__':
     root.mainloop()
