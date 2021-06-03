import discord
import os
import qrcode
import uuid

client = discord.Client(activity=discord.Game(name='With a Sharpie'))
ClientToken = os.environ['Token']


def QRmessage(mess):
 mess = (mess[mess.index(" "):(len(mess)+1)])
 img = qrcode.make(mess)
 imageName = str(uuid.uuid4()) + ".png"
 img.save(imageName)
 return imageName


@client.event
async def on_ready():
  print("Logged in as {0.user}".format(client))



@client.event
async def on_message(message):
 if message.author == client.user:
    return
 if message.content.startswith("!qr "):
  try:
   mess = message.content
   mess = (mess[mess.index(" "):(len(mess)+1)])
   img = qrcode.make(mess)
   imageName = str(uuid.uuid4()) + ".png"
   img.save(imageName)
   await message.channel.send(file=discord.File(imageName))  
   os.remove(imageName)
  except:
   await message.channel.send("Could Not Create QR Code")
client.run(ClientToken)