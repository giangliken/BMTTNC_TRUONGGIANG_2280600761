import hashlib

def bam_sha3_256(chuoi):
    # Tạo một objeto SHA-3 256
    sha3_256_hash = hashlib.sha3_256()
    
    # Chuyển chuỗi sang bytes và cập nhật hàm băm
    sha3_256_hash.update(chuoi.encode('utf-8'))
    
    # Trả về chuỗi băm
    return sha3_256_hash.hexdigest()

# Nhập chuỗi từ người dùng
chuoi = input("Nhập chuỗi bạn muốn băm: ")

# Băm chuỗi
chuoi_bam = bam_sha3_256(chuoi)

# In ra chuỗi băm
print("Chuỗi băm SHA-3 256:", chuoi_bam)
