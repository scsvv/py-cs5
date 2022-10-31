import json
import xlwt

def goods_init(items):
    build_str = '<div>'

    for item in items: 
        build_str += f"<div> \n <h3>{item['name']}</h3>\n <p>{item['price']}</p> \n </div>"

    build_str += '</div>'
    return build_str 



with open('goods.json') as f: 
    data = json.load(f)
    f.close()

print(data)

with open('index.html', 'w') as f: 
    f.write(f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
</head>
<body>
    <h1>Store</h1>
    {goods_init(data)}
</body>
</html>
    """)


file = xlwt.Workbook(encoding="utf-8")
sheet1 = file.add_sheet("GOODS")

sheet1.write(0, 0, "Name")
sheet1.write(0, 1, "Price")


i = 1
for good in data: 
    sheet1.write(i, 0, good["name"])
    sheet1.write(i, 1, good["price"])
    i+=1

file.save("check.xls")
