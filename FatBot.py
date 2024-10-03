import discord
from discord.ext import commands
import json
import os
import math
#I'm Makar and this is my first discord bot :)
#The bot will undergo some changes in the following days to add more functionality.
#Maybe even some fancy buttons and so on. :() (pawgchamp)
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())
scores_file = 'scores.json'

# Initialize scores if the file doesn't exist
if not os.path.exists(scores_file):
    with open(scores_file, 'w') as f:
        #If you wish to change the names, make sure you also do so at lines 27 & 33! (unfortunately i'm doxing myself a lil' here)
        json.dump({"Makar": {"wins": 0, "scores": [], "totalScore": 0}, 
                    "Yulia": {"wins": 0, "scores": [], "totalScore": 0}, 
                    "Palina": {"wins": 0, "scores": [], "totalScore": 0}, 
                    "Igor": {"wins": 0, "scores": [], "totalScore": 0}}, f)


@bot.command()
async def record(ctx, makar: int, yulia: int, palina: int, igor: int):
    with open(scores_file, 'r') as f:
        data = json.load(f)
        print(data)
    scoreswithnames = {"Makar":makar, "Yulia":yulia, "Palina":palina, "Igor":igor}
    scores=[makar,yulia,palina,igor]
    winner_index = scores.index(0)
    winner_name = list(data.keys())[winner_index]
    # Update wins
    data[winner_name]["wins"] += 1
    finalMSG=''
    for player in list(data.keys()):
        #Note that objects 'scoreswithnames' and 'data', share the same key names.
        data[player]["scores"].append(scoreswithnames[player])
        
        totalscore=0
        std_dev=0
        bigsum=0
        elements=len(data[player]["scores"])
        for datelet in data[player]["scores"]:
            totalscore+=datelet
        
        #This updates the total score in the 'data' and will later be stored in the JSON file
        data[player]["totalScore"] = totalscore
        
        #HERE i use std_dev as a temporary mean for the calculation of the actual standard deviation in the next 3 lines
        std_dev=totalscore/elements
        
        for datelet in data[player]["scores"]:
            bigsum+=((datelet-std_dev)*(datelet-std_dev))
        std_dev=round(math.sqrt(bigsum/elements),2)
        wins=data[player]["wins"]
        finalMSG+=f"Stats for {player}\nCombined Score: {totalscore}\nStandard Deviation: {std_dev}\n Average Score: {round(totalscore/elements,1)}\nWins: {wins}\n\n"

    # Save updated data
    with open(scores_file, 'w') as f:
        json.dump(data, f)

    await ctx.send(f'{finalMSG}')
        
#REMEMBAH TO CHANGE YOUR TOKEN IF YOU'RE GONNA USE THIS!!!
bot.run('BIG_FAT_TOKEN_GOES_HERE')
