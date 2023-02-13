def dec2hexa(num:int):

    dec = num
    hexa = ''
    hexa_list = []

    hexa_dic = {0:'0', 1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9', 10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}

    if dec == 0:
        hexa = '0'
    else:
        while dec > 0:
            hexa_list.append(dec%16)
            dec = dec//16
    
    for i in hexa_list:
        if i in hexa_dic:
            hexa = hexa_dic[i] + hexa
    if len(hexa) == 1:
        hexa = '0' + hexa    
    
    return hexa