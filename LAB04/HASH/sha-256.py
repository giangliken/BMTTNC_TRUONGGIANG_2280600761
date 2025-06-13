import hashlib

def bam_sha256(chuoi):
    # Tạo một objeto SHA-256
    sha256_hash = hashlib.sha256()
    
    # Chuyển chuỗi sang bytes và cập nhật hàm băm
    sha256_hash.update(chuoi.encode('utf-8'))
    
    # Trả về chuỗi băm
    return sha256_hash.hexdigest()

# Nhập chuỗi từ người dùng
chuoi = input("Nhập chuỗi bạn muốn băm: ")

# Băm chuỗi
chuoi_bam = bam_sha256(chuoi)

# In ra chuỗi băm
print("Chuỗi băm SHA-256:", chuoi_bam)
