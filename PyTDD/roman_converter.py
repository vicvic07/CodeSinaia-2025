

def roman_convertor (num):
    if isinstance(num, int) and num>=1 and num<=3999:
        out=''
        while num>=1000:
            out+='M'
            num=num-1000
        while num>=500:
            out+='D'
            num=num-500
        while num>=100:
            out+='C'
            num=num-100
        while num>=50:
            out+='L'
            num=num-50
        while num>=10:
            out+='X'
            num=num-10
        while num>=5:
            out+='V'
            num=num-5
        while num>=1:
            out+='I'
            num=num-1
        return out

    else:
        return
