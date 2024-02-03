import turtle

def draw_pifagor_tree(branch_length, level):
    if level == 0:
        return
    else:
        turtle.forward(branch_length)
        turtle.left(45)
        
        draw_pifagor_tree(0.7 * branch_length, level-1)
        
        turtle.right(90)
        
        draw_pifagor_tree(0.7 * branch_length, level-1)
        
        turtle.left(45)
        turtle.backward(branch_length)
        
def draw(level):
    turtle.speed(2)  
    turtle.left(90)
    
    draw_pifagor_tree(100, level)
    
    turtle.hideturtle()
    turtle.done()
    
    
if __name__ == "__main__":
   draw(5)