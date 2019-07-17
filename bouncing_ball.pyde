ball_y = 100
y_speed = 4
ball_x = 100
x_speed = 4
sball_y = 100
sy_speed = 2
sball_x = 100
sx_speed = 2
def setup():
    size(500,500)
    
    
def draw(): #runs mult. times (loops)
    global ball_y
    global y_speed
    global ball_x
    global x_speed
    global sball_y
    global sy_speed
    global sball_x
    global sx_speed
    background(200,200,200)
    ellipse(ball_x,ball_y,100,100)
    ellipse( sball_x, sball_y, 100, 100)
    line(0,400,500,400)
    if ball_y > 350:
        print("BOUNCE")
        y_speed = -y_speed
    if ball_y < 50 :
        y_speed = 4
    if ball_x < 50:
        x_speed = 4
    if ball_x > 450 :
        x_speed = 4
        x_speed = -x_speed
    if sball_y > 350: 
        sy_speed = -sy_speed
    if sball_y < 50: 
        sy_speed= 2
    if sball_x < 50 :
        x_speed = 2
    if sball_x > 450:
        sx_speed = 2
        sx_speed = - sx_speed
            
    
    
        
        
        
        
    
    ball_y = ball_y + y_speed #ball_y += 1
    ball_x = ball_x + x_speed
    sball_y = sball_y + sy_speed
    sball_x = sball_x + sx_speed
    print(ball_x, ball_y)
    
