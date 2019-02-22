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

Keep in mind 3.7 still has bugs so if possible downgrade th 3.6, but given this, the example in https://github.com/usacs/GuidedProjects/blob/master/week1.py

Before moving forward, play around with the output 

### Excerise 1:
Make a simple text based game before moving to the API Stage

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

### JSON Arrays
Sometimes we can also have arrays of JSON objects which we can access by iterating through the array.

### GET vs POST
Now that you have an understanding if JSON we move into interacting with APIs. There are 5 main HTTP methods, in which we will talk about two

#### HTTP GET:
GET is used to request data from a specified resource.

#### HTTP POST:
POST is Used to Create/Update a resource (logging in)

These are the main requests we will be dealing with while dealing with APIs for our project.To get started with requests in python, run
```python
pip install requests
#or
python3 -m pip install requests #if not using a virtual env
```
### Making Our First Requests:
Let's first look at the Rutgers Dining API
The endpoint is here: https://rumobile.rutgers.edu/1/rutgers-dining.txt

Below is an example snippet of the response on Sunday Feb 17 2019
```json
[
  {
    "location_name": "Brower Commons",
    "date": 1550434349891,
    "meals": [
      {
        "meal_name": "Breakfast",
        "meal_avail": false
      },
      {
        "meal_name": "Lunch",
        "meal_avail": true,
        "genres": [
          {
            "genre_name": "Breakfast Meats",
            "items": [
              "Grilled Turkey Sausage Links",
              "Pork Sausage Links",
              "Vegetarian Breakfast Patties"
            ]
          },
          {
            "genre_name": "Breakfast Entrees",
            "items": [
              "Apple Pancake",
              "Oatmeal",
              "Red Velvet Waffle",
              "Scramble Cholesterol Free Egg",
              "Scrambled Eggs",
              "Vegan Grits Hot Cereal"
            ]
          },
          {
            "genre_name": "Breakfast Bakery",
            "items": [
              "Assorted Bagels",
              "Assorted Contract Muffins",
              "Plain Bagels"
            ]
          },
          {
            "genre_name": "Salad Bar",
            "items": [
              "Grilled Chicken Breast 4Oz"
            ]
          },
          {
            "genre_name": "Soups",
            "items": [
              "Rsted Eggplan & Red Pepp Soup"
            ]
          },
          {
            "genre_name": "Entrees",
            "items": [
              "4\" Club Roll",
              "Belgian Waffles",
              "Breaded Chicken Patty",
              "Noodle Lungo"
            ]
          },
          {
            "genre_name": "Starch & Potatoes",
            "items": [
              "Spicy Diced Potatoes"
            ]
          },
          {
            "genre_name": "Accompaniments",
            "items": [
              "Chopped Red & Green Peppers",
              "Sausage Crumbles",
              "Shredded Cheddar Cheese",
              "Shredded Mozzarella Cheese",
              "Sliced Bacon",
              "Sliced Mushrooms",
              "Small Diced Ham"
            ]
          },
          {
            "genre_name": "Cook To Order Bar",
            "items": [
              "Diced Tomatoes",
              "Diced Onions",
              "Egg Mix Liquid And Whole",
              "Liquid Egg Cholesterol Free",
              "Omelets Made To Order",
              "Shred Monterey Jack Cheese"
            ]
          },
          {
            "genre_name": "Pizza/ Pasta",
            "items": [
              "Garlic Bread Sticks",
              "Hawaiian Chicken Pizza",
              "Pepperoni Cheese Pizza Thin",
              "Round Cheese Pizza Large",
              "Shrimp And Pesto Pizza"
            ]
          }
        ]
      },
      {
        "meal_name": "Dinner",
        "meal_avail": true,
        "genres": [
          {
            "genre_name": "Entrees",
            "items": [
              "Garlic Roasted Rosemary Chicken",
              "Jambalaya",
              "Roast Beef",
              "Shrimp W/ Tequilla Lime Sauce",
              "Whole Wheat Penne"
            ]
          },
          {
            "genre_name": "Sauces & Gravies",
            "items": [
              "Plain Tomato Sauce",
              "Roasted Onion Port Au Jus"
            ]
          },
          {
            "genre_name": "Starch & Potatoes",
            "items": [
              "Roasted Red Bliss Potato W/ Crumbled Blue Cheese"
            ]
          },
          {
            "genre_name": "Veggies",
            "items": [
              "Collard Greens",
              "Vegan Spaghetti Squash Roasted"
            ]
          },
          {
            "genre_name": "Desserts",
            "items": [
              "Ny Cheesecake"
            ]
          },
          {
            "genre_name": "Bakery Misc",
            "items": [
              "Cranberry Rasin Loaf"
            ]
          },
          {
            "genre_name": "Cook To Order Bar",
            "items": [
              "Asian Brown Sauce",
              "Baked Brown Rice",
              "Beef Strips For Stir Fry",
              "Diced Tofu",
              "Fresh Chicken Strips Raw",
              "Kung Pao Sauce",
              "Large Broken Pdi Shrimp",
              "Lo Mein",
              "Oyster Sauce",
              "Pasta Vegetable Side",
              "Soy Bragg",
              "Steamed White Rice",
              "Szechuan Sauce"
            ]
          }
        ]
      },
      {
        "meal_name": "Knight Room",
        "meal_avail": true,
        "genres": [
          {
            "genre_name": "Entrees",
            "items": [
              "Chicken Parmesan",
              "Eggplant Rollatini",
              "Grilled Chicken Breast 3Oz"
            ]
          },
          {
            "genre_name": "Knight Room",
            "items": [
              "Cucumbers",
              "Italian Dinner Roll",
              "Tomato Wedges",
              "Tossed Salad"
            ]
          }
        ]
      },
      {
        "meal_name": "Late Knight",
        "meal_avail": false
      }
    ]
  },
  {
    "location_name": "Busch Dining Hall",
    "date": 1550434349891,
    "meals": [
      {
        "meal_name": "Breakfast",
        "meal_avail": false
      },
      {
        "meal_name": "Lunch",
        "meal_avail": true,
        "genres": [
          {
            "genre_name": "Breakfast Meats",
            "items": [
              "Grilled Turkey Sausage Links",
              "Sliced Bacon",
              "Vegetarian Breakfast Patties"
            ]
          },
          {
            "genre_name": "Breakfast Entrees",
            "items": [
              "Apple Pancake",
              "Aspar & Sundriedtomato Quiche",
              "Belgian Waffles",
              "Hard Boiled Eggs",
              "Oatmeal",
              "Scrambled Eggs",
              "Vegan Grits Hot Cereal"
            ]
          },
          {
            "genre_name": "Breakfast Bakery",
            "items": [
              "Assorted Contract Muffins",
              "Bagel Weekend Assortment"
            ]
          },
          {
            "genre_name": "Breakfast Misc",
            "items": [
              "Grapefruit Halves Red",
              "Green Seedless Grapes",
              "Honeydew Melon",
              "Strawberries"
            ]
          },
          {
            "genre_name": "Salad Bar",
            "items": [
              "Baby Spinach",
              "Broccoli Buds Op",
              "Cucumbers",
              "Diced Tofu",
              "Ginger Marinated Vegetables",
              "Health Salad",
              "Salad Mesculen Greens",
              "Sweet Wheat Berry",
              "Thyme And Lemon Olives",
              "Tomato Wedges"
            ]
          },
          {
            "genre_name": "Soups",
            "items": [
              "Vegan Navy Bean Soup"
            ]
          },
          {
            "genre_name": "Deli Bar Entree",
            "items": [
              "Deli Meat",
              "German Potato Salad",
              "Grilled Chicken Montreal Seasoning Busch",
              "Ham Salad",
              "Scg Crunchy Slaw"
            ]
          },
          {
            "genre_name": "Entrees",
            "items": [
              "Hamburger Quarter Pounder",
              "Tortilla Crusted Tilapia"
            ]
          },
          {
            "genre_name": "Starch & Potatoes",
            "items": [
              "Spicy Diced Potatoes",
              "Steamed White Rice"
            ]
          },
          {
            "genre_name": "Veggies",
            "items": [
              "Sweet White Corn"
            ]
          },
]

```

