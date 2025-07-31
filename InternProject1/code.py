 t=0
    if (len(TestString)>254):
        print("Invalid email address")
        return 0
    for elements in TestString:
        if (elements=='@'):
            # a= elements
            t=t+1
        if (elements==' '):
            print("Invalid email add1ress")
            return 0
            break
        # if(t==2):
        #     print("Invalid email ad2dress")
        #     return 0
        #     break
    if (t==2):
        print("Invalid email add3ress")
        return 0






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