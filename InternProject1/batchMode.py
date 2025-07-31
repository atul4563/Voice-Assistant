# checking input for a string
def checkString(TestString):
    res= type(TestString)== str
    if (res!= True) :
        print("Invalid Input")
        return 0
    return 1


def consecutive(TestString):
   print(TestString)
   t=0
   for element in TestString:
       if(element=='@'):
           t=t+1
   if(t==2):
       print("invalid")
       return 0
   else:
       return 1
   


def localDomain(local, domain):
    last=local[len(local)-1]
    if ((local[0]=='!' or last=='!') or (local[0]=='#' or last=='#') or (local[0]=='$'or last=='$') or (local[0]=='%' or last=='%') or (local[0]=='&' or last=='&') or (local[0]=="'" or last=="'") or (local[0]=='*' or last=='*') or (local[0]=='+' or last=='+') or (local[0]=='-' or last=='-')  or (local[0]=='/' or last=='/') or (local[0]=='=' or last=='=') or (local[0]=='?' or last=='?') or (local[0]=='^' or last=='^') or (local[0]=='_' or last=='=') or (local[0]=='{'or last=='{') or (local[0]=='}' or last=='}') or (local[0]=='|' or last=='|') or (local[0]=='~' or last=='~') or (local[0]==',' or last==',') or (local[0]=='.' or last=='.')):
        return 0
        print("Invalid email address")
    else:
        list=['!','#','$','%','&',",",'*','+','*','=','/','=','?','^','_','{','}','|','~',',','.']
        for element in range(0,len(local)):
            for j in range(0,len(list)):
                if(local[element]==list[j] and local[element+1]==list[j]):
                    return 0
                    print("invalid email")
                    break
    t=0
    for element in domain:
        if(element=='.'):
            t=t+1
        if(element=='_'):
            return 0
            print("Invalid email address")
            break
        if(element.isalpha() or element.isdigit() or element!='-'):
            continue
        else:
            return 0
            print("Invalid email address")
            break
    if(t<1):
        return 0
        print("invalid email address")
    
    if(local.find(' ')!=-1 or local.find('/')!=-1 or local.find("'")!=-1 or local.find("'")!=-1 or local.find('"')!=-1 or local.find('"')!=-1 or local.find(';')!=-1 or local.find(':')!=-1 or local.find('!')!=-1 or local.find('?')!=-1 or local.find('-')!=-1 or local.find("'")!=-1 or local.find('(')!=-1 or local.find(')')!=-1 or local.find('[')!=-1 or local.find(']')!=-1):
        if(local[0]!='"' and local[len(local)-1]!='"'):
            return 0
            print("invalid emaail")  
    period=domain.rfind('.')
    if(len(domain.rsplit('.'))<2):
        return 0
        print("invalid email")
    if(local[0]=='@' or local[0]=='-' or domain[-1]=='-'):
        return 0
        print("invalid")

    list=['com','edu','org']
    dom=domain.rsplit('.')[1]
    for element in list:
        if(dom!=element):
            return 0
            print("invalid emailll")
            break
        else:
            break
    return 1  





def ValidateEmail(TestString):
   if(TestString[0]=='@'):
       return 0
   loc= TestString.find("@")
   local=TestString[0:loc]
   
   domain=TestString[loc:]
   if (len(domain)<=6):
       return 0
    #    print("Invalid email")
   elif (len(local)>64):
       return 0
       print("Invalid email")
   valid=localDomain(local,domain)
   valid=checkString(TestString)
   valid=consecutive(TestString)
   return valid
    


file= open("abc.txt",'r')
line=file.readlines()
# print(type(line))
file1=open("newEmail.txt","w")

for element in line:
    # print(element)
    valid=ValidateEmail(element)
    if(valid==1):
        file1.write("valid email\n")
    else:
        file1.write("invalid email\n")




file1.close()
file.close()


