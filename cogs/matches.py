import discord
import requests
from discord.ext import commands
import json

keys = json.load(open("./keys.json", "r"))


class Matches(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def matches(self, ctx, teamKey, eventKey):
        keys = json.load(open("../keys.json", "r"))
        url = f"https://www.thebluealliance.com/api/v3/team/{teamKey}/event/{eventKey}/matches/keys?X-TBA-Auth-Key={keys['tbaKey']}"
        data = requests.get(url).json()

        listToStr = "\n".join([str(elem) for elem in data])

        embed = discord.Embed(title=eventKey, color=discord.Color.from_rgb(40, 89, 165))
        embed.add_field(name="Keys", value=listToStr)

        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Matches(client))
