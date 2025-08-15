class oddEven():
   def oddEven():
     num = int(input("Enter a number:"))
     if((num%2)==1):
            print(num,"is odd number")
     else:
        print(num,"is even number")

class subfieldsInAI():
    def Subfields():
        list=("Machine Learning","Neural Network","Vision","Robotics","Speech Processing","Natural Language Processing")
        print("Sub-fields in AI are:")
        for temp in list:
            print(temp)
            
class ElegibilityforMarriage():
    def Eligible():
        Gender=input("Your Gender:")
        Age=int(input("Your Age:"))
        if(Gender=="Male" and Age >= 21):
            print("Eligible")
        elif(Gender=="Female" and Age >= 18):
            print("ELIGIBLE")
        else:
            print("NOT ELIGIBLE")
            
class findpercent():
    def percentage():
        Subject1=int(input("Subject1:"))
        Subject2=int(input("Subject2:"))
        Subject3=int(input("Subject3:"))
        Subject4=int(input("Subject4:"))
        Subject5=int(input("Subject5:"))
        Total=Subject1+Subject2+Subject3+Subject4+Subject5
        print("Total:",Total)
        percentage=(Total/500)*100
        print("Percentage:",percentage)
        
class triangle():
        def triangle():
            Height=int(input("Height:"))
            Breadth=int(input("Breadth:"))
            Area=(Height*Breadth)/2           
            print("Area formula:(Height*Breadth)/2")
            print("Area of Triangle:",Area)
            Height1=int(input("Height1:"))
            Height2=int(input("Height2:"))
            Breadth1=int(input("Breadth:"))
            Perimeter=Height1+Height2+Breadth1
            print("Perimeter formula:Height1+Height2+Breadth")
            print("Perimeter of Triangle:",Perimeter)