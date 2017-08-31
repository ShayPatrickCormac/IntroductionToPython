"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Zijian Huang "Shay".
"""
########################################################################
# DONE: 1.
# On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# DONE: 2.
#
#  You should have RUN the PREVIOUS module and READ its code.
#  (Do so now if you have not already done so.)
#
#  Below this comment, add ANY CODE THAT YOUR WANT, as long as:
#    1. You construct at least 2 rg.SimpleTurtle objects.
#    2. Each rg.SimpleTurtle object draws something
#         (by moving, using its rg.Pen).  ANYTHING is fine!
#    3. Each rg.SimpleTurtle moves inside a LOOP.
#
#  Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#  If you make syntax (notational) errors, no worries -- get help
#  fixing them at either this session OR at the NEXT session.
#
#  Don't forget to COMMIT your work by using  VCS ~ Commit and Push.
########################################################################
import rosegraphics as rg
window=rg.TurtleWindow()
hao=rg.SimpleTurtle()
nick=rg.SimpleTurtle('turtle')
for k in range(3):
    hao.pen=rg.Pen("red",10)
    hao.forward(200)
    hao.right(90)
    hao.forward(200)
    hao.right(90)
    hao.forward(200)
    hao.right(90)
    hao.forward(200)
    hao.pen_up()
    hao.forward(10)
    hao.right(90)
    hao.forward(10)
    hao.pen_down()
for k in range(4):
    nick.pen=rg.Pen("blue",5)
    nick.speed=7
    nick.left(90)
    nick.forward(130)
    nick.left(180)
    nick.forward(130)
    nick.left(130)
    nick.forward(130)
    nick.pen_up()
    nick.backward(30)
    nick.left(60)
    nick.pen_down()

window.close_on_mouse_click()