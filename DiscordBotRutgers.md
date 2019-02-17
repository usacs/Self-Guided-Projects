# RU Discord Bot
 
This Discord bot is a convenient multi-purpose bot to be used in a Discord server, outputting information such as bus times, course information, and degree navigator.
 
## What is Discord?
 
Discord is a messaging application available on desktop and mobile specializing in text, image, video, and audio communication between users in a chat channel.
 
You can download and install Discord **[here](https://discordapp.com/)**.
 
## Getting Started
 
The resources required include the following:
 
* [Python (Version 3)](https://www.python.org/downloads/)
* Discord
* Command Prompt
 
## Tutorial
 
#### Step 1: Inviting your Discord Bot
 
First, create a Discord account. It's free to create and use. Upon creating your account, verify with the email address you provided.
 
Second, to create a Discord bot, click on this **[link](https://www.discordapp.com/developers/applications)**. If this is your first time visiting this page, your applications should look empty. Create a new application by clicking "New Application". You should be directed to a page called "General Information", allowing you to name your bot and give it a description.
 
Third, we need to invite the Discord bot to a server. For testing purposes, you will need to create a Discord server of your own, so open up Discord (Desktop or Browser doesn't matter). On the left side of the Discord interface, there should be a circle with a plus sign in the center. Click on it and create your own Discord server.
 
Now that you have your own Discord server, you need to invite your bot. To do this, redirect back to your Discord Developer Portal and copy your bot's Client ID (not to be confused with Client Secret).
 
Enter the following URL (replace PASTEHERE with your Client ID): https://discordapp.com/oauth2/authorize?client_id=PASTEHERE&scope=bot
 
Congratulations! Now you've invited your Discord bot into your server.
 
### Step 2: Setting up your Discord Bot
 
Upon finishing Step 1, you'll notice your Discord bot is offline. This is because there is currently nothing controlling the bot at the moment. This is where Python comes into play.
 
[Download and install Python 3](https://www.python.org/downloads/). Then, once Python finishes installing, open Command Prompt and type the following commands:
 
* python -m pip install discord
 
Now open your IDE used to code in Python. Python comes with a built-in IDE called IDLE. Open it. Then, click on this **[link](https://github.com/Rapptz/discord.py)** and go to the Quick Example code. Copy the code into the IDE text editor. Run the program.
 
Upon running the program, you'll notice that the program doesn't work. This is because the program does not know which bot it should tell the instructions to. Redirect back to the Discord Developer Portal and go to the Bot section. In the section where it says "Token", reveal your token and copy it. Replace the 'token' string in Line 38 and paste your token. **KEEP THIS TOKEN SECRET AND DO NOT SHARE IT AT ALL.**
 
Finally with that done, run your Python program and check your Discord app. If the program is running successfully, you should see your bot online. If the bot is online running, that means you've successfully set up your bot! Congratulations!

### Python 3.7 Fix
The Current API is broken on 3.7 on PyPi which is the pip repo. First make sure your virtual envrionment is setup
if it is not run:
```
python3 -m venv .

source bin/activate

run

pip install -U https://github.com/Rapptz/discord.py/archive/rewrite.zip\#egg\=discord.py\[voice\]
```

Keep in mind 3.7 still has bugs so if possible downgrade th 3.6, but given this, the example in https://github.com/Rapptz/discord.py should work

## Getting Started with APIs
### What Are Apis?
APIS (Application Programming Interfaces) are services that companies can allow developers to safely interact with their data without giving direct access to their databases as well as interact with those companies technologies.
Some examples:
The Clarifai API allows us to perform computer vision on pictures (Interacting with a technology this company provides)

The Rutgers API Allows us to interact with Data rutgers has such as food and bus timings

Most APIs Use JSON(Javascript Object Noatation to communciate responses to the user)

### Understanding JSON:
JSON is a key value store (basically a python disctionary or a java HashMap<String,Object>). In JSON a Key which is a string points to an object which is the value.

Consdier this exmaple:
```python
example = {
 "apple":"pear",
 "juice":["orange","pineapple"],
  "other":{
    "a":"b",
    "c":"d"
  }

}
```
In this example , we have "key":value pairs.

So example["apple"] gives us the value "pear", where "apple" is the key and "pear" is the value. Remember, the value can also be any type . example["juice"] gives us the array ["orange","pineapple"]. 

### Check Your Understadning
What does example["other"] give, how do I access the value "b" or "d"?
 
