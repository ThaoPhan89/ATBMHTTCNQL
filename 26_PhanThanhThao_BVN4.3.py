def mahoa_rsa(p, q, e, plaintext):
    n = p * q
    phi_n = (p - 1) * (q - 1)
    print(f"n = {n}, phi(n) = {phi_n}")

    public_key = (e, n)

    ma = [(pow((ord(tu.upper()) - ord('A')), e, n)) for tu in plaintext if tu.isalpha()]

    return ma, public_key


#Test
p = 17
q = 23
e = 5
plaintext = "PhanThanhThao"
ma, public_key = mahoa_rsa(p, q, e, plaintext)

print("Khoa cong khai (e, n):", public_key)
print("Noi dung ban dau:", plaintext)
print("Ma hoa:", ma)
