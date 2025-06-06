import os
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

class ECCCipher:
    def __init__(self):
        pass

    def generate_keys(self):
        private_key = ec.generate_private_key(ec.SECP256R1(), default_backend())
        public_key = private_key.public_key()

        with open('cipher/ecc/keys/privateKey.pem', 'wb') as p:
            p.write(private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.PKCS8,
                encryption_algorithm=serialization.NoEncryption()
            ))

        with open('cipher/ecc/keys/publicKey.pem', 'wb') as p:
            p.write(public_key.public_bytes(
                encoding=serialization.Encoding.OpenSSH,
                format=serialization.PublicFormat.OpenSSH
            ))

    def load_keys(self):
        with open('cipher/ecc/keys/privateKey.pem', 'rb') as key_file:
            private_key = serialization.load_pem_private_key(
                key_file.read(),
                password=None,
                backend=default_backend()
            )

        with open('cipher/ecc/keys/publicKey.pem', 'rb') as key_file:
            public_key = serialization.load_ssh_public_key(
                key_file.read(),
                backend=default_backend()
            )

        return private_key, public_key

    def encrypt(self, message, key):
        encrypted_data = key.encrypt(
            message.encode('ascii'),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return encrypted_data

    def decrypt(self, ciphertext, key):
        try:
            decrypted_data = key.decrypt(
                ciphertext,
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None
                )
            )
            return decrypted_data.decode('ascii')
        except:
            return False

    def sign(self, message, key):
        signature = key.sign(
            message.encode('ascii'),
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return signature

    def verify(self, message, signature, key):
        try:
            key.verify(
                signature,
                message.encode('ascii'),
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )
            return True
        except:
            return False