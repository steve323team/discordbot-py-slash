import discord
from discord import app_commands 

class aclient(discord.Client):
    def __init__(self):
        super().__init__(intents = discord.Intents.default())
        self.synced = False

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced: 
            await tree.sync() 
            self.synced = True
        print(f'{self.user}이 시작되었습니다')  #  봇이 시작하였을때 터미널에 뜨는 말
        game = discord.Game('DDNN봇')          # ~~ 하는중
        await self.change_presence(status=discord.Status.idle, activity=game)


client = aclient()
tree = app_commands.CommandTree(client)


@tree.command(name = '안녕', description='슬래시 설명문') 
async def slash2(interaction: discord.Interaction):
    await interaction.response.send_message(f"슬래시 커맨드", ephemeral = True) 


client.run('토큰')
