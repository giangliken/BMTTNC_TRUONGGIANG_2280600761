import hashlib

def bam_md5(chuoi):
    # Tạo một objeto MD5
    md5_hash = hashlib.md5()
    
    # Chuyển chuỗi sang bytes và cập nhật hàm băm
    md5_hash.update(chuoi.encode('utf-8'))
    
    # Trả về chuỗi băm
    return md5_hash.hexdigest()

# Nhập chuỗi từ người dùng
chuoi = input("Nhập chuỗi bạn muốn băm: ")

# Băm chuỗi
chuoi_bam = bam_md5(chuoi)

# In ra chuỗi băm
print("Chuỗi băm MD5:", chuoi_bam)
