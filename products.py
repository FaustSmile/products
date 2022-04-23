import os # operating system

# 讀取檔案
products = []
if os.path.isfile("products.csv"): #檢查是否有此檔案
    print("有此檔案!")
    with open("products.csv", "r", encoding="utf-8") as f:
        for line in f:
            if "商品,價格" in line:
                continue # 繼續，直接跳到下一次迴圈
            name, price = line.strip().split(",") 
            # 先用strip 去掉\n 再用split 遇到","做切割
            products.append([name, price])
    print(products)

else:
    print("找不到此檔案....")

# 讓使用者輸入
while True:
    name = input("請輸入商品名稱: ")
    if name == "q":
        break
    price = input("請輸入商品價格: ")
    products.append([name, price])
print("商品與價格為: ", products)

# 印出所有購物紀錄
for p in products:
    print(p[0], "的價格是:", p[1])

# 寫入檔案
with open("products.csv", "w", encoding="utf-8") as f:
    f.write("商品,價格\n")
    for p in products:
        f.write(p[0] + "," + p[1] + "\n")