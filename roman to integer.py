def roman_convert():
    ip = input("Please enter your roman numeral:")
    ans=0
    roman_dict = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    for i in range(len(ip)-1):
        if roman_dict[ip[i]]<roman_dict[ip[i+1]]:
            ans=ans-roman_dict[ip[i]]
        else:
            ans=ans+roman_dict[ip[i]]
    return ans+ roman_dict[ip[-1]]
print(roman_convert())
# roman_dict = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
# print(roman_dict['I'])
# print(roman_dict['V'])



