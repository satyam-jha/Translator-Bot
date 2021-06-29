from translate import Translator
import discord
from .key import Token
from discord.ext import commands


#client ref
bot = discord.Client()


#ISO 639-1 language code search for ur language 
translist = {1:"ko",2:"zh",3:"hi",4:"ja",5:"ar",6:"bh",7:"ru"}

print("select lang")

print(translist)

lang = translist[int(input())]
print(lang)


#just to know bot is runing 

@bot.event
async def on_ready():
	print("{} is running".format(bot.user))
	

#main function 


def translator(text,lang):

	tanslator = Translator(from_lang = "autodetect",to_lang = lang)




	translation = tanslator.translate(text)


	return translation




#response on every msg

@bot.event
async def on_message(msg):
	
	testmsg = msg.content
	if msg.author==bot.user:
		return
	
	
	else:
		
		#create a text channel called translator or change this according to channel u want to response on 
		if msg.channel.name == "translator":

			

			reply = translator(msg.content,lang)
			await msg.channel.send(reply)
			
		else :
			

			return



bot.run(Token)
