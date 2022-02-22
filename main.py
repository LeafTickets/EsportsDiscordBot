# bot is working, now to do the embed and get the info from playvs
import http.cookiejar
import logging
import discord
import mechanize
from discord.ext import commands
import requests
from bs4 import BeautifulSoup
from random import randint

logging.basicConfig(level=logging.INFO)

bot = commands.Bot(command_prefix='$')
undefined = "undefined"
minigames = ['Sumo(armor)', 'Sumo(baller)', 'Hide and Seek', 'Same Weapon(Teams)', 'Same Weapon(Everyone)', 'Laser Tag',
             'Juggernaut', 'Splat Zones', 'Rainmaker', 'Turf War', 'Turf War(splatfest)', 'Clam Blitz', 'Tower Control']
rwf = open("Weapons.txt", "r")
weapons = rwf.readlines()
sw = open("sniper.txt", "r")
snipers = sw.readlines()
bw = open("ballers.txt", "r")
ballers = bw.readline()
embed = discord.Embed(title="Schedule", description="The upcoming five games for Esports", color=0x6a37c8)
embed.add_field(name="Game 1", value=undefined, inline=True)
embed.add_field(name="Game 2", value=undefined, inline=True)
embed.add_field(name="Game 3", value=undefined, inline=True)
embed.add_field(name="Game 4", value=undefined, inline=True)
embed.add_field(name="Game 5", value=undefined, inline=True)


@bot.command()
async def newgame(ctx, gamenum, team1, team2, time):
    if gamenum == "1":
        game = team1 + " vs " + team2 + " " + time
        embed.set_field_at(0, name="Game 1", value=str(game), inline=True)
        await ctx.send(game)
        return game
    elif gamenum == "2":
        game = team1 + " vs " + team2 + " " + time
        embed.set_field_at(1, name="Game 2", value=game, inline=True)
        await ctx.send(game)
        return game
    elif gamenum == "3":
        game = team1 + " vs " + team2 + " " + time
        embed.set_field_at(2, name="Game 3", value=game, inline=True)
        await ctx.send(game)
        return game
    elif gamenum == "4":
        game = team1 + " vs " + team2 + " " + time
        embed.set_field_at(3, name="Game 4", value=game, inline=True)
        await ctx.send(game)
        return game
    elif gamenum == "5":
        game = team1 + " vs " + team2 + " " + time
        embed.set_field_at(4, name="Game 5", value=game, inline=True)
        await ctx.send(game)
        return game
    else:
        await ctx.send("There can only be five games stored atm")


@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)


@bot.command()
async def schedule(ctx):
    await ctx.send(embed=embed)


@bot.command()
async def cleargame(ctx, gamenum):
    if gamenum == "1":
        embed.set_field_at(0, name="Game 1", value=undefined, inline=True)
        await ctx.send("Cleared")
        return
    elif gamenum == "2":
        embed.set_field_at(1, name="Game 2", value=undefined, inline=True)
        await ctx.send("Cleared")
        return
    elif gamenum == "3":
        embed.set_field_at(2, name="Game 3", value=undefined, inline=True)
        await ctx.send("Cleared")
        return
    elif gamenum == "4":
        embed.set_field_at(3, name="Game 4", value=undefined, inline=True)
        await ctx.send("Cleared")
        return
    elif gamenum == "5":
        embed.set_field_at(4, name="Game 5", value=undefined, inline=True)
        await ctx.send("Cleared")
        return
    else:
        await ctx.send("There can only be five games stored atm")


@bot.command()
async def clearschedule(ctx):
    embed.set_field_at(0, name="Game 1", value=undefined, inline=True)
    embed.set_field_at(1, name="Game 2", value=undefined, inline=True)
    embed.set_field_at(2, name="Game 3", value=undefined, inline=True)
    embed.set_field_at(3, name="Game 4", value=undefined, inline=True)
    embed.set_field_at(4, name="Game 5", value=undefined, inline=True)
    await ctx.send("Cleared")


@bot.command()
async def rm(ctx):
    rng1 = randint(0, len(minigames) - 1)
    await ctx.send(minigames[rng1])
    return minigames[rng1]


@bot.command()
async def rw(ctx):
    rng2 = randint(0, len(weapons))
    await ctx.send(weapons[rng2])
    return weapons[rng2]


