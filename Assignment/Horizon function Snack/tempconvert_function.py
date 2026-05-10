def farenheit_celsius(f):
        #f= int(input("Enter temperature in degrees Farenheit "))
        
        c= (f-32)*(5/9)
        
        if(c <= 0):
            messages= "Cold advisory"
        elif(c >= 100):
            messages= "Heat alert!"
        else:
            messages= "Temperature is not above or below threshold"
        return c, messages
        
print(farenheit_celsius(100) )

def celsius_farenheit(c):
        #c= int(input("Enter temperature in degrees celsius "))
        f= c * (9/5)+32
      
        if(f <= 32):
            messages= "Cold advisory"
        elif(f >= 212):
            messages= "Heat alert!"
        else:
            messages= "Temperature is not above or below threshold"
        return f, messages
        
print(celsius_farenheit(100) )
    
