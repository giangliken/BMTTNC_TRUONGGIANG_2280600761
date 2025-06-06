import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox 
from ui.rsa import Ui_MainWindow
import requests

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_gene.clicked.connect(self.call_api_gen_key)
        self.ui.btn_encrypt.clicked.connect(self.call_api_encrypt)
        self.ui.btn_decrypt.clicked.connect(self.call_api_decrypt)
        self.ui.btn_sign.clicked.connect(self.call_api_sign)
        self.ui.btn_verify.clicked.connect(self.call_api_verify)

    def call_api_gen_key(self):
        try:
            response = requests.get('http://localhost:5000/api/rsa/generate_keys')
            if response.status_code == 200:
                QMessageBox.information(self, "Thông báo", response.json()['message'])
            elif response.status_code == 500:
                QMessageBox.information(self, "Lỗi", "Lỗi server nội bộ")
            else:
                QMessageBox.information(self, "Lỗi", "Lỗi không xác định")
        except requests.exceptions.RequestException as e:
            QMessageBox.information(self, "Lỗi", "Lỗi kết nối mạng")
        except Exception as e:
            QMessageBox.information(self, "Lỗi", str(e))

    def call_api_encrypt(self):
        try:
            message = self.ui.txt_plan.toPlainText()
            response = requests.post('http://localhost:5000/api/rsa/encrypt', json={'message': message})
            if response.status_code == 200:
                self.ui.txt_cipher.setText(response.json()['encrypted_message'])
            elif response.status_code == 500:
                QMessageBox.information(self, "Lỗi", "Lỗi server nội bộ")
            else:
                QMessageBox.information(self, "Lỗi", "Lỗi không xác định")
        except requests.exceptions.RequestException as e:
            QMessageBox.information(self, "Lỗi", "Lỗi kết nối mạng")
        except Exception as e:
            QMessageBox.information(self, "Lỗi", str(e))

    def call_api_decrypt(self):
        try:
            encrypted_message = self.ui.txt_cipher.toPlainText()
            response = requests.post('http://localhost:5000/api/rsa/decrypt', json={'encrypted_message': encrypted_message})
            if response.status_code == 200:
                self.ui.txt_plan.setText(response.json()['decrypted_message'])
            elif response.status_code == 500:
                QMessageBox.information(self, "Lỗi", "Lỗi server nội bộ")
            else:
                QMessageBox.information(self, "Lỗi", "Lỗi không xác định")
        except requests.exceptions.RequestException as e:
            QMessageBox.information(self, "Lỗi", "Lỗi kết nối mạng")
        except Exception as e:
            QMessageBox.information(self, "Lỗi", str(e))

    def call_api_sign(self):
        try:
            message = self.ui.txt_plan.toPlainText()
            response = requests.post('http://localhost:5000/api/rsa/sign', json={'message': message})
            if response.status_code == 200:
                self.ui.txt_sign.setText(response.json()['signature'])
            elif response.status_code == 500:
                QMessageBox.information(self, "Lỗi", "Lỗi server nội bộ")
            else:
                QMessageBox.information(self, "Lỗi", "Lỗi không xác định")
        except requests.exceptions.RequestException as e:
            QMessageBox.information(self, "Lỗi", "Lỗi kết nối mạng")
        except Exception as e:
            QMessageBox.information(self, "Lỗi", str(e))

    def call_api_verify(self):
        try:
            message = self.ui.txt_info.toPlainText()
            signature = self.ui.txt_sign.toPlainText()
            response = requests.post('http://localhost:5000/api/rsa/verify', json={'message': message, 'signature': signature})
            if response.status_code == 200:
                if response.json()['is_verified']:
                    QMessageBox.information(self, "Thông báo", "Chữ ký hợp lệ")
                else:
                    QMessageBox.information(self, "Thông báo", "Chữ ký không hợp lệ")
            elif response.status_code == 500:
                QMessageBox.information(self, "Lỗi", "Lỗi server nội bộ")
            else:
                QMessageBox.information(self, "Lỗi", "Lỗi không xác định")
        except requests.exceptions.RequestException as e:
            QMessageBox.information(self, "Lỗi", "Lỗi kết nối mạng")
        except Exception as e:
            QMessageBox.information(self, "Lỗi", str(e))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
