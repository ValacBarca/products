products = []
while True:
	name = input("請輸入商品名稱：")
	if name == "q":
		break
	price = input ("請輸入價錢:")
	p = [name, price]
	products.append(p)
print(products)

for p in products:
	print(p[0],"的價格是",p[1],"元")

with open ("products.csv", "w", encoding = "utf-8") as f:   #給了檔名、寫入模式、編碼
	f.write("商品,價格\n")
	for p in products:
		f.write(p[0]+","+ p[1]+"\n")






