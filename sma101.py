import discord
from discord.ext import commands
import asyncio
import random

bot=commands.Bot(command_prefix='Yo-')

@bot.event
async def on_ready():
	print("What up")
	print("It is I", bot.user.name)
	print(bot.user.id)

	
@bot.command(pass_context=True)
async def ting(ctx):
    e = discord.Embed(title='ping')
    await ctx.send('ting', embed=e)
    
@bot.command(pass_context=True)
async def whosHannah(ctx):
    e = discord.Embed(title='Is the most perfect person in existence')
    await ctx.send('Hannah', embed=e)

@bot.command(pass_context=True)
async def whosHotto(ctx):
    e = discord.Embed(title='Is a soulless alien blob')
    await ctx.send('Maria (aka hottodogu)', embed=e)


@bot.command(pass_context=True)
async def whosAbuzar(ctx):
    e = discord.Embed(title='Who loves Hannah')
    await ctx.send('An idiot', embed=e)


@bot.command(pass_context=True)
async def hello(ctx):
    e = discord.Embed(title='Human')
    await ctx.send('Hello', embed=e)
   
@bot.command(pass_context=True)
async def whatsV(ctx):
    e = discord.Embed(title='Veronika(aka Pointless existence')
    await ctx.send('The following is pretty useless', embed=e)


@bot.command()
async def clear(ctx, amount=4):
	await ctx.channel.purge(limit=amount)
	await ctx.send(amount, "messages deleted")
	
