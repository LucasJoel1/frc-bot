import discord
import requests
from discord.ext import commands
import json

keys = json.load(open("./keys.json", "r"))


class Events(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def events(self, ctx, teamNumber, year=None):
        keys = json.load(open("../keys.json", "r"))
        if year == None or year == "all":
            url = f"https://www.thebluealliance.com/api/v3/team/{teamNumber}/events/keys?X-TBA-Auth-Key={keys['tbaKey']}"
            url2 = f"https://www.thebluealliance.com/api/v3/team/{teamNumber}/events/simple?X-TBA-Auth-Key={keys['tbaKey']}"
        elif year != None:
            url = f"https://www.thebluealliance.com/api/v3/team/{teamNumber}/events/{year}/keys?X-TBA-Auth-Key={keys['tbaKey']}"
            url2 = f"https://www.thebluealliance.com/api/v3/team/{teamNumber}/events/{year}/simple?X-TBA-Auth-Key={keys['tbaKey']}"
        url3 = f"https://www.thebluealliance.com/api/v3/team/{teamNumber}?X-TBA-Auth-Key={keys['tbaKey']}"
        data = requests.get(url).json()
        data2 = requests.get(url2).json()
        data3 = requests.get(url3)
        eventsNames = None

        listToStr = "\n".join([str(elem) for elem in data])

        for s in range(len(data2)):
            if data2[s]["name"] != None:
                eventsNames = str(eventsNames)
                eventsNames = eventsNames + data2[s]["name"] + "\n"

        eventsNames = eventsNames.replace("(Cancelled)", "")
        try:
            embed = discord.Embed(
                title=data3.json()["team_number"],
                url=data3.json()["website"],
                color=discord.Color.from_rgb(40, 89, 165),
            )
            embed.add_field(name="__Event Keys__", value=listToStr)
            embed.add_field(name="__Event Name__", value=eventsNames)
            await ctx.send(embed=embed)
        except:
            embed = discord.Embed(
                title=data3.json()["team_number"],
                url=data3.json()["website"],
                color=discord.Color.from_rgb(40, 89, 165),
            )
            embed.add_field(name="__Event Keys__", value=listToStr)
            await ctx.send(embed=embed)
            await ctx.send(
                "To many events to display names, only keys will be displayed. 😦"
            )


def setup(client):
    client.add_cog(Events(client))
