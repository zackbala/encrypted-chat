from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from settings import *

key = KEY
iv = IV

chiper = Cipher(algorithms.AES(key), modes.CBC(iv))


def encriptar(msg):
    msg_bytes = msg.encode('utf-8')
    padder = padding.PKCS7(128).padder()
    msg_bytes_padded = padder.update(msg_bytes) + padder.finalize()

    # ENCRIPTANDO A MENSAGEM
    encryptor = chiper.encryptor()
    cipher_text = encryptor.update(msg_bytes_padded) + encryptor.finalize()
    return cipher_text


def desencriptar(msg):
    decryptor = chiper.decryptor()
    plaintext_padded = decryptor.update(msg) + decryptor.finalize()
    unpadder = padding.PKCS7(128).unpadder()
    plaintext = unpadder.update(plaintext_padded) + unpadder.finalize()
    decodetext = plaintext.decode('utf-8')
    return decodetext
