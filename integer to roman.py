#integer to roman
def intToRoman():
    num = int(input("Please enter your numeral:"))
    roman=""
    # roman = []
    roman_dict = [(1000,"M"), (900,"CM"),(500,"D"),(400,"CD"),(100,"C"),(90,"XC"),(50,"L"),(40,"XL"),(10,"X"),(9,"IX"),(5,"V"),(4,"IV"),(1,"I")]
    for keys,values in roman_dict:
        if num == 0:
            break
        count = num // keys
        roman+=values*count
        # roman.append(values * count)
        num = num % keys
    return roman
    # return "".join(roman)
print(intToRoman())
