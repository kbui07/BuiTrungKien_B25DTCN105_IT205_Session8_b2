shop_name = ""
product_name = ""
description = ""
category = ""
keywords = []
discount_codes = []

while True:
    print("===== MENU =====")
    print("1. Nhap du lieu va xem bao cao")
    print("2. Chuan hoa ten shop")
    print("3. Kiem tra ma giam gia")
    print("4. Tim kiem va thay the")
    print("5. Thoat")

    choose = input("Nhap lua chon: ")
    if not choose.isdigit():
        print("Lua chon khong hop le")
        continue
    choose = int(choose)

    match choose:
        case 1:
            shop_name = input("Nhap ten shop: ").strip()
            if shop_name == "":
                print(
                    "Ten shop khong duoc bo trong"
                )
                continue

            product_name = input("Nhap ten san pham: ").strip().title()
            description = input("Nhap mo ta san pham: ").strip()
            if description == "":
                print("Mo ta san pham khong duoc rong")
                continue

            category = input("Nhap danh muc: ").strip().lower()
            temp = input("Nhap tu khoa (dau phay): ")
            keywords = []

            for i in temp.split(","):
                i = i.strip()
                if i != "":
                    keywords += [i]

            print("===== BAO CAO =====")
            print("Ten shop:", shop_name)
            print("Ten san pham:", product_name)
            print("Mo ta:", description)
            print("Do dai mo ta:", len(description))
            print("Danh muc:", category)
            print("Danh sach tu khoa:", keywords)
            print("So luong tu khoa:", len(keywords))
            print("Mo ta viet thuong:", description.lower())
            print("Mo ta viet hoa:", description.upper())

        case 2:
            shop = input("Nhap ten shop: ")
            if shop.strip() == "":
                print("Ten shop khong duoc bo trong")
            else:
                old = shop
                shop = shop.strip().lower()
                shop = "-".join(shop.split())

                if "shop-" not in shop:
                    shop = "shop-" + shop
                print("Ten ban dau:",old)
                print("Ten chuan hoa:",shop)

        case 3:
            code = input("Nhap ma giam gia: ").strip()
            if code == "":
                print("Ma giam gia khong duoc rong")

            elif " " in code:
                print("Ma khong duoc chua khoang trang")

            elif len(code) < 6 or len(code) > 12:
                print("Do dai tu 6 den 12")

            elif code != code.upper():
                print("Ma phai viet hoa")

            elif not code.isalnum():
                print("Chi duoc chua chu va so")

            elif not code.startswith("SALE"):
                print("Phai bat dau bang SALE")

            else:
                discount_codes += [code]
                print("Ma giam gia hop le")
                print("Danh sach ma:",discount_codes)

        case 4:
            if description == "":
                print("Chua co mo ta san pham")
            else:
                word = input("Nhap tu khoa can tim: ")
                new_word = input("Nhap tu thay the: ")
                if word in description:
                    count = description.count(word)
                    description = (description.replace(word,new_word))
                    print("So lan xuat hien:",count)
                    print("Mo ta moi:")
                    print(description)
                else:
                    print("Khong tim thay tu khoa")

        case 5:
            print("Thoat chuong trinh")
            break

        case _:
            print("Lua chon khong hop le")