@bot.command()
async def info(ctx, member: discord.Member):
	
	roles=[role for role in member.roles]
	
	embed = discord.Embed(color=member.color, timestamp=ctx.message.created_at)
	embed.set_author(name=f'User Info {member}')
	embed.set_thumbnail(url=member.avatar_url)
	embed.set_footer(text=f'Requested by {ctx.author}', icon_url=ctx.author.avatar_url)
	embed.add_field(name="ID:", value=member.id)
	embed.add_field(name="Server Name:", value=member.display_name)
	embed.add_field(name="Created At:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
	embed.add_field(name="Joined At:", value=member.joined_at.strftime("%a, %d %B %Y, %I:%M %p UTC"))
	embed.add_field(name=f"Roles ({len(roles)})", value=" ".join([role.mention for role in roles]))
	embed.add_field(name="Top role:", value=member.top_role.mention)
	embed.add_field(name="Is Bot?", value=member.bot)
	await ctx.send(embed=embed)
	
@bot.command(pass_context=True)
@commands.has_permissions(kick_members=True)
async def join(ctx):
	author = ctx.author
	Chanel = author.voice.channel
	await Chanel.connect()
	embed=discord.Embed(title="Joined Voice Channel")
	await ctx.send(embed=embed)

@bot.command(pass_context=True)
async def playtest(ctx):
	author = ctx.message.author
	Chanel = author.voice.channel
	vc = await Chanel.connect()
	Chanel.play(discord.FFmpegPCMAudio('/storage/emulated/0/bots/music/test.m4a'), after=lambda e: print('done', e))

@bot.command(aliases=['feedme', 'rice', 'food'])
async def hungry(ctx):
    foodlist=['/storage/emulated/0/bots/Food/Food1.gif', '/storage/emulated/0/bots/Food/Food2.gif','/storage/emulated/0/bots/Food/Food3.gif','/storage/emulated/0/bots/Food/Food4.gif','/storage/emulated/0/bots/Food/Food5.gif' , '/storage/emulated/0/bots/Food/Food6.gif', '/storage/emulated/0/bots/Food/Food7.gif','/storage/emulated/0/bots/Food/Food8.gif', '/storage/emulated/0/bots/Food/Food1.jpeg', '/storage/emulated/0/bots/Food/Food2.jpeg', '/storage/emulated/0/bots/Food/Food3.jpeg']
    chosen=random.choice(foodlist)
    with open(chosen, 'rb') as fp:
    	await ctx.channel.send(file=discord.File(fp, 'food.gif'))
    	await ctx.send(f"Here's your meal, {ctx.author}")

@bot.command(aliases=["eightball","8ball","٨ball"])
async def Eyball(ctx, *,  question):
	answers=["It is certain.","It is decidedly so.","Without a doubt.","Yes - definitely.","You may rely on it.","As I see it, yes.","Most likely.","Outlook good.","Yes.","Signs point to yes.","Ask again later.", "Better not tell you now.","Cannot predict now.", "Concentrate and ask again.", "I don't know.", "Ofcourse.", "Who knows, maybe.", "That's too hard of a question for me to answer."]
	answer = random.choice(answers)
	await ctx.send(f'Question: {question}\nAnswer:{answer}')


@bot.command(aliases=["Destroy","destroy", "makefunof", "improv"])
async def roast(ctx, *, person):
	Roast=[" My phone battery lasts longer than your relationships.", "I would roast you but my mom told me not to burn trash." "Oh you’re talking to me, I thought you only talked behind my back.", "My name must taste good because it’s always in your mouth.","Don’t you get tired of putting make up on two faces every morning?","Too bad you can’t count jumping to conclusions and running your mouth as exercise.","Is your drama going to an intermission soon?", "I’m an acquired taste. If you don’t like me, acquire so me taste.","If I wanted a bitch, I would have bought a dog.", "My business is my business. Unless you’re a thong, get out of my ass.", "It’s a shame you can’t Photoshop your personality.", "I don’t sugarcoat shit. I’m not Willy Wonka.", "Acting like a prick doesn’t make yours grow bigger.", "The smartest thing that ever came out of your mouth was a penis.", "Calm down. Take a deep breath and then hold it for about twenty minutes.", "Jealousy is a disease. Get well soon, bitch!", "Things You Need To Know Before You Date A Sarcastic Girl.","When karma comes back to punch you in the face, I want to be there in case it needs help.", "You have more faces than Mount Rushmore.","Sorry, sarcasm falls out of my mouth like bullshit falls out of yours.", "Don’t mistake my silence for weakness. No one plans a murder out loud.", "Yes, I am a bitch — just not yours.", "I’m sorry you got offended that one time you were treated the way you treat everyone all the time.", "You should wear a condom on your head. If you’re going to be a dick, you might as well dress like one.", "Maybe you should eat make-up so you’ll be pretty on the inside too.","Being a bitch is a tough job but someone has to do it. ","My middle finger gets a boner every time I see you.", "You’re entitled to your incorrect opinion.", "You’re so real. A real ass.", "Whoever told you to be yourself gave you really bad advice.", "If I had a face like yours I’d sue my parents.","Where’s your off button?", "I didn’t change. I grew up. You should try it sometime.", " I thought I had the flu, but then I realized your face makes me sick to my stomach.","Like you, The people who know me the least have the most to say.", "I’m jealous of people who don’t know you.","I’m sorry that my brutal honesty inconvenienced your ego.", "You sound reasonable… Time to up my medication.", "Aww, it’s so cute when you try to talk about things you don’t understand.","Is there an app I can download to make you disappear?", "I’m sorry, you seem to have mistaken me with a woman who will take your shit.", "I’m visualizing duck tape over your mouth.", "90% of your ‘beauty’ could be removed with a Kleenex.", "I suggest you do a little soul searching. You might just find one.", "Some people should use a glue stick instead of chapstick.", "My hair straightener is hotter than you.","I have heels higher than your standards.", "I’d smack you, but that would be animal abuse.", " Why is it acceptable for you to be an idiot but not for me to point it out?","If you’re offended by my opinion, you should hear the ones I keep to myself.", "If you’re going to be a smart ass, first you have to be smart, otherwise you’re just an ass.", "Your face is fine but you will have to put a bag over that personality.", "Hey, I found your nose, it’s in my business again!", "I’m not an astronomer but I am pretty sure the earth revolves around the sun and not you.","I might be crazy, but crazy is better than stupid.","It’s scary to think people like you are allowed to vote.","Keep rolling your eyes. Maybe you’ll find your brain back there.","No, no. I am listening. It just takes me a moment to process so much stupid information all at once.","I’m sorry, what language are you speaking? It sounds like bullshit.","Everyone brings happiness to a room. I do when I enter, you do when you leave.", "I keep thinking you can’t get any dumber and you keep proving me wrong.","I’m not shy. I just don’t like you.","Your crazy is showing. You might want to tuck it back in.","I am allergic to stupidity, so I break out in sarcasm.","You’re like a plunger. You like to bring up old shit.", "I am not ignoring you. I am simply giving you time to reflect on what an idiot you are being.","I hide behind sarcasm because telling you to go fuck yourself is rude in most social situations.","You’re the reason I prefer animals to people", "You’re not pretty enough to have such an ugly personality.", "Your birth certificate is an apology letter from the condom manufacturer", "I’d explain it to you but I left my English-to-Dumbass Dictionary at home.","You don’t like me, then fuck off. Problem solved.", "You have your entire life to be a jerk. Why not take today off?","Your ass must be pretty jealous of all the shit that comes out of your mouth.","Remember when I asked for your opinion? Me neither.","If you’re waiting for me to care, I hope you brought something to eat, ‘cause it’s gonna be a really long time.","Some day you’ll go far—and I really hope you stay there.", "I’m trying my absolute hardest to see things from your perspective, but I just can’t get my head that far up my ass.", "Sometimes it’s better to keep your mouth shut and give the impression that you’re stupid than open it and remove all doubt.", "I’m not a proctologist, but I know an asshole when I see one.", "You only annoy me when you’re breathing, really.", "Do yourself a favor and ignore anyone who tells you to be yourself. Bad idea in your case.", "I don’t know what your problem is, but I’m guessing it’s hard to pronounce.", "Do your parents even realize they’re living proof that two wrongs don’t make a right?", "Remember that time I said I thought you were cool? I lied.", "Everyone’s entitled to act stupid once in awhile, but you really abuse the privilege.", "I can’t help imagining how much awesomer the world would be if your dad had just pulled out.", "Do you ever wonder what life would be like if you’d gotten enough oxygen at birth?", "Please, save your breath. You’ll probably need it to blow up your next date.", "Can you die of constipation? I ask because I’m worried about how full of shit you are.", "Good story, but in what chapter do you shut the fuck up?", "Don’t hate me because I’m beautiful. Hate me because your boyfriend thinks so.", "Were you born on the highway? That is where most accidents happen.", "Please, keep talking. I only yawn when I’m super fascinated.", "If I wanted to hear from an asshole, I’d fart.", "Jesus might love you, but everyone else definitely thinks you’re an idiot.", "Sorry, I didn’t get that. I don’t speak bullshit.", "The only way you’ll ever get laid is if you crawl up a chicken’s ass and wait.", "If ignorance is bliss, you must be the happiest person on the planet.", "Are you always such an idiot, or do you just show off when I’m around?", "There are some remarkably dumb people in this world. Thanks for helping me understand that.", "I could eat a bowl of alphabet soup and shit out a smarter statement than whatever you just said.", "I was pro life. Then I met you.", "You’re about as useful as a screen door on a submarine.", "Whenever we hang out, I remember that God really does have a sense of humor.", "It’s kind of hilarious watching you try to fit your entire vocabulary into one sentence." "Please just tell me you don’t plan to home-school your kids.", "You always bring me so much joy—as soon as you leave the room.", "I was hoping for a battle of wits but it would be wrong to attack someone who’s totally unarmed.", "I’d tell you how I really feel, but I wasn’t born with enough middle fingers to express myself in this case.", "Stupidity’s not a crime, so feel free to go.","I’d tell you to go fuck yourself, but that would be cruel and unusual punishment"]
	roast = random.choice(Roast)
	await ctx.send(f'Dear {person}, \n {roast}')

@bot.command(aliases=['Hug', 'HUG', 'hug', 'Hugs'])
async def hugs(ctx, *, person):
	huglist = ['/storage/emulated/0/bots/Hugs/Hug1.gif', '/storage/emulated/0/bots/Hugs/Hug2.gif','/storage/emulated/0/bots/Hugs/Hug3.gif','/storage/emulated/0/bots/Hugs/Hug4.gif', '/storage/emulated/0/bots/Hugs/Hug5.gif','/storage/emulated/0/bots/Hugs/Hug6.gif','/storage/emulated/0/bots/Hugs/Hug7.gif','/storage/emulated/0/bots/Hugs/Hug8.gif']
	chosen = random.choice(huglist)
	with open(chosen, 'rb') as fp:
		await ctx.channel.send(file=discord.File(fp, 'hug.gif'))
		await ctx.send(f'Hug sent to {person} ^-^')


@bot.command(aliases=['cathug','CatHug','Cathug', 'hugcat'])
async def cahug(ctx, *, person):
	cathugs = ['/storage/emulated/0/bots/Cathugs/Cathug1.gif', '/storage/emulated/0/bots/Cathugs/Cathug2.gif', '/storage/emulated/0/bots/Cathugs/Cathug3.gif', '/storage/emulated/0/bots/Cathugs/Cathug4.gif', '/storage/emulated/0/bots/Cathugs/Cathug5.gif', '/storage/emulated/0/bots/Cathugs/Cathug6.gif', '/storage/emulated/0/bots/Cathugs/Cathug7.gif']
	chosen = random.choice(cathugs)
	with open(chosen, 'rb') as fp:
		await ctx.channel.send(file=discord.File(fp, 'cathug.gif'))
	await ctx.send(f'A cat was sent to hug {person} uwu')

bot.run("NTg1MDkxNDI0MjY1OTYxNDgz.XPUc1A.ezOe6MmK9lxI3uHJMC2vSZ-AKmo")
