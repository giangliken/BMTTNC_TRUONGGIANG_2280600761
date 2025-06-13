import hashlib

def bam_blake2b(chuoi):
    # Tạo một objeto Blake2b
    blake2b_hash = hashlib.blake2b()
    
    # Chuyển chuỗi sang bytes và cập nhật hàm băm
    blake2b_hash.update(chuoi.encode('utf-8'))
    
    # Trả về chuỗi băm
    return blake2b_hash.hexdigest()

def bam_blake2s(chuoi):
    # Tạo một objeto Blake2s
    blake2s_hash = hashlib.blake2s()
    
    # Chuyển chuỗi sang bytes và cập nhật hàm băm
    blake2s_hash.update(chuoi.encode('utf-8'))
    
    # Trả về chuỗi băm
    return blake2s_hash.hexdigest()

# Nhập chuỗi từ người dùng
chuoi = input("Nhập chuỗi bạn muốn băm: ")

# Băm chuỗi bằng Blake2b
chuoi_bam_blake2b = bam_blake2b(chuoi)

# Băm chuỗi bằng Blake2s
chuoi_bam_blake2s = bam_blake2s(chuoi)

# In ra chuỗi băm
print("Chuỗi băm Blake2b:", chuoi_bam_blake2b)
print("Chuỗi băm Blake2s:", chuoi_bam_blake2s)
