
def Main():
    while True:
        mode = input("Enter your mode:\n1:plain to cipher\n2:cipher to plain\nmode: ")
        try:
            mode = int(mode)
            break
        except:
            continue
    if mode == 1:
        text_cipher()
    elif mode == 2:
        Cipher_text()
    else:
        Main()


def text_cipher():
    while True:
        key = input("Enter an integer key: ")
        try:
            key = eval(key)
            break
        except:
            continue
    if type(key) == int:
        plain_text = input("Enter plain text: ")
        cipher_text = ''
        for i in plain_text:
            cipher_text += chr(ord(i)+key)
        print('cipher text : {}'.format(cipher_text))
    else:
        text_cipher()


def Cipher_text():
    while True:
        key = input("Enter an integer key: ")
        try:
            key = eval(key)
            break
        except:
            continue
    if type(key) == int:
        cipher_text = input("Enter cipher text: ")
        plain_text = ''
        for i in cipher_text:
            plain_text += chr(ord(i)-key)
        print('plain text: {}'.format(plain_text))
    else:
        Cipher_text()


Main()
