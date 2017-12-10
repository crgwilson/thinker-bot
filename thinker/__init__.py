import yaml
import os
import discord
import praw
from os.path import dirname, join, isfile
from discord.ext import commands
from discord.ext.commands import Bot

from thinker.commands.think import Think

""" Configs will be read from a yaml file and a custom path can be specified via env variable """
custom_config_path = os.environ.get('THINKER_CONFIG_PATH')
if custom_config_path:
    config_path = custom_config_path
else:
    config_path = dirname(dirname(__file__))
    config_path = join(config_path, 'config')
    config_path = join(config_path, 'default-config.yml')

print(config_path)
if isfile(config_path):
    config = yaml.safe_load(open(config_path))
else:
    # TODO: Setup proper logging
    print('No config file could be found! Startup failing')
    exit(1)

bot = Bot(description="Helps you think",command_prefix=config['command_prefix'])

@bot.event
async def on_ready():
    print('Ready to do some thinkin')

@bot.command(description="Validate bot connectivity")
async def think_health_check():
    await bot.say("I'm okay!")

@bot.command(description="Do some serious thinkin")
async def think():
    think = Think(config)
    await bot.say(think.get_random())

def run():
    bot.run(config['token'])
