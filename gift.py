from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x = -121.9
y = 34.0
z = 58.8
gift = mc.getBlock(x,y,z)

if gift == 57:
    mc.postToChat("Thanks for the diamond")
elif gift == 6:
    mc.postToChat("I guess tree saplings are as good as diamonds...")
else:
    mc.postToChat("Bring a gift to " + str(x) + "," + str(y) + "," +  str(z))