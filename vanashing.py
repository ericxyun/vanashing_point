from PIL import Image, ImageDraw
import os

def two_point(width, height, horizon):
    WIDTH, HEIGHT = width, height
    img = Image.new(mode='RGB', size=(WIDTH, HEIGHT), color='white')
    d = ImageDraw.Draw(img)

    horizon_line = HEIGHT * horizon
    
    d.ellipse([1, horizon_line - 5,10, horizon_line  + 5], fill=128)
    d.ellipse([WIDTH - 10, horizon_line - 5 ,WIDTH, horizon_line  + 5], fill=128)

    destination_x = 0
    destination_y = 0
    count = 0
    while destination_x <= WIDTH:
        d.line((0, horizon_line, destination_x, 0), fill ='black')
        d.line((WIDTH, horizon_line, destination_x , 0), fill ='black')

        d.line((0, horizon_line, destination_x, HEIGHT), fill ='black')
        d.line((WIDTH, horizon_line, destination_x , HEIGHT), fill ='black')
        destination_x += WIDTH / 4
        count += 1
        print(count)

    while destination_y <= HEIGHT:
        d.line((0, horizon_line, WIDTH, destination_y), fill ='black')
        d.line((WIDTH, horizon_line, 0, destination_y), fill ='black')
        # destination_y += (WIDTH / 4) * (HEIGHT/WIDTH)
        destination_y += HEIGHT / 8
        
    d.line((0, horizon_line, WIDTH, horizon_line), fill=128, width=3)
    filename = '2_point.png'
    img.save(filename)
    os.system("lp " + filename)

    # img.show()
    # filename
    # img.save('2_point.png')

for _ in [.1, .9, .3, .6]:
    two_point(1920, 1080, _)
