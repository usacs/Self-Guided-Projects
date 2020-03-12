# JavaScript Pokedex
This website (HTML / CSS / JavaScript) can get information about Pokemon! All you need is its name or Pokedex number.

## Who is This For?
This project is good for any beginner whatsoever. If you're trying to learn some web development, or what an API is or how they work, this is a great place to start.

## Getting Started
Here's what you'll need to complete this project:
- A text editor - VSCode, Atom, or Sublime will do fine.
- A browser, like Chrome or Firefox (*Note: there were some issues with Firefox, but none with Chrome.*)

## What is an API?
An API, or *Application Programming Interface*, is basically just a way to access some code or data that someone else has written / collected.

The best example for how APIs work are probably the Rutgers buses, and apps that tell you when the buses are coming - when you downloaded the app, you got a set of files that will just run on your phone, that don't really change (unless you get an update from the app store.) However, every time you run an app, no matter where you are or what time of day it is, you get (mostly) accurate information about when the next bus is coming to your stop. *This is because of the Transloc API* . Transloc is a company that wrote some code to know where any bus in the Rutgers fleet is at a given time, and approximately how far it is from each stop. Rider or the Rutgers app will simply *call this API*, and get some information about the buses at Rutgers, and render it for you. For this project, we're going to use an open *Pokemon API* to get some information about Pokemon, and render it for whoever wants to use it.

## Tutorial

