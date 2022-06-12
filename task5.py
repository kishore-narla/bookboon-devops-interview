$ pip install inflect
import inflect 
p=inflect.engine()
def printnum(n):
     for i in range(n+1):
         if(i%10==0):
             print(p.number_to_words(i))
             else:
                 print(i)
                 printnum(100)


