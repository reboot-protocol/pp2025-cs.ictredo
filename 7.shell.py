import os
def red_out(command,filename):
    read_fd,write_fd = os.pipe()
    pid = os.fork()
    if pid > 0:
        os.close(write_fd)
        with os.fdopen(read_fd,'r') as f:
            data = f.read()
            try :
                with open(filename,"w")as t:
                    t.write(data)    
            except Exception:
                with open(filename,"a")as t:   
                    t.write(data)
    else: 
        os.close(read_fd)  
        temp = os.popen(command).read()  
        with  os.fdopen(write_fd, 'w') as f:
            f.write(temp)
        os._exit(0)  





def red_inp(command,filename):
    read_fd,write_fd = os.pipe()
    pid = os.fork()
    if pid > 0:
        os.close(write_fd)
        with os.fdopen(read_fd,'r') as f:
            data = f.read()
            os.popen(command,'w').write(data)
        
            
    else: 
        os.close(read_fd)  

        with  os.fdopen(write_fd, 'w') as f:
            try :
                with open(filename,"r")as t:
                    lines = len(t.readlines())

                    t.close()
                with open(filename,"r")as t:
                    for i in range(0,int(lines)):
                        data = t.readline() 
                        f.write(data+ '\n')   
            except Exception as e:
                print(e)
                return
            
        os._exit(0)  






def normal_com(command):
            read_fd,write_fd = os.pipe()
            pid = os.fork()

            if pid > 0:
                os.close(write_fd)
                with os.fdopen(read_fd,'r') as f:
                    data = f.read()
                    print(data)
                
                

            else: 
                os.close(read_fd)  
                temp = os.popen(command).read()  
                with  os.fdopen(write_fd, 'w') as f:
                    f.write(temp)
                os._exit(0)  




                
def both_inp_out(command,filename,file_out):
    read_fd,write_fd = os.pipe()
    pid = os.fork()
    if pid > 0:
        os.close(write_fd)
        with os.fdopen(read_fd,'r') as f:
            data = f.read()
            com = "echo " + data.strip() + " | " + command
            temp = os.popen(com,'r').read()
            try:
                with open(file_out,"w") as t:
                    t.write(str(temp))
                    t.close()
            except Exception:
                with open(file_out,"a") as t:
                    t.write(str(temp))
                    t.close()

            
    else: 
        os.close(read_fd)  

        with  os.fdopen(write_fd, 'w') as f:
            try :
                with open(filename,"r")as t:
                    lines = len(t.readlines())

                    t.close()
                with open(filename,"r")as t:
                    for i in range(0,int(lines)):
                        data = t.readline() 
                        f.write(data+ '\n')   
            except Exception as e:
                print(e)
                return
            
        os._exit(0)  






while True:
    print(os.getcwd(),end=' ')
    command = input()
    if(command.rfind('cd') != -1):
        if(command.rfind(" ") != -1):

                temp1 = command.rfind(" ")
                argu = command[temp1+1:]
                com = command[:temp1]
        else:
                com = command
                argu =""
        if (argu.rfind("/") == -1 ):
            try:
                current_path = os.getcwd()
                full_path = current_path + "/" + argu
                os.chdir(full_path)
            except Exception:
                print(f"No such file or directory {argu} ")
        elif(argu == ""):
            try:
                os.chdir('/')
            except Exception:
                print("Cannot change to root directory")
        else:
            try:
                os.chdir(argu)
            except Exception:
                print("no such file or directory")
    elif(command.rfind('exit')!= -1):
        break
    elif(command.rfind('<') == -1 or command.rfind('>') == -1):
        normal_com(command)
    elif(command.rfind('<') == -1 and command.rfind('>') != -1):
        temp1 = command.rfind(">")
        
        argu = command[temp1+2:]
        com = command[:temp1]
        red_out(com,argu)
    elif(command.rfind('<') != -1 and command.rfind('>') == -1):
        command = str(command)
        temp1 = command.rfind("<")
        
        argu = command[temp1+2:]
        
        com = command[:temp1]
        

        red_inp(com,argu)
    elif(command.rfind('<') != -1 and command.rfind('>') != -1):
        temp1 = command.rfind("<")
        temp2 = command.rfind(">")
        inp = command[temp1+2:temp2-1]
        out = command[temp2+2:]
        com = command[:temp1]
        both_inp_out(com,inp,out)
    
