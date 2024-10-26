from base64 import b64encode as be, b64decode as bd
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from hashlib import sha256
import os


class MySession:
    def __init__(self, server_public_key, encrypted_challenge):
        self._server_public_key = server_public_key
        self._encrypted_challenge = encrypted_challenge
        self._session_key = sha256(str(0).encode()).digest()

        self.packet = self._get_encrypted_packet()
        self.challenge_hash = self._get_challenge_hash()

    def _get_encrypted_packet(self):
        iv = os.urandom(16)
        cipher = AES.new(self._session_key, AES.MODE_CBC, iv)
        encrypted_packet = iv + cipher.encrypt(pad("flag".encode(), 16))
        return be(encrypted_packet).decode()
    
    def _get_challenge_hash(self):
        decoded_challenge = bd(self._encrypted_challenge.encode())
        iv = decoded_challenge[:16]
        encrypted_challenge = decoded_challenge[16:]
        cipher = AES.new(self._session_key, AES.MODE_CBC, iv)
        try:
            decrypted_challenge = unpad(cipher.decrypt(encrypted_challenge), 16)
            return sha256(decrypted_challenge).hexdigest()
        except:
            raise
    
    def decrypt_flag(self, encrypted_flag):
        decoded_flag = bd(encrypted_flag.encode())
        iv = decoded_flag[:16]
        encrypted_flag = decoded_flag[16:]
        cipher = AES.new(self._session_key, AES.MODE_CBC, iv)
        try:
            decrypted_packet = unpad(cipher.decrypt(encrypted_flag), 16)
            flag = decrypted_packet.decode().strip()
        except:
            raise

        return flag
