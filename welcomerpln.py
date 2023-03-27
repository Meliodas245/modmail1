import discord
from discord.ext import commands

client = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    print('Bot is online')

@client.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.channels, name='welcome-channel')

    if channel is not None:
        embed = discord.Embed(
            title=f"Welcome to our server, {member.name}!",
            description=f"Thanks for joining our community, {member.name}!",
            color=0x00ff00
        )
        embed.set_thumbnail(url=member.avatar_url)

        await channel.send(embed=embed)

@client.command()
async def welcome_message(ctx):
    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    await ctx.send("Please enter the title of the welcome message:")
    title_msg = await client.wait_for('message', check=check)
    title = title_msg.content

    await ctx.send("Please enter the description of the welcome message:")
    desc_msg = await client.wait_for('message', check=check)
    description = desc_msg.content

    await ctx.send("Please enter the color of the embed in hexadecimal format (e.g. 0x00ff00):")
    color_msg = await client.wait_for('message', check=check)
    color = int(color_msg.content, 16)

    embed = discord.Embed(
        title=title,
        description=description,
        color=color
    )

    await ctx.send("The welcome message has been updated!")
    await ctx.send(embed=embed)
    
def setup(bot):
    bot.add_cog(Welcomer(bot))