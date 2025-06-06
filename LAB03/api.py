from flask import Flask, request, jsonify
from cipher.rsa import RSACipher
from cipher.ecc import ECCCipher

app = Flask(__name__)
rsa_cipher = RSACipher()


# Tạo khóa
@app.route("/api/rsa/generate_keys", methods=['GET'])
def generate_keys():
    rsa_cipher.generate_keys()
    return jsonify({'message': 'Khóa đã được tạo thành công'})


# Tải khóa
@app.route("/api/rsa/load_keys", methods=['GET'])
def load_keys():
    private_key, public_key = rsa_cipher.load_keys()
    return jsonify({
        'private_key': str(private_key),
        'public_key': str(public_key)
    })

# Mã hóa
@app.route("/api/rsa/encrypt", methods=['POST'])
def encrypt():
    data = request.json
    message = data['message']
    public_key = rsa_cipher.load_keys()[1]
    encrypted_message = rsa_cipher.encrypt(message, public_key)
    encrypted_message_hex = encrypted_message.hex()
    return jsonify({'encrypted_message': encrypted_message_hex})

# Giải mã
@app.route("/api/rsa/decrypt", methods=['POST'])
def decrypt():
    data = request.json
    encrypted_message_hex = data['encrypted_message']
    encrypted_message = bytes.fromhex(encrypted_message_hex)
    private_key, _ = rsa_cipher.load_keys()
    decrypted_message = rsa_cipher.decrypt(encrypted_message, private_key)
    return jsonify({'decrypted_message': decrypted_message})


# Ký
@app.route("/api/rsa/sign", methods=['POST'])
def sign():
    data = request.json
    message = data['message']
    private_key, _ = rsa_cipher.load_keys()
    signature = rsa_cipher.sign(message, private_key)
    signature_hex = signature.hex()
    return jsonify({'signature': signature_hex})

# Xác thực
@app.route("/api/rsa/verify", methods=['POST'])
def verify():
    data = request.json
    message = data['message']
    signature_hex = data['signature']
    signature = bytes.fromhex(signature_hex)
    _, public_key = rsa_cipher.load_keys()
    verified = rsa_cipher.verify(message, signature, public_key)
    return jsonify({'is_verified': verified})

ecc_cipher = ECCCipher()


@app.route('/api/ecc/generate_keys', methods = ['GET'])
def ecc_generate_keys():
    ecc_cipher.generate_keys()
    return jsonify({'message': 'Khóa được tạo thành công'})

@app.route("/api/ecc/sign", methods=["POST"])
def ecc_sign_message():
    data = request.json
    message = data['message']
    private_key, _ = ecc_cipher.load_keys()
    signature = ecc_cipher.sign(message, private_key)
    signature_hex = signature.hex()
    return jsonify({'signature': signature_hex})

@app.route("/api/ecc/verify", methods=["POST"])
def ecc_verify_signature():
    data = request.json
    message = data['message']
    signature_hex = data['signature']
    public_key ,_ = ecc_cipher.load_keys()
    signature = bytes.fromhex(signature_hex)
    is_verified = ecc_cipher.verify(message, signature, public_key)
    return jsonify({'is_verified': is_verified})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
