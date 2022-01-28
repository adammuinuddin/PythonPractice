#The purpose of this program is to convert temperature from celsius to farenheit

c_f_or_neither = str(input("Input c for celsius to farenheit calculation and input f for farenheit to celsius calculation: "))

if c_f_or_neither == str("c"):
    c = int(input("Input the temperature in celsius and wait for the result in farenheit: "))
    c_to_f = (9 * c / 5) + 32
    print(c, "degrees celsius is equal to", c_to_f, "degrees farenheit")
elif c_f_or_neither == str("f"):
    f = int(input("Input the temperature in farenheit and wait for the result in celsius: "))
    f_to_c = ((5 * f) - (5 * 32)) / 9
    print(f, "degrees farenheit is equal to", f_to_c, "degrees celsius")
else:
    print("If you do not want a calculation from celsius to farenheit or farenheit to celsius stop using this program")
