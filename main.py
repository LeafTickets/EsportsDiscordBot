# bot is working, now to do the embed and get the info from playvs
import logging
import discord
from discord.ext import commands
from random import randint
import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

logging.basicConfig(level=logging.INFO)
driver = webdriver.Chrome('chromedriver')
driver.get('https://app.playvs.com/app/schedule/upcoming')
bot = commands.Bot(command_prefix='$')
undefined = "undefined"
embed = discord.Embed(title="Schedule", description="The upcoming five games for Esports", color=0x6a37c8)
embed.add_field(name="Game 1", value=undefined, inline=True)
embed.add_field(name="Game 2", value=undefined, inline=True)
embed.add_field(name="Game 3", value=undefined, inline=True)
embed.add_field(name="Game 4", value=undefined, inline=True)
embed.add_field(name="Game 5", value=undefined, inline=True)

@bot.command()
async def updateschedule(ctx):
    games = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//p[@class="MuiTypography-root jss280 MuiTypography-body1 MuiTypography-colorTextPrimary"]')))
    gamenum = 0
    for game in games:
        print(games[gamenum].text)
        letters = 0
        for letter in games[gamenum].text:
            if games[gamenum].text[letters].isspace():
                team1 = games[gamenum].text[0:letters]
                team2 = games[gamenum].text[letters+3:len(games[gamenum].text)]
                game = team1 + " vs " + team2 + " " + "4:00"
                embed.set_field_at(gamenum, name="Game " + str(gamenum+1), value=str(game), inline=True)
                continue
            letters = letters+1
        gamenum = gamenum + 1
        if gamenum > 5:
            return

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


bot.run('Token Goes Here')