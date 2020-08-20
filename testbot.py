import discord
import requests
import json
import random
from time import perf_counter
import time

client = discord.Client()





@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="$help"))

    


    
@client.event
async def on_message(message):
   
    if message.author == client.user:
        return

    if message.content.startswith('$ping'):
      
        await message.channel.send("Elasped time: {} milliseconds".format(round(client.latency * 1000, 1)))



    if message.content.startswith('$credits'):
        await message.channel.send('''
    
-----Credits------
Meepy - made this mess

API(s) - https://www.rocketlaunch.live & http://open-notify.org/

------------------
''')

    
    if message.content.startswith('$help'):
        
        await message.channel.send('''
$nl - gets the next rocket launch
$ll - gets the next 5 rocket launches
$nauts - gets the # of astronauts in space (and there names)!
$iss - gets the postion of the ISS
$credits - does what the name says

                                   ''')

        

    if message.content.startswith('$nauts'):
        try:
          response = requests.get('http://api.open-notify.org/astros.json')
          w = response.json()
          if w["message"] == "success":
              nautmsg = "cant find it..."
              nautnum = w["number"]
              nautmsg = str(w["number"])
              await message.channel.send("There are {} Astronauts in space!".format(nautmsg))
              await message.channel.send("-------")
              y = w["people"]
              namemsg = "cant find it..."
              pn1 = 0
              for x in range(0, nautnum):
                nautmsg = str(y[pn1]["name"])
                pn1 = pn1 + 1
                await message.channel.send("• {}".format(nautmsg))
             
        except:
              await message.channel.send("Whoa we encountered an Error")
           
    if message.content.startswith('$iss'):
        try:
          response = requests.get('http://api.open-notify.org/iss-now.json')
          w = response.json()
          if w["message"] == "success":
              issmsg = "cant find it..."
            
              y = w["iss_position"]
           

              lat = str(y["latitude"])
              long = str(y["longitude"])
            
              await message.channel.send("ISS Postion: Lat: {0}, Long: {1}".format(lat,long))
             
        except:
              await message.channel.send("Whoa we encountered an Error")
    
        
           
    if message.content.startswith('$nl'):
        try:
           response = requests.get('https://fdo.rocketlaunch.live/json/launches/next/5')
           w = response.json()
           y = w["result"] 
           nlmsg = "cant find it..."
        
           nlmsg = str(y[0]["launch_description"])
        
           await message.channel.send(nlmsg)
           
        except:
              await message.channel.send("Whoa we encountered an Error")



  

        
    if message.content.startswith('$ll'):
        try:
           response = requests.get('https://fdo.rocketlaunch.live/json/launches/next/5')
           w = response.json()
           y = w["result"]
           llmsg = "cant find it..."
           pn = 0
           for x in range(0, 5):
             nlmsg = str(y[pn]["launch_description"])
             pn = pn + 1
             await message.channel.send("• {}".format(nlmsg))
        except: 
            await message.channel.send("Whoa we encountered an Error")
    
        
client.run('NzM0OTk0MzQ2NDQ4NzgxMzgz.XxZy0w.aJkEvI18vVtH4mhWFDKga-Z-uyQ')
