# import turtle
#
# timmy = turtle.Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("DeepPink", "DarkSeaGreen1")
# timmy.forward(100)
#
# myScreen = turtle.Screen()
# print(myScreen.canvheight)
# myScreen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = 'l'
print(table)
