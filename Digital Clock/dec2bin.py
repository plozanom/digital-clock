def dec2bin(num:int):

    binary = ''
    dec = num
        
    while dec > 1:

        binary = str(dec%2) + binary
        dec = dec//2
    else:
        binary = str(dec) + binary
    
    if len(binary) < 6:
        binary = (6- len(binary))*'0' + binary

    return binary