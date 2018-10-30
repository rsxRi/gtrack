import discord
from discord.ext import commands
import asyncio
from json import load, dump
from os import chdir, makedirs, remove
from os.path import isfile, dirname, realpath
import datetime


if not isfile("config.json"):
    with open("config.json", "w") as f:
        dump({'prefix': ["."], 'token':'', 'ip':''}, f,
             sort_keys=True, indent=4, separators=(',', ': '))

config = load(open("config.json", "r"))

bot = commands.Bot(command_prefix=config['prefix'], description="A simple bot for GMOD server stats courtesy of gametracker.")

iip = config['ip']
image = (f'https://cache.gametracker.com/server_info/{iip}/banner_560x95.png?')

@bot.command()
async def stats(ctx):
    """output stats for server"""
    msg = await ctx.send(image)
    msg = await ctx.send(datetime.datetime.now().replace(microsecond=0).isoformat(' '))

@commands.has_permissions(administrator=True)
@bot.command()
async def restart(ctx):
    """restart bot"""
    await ctx.send("`Restarting bot.`")
    run([executable, "gtrack.py"])
    sysexit()

@commands.has_permissions(administrator=True)
@bot.command()
async def stop(ctx):
    """stops bot"""
    await ctx.send("`closing`")
    await bot.logout()
    sysexit()

bot.run(config['token'])

