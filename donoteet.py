import discord
from discord.ext import commands
import aiohttp

token

bot = commands.Bot(command_prefix="§",description="Beware...")

@bot.event
async def on_ready():
    print("I'm ready for Shacoterie!")
    
@bot.command()
async def bonjour(ctx):
    print("Salut.")
    await ctx.send("Salut.")
    
@bot.command()
async def gpt(ctx: commands.Context, *, prompt: str):
    async with aiohttp.ClientSession() as session:
        payload = {
            "model": "text-davinci-003",
            "prompt": prompt,
            "temperature": 0.5,
            "max_tokens": 50,
            "presence_penalty": 0,
            "frequency_penalty": 0,
            "best_of": 1,
        }
        headers = {"Authorization": f"Bearer {tkt}"}
        async with session.post("https://api.openai.com/v1/completions", json=payload, headers=headers) as resp:
            response = await resp.json()
            embed = discord.Embed(title="Chat GPT's Response:", description=response["choices"][0]["text"])
            await ctx.reply(embed=embed)
    

bot.run("tkt")

