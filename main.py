import nextcord
from nextcord.ext import commands
import os
import anthropic

# สร้างคีย์ API Claude AI จาก Anthropic
anthropic.api_key = os.environ['key']

# สร้างคลายแอนท์ตัวช่วย
claude = anthropic.Claude()

# สร้างอินเทนต์สำหรับบอท
#intents = nextcord.Intents.default()
#intents.typing = False
#intents.presences = False

# สร้างบอท
bot = commands.Bot(
    command_prefix='!',
    help_command=None,
    intents=discord.Intents.all(),
    strip_after_prefix=True,
    case_insensitive=True, 
)

# ฟังก์ชันเมื่อบอทพร้อมใช้งาน
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

# คำสั่งสำหรับถามคำถาม
@bot.command()
async def ask(ctx, *, question):
    # ส่งคำถามไปยัง Claude AI
    response = claude.get_response(question)

    # ส่งคำตอบกลับไปยังผู้ใช้
    await ctx.send(response.response)

# รันบอท
token = os.environ['bot']
bot.run(token)
