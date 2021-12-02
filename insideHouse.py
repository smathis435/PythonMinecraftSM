from mcpi.minecraft import Minecraft
mc = Minecraft.create()

buildX =59.2
buildY =52.2
buildZ =-0.1
width = 10
height = 5
length = 6

pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

inside = buildX < x < buildX + width and buildY < y < buildY + height and buildZ < z < buildZ + length
mc.postToChat("Inside: " + str(inside))