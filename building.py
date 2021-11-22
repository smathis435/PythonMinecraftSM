from mcpi.minecraft import Minecraft
mc = Minecraft.create()
pos = mc.player.getPos()
x = pos.x
y = pos.y
z = pos.z
width = 50
height = 50
length = 450
blockType = 20
air = 0
mc.setBlocks(x, y, z, x + width, y + height, z + length, blockType)