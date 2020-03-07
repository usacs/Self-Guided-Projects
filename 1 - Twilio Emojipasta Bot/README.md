# Twilio Emojipasta Bot
This Python Twilio bot is a fun little way to prank your friends by sending them a seasonally relevant emojipasta every month.

## Who is This For?
This project is good for any beginner whatsoever. The only real prerequisite for this project is that you understand the bare essentials of computer science (loops, if/else statements, etc.) Everything else you'll learn through the guide.

## Getting Started
Here's what you'll need to complete this project:
- A Command Prompt or Terminal (Mac and Linux users, just use your terminal. Windows users, [I strongly advise downloading the Windows Subsystem for Linux](https://www.howtogeek.com/249966/how-to-install-and-use-the-linux-bash-shell-on-windows-10/). )
- Python 2.7 (this comes pre-installed a Linux-friendly terminal.)
- The pip package manager (once again, this comes pre-installed.)
- A Twilio developer account.

## What is pip?
pip is a package manager for Python packages/modules - basically, at some point in time a developer wrote some code that did some specific function, and rather than making any developer who wanted to use such a function in their code have to write their own code to implement it, they just let other developers use their version. The way that you install that code and use it is through pip.

## What is Twilio?
Twilio's API allows software developers to programmatically make and receive phone calls, send and receive text messages, and perform other communication functions.

### For Windows Users
If you downloaded the Windows Subsystem for Linux as was recommended in the last step, setting it up will take a few extra steps - once you've done those, you're good to go.

1. In your terminal, once it's installed, run `sudo apt-get update` .
2. Next, run `sudo apt-get install python-pip` .

Cool, now you have pip installed in your terminal. Time to navigate your terminal to your Windows filesystem.

3. Run `cd ~` .
4. Then, run `cd ..` .
5. Run `cd mnt/c/Users` .
6. At this point, if you run `ls`, your terminal should output a list of your Windows users. `cd` into your preferred Windows user account.
7. At this point, you'll have access to the same folders and files that you would from your Windows File Explorer (e.g. Documents, Desktop, and so on). You'll need to make a new folder for this project, so wherever you do that, just make sure that your terminal ends up there as well.

You should be all set up now!


## Tutorial
### Step 1: Installing your packages.
In your terminal, create and navigate to a new folder for this project. Once you're in there, you're gonna wanna use pip to install a few packages. Since we want to be able to render emojis, the Python [emoji](https://pypi.org/project/emoji/) library is going to come in handy. We're also going to want to install [Twilio's Python API](https://pypi.org/project/twilio/) to be able to send text messages with this program.

In your terminal, run:

```
pip install emoji
pip install twilio
```

### Step 2: Setting up Twilio.
Twilio graciously gives $15 in free trial credits to people who sign up for a developer account (no credit card needed.) All you need to do is:

1. Go to [twilio.com/try-twilio](https://twilio.com/try-twilio)
2. Sign up for an account.
3. Put in your phone number for verification, and fill out the verification code on the next page.
4. If necessary, "skip to dashboard" .

Right now, you should be on the Twilio dashboard. All you need from here to complete this project is a Twilio number to send our emojipasta messages from.

5. On the dashboard, there should be a big red button that says "Get a trial number". Click it. It'll auto-recommend a U.S. number for you to send your text from.
6. Click "choose this number".
7. Once your trial number is confirmed, it'll say that it has an "Account SID" and an "Auth Token". You should store these somewhere - we're going to need them later.

Great! Now Twilio is set up for our application. Onto the code.

### Step 3: Messing around with APIs.
In your project folder, create a new file called `emojipasta.py`.

#### 3 a.) Importing your Modules.
If you remember from Step 1, we installed a couple of packages with pip. We're going to want to import them into our Python file. In emojipasta.py, write:

```python
import emoji
from twilio.rest import Client
```
(don't worry about that `from twilio.rest import Client` bit. All that means is that since Twilio's library is so big, we only want a small part of it - specifically, the TwilioClient, which is stored under the library as "Client". )

There's one more thing you should know - Python has a couple of built-in libraries. What that means practically is that you don't need to install these libraries with pip, but if you want to use them with your program, you still need to import them. In our case, since we want to be able to send one of these emojipasta messages every month, knowing the date would be useful - to get it, we can use the built-in `datetime` library, and also import it into our program.

Your code should look like this at the end of this step:
```python
import datetime
import emoji
from twilio.rest import Client
```

#### 3 b.) Getting Started with emoji
The Python emoji library is pretty easy to use - the emoji library has an instance method `emojize()`, which when passed a string, if it contains any emoji aliases (a string which describes an emoji that can be interpreted as that emoji) , will translate the alias to the emoji it represents. For example:

```python
emoji.emojize(":smile:", use_aliases = True)
```
Would return `😀`, and

```python
emoji.emojize("College Avenue is my favorite campus :smile:", use_aliases = True)
```
Would return `College Avenue is my favorite campus 😀`

You try! Mess around with the emoji library - edit your code in `emojipasta.py`, and in your terminal, run `python emojipasta.py` to see what prints.

At the end of this step, your code should look something like:

```python
import datetime
import emoji
from twilio.rest import Client

print(emoji.emojize("College Avenue is my favorite campus :smile:", use_aliases = True))

```

#### 3 c.) Formatting your Emojipasta
This step is really easy - as you know, an emojipasta is a copypasta that uses emoji. Here's a classic:

`I 👱🏾‍♂️👌was🔙 actually a devops 💻 intern🎓 for the past 👈 two ✌️🥈years, so this 👇👌is really 💯 relevant🤔😮👀.  I interned🎓💻 at Oscar🚗, a health⚕️👨‍⚕️😷 insurance💵💸 startup 🏢 in NYC🌃. Do you🧓🏼 have👇 or can we👬 watch👀👀 videos🎬🎥 of people 👦👧👩‍🏫👩‍🍳at devops💻☁️ conferences🙋👥?`

The emoji library can read in and print out the emoji icons - if for whatever reason, it gives you a hard time though, you should replace each emoji with its alias. Aliases can be found on the [emoji cheat sheet](https://www.webfx.com/tools/emoji-cheat-sheet/).

Find one emojipasta for each month - try to find ones relevant to holidays! If you can't find one, maybe you can write your own.

At the end of this step, your code should look something like:

```python
import datetime
import emoji
from twilio.rest import Client

print(emoji.emojize("I 👱🏾‍♂️👌was🔙 actually a devops 💻 intern🎓 for the past 👈 two ✌️🥈years, so this 👇👌is really 💯 relevant🤔😮👀.  I interned🎓💻 at Oscar🚗, a health⚕️👨‍⚕️😷 insurance💵💸 startup 🏢 in NYC🌃. Do you🧓🏼 have👇 or can we👬 watch👀👀 videos🎬🎥 of people 👦👧👩‍🏫👩‍🍳at devops💻☁️ conferences🙋👥?", use_aliases = True))

```


#### 3 d.) Getting Started with datetime
The datetime library allows you to access a bunch of datapoints about the current time, the current date, and so on. The easiest way to use datetime, at least for this project, is just to use `datetime.today()`, which returns an object about the current day.

You're going to want to store this object in a variable in order to keep accessing it:

```python
today = datetime.today()
```

Now, you can print information about today! Something like this:

```python
today = datetime.today()
print(today.month)
print(today.day)
print(today.year)
```

Should return something like:

```console
5
17
2019
```

At the end of this step, your code should look something like:

```python
import datetime
import emoji
from twilio.rest import Client

print(emoji.emojize("I 👱🏾‍♂️👌was🔙 actually a devops 💻 intern🎓 for the past 👈 two ✌️🥈years, so this 👇👌is really 💯 relevant🤔😮👀.  I interned🎓💻 at Oscar🚗, a health⚕️👨‍⚕️😷 insurance💵💸 startup 🏢 in NYC🌃. Do you🧓🏼 have👇 or can we👬 watch👀👀 videos🎬🎥 of people 👦👧👩‍🏫👩‍🍳at devops💻☁️ conferences🙋👥?", use_aliases = True))


today = datetime.today()
print(today.month)
print(today.day)
print(today.year)

```

#### 3 e.) Getting Started with Twilio
Now the fun part! We get to send ourselves a text from our laptop. The Twilio API is pretty simple to set up - remember how we imported the TwilioClient on line 1? How we have to set it up, like so:

```python
account_sid = "some very long alphanumeric value"
auth_token = "another very long alphanumeric value"
client = Client(account_sid, auth_token)
```
You're gonna wanna replace `account_sid` and `auth_token` with YOUR Twilio number's Account SID and Auth Token from when you set up your Twilio account. Afterwards, the rest is pretty simple:

```python
account_sid = "some very long alphanumeric value"
auth_token = "another very long alphanumeric value"
client = Client(account_sid, auth_token)

message = client.messages.create(
    body="College Avenue is my favorite campus!",
    from_='+Twilio Number',
    to='+Your Phone Number'
)

```
After saving and running this, you should have just received a text from your Twilio number just now! Pretty cool right? To send these texts to your friends, you're going to need to register their numbers in your Twilio account - they're going to get a verification number from Twilio, and once you input that into your dashboard, you can send texts to their phone as well.


At the end of this step, your code should look something like:

```python
import datetime
import emoji
from twilio.rest import Client

print(emoji.emojize("I 👱🏾‍♂️👌was🔙 actually a devops 💻 intern🎓 for the past 👈 two ✌️🥈years, so this 👇👌is really 💯 relevant🤔😮👀.  I interned🎓💻 at Oscar🚗, a health⚕️👨‍⚕️😷 insurance💵💸 startup 🏢 in NYC🌃. Do you🧓🏼 have👇 or can we👬 watch👀👀 videos🎬🎥 of people 👦👧👩‍🏫👩‍🍳at devops💻☁️ conferences🙋👥?", use_aliases = True))


today = datetime.today()
print(today.month)
print(today.day)
print(today.year)

account_sid = "some very long alphanumeric value"
auth_token = "another very long alphanumeric value"
client = Client(account_sid, auth_token)

message = client.messages.create(
    body="College Avenue is my favorite campus!",
    from_='+Twilio Number',
    to='+Your Phone Number'
)

```

### Step 4: Building your app.

This is where we should start thinking about how our application should behave logic-wise.

- We need to be able to send a specific block of emoji-fied text
- Based on what month it is.
- And when the month changes, we should send the next month's message.

#### 4 a.) "Based on What Month It Is"

Let's say that it's the month of October. I want to be able to send my Halloween-themed emojipasta. However, this message should ONLY send if it's the month of October.

In other words,

```python

today = datetime.today()

month = int(str(today.month))

if month  == 10:  # if we're in October...
    message = client.messages.create(  # We should send the Halloween themed emojipasta.
        body= emoji.emojize("", use_aliases = True),
        from_='+Twilio Number',
        to='+Your Phone Number'
    )
```
You might be wondering what does `month = int(str(today.month))` mean - basically, `datetime.today()` returns an object, and the month property of that object is of a weird type that's not easy to compare. Basically, we just converted that property into a string, and then into an int, so we could more easily check what month we're in.

You're going to now want to construct one of these if/else blocks for every month.

With some re-structuring for readability, and after deleting all of the stuff we did to test that our APIs were working, at the end of this step, your code should look something like:

```python
import datetime
import emoji
from twilio.rest import Client

# Twilio API Setup
account_sid = "some very long alphanumeric value"
auth_token = "another very long alphanumeric value"
client = Client(account_sid, auth_token)

# What month is it?
today = datetime.today()
month = int(str(today.month))


if month == 1:  # if we're in January...
    message = client.messages.create(  # We should send the January-themed emojipasta.
        body= emoji.emojize("YOUR JANUARY EMOJIPASTA", use_aliases = True),
        from_='+Twilio Number',
        to='+Your Phone Number'
    )

elif month == 2:  # if we're in February...
    message = client.messages.create(  # We should send the February-themed emojipasta.
        body= emoji.emojize("YOUR FEBRUARY EMOJIPASTA", use_aliases = True),
        from_='+Twilio Number',
        to='+Your Phone Number'
    )

elif month == 3:  # if we're in March...
    message = client.messages.create(  # We should send the March-themed emojipasta.
        body= emoji.emojize("YOUR MARCH EMOJIPASTA", use_aliases = True),
        from_='+Twilio Number',
        to='+Your Phone Number'
    )

elif month == 4:  # if we're in April...
    message = client.messages.create(  # We should send the April-themed emojipasta.
        body= emoji.emojize("YOUR APRIL EMOJIPASTA", use_aliases = True),
        from_='+Twilio Number',
        to='+Your Phone Number'
    )

elif month == 5:  # if we're in May...
    message = client.messages.create(  # We should send the May-themed emojipasta.
        body= emoji.emojize("YOUR MAY EMOJIPASTA", use_aliases = True),
        from_='+Twilio Number',
        to='+Your Phone Number'
    )

elif month == 6:  # if we're in June...
    message = client.messages.create(  # We should send the June-themed emojipasta.
        body= emoji.emojize("YOUR JUNE EMOJIPASTA", use_aliases = True),
        from_='+Twilio Number',
        to='+Your Phone Number'
    )

elif month == 7:  # if we're in July...
    message = client.messages.create(  # We should send the July-themed emojipasta.
        body= emoji.emojize("YOUR JULY EMOJIPASTA", use_aliases = True),
        from_='+Twilio Number',
        to='+Your Phone Number'
    )

elif month == 8:  # if we're in August...
    message = client.messages.create(  # We should send the August-themed emojipasta.
        body= emoji.emojize("YOUR AUGUST EMOJIPASTA", use_aliases = True),
        from_='+Twilio Number',
        to='+Your Phone Number'
    )

elif month == 9:  # if we're in September...
    message = client.messages.create(  # We should send the September-themed emojipasta.
        body= emoji.emojize("YOUR SEPTEMBER EMOJIPASTA", use_aliases = True),
        from_='+Twilio Number',
        to='+Your Phone Number'
    )

elif month == 10:  # if we're in October...
    message = client.messages.create(  # We should send the October-themed emojipasta.
        body= emoji.emojize("YOUR OCTOBER EMOJIPASTA", use_aliases = True),
        from_='+Twilio Number',
        to='+Your Phone Number'
    )

elif month == 11:  # if we're in November...
    message = client.messages.create(  # We should send the November-themed emojipasta.
        body= emoji.emojize("YOUR NOVEMBER EMOJIPASTA", use_aliases = True),
        from_='+Twilio Number',
        to='+Your Phone Number'
    )

elif month == 12:  # if we're in December...
    message = client.messages.create(  # We should send the December-themed emojipasta.
        body= emoji.emojize("YOUR DECEMBER EMOJIPASTA", use_aliases = True),
        from_='+Twilio Number',
        to='+Your Phone Number'
    )

```

#### 4 b.) "And When the Month Changes"
What we have so far should be working pretty well! All we need to do now is check if the month has changed. When you declare `today = datetime.today()`, the variable today stores the value of `today` at the time that you called that function. Meaning tomorrow, `today` would hold the value for yesterday, and the day after that would store the value from two days ago.

One way to do this is to constantly, always check what month it is. One way to do something like that might be:

```python
current_month = int(str(datetime.today().month))  # this is the month at the time of starting the program.

while True:  # This is an infinite loop. We are CONSTANTLY checking what month it is. Like every microsecond.
    month = int(str(datetime.today().month))

    if current_month != month:  # The SECOND the month changes,
        current_month = month  # We reassign current_month, and wait for the month to change again.
        # Something should go here...
```

So if we were to modularize our if/else block that sends a text based on what month it is...
```python

def sendText(month): #This function accepts an int parameter month, with the value of what month it is.

    if month == 1:  # if we're in January...
    message = client.messages.create(  # We should send the January-themed emojipasta.
        body= emoji.emojize("YOUR JANUARY EMOJIPASTA", use_aliases = True),
        from_='+Twilio Number',
        to='+Your Phone Number'
    )

    elif month == 2:  # if we're in February...
        message = client.messages.create(  # We should send the February-themed emojipasta.
            body= emoji.emojize("YOUR FEBRUARY EMOJIPASTA", use_aliases = True),
            from_='+Twilio Number',
            to='+Your Phone Number'
        )

    elif month == 3:  # if we're in March...
        message = client.messages.create(  # We should send the March-themed emojipasta.
            body= emoji.emojize("YOUR MARCH EMOJIPASTA", use_aliases = True),
            from_='+Twilio Number',
            to='+Your Phone Number'
        )

    elif month == 4:  # if we're in April...
        message = client.messages.create(  # We should send the April-themed emojipasta.
            body= emoji.emojize("YOUR APRIL EMOJIPASTA", use_aliases = True),
            from_='+Twilio Number',
            to='+Your Phone Number'
        )

    elif month == 5:  # if we're in May...
        message = client.messages.create(  # We should send the May-themed emojipasta.
            body= emoji.emojize("YOUR MAY EMOJIPASTA", use_aliases = True),
            from_='+Twilio Number',
            to='+Your Phone Number'
        )

    elif month == 6:  # if we're in June...
        message = client.messages.create(  # We should send the June-themed emojipasta.
            body= emoji.emojize("YOUR JUNE EMOJIPASTA", use_aliases = True),
            from_='+Twilio Number',
            to='+Your Phone Number'
        )

    elif month == 7:  # if we're in July...
        message = client.messages.create(  # We should send the July-themed emojipasta.
            body= emoji.emojize("YOUR JULY EMOJIPASTA", use_aliases = True),
            from_='+Twilio Number',
            to='+Your Phone Number'
        )

    elif month == 8:  # if we're in August...
        message = client.messages.create(  # We should send the August-themed emojipasta.
            body= emoji.emojize("YOUR AUGUST EMOJIPASTA", use_aliases = True),
            from_='+Twilio Number',
            to='+Your Phone Number'
        )

    elif month == 9:  # if we're in September...
        message = client.messages.create(  # We should send the September-themed emojipasta.
            body= emoji.emojize("YOUR SEPTEMBER EMOJIPASTA", use_aliases = True),
            from_='+Twilio Number',
            to='+Your Phone Number'
        )

    elif month == 10:  # if we're in October...
        message = client.messages.create(  # We should send the October-themed emojipasta.
            body= emoji.emojize("YOUR OCTOBER EMOJIPASTA", use_aliases = True),
            from_='+Twilio Number',
            to='+Your Phone Number'
        )

    elif month == 11:  # if we're in November...
        message = client.messages.create(  # We should send the November-themed emojipasta.
            body= emoji.emojize("YOUR NOVEMBER EMOJIPASTA", use_aliases = True),
            from_='+Twilio Number',
            to='+Your Phone Number'
        )

    elif month == 12:  # if we're in December...
        message = client.messages.create(  # We should send the December-themed emojipasta.
            body= emoji.emojize("YOUR DECEMBER EMOJIPASTA", use_aliases = True),
            from_='+Twilio Number',
            to='+Your Phone Number'
        )

```

Then, our check for what month it is would look something like this:

```python

current_month = int(str(datetime.today().month))  # this is the month at the time of starting the program.

while True:  # This is an infinite loop. We are CONSTANTLY checking what month it is. Like every microsecond.
    month = int(str(datetime.today().month))

    if current_month != month  # The SECOND the month changes,
        current_month = month  # We reassign current_month, and wait for the month to change again.
        sendText(current_month)  # Send the text based on what month we're in.
```


### Step 5: Finish your Program
And with a little formatting to make this be fully functional Python code, your final project should look like this:

```python
import datetime
import emoji
from twilio.rest import Client

# Twilio API Setup
account_sid = "some very long alphanumeric value"
auth_token = "another very long alphanumeric value"
client = Client(account_sid, auth_token)

current_month = int(str(datetime.today().month))  # this is the month at the time of starting the program.

def main():  # This is our main method - it should execute on run.
    
    while True:  # Our check for the month changing.
    month = int(str(datetime.today().month))

    if current_month != month  # When the month changes...
        current_month = month 
        sendText(current_month)  # Send the text based on what month we're in.


def sendText(month):  # This function accepts an int parameter month, with the value of what month it is.

    if month == 1:  # if we're in January...
    message = client.messages.create(  # We should send the January-themed emojipasta.
        body= emoji.emojize("YOUR JANUARY EMOJIPASTA", use_aliases = True),
        from_='+Twilio Number',
        to='+Your Phone Number'
    )

    elif month == 2:  # if we're in February...
        message = client.messages.create(  # We should send the February-themed emojipasta.
            body= emoji.emojize("YOUR FEBRUARY EMOJIPASTA", use_aliases = True),
            from_='+Twilio Number',
            to='+Your Phone Number'
        )

    elif month == 3:  # if we're in March...
        message = client.messages.create(  # We should send the March-themed emojipasta.
            body= emoji.emojize("YOUR MARCH EMOJIPASTA", use_aliases = True),
            from_='+Twilio Number',
            to='+Your Phone Number'
        )

    elif month == 4:  # if we're in April...
        message = client.messages.create(  # We should send the April-themed emojipasta.
            body= emoji.emojize("YOUR APRIL EMOJIPASTA", use_aliases = True),
            from_='+Twilio Number',
            to='+Your Phone Number'
        )

    elif month == 5:  # if we're in May...
        message = client.messages.create(  # We should send the May-themed emojipasta.
            body= emoji.emojize("YOUR MAY EMOJIPASTA", use_aliases = True),
            from_='+Twilio Number',
            to='+Your Phone Number'
        )

    elif month == 6:  # if we're in June...
        message = client.messages.create(  # We should send the June-themed emojipasta.
            body= emoji.emojize("YOUR JUNE EMOJIPASTA", use_aliases = True),
            from_='+Twilio Number',
            to='+Your Phone Number'
        )

    elif month == 7:  # if we're in July...
        message = client.messages.create(  # We should send the July-themed emojipasta.
            body= emoji.emojize("YOUR JULY EMOJIPASTA", use_aliases = True),
            from_='+Twilio Number',
            to='+Your Phone Number'
        )

    elif month == 8:  # if we're in August...
        message = client.messages.create(  # We should send the August-themed emojipasta.
            body= emoji.emojize("YOUR AUGUST EMOJIPASTA", use_aliases = True),
            from_='+Twilio Number',
            to='+Your Phone Number'
        )

    elif month == 9:  # if we're in September...
        message = client.messages.create(  # We should send the September-themed emojipasta.
            body= emoji.emojize("YOUR SEPTEMBER EMOJIPASTA", use_aliases = True),
            from_='+Twilio Number',
            to='+Your Phone Number'
        )

    elif month == 10:  # if we're in October...
        message = client.messages.create(  # We should send the October-themed emojipasta.
            body= emoji.emojize("YOUR OCTOBER EMOJIPASTA", use_aliases = True),
            from_='+Twilio Number',
            to='+Your Phone Number'
        )

    elif month == 11:  # if we're in November...
        message = client.messages.create(  # We should send the November-themed emojipasta.
            body= emoji.emojize("YOUR NOVEMBER EMOJIPASTA", use_aliases = True),
            from_='+Twilio Number',
            to='+Your Phone Number'
        )

    elif month == 12:  # if we're in December...
        message = client.messages.create(  # We should send the December-themed emojipasta.
            body= emoji.emojize("YOUR DECEMBER EMOJIPASTA", use_aliases = True),
            from_='+Twilio Number',
            to='+Your Phone Number'
        )


if __name__ == "__main__":  # This just calls your main method when you run emojipasta.py.
	main()
```

And that's it! You've just built a Twilio bot that sends emojipastas!

## Post Script
Congratulations on finishing this tutorial! You should be proud of yourself. Here's what you learned:
- Some basic Python.
- How to use some pretty basic APIs, like `emoji` and `datetime`.
- How to use a slightly more complicated API, like Twilio.

That being said, if you couldn't tell already, this program is pretty inefficient. First off, for it to work the way it's intended to, it would need to run on your computer all year without ever terminating (or, you would have to stop it the second it sent the text, and run it again at the first of each month.) Also, you'd need to manually add phone numbers, and the if/else block we constructed isn't super great for readability. 

If you want to improve this project, maybe think about how to fix some of the following issues:

- How do I make this code more readable? Is there a way to cut down on the number of if/else blocks we use in sendText()?

- How do I make this program less resource-intensive? Is there a way to possibly "pause" my program for a month so that it isn't always pinging the `datetime` API, and so it pings it only about once a month? Or if the program has to run the whole time, maybe there's a better way for me to write my code such that it's a little bit more stable than just a while loop with some if statements?

- Let's say I want to send these texts to multiple friends: is there an effective way to manage multiple phone numbers? If I'm feeling really fancy, how do I allow people to opt-in to receive a monthly emojipasta and handle that automatically?

This is the first iteration of an app like this. As time progresses, you're going to learn a lot more about programming, how to more effectively manage data, more efficiently use APIs, and how to make your code easier to read and convenient to run. At any rate, you've built a really cool app that you can use to confuse some of your friends, and that's a really good place to start.
