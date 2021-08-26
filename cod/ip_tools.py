# import librery
from os import system
from posixpath import dirname
import time
import webbrowser
import socket
import tkinter as tk
from tkinter.constants import DISABLED, HIDDEN, NORMAL
# root is windows for Home(class: frame)
root = tk.Tk()
root.geometry("745x449+444+290")
root.resizable()
root.title("ip_tools")
root.resizable(False, False)
root.configure(background="black")


class info1:
    def __init__(self):
        import tkinter as tk
        import time
        import webbrowser
        root_i = tk.Tk()
        root_i.geometry('400x400')
        root_i.title('info app ')
        root_i.resizable(False, False)
        root_i.configure(background='black')

        # var link
        link = 'https://github.com/RedAnonymusITA/ip-tools/releases/tag/v0.0.1'

        t = tk. Label(root_i, text=""" dev nikname:  RDA(REDANONYMUS2)
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

            self.t = time.sleep(3)
            self.web = webbrowser.open(link)

          # buttun more
        self.bt_m = tk.Button(root_i, text='github ', command=more1)
        self.bt_m.place(x=200, y=310)
        self.bt_m.configure(bg='red', fg='black',
                            activebackground='black', activeforeground='red')
        self.bt_m.configure(borderwidth='3')
        self.bt_m.configure(relief='flat')


class ip_web:
    def __init__(self):

        # tk root
        import os
        import time
        import socket
        import tkinter as tk
        root2 = tk.Tk()
        root2.geometry("600x450+444+290")
        root2.minsize(120, 1)
        root2.maxsize(1444, 881)
        root2.resizable(False, False)
        root2.title("web_ip")
        root2.configure(background="#000000")

        # text box
        textbox1 = tk.Entry(root2, bg='white', fg='black', borderwidth='1')
        textbox1.place(relx=0.270, rely=0.190, height=29, width=279)
        textbox1.configure(bg='black', fg='red')

        def help():
            import tkinter as tk
            root6 = tk.Tk()
            root6.geometry('300x300')
            root6.title('HELP_WEBIP')
            root6.configure(bg='black')
            root6.resizable(False, False)
            t_h = tk.Label(root6, text=""" write hostname ex:pc99
            write web ip ex:www.webname.com
            and localhost for localhost ip""")
            t_h.configure(fg='red')
            t_h.place(x=50, y=100)
            root.mainloop()

        def go1():
            try:
                time.sleep(2)
                web_ip = socket.gethostbyname(textbox1.get())
                res = tk.Label(root2, text=web_ip)
                res.place(x=260, y=200)
                res.configure(bg='black', fg='red')
                res.configure(font="-family {Segoe UI} -size 21 -weight bold")
                textbox1.configure(state=DISABLED)
                class dir1():
                    def __init__(self):

                        win = tk.Tk()
                        win.geometry('500x300')
                        win.title("SAVE FILE")

                        self.txt1 = tk.Label(win, text="WRITE  FILE NAME : ")
                        self.txt1.place(relx=0.220, rely=0.099)
                        self.filename = tk.Entry(win)
                        self.filename.place(relx=0.220, rely=0.190, height=29, width=279)
                        self.txt2 = tk.Label(win, text="WRITE FOLDER PATH : ")
                        self.txt2.place(relx=0.220, rely=0.320)
                        self.folder = tk.Entry(win)
                        self.folder.place(relx=0.220, rely=0.420, height=29, width=279)
              
                        def help_save():
                            win2 = tk.Tk()
                            win2.geometry("400x99")
                            win2.title("HELP")
                            txt3 = tk.Label(win2, text="""example filename : my-web-ip.txt \n
                    example folder path:/home/user-name/Desktop""")
                            txt3.place(x=4, y=3)
                            win2.mainloop()
        
                        def save_file():
                            name = self.filename.get()
                            src = self.folder.get()
                            file=open(src+name,'w')
                            file.write(web_ip)
                            file.close()
                            pass

                        self.bt_save1 = tk.Button(win, text="SAVE FILE",command=save_file)
                        self.bt_save1.place(relx=0.220, rely=0.620, height=44, width=99)

                        self.bt_clear = tk.Button(win, text="HELP", command=help_save)
                        self.bt_clear.place(relx=0.590, rely=0.620, height=44, width=99)

            


                def save():
                    dir1()
                    pass

                def reset():
                    res.destroy()
                    bt_res.destroy()
                    bt_save.destroy()
                    textbox1.configure(state=NORMAL)

                bt_res = tk.Button(root2, text="CLEAR", command=reset)
                bt_res.place(x=230, y=345)
                bt_res.configure(
                    bg='red', fg='black', activeforeground='red', activebackground='black')
                bt_res.configure(relief='flat')

                bt_save = tk.Button(root2, text="SAVE FILE", command=save)
                bt_save.place(x=310, y=345)
                bt_save.configure(
                    bg='red', fg='black', activeforeground='red', activebackground='black')
                bt_save.configure(relief='flat')

            except:
                print(' website or host not existing :(')
       # label res
        spa = tk.Label(root2, text='             ',
                       bg='black').grid(row=1, column=8)
        bt_go = tk.Button(root2, text='GO', command=go1)
        bt_go.place(x=493, y=90)
        bt_go.configure(bg='red', fg='black',
                        activeforeground='red', activebackground='black')
        bt_go.configure(relief='flat')
        bt_help = tk.Button(root2, text='HELP', command=help)
        bt_help.place(x=100, y=200)
        bt_help.configure(bg='red', state=DISABLED, fg='black',
                          activeforeground='red', activebackground='black')
        bt_help.configure(relief='flat')
        

        if __name__ == "__main__":
            root2.mainloop()


class frame():
    def __init__(self, master):

        self.Frame1 = tk.Frame(master)
        self. Frame1.place(relx=0.068, rely=0.044,
                           relheight=0.744, relwidth=0.899)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="3")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#000000")
        hostname = socket.gethostname()
        ip_pc = socket.gethostbyname(hostname)
        self.t1 = tk.Label(master, text='HOSTNAME_PC: ', bg='black', fg='red')
        self.t1.place(relx=0.267, rely=0.06, height=41, width=300)
        self.t1.configure(font="-family {Segoe UI} -size 21 -weight bold")

        self.t_host = tk.Label(master, text=hostname, bg='black', fg='red')
        self.t_host.place(relx=0.267, rely=0.239, height=41, width=300)
        self.t_host.configure(font="-family {Segoe UI} -size 21 -weight bold")

        self.t2 = tk.Label(master, text='     PC_IP:  ', bg='black', fg='red')
        self.t2.place(relx=0.220, rely=0.388, height=41, width=300)
        self.t2.configure(font="-family {Segoe UI} -size 21 -weight bold")

        self.t_ip = tk.Label(master, text=ip_pc, bg='black', fg='red')
        self.t_ip.place(relx=0.248, rely=0.537, height=41, width=300)
        self.t_ip.configure(font="-family {Segoe UI} -size 21 -weight bold")

        self.bt_next = tk.Button(root, text='web_ip', command=ip_web, bg='red', fg='black',
                                 activebackground='black', activeforeground='red', relief='flat', borderwidth='2')
        self.bt_next.place(relx=0.100, rely=0.822, height=44, width=217)
        self.bt_info = tk.Button(root, text='INFO', command=info1, bg='red', fg='black',
                                 activebackground='black', activeforeground='red', relief='flat', borderwidth='2')
        self.bt_info.place(relx=0.538, rely=0.822, height=44, width=217)


e = frame(root)




root.mainloop()
