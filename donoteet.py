import discord
import random
from discord.ext import commands
from discord.ext.commands import context
import aiohttp
import openai

openai.api_key = "tkt"
intents = discord.Intents.default()
intents.message_content = True
intents.guild_messages = True
intents.guild_reactions = True
intents.members = True 
client = discord.Client(intents=intents)

bot = commands.Bot(command_prefix="§",description="Beware...", intents=intents)
bot.remove_command('help')

#-----------------FONCTION EXTERNE------------------------#

def lire_fichier(nom_fichier, encodage='utf-8'):
    try:
        with open(nom_fichier, 'r') as fichier:
            contenu = fichier.read()
        return contenu
    except FileNotFoundError:
        return "Le fichier spécifié n'a pas été trouvé."
    except Exception as e:
        return f"Une erreur s'est produite : {str(e)}"
    
def correct(text: str):
    text2 = text.replace('Ã', 'à')
    text2 = text2.replace('à©', 'é')
    text2 = text2.replace('à¨', 'è')
    text2 = text2.replace('àª', 'ê')
    text2 = text2.replace('à¹', 'ù')
    text2 = text2.replace('à§', 'ç')
    return text2
#---------------------------------------------------------#

#------------------------MUSIC----------------------------#


#--------------------------------------------------------#

@bot.event
async def on_ready():
    print("I'm ready for Shacoterie!")
    
@bot.command()
async def bonjour(ctx):
    print("Salut.")
    await ctx.send("Salut.")

@bot.command()
async def help(ctx):
    texte = lire_fichier("help.txt", encodage='utf-8')
    await ctx.send(correct(texte)) 

#Fonction random
@bot.command()
async def rand(ctx, nbr1 : int , nbr2 : int ):
    if(nbr2 > 100000000000000000000000000000000):
        ctx.send("Le nombre entrée est trop long.")
        return
    else:
        if (nbr1 > nbr2):
            nbre = random.randint(nbr2, nbr1)
        else:
            nbre = random.randint(nbr1, nbr2)
        await ctx.send(f"**Résultat:** {nbre}")

@bot.command()
async def ask(ctx, *, question):
    try:
        # Utilisez l'API GPT-3 pour obtenir une réponse à la question
        response = openai.Completion.create(
            engine="davinci",  # Utilisez le moteur GPT-3 de votre choix
            prompt=question,
            max_tokens=100,  # Limitez la longueur de la réponse
            stop=None  # Vous pouvez spécifier des mots pour arrêter la réponse ici
        )

        # Envoyez la réponse au canal Discord
        await ctx.send(response.choices[0].text)
    except Exception as e:
        await ctx.send(f"Une erreur s'est produite : {str(e)}")
    
bot.run("tkt")

