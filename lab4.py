# Tính tiền nước
def tinh_tien_nuoc(so_nuoc):
    gia_ban_nuoc = (7500, 8800, 12000, 24000)
    if so_nuoc <= 10:
        tien_nuoc = so_nuoc * gia_ban_nuoc[0]
    elif so_nuoc <= 20:
        tien_nuoc = 10 * gia_ban_nuoc[0] + (so_nuoc - 10) * gia_ban_nuoc[1]
    elif so_nuoc <= 30: 
        tien_nuoc = 10 * gia_ban_nuoc[0] + 10 * gia_ban_nuoc[1] + (so_nuoc - 20) * gia_ban_nuoc[2]
    else:
        tien_nuoc = 10 * gia_ban_nuoc[0] + 10 * gia_ban_nuoc[1] + 10 * gia_ban_nuoc[2] + (so_nuoc - 30) * gia_ban_nuoc[3]
    return tien_nuoc

# Nguyên liệu làm bánh
def tinh_nguyen_lieu(sl_bdx, sl_btc, sl_bd):
    banh_dau_xanh = {"đường":0.04, "đậu":0.07}
    banh_thap_cam = {"đường":0.06, "đậu":0}
    banh_deo = {"đường":0.05, "đậu":0.02}
    nguyen_lieu = {}
    duong_trong_banh = sl_bdx * banh_dau_xanh["đường"] + sl_btc * banh_thap_cam["đường"] + sl_bd * banh_deo["đường"]
    dau_trong_banh = sl_bdx * banh_dau_xanh["đậu"] + sl_btc * banh_thap_cam["đậu"] + sl_bd * banh_deo["đậu"]
    nguyen_lieu["đường"] = duong_trong_banh
    nguyen_lieu["đậu"] = dau_trong_banh
    return nguyen_lieu




#Bài 5
import math
from datetime import datetime
lich_su_pheptinh = []

#1.Phép tính cơ bản: cộng, trừ, nhân, chia
def tinh_toan_co_ban():
    a = float(input("Nhập số thứ nhất: "))
    b = float(input("Nhập số thứ hai: "))
    phep_tinh = input("Chọn phép tính (+, -, *, /): ")
    ket_qua = None
    if phep_tinh == '+':
        ket_qua = a + b
    elif phep_tinh == '-':
        ket_qua = a - b
    elif phep_tinh == '*':
        ket_qua = a * b
    elif phep_tinh == '/':
        if b != 0:
            ket_qua = a / b
        else:
            print("Lỗi: Không thể chia cho 0.")
            return
    else:
        print("Lỗi: Phép tính không hợp lệ.")
        return
    if ket_qua is not None:
        print(f"Kết quả {a} {phep_tinh} {b} = {ket_qua}")
        lich_su_pheptinh.append(f"{a} {phep_tinh} {b} = {ket_qua}")

#2.Lũy thừa
def luy_thua():
    a = float(input("Nhập cơ số (a): "))
    kq = float(input("Nhập số mũ (kq): "))
    ket_qua = a ** kq
    print(f"Lũy thừa: {a}^{kq} = {ket_qua}")
    lich_su_pheptinh.append(f"Lũy thừa: {a} ^ {kq} = {ket_qua}")

#3.Căn bậc hai
def can_bac_hai():
    a = float(input("Nhập số cần tính căn bậc hai (a): "))
    if a >= 0:
        ket_qua = a ** 0.5
        print(f"Căn bậc hai của {a} là: {ket_qua}")
        lich_su_pheptinh.append(f"Căn bậc hai: sqrt({a}) = {ket_qua}")
    else:
        print("Lỗi: Không thể tính căn bậc hai của số âm trong số thực.")

#4.Hàm lượng giác
def ham_luong_giac():
# Chuyển đổi độ sang radian ngay trong hàm
    a_do = float(input("Nhập góc theo độ (a): "))
    a_rad = math.radians(a_do) #Chuyển đổi sang radian
    sin_a = math.sin(a_rad)
    cos_a = math.cos(a_rad)
    tan_a = math.tan(a_rad)
    print("--- Kết quả lượng giác ---")
    print(f"Sin({a_do}°) = {sin_a:.4f}") #Làm tròn 4 chữ số thập phân
    print(f"Cos({a_do}°) = {cos_a:.4f}")
    print(f"Tan({a_do}°) = {tan_a:.4f}")
    lich_su_pheptinh.append(f"Lượng giác ({a_do}°): Sin={sin_a:.4f}, Cos={cos_a:.4f}, Tan={tan_a:.4f}")

