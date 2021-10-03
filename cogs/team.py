import discord
import requests
from discord.ext import commands
import json

keys = json.load(open("./keys.json", "r"))


class Team(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def team(self, ctx, teamNumber):
        url = f"https://www.thebluealliance.com/api/v3/team/{teamNumber}?X-TBA-Auth-Key={keys['tbaKey']}"
        url2 = f"https://www.thebluealliance.com/api/v3/team/{teamNumber}/awards?X-TBA-Auth-Key={keys['tbaKey']}"
        data = requests.get(url)
        data2 = requests.get(url2).json()
        chairmans = 0
        chairmans_finalists = 0
        winner = 0
        woodie_flowers = 0
        skills_competition_winner = 0

        for s in range(len(data2)):
            if data2[s]["award_type"] == 0:
                chairmans += 1

        for s in range(len(data2)):
            if data2[s]["award_type"] == 69:
                chairmans_finalists += 1

        for s in range(len(data2)):
            if data2[s]["award_type"] == 1:
                winner += 1

        for s in range(len(data2)):
            if data2[s]["award_type"] == 3:
                woodie_flowers += 1

        for s in range(len(data2)):
            if data2[s]["award_type"] == 74:
                skills_competition_winner += 1

        blue_banners = (
            chairmans
            + chairmans_finalists
            + winner
            + woodie_flowers
            + skills_competition_winner
        )

        embed = discord.Embed(
            title=data.json()["team_number"],
            url=data.json()["website"],
            color=discord.Color.from_rgb(40, 89, 165),
        )
        embed.add_field(
            name="__Location__",
            value=f"**City: ** {data.json()['city']}\n**State/Province: ** {data.json()['state_prov']}\n**Country: ** {data.json()['country']}\n **Postal Code: ** {data.json()['postal_code']}",
            inline=True,
        )
        embed.add_field(
            name="__Team Info__",
            value=f"**Nickname: ** {data.json()['nickname']}\n**School Name: ** {data.json()['school_name']}\n**Rookie Year: ** {data.json()['rookie_year']}\n**Team Key: ** {data.json()['key']}",
            inline=True,
        )
        embed.add_field(
            name="__Awards__",
            value=f"**Chairmans: ** {chairmans}\n**Chairmans Finalists: ** {chairmans_finalists}\n**Winner: ** {winner}\n **Woodie Flowers: ** {woodie_flowers}\n **Skills Competition Winner: ** {skills_competition_winner}\n **Total Blue Banners: ** {blue_banners}",
            inline=False,
        )
        embed.add_field(
            name="__External Sources__",
            value=f"**TBA: ** https://thebluealliance.com/team/{teamNumber}\n**FIRST: ** https://frc-events.firstinspires.org/team/{teamNumber}",
            inline=True,
        )
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Team(client))
