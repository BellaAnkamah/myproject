inp=input("enter the temperature in celsius")
celsius=float(inp)
print(celsius)
fahrenheit = (celsius * 9/5) + 32
if celsius < -273.15:
    print("ERROR ERROR ERROR")
else: 
    print(f"The temperature is {celsius}C or {fahrenheit}F")

