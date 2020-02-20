from translate import Translator
import discord

token = "your token"

tex = "this is a test pls help "

bot=discord.Client()


@bot.event
async def on_ready():
	print("{} is running".format(bot.user))
	
def translator(text):

	tanslator = Translator(to_lang = "hi")




	translation = tanslator.translate(text)


	return translation


@bot.event
async def on_message(msg):
	if msg.author==bot.user:
		return
	else:
		ds = translator(msg.content)
		await msg.channel.send(ds)
		

bot.run(token)
