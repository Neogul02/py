import turtle

geobuk=turtle.Turtle()
geobuk.shape('turtle')

color_list = ['aqua', 'black', 'blue', 'fuchsia', 'gray', 'green', 'lime', 'maroon', 'navy', 
                 'olive', 'orange', 'purple', 'red', 'silver', 'teal', 'white', 'yellow', 'violet']

geobuk.speed(0)        # 거북이 최대 속도

geobuk.pensize(5)

n = int(input())
  

for j in range(n) :
    geobuk.fillcolor(color_list[j % 18])
    geobuk.begin_fill()
    for i in range(4) :    
        geobuk.forward(100)
        geobuk.left( 90)
    geobuk.end_fill()
    geobuk.left(int(360/n))
