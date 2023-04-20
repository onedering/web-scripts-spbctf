import subprocess

def ranger(iter):
    i=0
    output = subprocess.check_output(['curl' ,'-v', 'https://intro.spbctf.com/cookie2/']).decode('utf-8')
    print('its print',output)
    a = []
    while i!=iter:
        i+=1                                                  
        a.append("name"+i+"=vote")                                                         
        print(a)
        d = output.find("votes=")
        print('its coockie id',id)
        flag = output[id:id+45]
        print('its coockie',flag)
        output = subprocess.check_output(['curl' ,'-b',flag, 'https://intro.spbctf.com/cookie2/']).decode('utf-8')
    print("end ", output)

def coockie_create(num):
    subprocess.run(['curl' ,'-v', 'https://intro.spbctf.com/cookie2/'])
    a = []
    i=0
    while i!=num:
        i+=1                                                  
        a.append("name"+str(i)+"=vote")                                                         
    print(a)
    subprocess.run(['curl' ,'-b', a , 'https://intro.spbctf.com/cookie2/'])
       













