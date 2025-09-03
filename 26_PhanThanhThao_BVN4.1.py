# -*- coding: utf-8 -*-
def mahoa_caesar(vanban, k):
    kq = ""
    for tu in vanban:
        if tu.isalpha(): 
            s = 'A' if tu.isupper() else 'a'
            kq += chr((ord(tu) - ord(s) + k) % 26 + ord(s))
        else:
            kq += tu 
    return kq


def giaima_caesar(vbmh, k):
    return mahoa_caesar(vbmh, -k)



#Test
plaintext = "Phan Thanh Thao"
k = 26

mahoa = mahoa_caesar(plaintext, k)
giaima = giaima_caesar(mahoa, k)

print(f'Van ban: {plaintext}')
print(f"Ma hoa: {mahoa}")
print(f"Giai ma: {giaima}")