#5.Logarit
def logarit():
    a = float(input("Nhập số (a > 0): "))
    b = float(input("Nhập cơ số (b > 0, b != 1): "))
    if a <= 0 or b <= 0 or b == 1:
        print("Lỗi: Điều kiện Logarit không hợp lệ (a > 0, b > 0, b != 1).")
        return
#Tính Logarit cơ số 10
    log_10_a = math.log10(a)
    print(f"Logarit cơ số 10 của {a}: {log_10_a}")
    lich_su_pheptinh.append(f"log10({a}) = {log_10_a}")
#Tính Logarit tự nhiên
    log_e_a = math.log(a)
    print(f"Logarit tự nhiên (ln) của {a}: {log_e_a}")
    lich_su_pheptinh.append(f"ln({a}) = {log_e_a}")
#Tính Logarit cơ số tùy chọn
    try:
        log_b_a = math.log(a, b)
        print(f"Logarit cơ số {b} của {a}: {log_b_a}")
        lich_su_pheptinh.append(f"logarit cơ số {b}: log({a}, {b}) = {log_b_a}")
    except ValueError:
        print("Lỗi khi tính Logarit cơ số tùy chọn.")


#6.Giải phương trình bậc nhất
def giai_pt_bac_nhat():
    print("Giải phương trình bậc nhất: ax + b = 0")
    a = float(input("Nhập hệ số a (a khác 0): "))
    b = float(input("Nhập hệ số b: "))
    if a == 0:
        if b == 0:
            nghiem = "Vô số nghiệm (0x + 0 = 0)"
        else:
            nghiem = "Vô nghiệm (0x + b = 0, b != 0)"
    else:
        x = -b / a
        nghiem = f"Nghiệm duy nhất: x = {x}"
    print(nghiem)
    lich_su_pheptinh.append(f"PT bậc nhất: {a}x + {b} = 0 -> {nghiem}")


#7.Giải phương trình bậc hai
def giai_pt_bac_hai():
    print("Giải phương trình bậc hai: ax^2 + bx + c = 0")
    a = float(input("Nhập hệ số a (a khác 0): "))
    b = float(input("Nhập hệ số b: "))
    c = float(input("Nhập hệ số c: "))
    if a == 0:
        print("Vì a=0, đây là phương trình bậc nhất. Chuyển sang chức năng giải PT bậc nhất.")
        giai_pt_bac_nhat_tu_bac_hai(b, c)
        return
    delta = b**2 - 4*a*c
    nghiem_str = ""
    if delta < 0:
        real_part = -b / (2 * a)
        imag_part = math.sqrt(-delta) / (2 * a)
        nghiem_str = f"Nghiệm phức: x1 = {real_part:.4f} + {imag_part:.4f}i, x2 = {real_part:.4f} - {imag_part:.4f}i"
        print(nghiem_str)
    elif delta == 0:
        x = -b / (2 * a)
        nghiem_str = f"Nghiệm kép: x1 = x2 = {x}"
        print(nghiem_str)
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        nghiem_str = f"Hai nghiệm phân biệt: x1 = {x1}, x2 = {x2}"
        print(nghiem_str)
    lich_su_pheptinh.append(f"PT bậc hai: {a}x^2 + {b}x + {c} = 0 -> {nghiem_str}")
def giai_pt_bac_nhat_tu_bac_hai(a, b):
    if a == 0:
        nghiem = "Vô số nghiệm" if b == 0 else "Vô nghiệm"
    else:
        x = -b / a
        nghiem = f"Nghiệm duy nhất: x = {x}"
    lich_su_pheptinh.append(f"PT bậc nhất: {a}x + {b} = 0 (từ PT bậc 2 a=0) -> {nghiem}")
    print(nghiem)


#8.Xem lịch sử
def xem_lich_su():
    if not lich_su_pheptinh:
        print("Lịch sử phép tính trống. Vui lòng thực hiện phép tính trước.")
        return
    print("--- Lịch Sử Phép Tính ---")
    for i, phep_toan in enumerate(lich_su_pheptinh, start=1):
        print(f"{i}. {phep_toan}")

#9.Xem thời gian hiện tại
def xem_thoi_gian():
    thoi_gian = datetime.now()
    thoi_gian_format = thoi_gian.strftime("%A, %d/%m/%Y, %H:%M:%S")
    print(f"Thời gian hiện tại: {thoi_gian_format}")