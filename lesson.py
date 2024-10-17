import random

# 65~90 (A-Z)  97~122 (a-z)

# 暗号化処理
def Encrypt(key_number, text):
    # 入力された平文をアスキーコードの数値に変換して、配列に格納している
    ord_text = [ord(x) for x in text]
    encryption = []

    for i in range(len(ord_text)):
        # 大文字だった場合の処理
        if ord_text[i] >= 65 and ord_text[i] <= 90:
            # 0~25の間で収まるようにするために25のあまりをとっている。
            # 65基づきで、アルファベットがまた行った場合にまた戻れるようになる
            encryption.append(chr(((ord_text[i] - 65 + key_number) % 26) + 65))
        # 小文字だった場合の処理
        elif ord_text[i] >= 97 and ord_text[i] <= 122:
            encryption.append(chr(((ord_text[i] - 97 + key_number) % 26) + 97))
        else:
            encryption.append(text[i])
    return "".join(encryption)

# 復号処理
def Decrypt(key_number, Encrypt_text):
    ord_text = [ord(x) for x in Encrypt_text]
    decryption = []

    for i in range(len(ord_text)):
        # 大文字だった場合の処理
        if ord_text[i] >= 65 and ord_text[i] <= 90:
            # 0~25の間で収まるようにするために25のあまりをとっている。
            # 65基づきで、アルファベットがまた行った場合にまた戻れるようになる
            decryption.append(chr(((ord_text[i] - 65 - key_number) % 26) + 65))
        # 小文字だった場合の処理
        elif ord_text[i] >= 97 and ord_text[i] <= 122:
            decryption.append(chr(((ord_text[i] - 97 - key_number) % 26) + 97))
        else:
            decryption.append(text[i])
    return "".join(decryption)

# ブルートフォース
def brute_force_attack(text):
    for i in range(26):
        decrypted_text = Decrypt(i, text)
        print('鍵 {} の場合の復号文: {}'.format(i, decrypted_text))

key_number = random.randint(0, 25)
print('100文字以内で入力してください')
text = input()

Encrypt_text = Encrypt(key_number, text)

# 暗号化
print('鍵{}個で暗号化した文は{}'.format(key_number, Encrypt(key_number, text)))
print()

# 復号化
print('鍵{}個で暗号化した文は{}'.format(key_number, Decrypt(key_number, Encrypt_text)))
print()

# ブルートフォース
brute_force_attack(Encrypt_text)

