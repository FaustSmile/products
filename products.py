products = []
while True:
    name = input("請輸入商品名稱: ")
    if name == "q":
        break
    price = input("請輸入商品價格: ")
    p = [name, price]
    products.append([name, price])
print("商品與價格為: ", products)

for product in products:
    print(product)
    print(product[0], "的價格是:", p[1])