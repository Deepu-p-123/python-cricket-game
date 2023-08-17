#odd or even
import random

dict1={}
result={'usr':0,'cmp':0}
def dictcheck():
    option=input("enter odd or even :) \t")
    if option=='odd':
        dict1['usr'] ='odd'
        dict1['cmp']='even'
    elif option=='even':
        dict1['usr'] ='even'
        dict1['cmp']='odd'
    else:
        print("please enter a valid option !") 
    return dict1    

  


def inpu():
    num1=int(input("enter a number between 1 to 5 : --->   "))
    if num1>5:
        print("please enter a value between 1 to 5")
        exit(0)
    num2=random.randint(1,5)
    print(num2)
    sum=num1+num2
    if sum%2==0:
        s='even'
    else:
        s='odd' 
    return s        

def check(s):
    if s== dict1['usr']:
        print("user wins you can choose balling or batting")
        bt=input("enter balling or batting :---\t\t")
        print(f"""
            #######    starting  {bt}     #######
              
              """)
    else:
        
        bt=random.choice(['balling','batting'])
        print(f'computer wins computer chooses {bt}') 
        
        print(f"""
            #######    starting  {bt}     #######
              
              """)
        
         
    return bt      


    
    
    
    
    
    
            
def btingusr():
    score=0
    while True:
        n1=int(input("enter a number between 0 to 6 :---> \t"))
        if n1>6:
            print("cheeting!  YOU failed")
            exit(0)   
        n2=random.randint(0,6)
        print(f"""
                  {n1} : {n2}
              """)
        if n1==n2:
            print(">>>>>>>>  OUT   <<<<<<<<<<<<<<  ")
            print("your score is \t ",score)
            result['usr'] = score
            break
        else:
            score=score+n1+n2 
    return score


def btingcmp():
    score=0
    while True:
        n1=int(input("enter a number between 0 to 6"))
        if n1>6:
            print("cheeting!  YOU failed")
            exit(0)
        n2=random.randint(0,6)
        print(f"""
                  {n1} : {n2}
              """)
        if n1==n2:
            print(">>>>>>>>  OUT   <<<<<<<<<<<<<<  ")
            print("computer score is ",score)
            result['cmp']=score
            break
        else:
            score=score+n1+n2
             
            
    return score

          
            
     
 
dictcheck()
s=inpu()
print(dict1) 
bt=check(s)
 

if bt=='batting' and dict1['usr'] ==s:
    score1=btingusr()
    print(score1)
    print("$$$$  computer is batting $$$$")
    score2=btingcmp()
    print(score2)
    
else:
    score2=btingcmp()
    print(score2)
    print("$$$$ user start baatting  $$$$")
    score1=btingusr()
    print(score1)
    
    
    
if score1>score2:
    print("you win the match") 
    print(result)
else:
    print("computer wins the match") 
    print(result)      
    
    
    