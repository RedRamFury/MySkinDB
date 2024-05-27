from minepi import Skin
from PIL import Image
from pathlib import Path
import asyncio
import os

indexcontents = '<link href="style.css" rel="stylesheet"><title>SkinDB</title><h1>SkinDB</h1><br>'

async def create_render(imagepath):
    image = Image.open(imagepath)
    skin = Skin(image)
    await skin.render_skin(-25)
    skin.skin.save(os.path.join("skinrenders", os.path.basename(imagepath)))

for skin in os.listdir("skins"):
    if skin != ".gitkeep":
        asyncio.run(create_render(os.path.join("skins", skin)))
        indexcontents += f'<img src={os.path.join("skinrenders", skin)}><br><a download href="skins/{skin}"><h1>{Path(skin).stem}</h1></a><br>'

with open("index.html", "w") as indexfile:
    indexfile.write(indexcontents)