### Step 1: Messing around with the PokeApi
If you go to [http://pokeapi.co](http://pokeapi.co), you can see how this works a little - in the little text bar, if you add the name of a Pokemon to the end of the url (i.e. https://pokeapi.co/api/v2/pokemon/chimchar) and click submit, you get some information about that Pokemon in the textbox below. That link is called an *endpoint* - when you make a request to that URL, it returns you some data.let's try and get this information, but with code.

#### fetch()
The fetch() method is how JavaScript makes API calls - you simply pass it an endpoint, and it returns some data after making a web request with something called a *Promise*. 

```javascript
fetch("https://pokeapi.co/api/v2/pokemon/pikachu")
    .then(res => res.json())
    .then(body => console.log(body));
```

The way that Promises work is similar to how they work in real life - if I promise to lend you a pencil, there is an expectation that I will somehow get a pencil, and then I will give it to you. When I give you the pencil, you are then able to write with it. When you call `fetch("http://pokeapi.co/pokemon/pikachu")`, it essentially promises you that it will return information about Pikachu, and then you'll be able to print it (with the `then()` function.)

You'll notice there are two `then()` functions with some funky syntax - don't worry about it too much. The syntax inside of the thens are arrow functions, and are basically just a way of saying "hey, this is your parameter, do this thing to the parameter, and then return it." The first one takes the response from the `fetch()` (res for short) and converts it to json. After returning the json, the second one just prints it to the JavaScript console. You don't need to understand this 100% - its totally fine to just steal this code as long as you vaguely get what's going on.

##### Testing fetch()
Let's test this - in your text editor, open a new file called `pokedex.html`. Inside that file, add this code:

```html
<script>
    fetch("https://pokeapi.co/api/v2/pokemon/pikachu")
        .then(res => res.json())
        .then(body => console.log(body));
</script>
```

What we're doing is basically creating an HTML page, and adding a `<script>` tag to run some JavaScript on our webpage. Now, if you open your `pokedex.html` file (double clicking it in your File Explorer), and then open your browser's console (`Ctrl-Shift-J` on Windows, `Cmd-Option-J` on Mac), you should see a JSON object there! If you sent a request for Pikachu, it should look a little something like this:

```json
{
  "name": "pikachu",
  "order": 35,
  "species": {
    "name": "pikachu",
    "url": "https://pokeapi.co/api/v2/pokemon-species/25/"
  },
  "sprites": {
    "back_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/25.png",
    "back_female": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/female/25.png",
    "back_shiny": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/shiny/25.png",
    "back_shiny_female": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/shiny/female/25.png",
    "front_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png",
    "front_female": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/female/25.png",
    "front_shiny": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/25.png",
    "front_shiny_female": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/female/25.png"
  }
  //...
}
```

#### JSON
JSON, or *JavaScript Object Notation*, is something called a *serialization format*. Basically, when you make an API call (or communicate with another computer in any way) the information that you receive needs to be structured in a specific way as it travels over the internet. JSON structures the data as a JavaScript object.

##### What is an object?
An object is a way of structuring data of different types that are relevant to representing a greater concept. While an array might be full of integers that represent grades on a test, an object of strings, ints, and boolean values might be more useful to represent a student:

```javascript
let student = {
    "name": "Srihari Shankar",
    "gradYear": 2019,
    "commuter": false
}
```
To access values from an object, you'd basically just do this:
```javascript
// This would print out the name property of the student object we defined earlier, so "Srihari Shankar"!
console.log(student.name)
```
Objects are composed as a set of *key/value pairings*. By doing `student.<insert key here>`, you get the value stored at that key.

#### Reading JSON
While some objects are more simple, others tend to nest a lot more - let's look at the PokeApi's response for our Pikachu request again:
```json
{
  "name": "pikachu",
  "order": 35,
  "species": {
    "name": "pikachu",
    "url": "https://pokeapi.co/api/v2/pokemon-species/25/"
  },
  "sprites": {
    "back_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/25.png",
    "back_female": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/female/25.png",
    "back_shiny": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/shiny/25.png",
    "back_shiny_female": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/shiny/female/25.png",
    "front_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png",
    "front_female": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/female/25.png",
    "front_shiny": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/25.png",
    "front_shiny_female": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/female/25.png"
  }
  //...
}
```
If you call `body.name` or `body.order`, that returns an int or a string value - but if you call `body.sprites`, that returns another object with a bunch of different key/value pairings for photos of Pikachu. So if we wanted a specific photo of Pikachu, we'd have to do something like this:

```javascript
// Since "sprites" is a key for the Pikachu object, and "front_default" is a key for the "sprites" object, we just need to chain those two properties to get that image url, like this:
console.log(body.sprites.front_default)
```
Some JSON values are arrays, so you would simply do something like `body.<insert key here>[index]`, and some are arrays of objects, so if you wanted a specific property of an element in an array, you might do something like `body.<insert key here>[index].<insert key here>`. It can get a little confusing at times, but as long as you're able to visualise your data, and see how D is a child of C, C is a child of B, and so on, getting from A to D shouldn't be too bad. 
### Step 2: Building your app.
For this project, we would like to:
1. Build a website
2. that when a user types in the name of a Pokemon,
3. it calls the Pokemon API, and then
4. some information about that Pokemon appears on the page.

#### 2 a.) "Build a website"

##### What is HTML?
HTML, or *Hypertext Markup Language* is the primary way websites are designed. It's different than a traditional programming language like Python or JavaScript because there's no sort of boolean or operational logic to what you're building - its about stringing components together in a way that a browser can understand them and show stuff. The general structure of HTML pages are as follows:
```html
<head>
    <!--This is where the things that the user doesn't see go-->
</head>

<body>
    <!--This is where the things that the user does see go-->
</body>
```
HTML is constructed as a set of tags - if you wanted to make a website that said "Hi Srihari!" on it, you would do this:
```html
<head>
    <!--This is where the things that the user doesn't see go-->
</head>

<body>
    <h1>Hi Srihari!</h1>
</body>
```
The `h1` tag is a header tag, which means it takes the text you give it, and renders it in a large, bold font face. There are also `h2`, `h3`, `h4`, `h5`, and `p` tags which are decreasingly smaller and less bold, and then `b` and `i` tags for bold and italics, and so on. If you wanna show a picture on your website, you'd use an `img` tag, and if you wanted say, checkboxes or some kind of multiple choice user input, you'd use an `input` tag. If you wanna  look at all of the different tags you can use to make  websites, I strongly recommend looking at [W3Schools](https://www.w3schools.com/html/)!

#### 2 b.) "When a user types in the name of a Pokemon"
We want to take in a string from a user (assumedly the name of a Pokemon) - as aforementioned, this can be done, with an input tag:
```html
<head>
    <!--This is where the things that the user doesn't see go-->
</head>

<body>
    <h1>Pokedex</h1>
    <h2>Please put in a name of a Pokemon:</h2>
    <input type = "text">
    <input type = "button" value = "Submit">
</body>
```
The line `<input type = "text">` creates a text bar for users to type into, and the `<input type = "button" value = "Submit">` is a button for them to click once they're done to get a response (we haven't gottten that bit to work yet, but at least we have a button!)

At the end of this step our code for our project should look a little something like this:

```html
<head>
    <!--This is where the things that the user doesn't see go-->
</head>
    
<body>
    <h1>Pokedex</h1>
    <h2>Please put in a name of a Pokemon:</h2>
    <input type = "text">
    <input type = "button" value = "Submit">
</body>

<script>
    fetch("https://pokeapi.co/api/v2/pokemon/pikachu")
        .then(res => res.json())
        .then(body => console.log(body));
</script>
```
#### 2 c.) "It calls the Pokemon API"
From here, we want to set up an *event* for when the button is clicked. A JavaScript event is basically any way a user interacts with a web page - clicking something, hovering over something, typing something, and so on. We want something to happen when our button is clicked, so we would simply add the "onclick" listener to our button, and pass it a JavaScript function:
```html
<body>
    <h1>Pokedex</h1>
    <h2>Please put in a name of a Pokemon:</h2>
    <input type = "text">
    <input type = "button" value = "Submit" onclick = "getPokemon()">
</body>
```

In our `<script>` tag, we want to bound our fetch call in a function, so that it's only called when our button is pushed:
```html
<script>
    function getPokemon() {
        fetch("https://pokeapi.co/api/v2/pokemon/pikachu")
            .then(res => res.json())
            .then(body => console.log(body));
    }
</script>
```
Now you'll get a JSON response about Pikachu in your console whenever you push the button - and only when you push it. But how do we get it to print a response for any Pokemon?

##### The Document Object Model
the *DOM*, or Document Object Model, is how JavaScript interacts with web pages, and why JavaScript is the best language for web development.

When you add a `<script>` tag to your HTML, all of your HTML code is then translated to a JavaScript object, meaning that you can manipulate your HTML with JavaScript. To access this object, you'd simply invoke the `document` variable in your JS code. If you wanted to print out the object representation of your HTML, you'd run `console.log(document)`. If you wanted to create a new `h1` tag to your HTML file, you could do something like:
```javascript
let h1 = document.createElement('h1')  // This creates a new h1 tag, in JS.
h1.innerHTML = "Hi Srihari!"  // This makes the h1 tag say "Hi Srihari!"
document.appendChild(h1)  // This adds the h1 tag to the entire document object, meaning it'll appear on your HTML page!
```
The DOM can also be used to access elements and their values in your HTML, using `id` and `class` properties.

##### HTML ids
If we give specific elements in our HTML ids, like so:
```html
<body>
    <h1>Pokedex</h1>
    <h2>Please put in a name of a Pokemon:</h2>
    <input type = "text" id = "pokemon-input">
    <input type = "button" value = "Submit" onclick = "getPokemon()">
</body>
```
In our JavaScript, we can use the `document.getElementById()` function to get the object representation of that element:
```javascript
// This returns the object representation of the element with the "pokemon-input" id.
document.getElementById("pokemon-input")
```
And since this is an object, it has properties, such as `value`, which is a property of input tags that represents what text is typed inside of them:

```javascript
// This will return whatever a user has typed, which is presumably a Pokemon's name!
let pokemon = document.getElementById("pokemon-input").value
```
So if we modify our script tag a little bit:
```html
<script>
    function getPokemon() {
        let pokemon = document.getElementById("pokemon-input").value
        let apiEndpoint = "https://pokeapi.co/api/v2/pokemon/" + pokemon
        fetch(apiEndpoint)
            .then(res => res.json())
            .then(body => console.log(body))
    }
</script>
```
Now, whenever we push our button after typing in the name of a Pokemon, we get info about whatever Pokemon's name we typed in. Our API's endpoint (stored in the variable `apiEndpoint`) is now the base of the API's url, plus the name of the Pokemon (our `pokemon`, which we got from the inside of our textbar.)
##### Synthesis
So by giving our button an `onlClick()` listener, giving our textbar an `id`, and structuring our JavaScript (our `fetch()` and DOM manipulation to get `pokemon`) as a function, we have created that prints to the console some info about a Pokemon on the push of a button! Your `pokedex.html` should look something like this now: 
```html
<head>
    <!--This is where the things that the user doesn't see go-->
</head>
    
<body>
    <h1>Pokedex</h1>
    <h2>Please put in a name of a Pokemon:</h2>
    <input type = "text" id = "pokemon-input">
    <input type = "button" value = "Submit" onclick="getPokemon()">
</body>

<script>
    function getPokemon() {
        let pokemon = document.getElementById("pokemon-input").value
        let apiEndpoint = "https://pokeapi.co/api/v2/pokemon/" + pokemon
        fetch(apiEndpoint)
            .then(res => res.json())
            .then(body => console.log(body))
    }
</script>
```
but what if we wanted to show that info on the webpage?

#### 2 d.) "Some information about that Pokemon appears on the page"
If you guessed that we'd do this with some DOM Manipulation, you'd be absolutely correct. For the sake of simplicity, we'll say that the only info we're gonna return about our Pokemon of choice is their name, type, and a photo of them. We're gonna wanna add some HTML elements for those fields:

```html
<body>
    <h1>Pokedex</h1>
    <h2>Please put in a name of a Pokemon:</h2>
    <input type = "text" id = "pokemon-input">
    <input type = "button" value = "Submit" onclick="getPokemon()">
    <br/>
    <img id = "pokemon-photo"/>
    <h3 id = "pokemon-name"></h3>
    <h3 id = "pokemon-type"></h3>
</body>
```
We added an `img`, and an `h3` for the Pokemon's name, and an `h4` for its type, all with corresponding ids, as well as a `br`, or line break, between our search bar and image to give it a little bit of space. So in your JavaScript, we'll probably wanna do something with that information:
```javascript
let pokemonPhoto = document.getElementById("pokemon-photo")
let pokemonName = document.getElementById("pokemon-name")
let pokemonType = document.getElementById("pokemon-type")
```
Next, we wanna populate those variables with info from our API call - we can do this with a new JavaScript function:
```javascript
function renderPokemon(pokemon) {
    let pokemonPhoto = document.getElementById("pokemon-photo")
    let pokemonName = document.getElementById("pokemon-name")
    let pokemonType = document.getElementById("pokemon-type")
    
    pokemonPhoto.src = pokemon.sprites.front_default
    pokemonName.innerHTML = pokemon.name
    pokemonType.innerHTML = pokemon.types[0].type.name
}
```
We did a lot here - let's break it down.

Assuming the `pokemon` parameter of our function is the response from our API call:
- we're setting `pokemonPhoto.src`, the source of our `img` tag (where the photo is displayed from) to our `pokemon` variable's `sprites` property's `front_default` property.
- We're setting `pokemonName.innerHTML`, our `h3` tag's inner HTML (the code inside of it, basically the text inside the tag) to our Pokemon's name (`pokemon.name`)
- We're setting `pokemonType.innerHTML`, our `h4` tag's inner HTML to our Pokemon's first type's name (`pokemon.types` returns an array of all its types - to simplify, we got the first element, `pokemon.types[0]`, and got its type property `pokemon.types[0].type`, and then got its name property `pokemon.types[0].type.name`).

So if we change our `getPokemon()` function a little bit, and instead of printing our response to the console, we pass it as a parameter to `renderPokemon()`, our code should work!

```html
<head>
    <!--This is where the things that the user doesn't see go-->
</head>
    
<body>
    <h1>Pokedex</h1>
    <h2>Please put in a name of a Pokemon:</h2>
    <input type = "text" id = "pokemon-input">
    <input type = "button" value = "Submit" onclick="getPokemon()">
    <br/>
    <img id = "pokemon-photo"/>
    <h3 id = "pokemon-name"></h3>
    <h3 id = "pokemon-type"></h3>
</body>

<script>
    function getPokemon() {
        let pokemon = document.getElementById("pokemon-input").value
        let apiEndpoint = "https://pokeapi.co/api/v2/pokemon/" + pokemon
        fetch(apiEndpoint)
            .then(res => res.json())
            .then(body => renderPokemon(body))
    }
    function renderPokemon(pokemon) {
        let pokemonPhoto = document.getElementById("pokemon-photo")
        let pokemonName = document.getElementById("pokemon-name")
        let pokemonType = document.getElementById("pokemon-type")
        
        pokemonPhoto.src = pokemon.sprites.front_default
        pokemonName.innerHTML = pokemon.name
        pokemonType.innerHTML = pokemon.types[0].type.name
    }
</script>
```
And that's it! You built a Pokedex!

## Post Script
Congratulations on finishing this tutorial! You should be proud of yourself. Here's what you learned:
- Some basic JavaScript.
- How to use the PokeApi.
- How to use the DOM.

This is a pretty cool project, but there's a lot of room for improvement - think about some ways to make this project better on your own, including:
- Showing more information about a Pokemon.
- Changing how you accept info about a Pokemon (maybe the user chooses from a list of all Pokemon, not just types the name of one in?)
- Making the website more aesthetically pleasing with [CSS](https://www.w3schools.com/css/)!

This is the first version of a program like this - as you work on it more, it only gets better, and you'll only learn more. Good luck!
