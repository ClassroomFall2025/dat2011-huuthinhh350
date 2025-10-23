class SanPham:
    def __init__(self, ten_san_pham, gia, giam_gia):
        self.__ten_san_pham = ten_san_pham
        self.__gia = gia
        self.__giam_gia = giam_gia
    #get
    def get_ten(self):
        return self.__ten_san_pham
    def get_ten(self):
        return self.__gia
    def get_ten(self):
        return self.__giam_gia
    #set
    def set_ten(self, ten_san_pham):
        self.__ten_san_pham = ten_san_pham
    def set_ten(self, gia):
        self.__gia = gia
    def set_ten(self, giam_gia):
        self.__giam_gia = giam_gia

    def thue_nhap_khau(self):
        return self.__gia * 0.1
    def nhap_sp(self):
        self.__ten_san_pham = input("Tên sản phẩm: ")
        self.__gia = float(input("Giá: "))
        self.__giam_gia = float(input("Giảm giá: "))
        
    def xuat_tt_sp(self):
        print(f"sản phẩm {self.__ten_san_pham} có giá {self.__gia} và được giảm giá {self.__giam_gia} và thuế nhập khẩu: {self.thue_nhap_khau()}")
    def __str__(self):
        print(f"sản phẩm {self.__ten_san_pham} có giá {self.__gia} và được giảm giá {self.__giam_gia} và thuế nhập khẩu: {self.thue_nhap_khau()}")