We see that the data is formatted in an odd way, we have a JSON array and each object represents and dining hall.  This JSON is harder to decode and read so take your time to understand it.
Before looking at the answer to the below questions think about the soln yourself

#### How do we know if are in the Brower's object ?

Well we see that there is a top level key called "location_name", and we discussed previously the response was a json array.
So to get the json object for brower

```python
import requests
r = requests.get("https://rumobile.rutgers.edu/1/rutgers-dining.txt") # WHY a GET request?
resp = r.json()
for i in resp:
    if i["location_name"] == "Brower Commons":
       #do stuff with that object
```
We First make the request to the endpoint and store the json array in the resp object.
Then, we iterate through the json array and check the top level key "location_name" for our desired location. Now given an object (say the brower object) how do we access the meals ( The brower object is posted below for conveneince)

```json
  {
    "location_name": "Brower Commons",
    "date": 1550434349891,
    "meals": [
      {
        "meal_name": "Breakfast",
        "meal_avail": false
      },
      {
        "meal_name": "Lunch",
        "meal_avail": true,
        "genres": [
          {
            "genre_name": "Breakfast Meats",
            "items": [
              "Grilled Turkey Sausage Links",
              "Pork Sausage Links",
              "Vegetarian Breakfast Patties"
            ]
          },
          {
            "genre_name": "Breakfast Entrees",
            "items": [
              "Apple Pancake",
              "Oatmeal",
              "Red Velvet Waffle",
              "Scramble Cholesterol Free Egg",
              "Scrambled Eggs",
              "Vegan Grits Hot Cereal"
            ]
          },
          {
            "genre_name": "Breakfast Bakery",
            "items": [
              "Assorted Bagels",
              "Assorted Contract Muffins",
              "Plain Bagels"
            ]
          },
          {
            "genre_name": "Salad Bar",
            "items": [
              "Grilled Chicken Breast 4Oz"
            ]
          },
          {
            "genre_name": "Soups",
            "items": [
              "Rsted Eggplan & Red Pepp Soup"
            ]
          },
          {
            "genre_name": "Entrees",
            "items": [
              "4\" Club Roll",
              "Belgian Waffles",
              "Breaded Chicken Patty",
              "Noodle Lungo"
            ]
          },
          {
            "genre_name": "Starch & Potatoes",
            "items": [
              "Spicy Diced Potatoes"
            ]
          },
          {
            "genre_name": "Accompaniments",
            "items": [
              "Chopped Red & Green Peppers",
              "Sausage Crumbles",
              "Shredded Cheddar Cheese",
              "Shredded Mozzarella Cheese",
              "Sliced Bacon",
              "Sliced Mushrooms",
              "Small Diced Ham"
            ]
          },
          {
            "genre_name": "Cook To Order Bar",
            "items": [
              "Diced Tomatoes",
              "Diced Onions",
              "Egg Mix Liquid And Whole",
              "Liquid Egg Cholesterol Free",
              "Omelets Made To Order",
              "Shred Monterey Jack Cheese"
            ]
          },
          {
            "genre_name": "Pizza/ Pasta",
            "items": [
              "Garlic Bread Sticks",
              "Hawaiian Chicken Pizza",
              "Pepperoni Cheese Pizza Thin",
              "Round Cheese Pizza Large",
              "Shrimp And Pesto Pizza"
            ]
          }
        ]
      },
      {
        "meal_name": "Dinner",
        "meal_avail": true,
        "genres": [
          {
            "genre_name": "Entrees",
            "items": [
              "Garlic Roasted Rosemary Chicken",
              "Jambalaya",
              "Roast Beef",
              "Shrimp W/ Tequilla Lime Sauce",
              "Whole Wheat Penne"
            ]
          },
          {
            "genre_name": "Sauces & Gravies",
            "items": [
              "Plain Tomato Sauce",
              "Roasted Onion Port Au Jus"
            ]
          },
          {
            "genre_name": "Starch & Potatoes",
            "items": [
              "Roasted Red Bliss Potato W/ Crumbled Blue Cheese"
            ]
          },
          {
            "genre_name": "Veggies",
            "items": [
              "Collard Greens",
              "Vegan Spaghetti Squash Roasted"
            ]
          },
          {
            "genre_name": "Desserts",
            "items": [
              "Ny Cheesecake"
            ]
          },
          {
            "genre_name": "Bakery Misc",
            "items": [
              "Cranberry Rasin Loaf"
            ]
          },
          {
            "genre_name": "Cook To Order Bar",
            "items": [
              "Asian Brown Sauce",
              "Baked Brown Rice",
              "Beef Strips For Stir Fry",
              "Diced Tofu",
              "Fresh Chicken Strips Raw",
              "Kung Pao Sauce",
              "Large Broken Pdi Shrimp",
              "Lo Mein",
              "Oyster Sauce",
              "Pasta Vegetable Side",
              "Soy Bragg",
              "Steamed White Rice",
              "Szechuan Sauce"
            ]
          }
        ]
      },
      {
        "meal_name": "Knight Room",
        "meal_avail": true,
        "genres": [
          {
            "genre_name": "Entrees",
            "items": [
              "Chicken Parmesan",
              "Eggplant Rollatini",
              "Grilled Chicken Breast 3Oz"
            ]
          },
          {
            "genre_name": "Knight Room",
            "items": [
              "Cucumbers",
              "Italian Dinner Roll",
              "Tomato Wedges",
              "Tossed Salad"
            ]
          }
        ]
      },
      {
        "meal_name": "Late Knight",
        "meal_avail": false
      }
    ]
  }
  ```

As we can see meals is another JSON array and within that we can access the name of the meal in a meal_name key. And the actual meals themselves are under the JSON array genres which is also a JSON array and within that an array of items. Crazy eh?

Lets now tie it all together in our discord bot.
```python3
import discord
import asyncio
import requests


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return
        if message.content.startswith('!food'):
            await message.channel.send("Getting food")
            msg = message.content.split(" ")
            if(len(msg) < 3):
                await message.channel.send("not enough arguments")
            else:
                data = requests.get("https://rumobile.rutgers.edu/1/rutgers-dining.txt")
                location = msg[1]
                meal = msg[2]
                data_json = data.json()
                for i in data_json:
                    if location.lower() in i['location_name'].lower():
                        for j in i['meals']:
                            if meal.lower() in  j['meal_name'].lower():
                                for k in j['genres']:
                                    for s in k['items']:
                                        await message.channel.send(s)
```


Feel Free to make changes and add on to what we have

### Excerise: Now that we can get all the items for a particular meal, Now get it for a particular genre given a meal
