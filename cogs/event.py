import discord
import requests
from discord.ext import commands
import json

keys = json.load(open("./keys.json", "r"))


class Event(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def event(self, ctx, eventKey):
        keys = json.load(open("../keys.json", "r"))
        url = f"https://www.thebluealliance.com/api/v3/event/{eventKey}?X-TBA-Auth-Key={keys['tbaKey']}"
        data = requests.get(url).json()

        if data["website"] == None:
            website = f"https://www.thebluealliance.com/event/{eventKey}"
        else:
            website = data["website"]

        if data["gmaps_url"] == None:
            mapsURL = "no Google Maps URL Available"
        else:
            mapsURL = data["gmaps_url"]

        if data["playoff_type_string"] == None:
            playoffType = "Not a playoff"
        else:
            playoffType = data["playoff_type_string"]

        embed = discord.Embed(
            title=data["name"], url=website, color=discord.Color.from_rgb(40, 89, 165)
        )
        embed.add_field(
            name="__Location__",
            value=f"**City: ** {data['city']}\n**State/Province: ** {data['state_prov']}\n**Country: ** {data['country']}\n**Longitude: ** {data['lng']}\n**Latitude: ** {data['lat']}\n**Time Zone: ** {data['timezone']}\n**Google Maps URL: **[Google Maps URL]({mapsURL})",
            inline=True,
        )
        embed.add_field(
            name="__Event Info__",
            value=f"**Event Type: ** {data['event_type_string']}\n**Start Date: ** {data['start_date']}\n**End Date: ** {data['end_date']}\n**Event Code: ** {data['first_event_code']}\n**Parent Event Key: ** {data['parent_event_key']}\n**Year: ** {data['year']}\n**Playoff Type: ** {playoffType}",
        )
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Event(client))
