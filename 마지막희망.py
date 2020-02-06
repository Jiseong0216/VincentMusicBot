import discord
import asyncio
import datetime

TOKEN = "Njc0MTk3OTY3MDI4MzU1MDgy.Xjvl5A.IMmnCesS9obyEEPs4UTCFNykkns"
now = datetime.datetime.now()
app = discord.Client()

@app.event
async def on_ready():
    print("다음으로 로그인 합니다. : ")
    print(app.user.name)
    print(app.user.id)
    game = discord.Game("반가워요 :D")
    await app.change_presence(status=discord.Status.online, activity=game)

@app.event
async def on_message(message):
    if message.author.bot:
        return None

    if message.content.startswith(".도움말"):
        embed = discord.Embed(color=0x555555)
        embed.add_field(name="도움", value="모든 명령어에는 '.' 을 붙여주세요.\n\n", inline=False)
        embed.set_footer(text = str(now.year) + "년 " + str(now.month) + "월 " + str(now.day) + "일 | " + str(now.hour) + ":" + str(now.minute) + ":" + str(now.second))
        await message.channel.send(embed=embed)



app.run(TOKEN)
