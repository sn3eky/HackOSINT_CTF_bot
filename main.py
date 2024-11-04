import discord
from discord.ext import commands
from disc_token import token
from discord.ui import Select, View

def run():
    bot=commands.Bot(command_prefix=">>>", intents=discord.Intents.all())
    channel=[{$CHANNELS_ID}]
    @bot.command()
    async def ptEPQ9o4iDXfp7F(ctx):
        if ctx.channel.id in channel:
            await ctx.send("```Spybot APT 509```")

    @bot.command()
    async def ptEPQ9o4iDXfp7F_menu(ctx):
        if ctx.channel.id in channel:
            select= Select(
                placeholder="Choisissez une option!",
                options=[
                    discord.SelectOption(
                        label="Informations",
                        value="0x1",
                        emoji="👨🏻‍🔧",
                        description="",
                    ),
                    discord.SelectOption(
                        label="Victims",
                        value="0x2",
                        emoji="😞",
                        description="",
                    ),
                    discord.SelectOption(
                        label="Activate bot",
                        value="0x3",
                        emoji="✅",
                        description="",
                    ),
                    discord.SelectOption(
                        label="Disable bot",
                        value="0x4",
                        emoji="❌",
                        description="",
                    ),
                    discord.SelectOption(
                        label="Crédits",
                        value="0x5",
                        emoji="🪙",
                        description="",
                    ),
                ])
            
            async def retour(interaction):
                if select.values[0] == "0x1":
                    await interaction.response.send_message(f"```Backbot V0.1.2 🤖```")
                elif select.values[0] == "0x2":
                    await interaction.response.send_message(f"```This bot is online on 18 servers 🌐```")
                elif select.values[0] == "0x3":
                    await interaction.response.send_message(f"```Read only you need more privileges to enable or activate bot  please use : ptEPQ9o4iDXfp7F_activation_ROOTPASSWORD ✅```")
                elif select.values[0] == "0x4":
                    await interaction.response.send_message(f"```Read only you need more privileges to enable or disable bot  please use : ptEPQ9o4iDXfp7F_disable_ROOTPASSWORD ❌```")
                elif select.values[0] == "0x5":
                    await interaction.response.send_message(f"```Crafted by LimaDevv© for APT509. All communications are encrypted and sent to a C2 Server. For more informations, please refer to the C2 Menu 🗄️```")
                
            select.callback = retour
            view=View()
            view.add_item(select)
            await ctx.send("Choisissez une option!", view=view)

    @bot.command()
    async def ptEPQ9o4iDXfp7F_activation_7aJxCxcmdtQYsi6(ctx):
        if ctx.channel.id in channel:
            await ctx.send("```Bot is active since the 17/05/2024 15:23:54 by 1228296765036302418 - 0x74889OK```")
    @bot.command()
    async def ptEPQ9o4iDXfp7F_disable_7aJxCxcmdtQYsi6(ctx):
        if ctx.channel.id in channel:
            await ctx.send("```Are you sure you want the disable the bot on this server ? Use ptEPQ9o4iDXfp7F_disable_7aJxCxcmdtQYsi6_sure for confirmation!```")
    @bot.command()
    async def ptEPQ9o4iDXfp7F_disable_7aJxCxcmdtQYsi6_sure(ctx):
        if ctx.channel.id in channel:
            await ctx.send("```You must use the web console to disable the bot on this server! 💻```")

    @bot.command()
    async def ptEPQ9o4iDXfp7F_menu_c2(ctx):
        if ctx.channel.id in channel:
            await ctx.send("```C2 Server URL: {$ONION_URL} 🔗```")

    @bot.event
    async def on_command_error(ctx, error):
        if isinstance(error,  commands.CommandNotFound):
            await ctx.send("Qu'essaies-tu de faire?")

    @bot.event
    async def on_ready():
        await bot.change_presence(status=discord.Status.dnd, activity=discord.Activity(type = discord.ActivityType.listening, name="les informations OSINT 🕵️"))
    bot.run(token)


if __name__ == "__main__":
    run()
