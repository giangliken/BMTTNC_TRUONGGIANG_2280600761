from flask import Flask, request, jsonify
from cipher.caesar import CaesarCipher
from cipher.railfence import RailFenceCipher 
from cipher.vigenere import VigenereCipher
from cipher.playfair import PlayfairCipher
from cipher.transposition import TranspositionCipher

app = Flask(__name__)
caesar_cipher = CaesarCipher()
@app.route("/api/caesar/encrypt", methods=['POST'])
def caesar_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = int(data['key'])
    encrypted_text = caesar_cipher.encrypt(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})
@app.route("/api/caesar/decrypt", methods=['POST'])
def caesar_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = int(data['key'])
    decrypted_text = caesar_cipher.decrypt_text(cipher_text, key)
    return jsonify({'decrypted_message': decrypted_text})

railfence_cipher = RailFenceCipher() 
@app.route("/api/railfence/encrypt", methods=['POST']) #
def encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = int(data['key'])
    encrypted_text = railfence_cipher.rail_fence_encrypt(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})
@app.route("/api/railfence/decrypt", methods=['POST']) #
def decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = int(data['key'])
    decrypted_text = railfence_cipher.rail_fence_decrypt(cipher_text, key)
    return jsonify({'decrypted_message': decrypted_text})

vigenere_cipher = VigenereCipher()  


@app.route("/api/vigenere/encrypt", methods=['POST'])
def vigenere_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = data['key']
    encrypted_text = vigenere_cipher.encrypt(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})


@app.route("/api/vigenere/decrypt", methods=['POST'])
def vigenere_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = data['key']
    decrypted_text = vigenere_cipher.decrypt(cipher_text, key)
    return jsonify({'decrypted_message': decrypted_text})


playfair_cipher = PlayfairCipher()

@app.route("/api/playfair/create_matrix", methods=['POST'])
def create_matrix():
    data = request.json
    key = data['key']
    playfair_cipher = PlayfairCipher(key)
    matrix = playfair_cipher.table
    return jsonify({'matrix': matrix})

@app.route("/api/playfair/encrypt", methods=['POST'])
def playfair_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = data['key']
    playfair_cipher = PlayfairCipher(key)
    encrypted_text = playfair_cipher.encrypt(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})

@app.route("/api/playfair/decrypt", methods=['POST'])
def playfair_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = data['key']
    playfair_cipher = PlayfairCipher(key)
    decrypted_text = playfair_cipher.decrypt(cipher_text, key)
    return jsonify({'decrypted_message': decrypted_text})


transposition_cipher = TranspositionCipher()
@app.route("/api/transposition/encrypt", methods=['POST'])
def transposition_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = int(data['key'])
    encrypted_text = transposition_cipher.transposition_encrypt(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})

@app.route("/api/transposition/decrypt", methods=['POST'])
def transposition_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = int(data['key'])
    decrypted_text = transposition_cipher.transposition_decrypt(cipher_text, key)
    return jsonify({'decrypted_message': decrypted_text})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)