# Katerina Chinnappan
# your kachinna@ucsc.edu
# programming assignment 2
# uses the turtle module to draw an n pointed star,
#where n is any odd integer greater than or equal to 3 to 
#be obtained from user input. 

import turtle
#enter any key to proceed and q to quit.
choice = input("Enter 'q' to quit or any key to proceed ")
while choice != "q":
    n = int(input('Enter an odd integer greater than or equal to 3: '))
    #check if number is even
    if n % 2 == 0:
        print("Integer is even")
    #check if number is less than 3
    elif n < 3:
        print("Integer too small")
    #if choice  == "q", break from loop
    elif choice == "q":
        break
    #else break and continue with drawing the star
    else:
        print("success")
        break
#if choice != q, proceed to draw the star
if choice != "q":
    wn = turtle.Screen()      
    wn.bgcolor("white")
    wn.title(str(n)+"-pointed star")

    bob = turtle.Turtle()  
    bob.color("blue", "green")  # pen color, fill color
    bob.width(2)
    #set the initial position to (-150, 0)
    bob.setposition(-150, 0)

    #angle for 5 pointed star is 144
    angle = 180.0 - 180.0 / n
    print("angle: " , angle)

    bob.begin_fill()
    for i in range(n):
        bob.forward(300)
        bob.right(angle)
        bob.dot(10, 'red')
    bob.setposition(150, 0)

    bob.end_fill()
    wn.mainloop()
#else, don't draw anything and print goodbye message
elif choice == "q":
        print("Ciao")