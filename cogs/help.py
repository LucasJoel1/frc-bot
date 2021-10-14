import discord
from discord.ext import commands


class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def help(self, ctx, command=None):
        embed = discord.Embed(
            title=f"2056 Bot Help Command: {command}",
            color=discord.Color.from_rgb(40, 89, 165),
        )
        if command == None:
            embed = discord.Embed(
                title="2056 Bot Help Command", color=discord.Color.from_rgb(40, 89, 165)
            )
            embed.add_field(
                name="team",
                value=f"Shows info about an FRC team\n!team <team number>",
                inline=False,
            )
            embed.add_field(
                name="events",
                value=f"Shows the events a team participated in\n!events <team number>",
                inline=False,
            )
            embed.add_field(
                name="event",
                value=f"Show info about an FRC event\n!event <event key>",
                inline=False,
            )
            embed.add_field(
                name="matches",
                value=f"Shows what matches a team has participated in, in a specific event\n!matches <team number> <event key>",
                inline=False,
            )
            embed.add_field(
                name="robots",
                value=f"Gives the names of the robots a team has created\n!robots <team number>",
                inline=False,
            )
            embed.add_field(
                name="help",
                value=f"Gives the syntax about the commands this bot accepts\n!help <command>",
                inline=False,
            )
            await ctx.send(embed=embed)
        elif command == "team":
            embed.add_field(
                name="team",
                value=f"Shows info about an FRC team\n!team <team number>",
                inline=False,
            )
            await ctx.send(embed=embed)
        elif command == "events":
            embed.add_field(
                name="events",
                value=f"Shows the events a team participated in\n!events <team number> <year>",
                inline=False,
            )
            await ctx.send(embed=embed)
        elif command == "event":
            embed.add_field(
                name="event",
                value=f"Show info about an FRC event\n!event <event key>",
                inline=False,
            )
            await ctx.send(embed=embed)
        elif command == "help":
            embed.add_field(
                name="help",
                value=f"Gives the syntax about the commands this bot accepts\n!help <command>",
                inline=False,
            )
            await ctx.send(embed=embed)
        elif command == "matches":
            embed.add_field(
                name="matches",
                value=f"Shows what matches a team has participated in, in a specific event\n!matches <team number> <event key>",
                inline=False,
            )
            await ctx.send(embed=embed)
        elif command == "robots":
            embed.add_field(
                name="robots",
                value = f"Gives the names of the robots a team has created\n!robots <team number>",
                inline=False,
            )
            await ctx.send(embed=embed)
        else:
            await ctx.send(f"{command} is not a valid help argument")


def setup(client):
    client.add_cog(Help(client))
