import random
quit=False
while quit is not True:
    reply=random.randint(0,6)
    a=input("You:\t")
    if reply == 0:
        print("""--
  /                        _.--._ _.---.__
 /                       .'  .-.'__.-----.\
J                       /    `-'(__--'
|                     .'       `. _ `--._
|                    /            .`--'''`
|                   /           .'   d88bd db od8
|                _.'-.         J    dP'`Y8 YP  88
L               /    J         F    88         88
J             .'     F        J     Y8b.  od8  88 Y88P Y88P d8b dbd88b
 L           /      /         /-.    Y88b  88  88  Y8   8P d8 8b 88P '
J           /      /         /   \    `Y8b 88  88  `8. .8' 88d88 88
|          /      /         J    |      88 88  88   Yb dP  88    88
|         /      /          /   /   8b..8P 88  88    8.8   Y8b d 88
|        /   /  /          J   /    PY88P o88oo88o   `8'    Y88Po88o
|       /   /  /           /-'/
|      /   / -'           /  /    Y8888b
|     J   / /            / .'      88  8b
|     / -'-'   /        /-'        88  8P
L    (/|      |        /           88 dP    d8b Y88P Y88P d8b od8.db
J     /.'   ) | _.--  /            8888    8P 8b Y8   8P d8 8b 888P8b
 L   //     < \/   (  |            88 8b    d888 `8. .8' 88d88 88  88
 J  //       `.\    `.`.           88 88   dP 88  Yb dP  88    88  88
  \//     ___/_\ `-.__`.`._.----'' 88  8b  8b 88   8.8   Y8b d 88  88
   `.----'      )|`.\)  `-))\-')  o88o o8boY8888o  `8'    Y88Po88o 88o
                '   )     ')/
VK                         '     """)
    if "Quit" in a:
        quit= True
        exit()
    print("Quoth The Raven:")
    print("Nevermore "*reply)
