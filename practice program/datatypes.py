maths = int(input("enter maths marks : "))
physics = int(input("enter physics marks : "))
biology = int(input("enter biology marks : "))
telugu = int(input("enter telugu marks : "))
hindi = int(input("enter  hindi marks : "))
avarage = int(maths + physics + biology + telugu + hindi / 5)
print(avarage)
if avarage == 150 or avarage < 250:
    print("you are very poor in studies go and bend infront of MLA")
elif avarage > 450 or avarage <= 500:
    print("you are outstanding and excellent in studies")    
else:
    print("you are just avarage in studies")    
if maths == 35:
    print("you are border Pass in maths")
elif maths >= 40 and maths < 50:
    print("maths Grade C")
elif maths >= 50 and maths < 60:
    print("maths Grade B")   
elif maths >= 60 and maths < 70:
    print("maths Grade B+")
elif maths >= 70 and maths < 80:    
    print("maths Grade A")
elif maths >= 80 and maths < 90:
    print("maths Grade A+") 
elif maths >= 90 and maths < 100:
    print("maths Grade O") 
else:
    print("you are Fail in maths fool")         
if physics == 35:
    print("you are just boader pass in physics ")   
elif physics >= 40 and physics < 50:
    print("Grade C")
elif physics >= 50 and physics < 60:
    print("Grade B")   
elif physics >= 60 and physics < 70:
    print("Grade B+")
elif physics >= 70 and physics < 80:    
    print("Grade A")
elif physics >= 80 and physics < 90:
    print("Grade A+") 
elif physics >= 90 and physics < 100:
    print("Grade O") 
else:
    print("you are Fail in physics") 
if biology == 35:
    print("you are border Pass in biology")
elif biology >= 40 and biology < 50:
    print("Grade C")
elif biology >= 50 and biology < 60:
    print("Grade B")   
elif biology >= 60 and biology < 70:
    print("Grade B+")
elif biology >= 70 and biology < 80:    
    print("Grade A")
elif biology >= 80 and biology < 90:
    print("Grade A+") 
elif biology >= 90 and biology < 100:
    print("Grade O") 
else:
    print("you are Fail in biology")  
if telugu == 35:
    print("you are border Pass in telugu")
elif telugu >= 40 and telugu < 50:
    print("Grade C")
elif telugu >= 50 and telugu < 60:
    print("Grade B")   
elif telugu >= 60 and telugu < 70:
    print("Grade B+")
elif telugu >= 70 and telugu < 80:    
    print("Grade A")
elif telugu >= 80 and telugu < 90:
    print("Grade A+") 
elif telugu >= 90 and telugu < 100:
    print("Grade O") 
else:
    print("you are Fail in telugu")  
if hindi == 35:
    print("you are border Pass in hindi")
elif hindi >= 40 and hindi < 50:
    print("Grade C")
elif hindi >= 50 and hindi < 60:
    print("Grade B")   
elif hindi >= 60 and hindi < 70:
    print("Grade B+")
elif hindi >= 70 and hindi < 80:    
    print("Grade A")
elif hindi >= 80 and hindi < 90:
    print("Grade A+") 
elif hindi >= 90 and hindi < 100:
    print("Grade O") 
else:
    print("you are Fail in hindi")             