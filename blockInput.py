from mcpi.minecraft import Minecraft
mc = Minecraft.create()
blockType = input()
pos = mc.player.getTilepos()
x = pos.x
y = pos.y
z = pos.z
mc.setBlock(x, y, z, blockType)