@bot.command()
async def setscore(ctx, gamenum, teamnum, score):
    if gamenum == "1":
        gamevalue = embed.fields[0].value
        vsplace = gamevalue.find("vs")
        if teamnum == "1":
            gamevalue = gamevalue[:vsplace] + score + ' ' + gamevalue[vsplace:]
            embed.set_field_at(0, name="Game 1", value=str(gamevalue), inline=True)
            await ctx.send(gamevalue)
        elif teamnum == "2":
            index = gamevalue.find(" ", vsplace + 3)
            gamevalue = gamevalue[:index] + ' ' + score + ' ' + gamevalue[index:]
            embed.set_field_at(0, name="Game 1", value=str(gamevalue), inline=True)
            await ctx.send(gamevalue)
        else:
            return
    if gamenum == "2":
        gamevalue = embed.fields[1].value
        vsplace = gamevalue.find("vs")
        if teamnum == "1":
            gamevalue = gamevalue[:vsplace] + score + ' ' + gamevalue[vsplace:]
            embed.set_field_at(1, name="Game 1", value=str(gamevalue), inline=True)
            await ctx.send(gamevalue)
        elif teamnum == "2":
            index = gamevalue.find(" ", vsplace + 3)
            gamevalue = gamevalue[:index] + score + ' ' + ' ' + gamevalue[index:]
            embed.set_field_at(1, name="Game 1", value=str(gamevalue), inline=True)
            await ctx.send(gamevalue)
        else:
            return
    if gamenum == "3":
        gamevalue = embed.fields[2].value
        vsplace = gamevalue.find("vs")
        if teamnum == "1":
            gamevalue = gamevalue[:vsplace] + score + ' ' + gamevalue[vsplace:]
            embed.set_field_at(2, name="Game 1", value=str(gamevalue), inline=True)
            await ctx.send(gamevalue)
        elif teamnum == "2":
            index = gamevalue.find(" ", vsplace + 3)
            gamevalue = gamevalue[:index] + score + ' ' + ' ' + gamevalue[index:]
            embed.set_field_at(2, name="Game 1", value=str(gamevalue), inline=True)
            await ctx.send(gamevalue)
        else:
            return
    if gamenum == "4":
        gamevalue = embed.fields[3].value
        vsplace = gamevalue.find("vs")
        if teamnum == "1":
            gamevalue = gamevalue[:vsplace] + score + ' ' + gamevalue[vsplace:]
            embed.set_field_at(3, name="Game 1", value=str(gamevalue), inline=True)
            await ctx.send(gamevalue)
        elif teamnum == "2":
            index = gamevalue.find(" ", vsplace + 3)
            gamevalue = gamevalue[:index] + score + ' ' + ' ' + gamevalue[index:]
            embed.set_field_at(3, name="Game 1", value=str(gamevalue), inline=True)
            await ctx.send(gamevalue)
        else:
            return
    if gamenum == "5":
        gamevalue = embed.fields[4].value
        vsplace = gamevalue.find("vs")
        if teamnum == "1":
            gamevalue = gamevalue[:vsplace] + score + ' ' + gamevalue[vsplace:]
            embed.set_field_at(4, name="Game 1", value=str(gamevalue), inline=True)
            await ctx.send(gamevalue)
        elif teamnum == "2":
            index = gamevalue.find(" ", vsplace + 3)
            gamevalue = gamevalue[:index] + score + ' ' + ' ' + gamevalue[index:]
            embed.set_field_at(4, name="Game 1", value=str(gamevalue), inline=True)
            await ctx.send(gamevalue)
        else:
            return


@bot.command()
@commands.has_role("Never")
async def never(ctx, targetID):
    lyric = open("Never.txt", "r")
    lyrics = lyric.readlines()
    line = 0
    for lines in lyrics:
        lineval = ""
        lineval = lyrics[line] + "<@" + str(targetID) + ">"
        await ctx.send(lineval)
        line = line + 1
    lyric.close()
    return
    

@bot.command()
async def rg(ctx, numofplayers):
    rng1 = randint(0, len(minigames) - 1)
    message = minigames[rng1] + "\n"
    if minigames[rng1] == "Same Weapon(Teams)":
        numofplayers = 2
        message = minigames[rng1] + "\n"
    elif minigames[rng1] == "Same Weapon(Everyone)":
        numofplayers = 1
        message = minigames[rng1] + "\n"
    elif minigames[rng1] == "Laser Tag":
        message = minigames[rng1] + "\n"
        for players in range(0, int(numofplayers)):
            rng2 = randint(0, len(snipers))
            message = message + snipers[rng2]
        await ctx.send(message)
        return
    elif minigames[rng1] == "Sumo(armor)":
        message = message + "Classic Squiffer"
        await ctx.send(message)
        return
    elif minigames[rng1] == "Sumo(baller)":
        message = minigames[rng1] + "\n"
        for players in range(0, int(numofplayers)):
            rng2 = randint(0, len(ballers))
            message = message + ballers[rng2]
        await ctx.send(message)
    else:
        message = minigames[rng1] + "\n"
    for players in range(0, int(numofplayers)):
        rng2 = randint(0, len(weapons))
        message = message + weapons[rng2]
    await ctx.send(message)


bot.run()