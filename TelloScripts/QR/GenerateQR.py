import qrcode

data = "circle"
data2 = "square"
data3 = "triangle"

data = "ID_One_Square"
data2 = "ID_Two_Circle"
data3 = "ID_Three_Triangle"

filename = "Square.png"
img = qrcode.make(data)
img.save('cmd_png/'+filename)

filename = "Circle.png"
img = qrcode.make(data2)
img.save('cmd_png/'+filename)

filename = "Triangle.png"
img = qrcode.make(data3)
img.save('cmd_png/'+filename)

if False:
    data = "command"

    for i in range(10):
        filename = "drone_cmd_{}.png".format(i)
        img = qrcode.make(data + " " + str(i))
        img.save('cmd_png/'+filename)