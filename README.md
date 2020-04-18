[![Sibyl System](https://i.imgur.com/elrXfOE.jpg "Sibyl System")](https://github.com/AnimeKaizoku/SibylSystem "Sibyl System")


# Sibyl System
> A proactive judgement system for group chats.

## A Telethon UserBot to make gbanning easy 
> (asyncio)

## Config
Here stuff you need to put in config.py or Environment variables:
- ` API_ID_KEY`
- ` API_HASH_KEY`
You can get both of these from my.telegram.org
- `STRING_SESSION`:  You can get this by doing `python3 generatestringsession.py` on Linux and Mac, If on windows just python will work
- ` SIBYL `: Users who approve gbans, manage blacklist etc.
- ` ENFORCERS `: Users who send gban request
- ` Sibyl_logs `: In this group all scan request come
- ` Sibyl_approved_logs `: When approved it sends a message there
- ` GBAN_MSG_LOGS `:Where to gban user, Set to None and it will send /gban in Sibyl_logs
------------

## Purpose and schematics

Based on the popular anime series "Psycho Pass", Sibyl is designed to work in a judgement and scan system where groups can request Cymatic scans for spammers, this then connects to the Sibyl network and sends the data to Sibyl for judgement, upon the approval of which the user is judged by the dominator. [Base idea of Sibyl](https://psychopass.fandom.com/wiki/Sibyl_System "Base idea of Sibyl")

> To create and manage all Dominators and scanner systems in-country and to monitor the behavior of MWPSB personnel

------------

### Location

Sibyl can be seen around telegram judging people and chats and logging the information at [@SibylSystem](http://t.me/SibylSystem "@SibylSystem")
The base of operations of Sibyl are Beneath the NONA Tower and are only accessible by select personnel. 

------------

### Commands list
Users can access the following commands, usage is limited based on enforcer privileges.

    *scan *- Reply to a message with reason to send a request for gbans
    *approve* - Approve a scan request
    *proof* - Get message from proof id which is at the end of gban msg

------------

#### Development and planning

Sibyl is under active development and some future plans include 
- Gif responses
- Better and detailed scanning 
- Improved logging, access and replies strings 
- Anything else we come up with as this project goes on.

------------

##### Trivia
- The use of the Sibyl System to determine latent criminals with the help of Crime Coefficients is introduced at some point between 2090 and 2100.
- The first version of the Sibyl System was introduced between 2030 and 2049. At this point it is solely a supercomputer which was able to make precise and extensive cymatic scans, so the Employment Aptitude Exam of the Ministry of Health, Labor and Welfare would become more efficient and valid. Along with the cymatic scans, the Psycho-Pass measurement is introduced.

- A replacement for the Sibyl System was proposed by the Ministry of Economy called the Panopticon, monitoring the economic and traffic activities of its citizens. As Jeremy Bentham designed Panopticon to be a prison to monitor criminals without them knowing that they're in fact being monitored, inmates would always behave as if being monitored. Its employment as a trial system to monitor traffic was both met with controversy and failure, thus Sibyl System remained.

- Based upon visual inspection, it appears that the physical structure of the Sibyl System contains 2,601 slots in total, despite having only 247 members.

- The Sibyl System's Crime Coefficient is revealed to be over 300, even though it consists of only criminally asymptomatic brains. The brains contributing to this Coefficient are destroyed, lowering the number to zero.

- In case of emergency and/or if the System thinks that it is in danger, it can falsify the judgement of the Dominator, in order to suppress the threat.

##### Why that? 

>Why use regex for so proof and approve? 
- How else would I get reason, message etc? ( I know about split but that'd make the code hard for me to read) 

>Why such noob code?
- Cuz I'm a noob?

>Why not classes for config?
- Because I don't want it to be hard for newbies (to python (or those who don't know it)) to setup the bot

>Why not getting list of all module instead of manually putting module in to_load?
- I don't want people from uniborg or ftg or other userbots to put there plugins (those weird animation ones or useless ones) in Sibyl System 
