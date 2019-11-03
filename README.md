# discord-bot-app

Discord bot invite link: https://discordapp.com/api/oauth2/authorize?client_id=639773114141507617&permissions=206848&scope=bot

Steps to run discord-bot server in local:

1. Create a virtual environment
    python3.6 -m virtualenv venv
2. Install all the dependencies 
    venv/bin/pip install -r requirements.txt
3. Create your discord bot token in Discord Developer Console and add to 'bot.py' file
4. Create your PostgreSQL database and enter credentials in 'db.py' file
5. Create the table 'searches' using the SQL query:
    Create table searches (user_id varchar(256), keyword varchar(256), search_time timestamp);
6. Create custom search engine using Google Search API and insert the developer and search engine ID in     'search.py'
7. Run the app
    venv/bin/python bot.py

Features:

1. If a user sends 'hi', the bot will reply 'hey'
2. if a user sends '!google YOUR_QUERY_HERE', and it'll reply with the top five links
3. if a user sends '!recent YOUR_QUERY_HERE', and it'll reply with a list of similar searches in the user's history
