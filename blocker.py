#!/usr/bin/env python3
import subprocess
import sys
import os

def blocker():
    while True:
        ip_address = input('IP> ')
        print('Block',ip_address,'?')
        flag = input('(Y/n)>')
        if len(flag) == 0 or flag == 'Y':
            break
    
    subprocess.run(['iptables','-A','OUTPUT','-d',ip_address,'-j','DROP'])
    subprocess.run(['iptables','-A','INPUT','-s',ip_address,'-j','DROP'])
    print('Completed.')

def allow():
    print("*****************************************************************")
    status = subprocess.run(['iptables','-L','INPUT','--line-numbers'],stdout = subprocess.PIPE)
    print(status.stdout.decode("utf8"))
    print("*****************************************************************")
    
    number = input('number> ')
    subprocess.run(['iptables','-D','OUTPUT',number])
    subprocess.run(['iptables','-D','INPUT',number])
    print('Completed.')
    

def status():
    print("*****************************************************************")
    status = subprocess.run(['iptables','-L','--line-numbers'],stdout = subprocess.PIPE)
    print(status.stdout.decode("utf8"))
    print("*****************************************************************")

def main():
    if os.geteuid() == 0 and os.getuid() == 0 :
        pass
    else:
        print("Please root.")
        sys.exit(0)
    
    
    while True:
        print("""
        [1] IP BLOCK
        [2] IP ALLOW
        [3] STATUS
        [4] EXIT
        """)
        flag = input('> ')
        
        if flag == '1':
            blocker()
        elif flag == '2':
            allow()
        elif flag == '3':
            status()
        elif flag == '4':
            sys.exit(1)
        else:
            pass

if __name__ == "__main__":
    banner = """
 ### ##   ####      ## ##    ## ###  ###  ##  ### ###  ### ##  
  ##  ##   ##      ##   ##  ##   ##   ##  #    ##   #   ##  ## 
  ##  ##   ##      ##   ##  ##        ## #     ##  #    ##  ## 
  ## ##    ##      ##   ##  ##        ## #     ## ##    ## ##  
  ##  ##   ##      ##   ##  ##        ## ##    ##  #    ##  ## 
  ##  ##   ##   #  ##   ##  ##    #   ## ###   ##   #   ##  ## 
 ### ##    ## ###   ## ##    ## ##   ###  ##  ### ###  ###   # 
                                                               

"""
    print(banner)
    main()