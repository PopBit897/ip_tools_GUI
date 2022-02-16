# import librery
import os
import socket
from tkinter import Menu
import tkinter as tk
from tkinter.constants import DISABLED, HIDDEN, NORMAL
# root is windows for Home(class: frame)
root = tk.Tk()
root.geometry("745x449+444+290")
root.title("ip_tools")
root.resizable(False, False)
root.configure(background="black")


class info1:
    def __init__(self):
        import os
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
    req:python 3.0 or latest version (not python 2.0)
    original lenguage ip_tools: italy
    --------------------------------------
               other software by rda
    ip_tools_0.0.1 for termux and cmd 
    leg : en
    Os= windows,Mac and GUI/linux
    ip_tools_0.1.1 for termux and cmd
        leg= ita and en 
    Os= windows,Mac and GUI/linux """, bg='black', fg='red')
        t.place(x=20, y=3)
        def other():
            win_install = tk.Tk()
            win_install.geometry("500x200")
            win_install.resizable(False, False)
            win_install.configure(background="black")
            win_install.title("install_ip_tools for terminal and cmd ")
            
            def l_dow():
               
                   
                 t2 =time.sleep(2)
                 terminal = os.system('git clone https://github.com/RedAnonymusITA/ip-tools.git')
                 win_start = tk.Tk()
                 win_start.title('start-ip.sh execution permissions')
                 win_start.geometry('400x300')
                 txt4 = tk.Label(win_start,text='open folder cod/ip-tools double click start-ip.sh')
                 txt4.place(x=7,y=100)
              

            def dow():
                
                url2 = "https://github.com/RedAnonymusITA/ip-tools/releases/tag/v0.0.1"
                self.t = time.sleep(2)
                self.web = webbrowser.open(url2)
            bt_dow1 = tk.Button(win_install, text="download latest version",command=l_dow)
            bt_dow1.place(relx=0.220, rely=0.120, height=41, width=300)
            bt_dow1.configure(bg="red",fg='black',activebackground='black',activeforeground='red')
            bt_dow1.configure(relief='flat')


            bt_dow = tk.Button(win_install,text="download V0.0.1",command=dow)
            bt_dow.place(relx=0.220, rely=0.520, height=41, width=300)
            bt_dow.configure(bg="red",fg="black",activebackground='black',activeforeground='red')
            bt_dow.configure(relief='flat')
           


          # buttun more
        self.bt_other = tk.Button(root_i, text='other ', command=other)
        self.bt_other.place(x=200, y=310)
        self.bt_other.configure(bg='red', fg='black',
                            activebackground='black', activeforeground='red')
        self.bt_other.configure(borderwidth='3')
        self.bt_other.configure(relief='flat')


class ip_web:
    def __init__(self):

        # tk root
        import os
        import time
        import socket
        import tkinter as tk
        import webbrowser
        
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
                        from tkinter import Menu
                        win.geometry("500x300")
                        win.title("SAVE FILE")
                        win.resizable(False,False)
                        win.configure(background='black')

                        self.txt1 = tk.Label(win, text="WRITE  FILE NAME : ")
                        self.txt1.place(relx=0.220, rely=0.099)
                        self.txt1.configure(bg='black',fg='red')
                        self.filename = tk.Entry(win)
                        self.filename.place(relx=0.220, rely=0.190, height=29, width=279)
                        self.filename.configure(bg='black',fg='red')
                        self.txt2 = tk.Label(win, text="WRITE FOLDER PATH : ")
                        self.txt2.place(relx=0.220, rely=0.320)
                        self.txt2.configure(bg='black',fg='red')
                        self.folder = tk.Entry(win)
                        self.folder.place(relx=0.220, rely=0.420, height=29, width=279)
                        self.folder.configure(bg='black',fg='red')
              
                        def help_save():
                            win2 = tk.Tk()
                            win2.geometry("400x99")
                            win2.resizable(False, False)
                            win2.configure(background="black")
                            win2.title("HELP")
                            txt3 = tk.Label(win2, text="""example filename : my-web-ip.txt \n
                example folder path:/home/user-name/Desktop/""")
                            txt3.place(x=4, y=3)
                            txt3.configure(bg='black',fg='red' )
                            win2.mainloop()
        
                        def save_file():
                             try:
                                name = self.filename.get()
                                src = self.folder.get()
                                file=open(src+name,'w')
                                file.write(web_ip)
                                file.close()
                                file_info = tk.Label(win,text='file saved in folder:')
                                file_info2 =tk.Label(win, text=file)
                                file_info.configure(bg='black',fg='red')
                                file_info2.configure(bg='black',fg='red')
                                file_info2.place(relx=0.489,rely=0.870,width=212)
                                file_info.place(relx =0.220,rely=0.870,width=124)
                             except:
                                 pass
                       
                            

                        self.bt_save1 = tk.Button(win, text="SAVE FILE",command=save_file)
                        self.bt_save1.place(relx=0.220, rely=0.620, height=44, width=99)
                        self.bt_save1.configure(bg='red',fg="black",activebackground='black',activeforeground="red")
                        self.bt_save1.configure(relief='flat')

                        self.bt_help = tk.Button(win, text="HELP", command=help_save)
                        self.bt_help.place(relx=0.590, rely=0.620, height=44, width=99)
                        self.bt_help.configure(bg='red',fg="black",activebackground='black',activeforeground="red")
                        self.bt_help.configure(relief='flat')
                    # -------------------------------------
                      
            


                def save():
                    dir1()
                    pass

                def reset():
                    res.destroy()
                    bt_res.destroy()
                    bt_save.destroy()
                    open_browser.destroy()
                    
                    textbox1.configure(state=NORMAL)
                
                   
                

                    
                    pass

                def open_wb():
                    ip = str(web_ip)
                    txt_ip =str("http://%s"%((ip)))
                    web = webbrowser.open(txt_ip)
                    
                    
                    
                    
    
                 
                      
              

                bt_res = tk.Button(root2, text="CLEAR", command=reset)
                bt_res.place(x=230, y=345)
                bt_res.configure(
                    bg='red', fg='black', activeforeground='red', activebackground='black')
                bt_res.configure(relief='flat')

                bt_save = tk.Button(root2, text="SAVE FILE", command=save)
                bt_save.place(x=310, y=345)
                bt_save.configure(bg='red', fg='black', activeforeground='red', activebackground='black')
                bt_save.configure(relief='flat')
                open_browser= tk.Button(root2, text = ' open_browser',command=open_wb)
                open_browser.place(x=410, y=345)
               
        
                open_browser.configure(bg='red', fg='black', activeforeground='red', activebackground='black')
                open_browser.configure(relief='flat')
                


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

class  more_tools:
    def __init__(self):
        master = tk.Tk()
        master.geometry('300x300')
        master.title('More Tools')
        master.configure(bg='black')
        master.resizable(False, False)
       
        # set button  
        self.bt_new_host = tk.Button(master, text='set_new_hostname',command=hostname1)
        self.bt_new_host.place(x=20, y=10)
        self.bt_new_host.configure(bg='red', fg='black',
                                 activebackground='black', activeforeground='red', relief='flat', borderwidth='2')
class hostname1:
    def __init__(self):
       
       
        master = tk.Tk()
        master.geometry('600x300')    
        master.title('Set_Hostname')
        master.configure(bg='black')
        master.resizable(False, False)
        # def command for  button  go and entry 
        def  go_host ():
          
                self.entry_convert = self.new_hostname.get()
                self.host =os.system('hostnamectl set-hostname  %s'%((self.entry_convert)))
                self.myhostname =os.system('hostname')
                self.help1 = tk.Label(master,text="open you terminal and type : hostname or hostnamectl")
                self.help1.place(x=120,y=100)

         


       
        # set entry 
        self.new_hostname= tk.Entry(master, text= 'new_hostname')
        self.new_hostname.place(relx=0.270, rely=0.190, height=29, width=279)
        self.new_hostname.configure(bg='black', fg='red')
        # set button  go to entry 
        self.bt_go = tk.Button(master,text='GO',command=go_host)
        self.bt_go.place(x=470, y=60)
        self.bt_go.configure(bg='red', fg='black',activebackground='black', activeforeground='red', relief='flat', borderwidth='2')

class frame():
    def __init__(self, master):

        self.Frame1 = tk.Frame(master)
        self. Frame1.place(relx=0.068, rely=0.044,
                           relheight=0.744, relwidth=0.899)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="3")
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

       
       

       
        menu1=tk.Menu(root,bg="black",fg='red',borderwidth=0)
        root.configure(menu=menu1)
        file_menu=Menu(menu1,bg="black")
        menu1.add_cascade(label="Menu",menu=file_menu)
        file_menu.add_command(label="web_ip",command=ip_web,activebackground='red')
        file_menu.add_command(label="more tools",command=more_tools,activebackground='red')
        file_menu.add_separator()
        file_menu.add_command(label="INFO",command=info1,activebackground='red')
        file_menu.add_command(label="EXIT",command=quit,activebackground='red')


e = frame(root)



root.mainloop()
