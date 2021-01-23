import discord
from discord.ext import commands
import Phoinex


client = commands.Bot(command_prefix="!")

def MModPackage():
    #kick
    @client.command()
    async def kick(ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)

    #ban
    @client.command()
    async def ban(ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)

    #mute
    @client.command()
    @commands.has_permissions(manage_messages=True)
    async def mute(ctx, member: discord.Member, *, reason=None):
        guild = ctx.guild
        mutedRole = discord.utils.get(guild.roles, name="Muted")

        if not mutedRole:
            mutedRole = await guild.create_role(name="Muted")

            for channel in guild.channels:
                await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True,
                                              read_messages=False)

        await member.add_roles(mutedRole, reason=reason)
        await ctx.send(f"Muted {member.mention} for reason {reason}")
        await member.send(f"You Are Muted In {guild.name} For {reason}")


    #unmute
    @client.command()
    @commands.has_permissions(manage_messages=True)
    async def unmute(ctx, member: discord.Member):
        mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")

        await member.remove_roles(mutedRole)
        await ctx.send(f"Unmuted {member.mention}")
        await member.send(f"You Are Unmuted From {ctx.guild.name}")

#run
def MRun(Mtoken):
    client.run(Mtoken)

#Bot Ready
def MBotReady():
    @client.event
    async def on_ready():
        print(f"{client.user} Is Ready")



def DM():

    @client.command()
    async def dm(ctx, member: discord.Member, reason):
        guild = ctx.guild
        await member.send(reason)