<div align="center">
    <h1>FRC2056 Discord Bot</h1>
</div>

## Information and disclaimers

The FRC2056 Discord Bot is a discord bot that is being made for the [FRC2056](https://2056.ca) FIRST robotics team.  The bot itself curently has no affiliation with the team, I myself am a member of said robotics team though I am just making a open source discord bot for [FRC2056](https://2056.ca) and named after [FRC2056](https://2056.ca) as it seemed suiting.  This bot is open source as anybody or team is aloud to use and edit the bot to their preference as they seem suiting without permsission from myself (the developer).  If you have a change to the bot that you think would help develpment or improve the bot please open a PR.  This bot is developed using the [discord.py](https://discordpy.readthedocs.io/en/stable/) library and the [TBA](https://thebluealliance.com)(The Blue Alliance) API.

## Startup

**You will need to have git and python 3.9 or later installed on your computer or server**

**To use the bot you will first need to create a discord developer application to create you bot.**
1. Go to https://discord.com/developers/applications
2. Create an application
3. Go to the bot section and create your bot
4. Using OAuth2 invite the bot to your server
5. Go back to the bot section and keep the browser tab open for later

**You will also need a [TBA](https://thebluealliance.com)(The Blue Alliance) API key.**
1. Go to the [TBA login page](https://www.thebluealliance.com/account/login_required?redirect=http%3A//www.thebluealliance.com/account)
2. Sign into you google account through [TBA](https://thebluealliance.com)(The Blue Alliance)
3. Create a new **READ API KEY** with a description
4. keep the browser tab open for later

**You will now need to get the bot files**
1. On your computer, create a folder for the bots files to be located in
2. Open a new command line with the file path set to the path you want the bot files to be located in
3. Copy and paste `git clone https://github.com/LucasJoel1/2056Bot.git` into your cmd and hit enter

**You will now need to fill in the bot token for your token, [TBA](https://thebluealliance.com)(The Blue Alliance) API key and prefix.**
1. In [app.py](./app.py) replace `clientToken` with your bots token
2. In [app.py](./app.py) replace `prefix` with your prefered prefix
3. In the bots **cogs** directory have the variable `tbaKey` be equal to your api key

**You need to install the requests and discordpy packages.  You can install these packages using ```pip install discord.py``` and ```pip install requests```**
**After completing these steps run the [app.py](./app.py) file using the Python interpreter(Must be 3.9 or later)**

## Commands

**This section of the docs was taken directly from the help command in no particular order, all info here can be found by runing the help command**
**The ! will represent whatever prefix you use for simplicity, () will represent argument(s) and when inputting a tem number, the team number must always begin with frc (i.e. frc2056)**

- **event:** shows info about a FRC event</br>
    !event (event key)
- **events:** shows all the FRC events a team has competed in, in a specific year or all time (for all time use the keyword **all** or leave the year argument blank)</br>
    !events (team number) (year)
- **help:** shows al the commands the bot has to offer and their syntax (the command argument can be left blank to show all commands or input a specific command to show the syntax of the command)
    !help (command)
- **matches:** shows the matches that occured in a specific event
    !matches (event key)
- **team:** shows info about a FRC team
    !team (team number)
- **robots:** shows the robots an FRC team has created over the years
    !robots (team number)

## Contributing

**If you find an issue or bug with the bot please open a issue and if you are a developer and have a fix for an issue please open a PR and link back to the issue.**
**If you want to add a feature to the bot please open a PR.  When adding a feature please follow the [pep8](https://www.python.org/dev/peps/pep-0008/) guidlines, it is not required however it is recommended.**
**As I am a student I work on the bot in my free time so if you want a feature in the bot and you are not a part of a FRC team please add it yourself and open an issue with the `feature` tag and `frcteam` tag to the main branch.  If you are apart of a FRC team please open a PR and include what FRC team you are apart of, the feature you or your team would like added and why you think this feature would be helpful to your team and other teams as well.**

*btw I wrote this readme at 1 am on saturday night so if it has some spelling mistakes or something is not working please let me know*</br>
**For direct contact you can email me at <a href = "mailto: lucas@ljoel.tech">lucas@ljoel.tech</a>**
