import colorgram

a = []
colors = colorgram.extract('hirst-img.jpg', 30)

for i in colors:
    r = i.rgb.r
    g = i.rgb.g
    b = i.rgb.b
    res = (r, g, b)
    a.append(res)
print(a)