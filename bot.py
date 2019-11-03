# Work with Python 3.6
import discord
from db import post_search_data, fetch_search_data
from search import search_main

TOKEN = 'YOUR_DISCORD_TOKEN_HERE'

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('hi'):
        msg = 'Hey {0.author.mention}'.format(message)
        await message.channel.send(msg)

    if message.content.startswith('!google'):
        query = message.content.split(None, 1)[1]
        author_id = message.author.id
        post_search_data(author_id, query)

        #Test API Data
        #results = ['https://en.wikipedia.org/wiki/Greta_Gerwig', 'https://www.imdb.com/name/nm1950086/', 'https://www.nytimes.com/2019/10/31/movies/greta-gerwig-little-women.html', 'https://www.theguardian.com/film/2018/jan/11/greta-gerwig-regrets-woody-allen-film-i-will-not-work-for-him-again', 'https://www.nytimes.com/2018/01/09/opinion/greta-gerwig-woody-allen-aaron-sorkin.html']
        
        results = search_main(query)
        if results:
            links = ' \n'.join(results)
            print(links)
            msg = 'Hello {}, you searched for {}. The top five results are: \n {}'.format(message.author.mention, query, links)
        else:
            msg = 'Hello {}, you searched for {}. \n Sorry, no matching links found.'.format(message.author.mention, query)
        await message.channel.send(msg)

    if message.content.startswith('!recent'):
        query = message.content.split(None, 1)[1]
        author_id = message.author.id
        results = fetch_search_data(author_id, query)
        print(results)
        if(len(results) > 0):
            keywords = 'Your matching search results are: \n' + ' \n'.join([x[1] for x in results])
        else: 
            keywords = 'No matching results found'
        await message.channel.send(keywords)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)