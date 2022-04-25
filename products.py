import os # operating system

# 讀取檔案
def read_file(filename):
    products = []
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            if "商品,價格" in line:
                continue # 繼續，直接跳到下一次迴圈
            name, price = line.strip().split(",") 
            # 先用strip 去掉\n 再用split 遇到","做切割
            products.append([name, price])    
    return products


# 讓使用者輸入
def user_input(products):
    while True:
        name = input("請輸入商品名稱: ")
        if name == "q":
            break
        price = input("請輸入商品價格: ")
        products.append([name, price])
    print("商品與價格為: ", products)
    return products

# 印出所有購物紀錄
def print_products(products):
    for p in products:
        print(p[0], "的價格是:", p[1])

# 寫入檔案
def write_file(filename, products):
    with open(filename, "w", encoding="utf-8") as f:
        f.write("商品,價格\n")
        for p in products:
            f.write(p[0] + "," + p[1] + "\n")


def main():  #想像成 程式的 進入點
    filename = "products.csv"
    if os.path.isfile(filename): #檢查是否有此檔案
        print("有此檔案!")
        products = read_file(filename)
    else:
        print("找不到此檔案....")


    products = user_input(products)
    print_products(products)
    write_file("products.csv", products)


main()