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