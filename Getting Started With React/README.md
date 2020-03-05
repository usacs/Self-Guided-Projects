# Creating a To-Do App with React

[Live Demo](https://codesandbox.io/s/self-guided-project-react-to-do-app-v3ju1) | _45 min_ - _1 hr_

## What Will Be Covered?

In this tutorial, we'll be learning just enough JavaScript, HTML and CSS to create a basic To-Do app in React. I won't cover how to setup React on your machine, that's a separate beast. Instead, we'll be using an online IDE.

## Prerequisites

Experience with HTML and CSS is preferred, but not required. If you don't have either, try the [Codecademy tutorial](https://www.codecademy.com/catalog/language/html-css) on each before continuing.

## Setting Up

- **Navigate to [Code Sandbox](https://codesandbox.io/)**. You'll be writing code in this online IDE instead of on your local machine. This saves time and allows us to focus on React, not React setup.

- **Click on "Create Sandbox", then "React"**. On your right side should be an app preview.

## What Is React?

React is a popular JavaScript framework for writing complex web apps. Netflix, Facebook, and Airbnb all use React in production, so it's definitely a fair bet to say that React.js is a valuable skill to learn.

### Getting Started

Open `App.js`. Notice how some HTML markup is being returned by `function App()`. If you have some front-end experience, you might be thinking:

> Why is there HTML mixed with my JavaScript, aren't they separate languages?

_React combines JavaScript and HTML to make writing front-ends easier_. React developers refer to this HTML-in-JavaScript syntax as _JSX_. The _JSX_ syntax is very similar to HTML, with a few minor differences to make it easier to work with in JavaScript.

Remember the term _JSX_ because I'll be using it frequently to refer to the HTML-in-JavaScript parts of our code.

## Components

To be quick, _components are functions_ that return views. Views are the things that you see on screen. The `function App()` component, for example, returns a view which is what you see in the preview screen on your right.

> Just as classes are blueprints for Java objects, React components are blueprints for views.

Modify some of the text inside of the `h1` tag returned by `function App()` component and observe what happens.

```jsx
<div className="App">
  <h1>New Different Unique Text!</h1>
  <h2>Start editing to see some magic happen!</h2>
</div>
```

The text in the preview screen changed! The _JSX_ returned by a component directly effects what we see in our preview.

### Creating Our Own Components

`function App()` is one component. We call it the "root" component becuase it contains all other components. It's kind of like the `main()` method in Java, it's where everything starts from.

We can make new components and add them to `function App()`. For example, below is a `function TodoItem()` component.

```jsx
function TodoItem() {
  return <div>I am a todo item</div>;
}
```

Add the code for `function TodoItem()` above `export default function App()`.

```javascript
function TodoItem() {
  return <div>I am a todo item</div>
}

export default function App() {
```

Awesome, you've created your first component. It's a `function TodoItem()` component which returns a view, as all components should. Add `<TodoItem />` to the `function App()` component and remove the remaining tags.

```jsx
<div className="App">
  <TodoItem />
</div>
```

You should see "I am a todo item" in your preview.

To re-iterate, we:

- Created a new component, `function TodoItem()`. Components are functions that return views. They're also "blueprints" for views, kind of like Java classes are for objects.
- We added an instance of our `function TodoItem()` to `function App()` by writing `<TodoItem />`. Writing out our component name as `<ComponentName />` allow us to make an instance of it.

The `<TodoItem />` component returns a view (`<div>I am a todo item</div>`) to it's parent component `function App()`, which renders it at the location that we added it.

That's it. Components returns views, which are written in _JSX_. In practice, we _nest_ components within components to create hierarchy. A real-world example of a nested component structure might be:

```jsx
<AppContainer>
  <Nav />
  <Dashboard>
    <Sidebar />
    <Timeline />
  </Dashboard>
</AppContainer>
```

We can go as deep as we like with this nesting structure and often times we do. The ultimate goal is to make each individual component as small and self-contained as possible. This helps us avoid repitition and make our program easier to manage.

## Props

`<TodoItem />` isn't that useful yet because it just displays text. Let's give it more functionality.

Specifically, we want our `function TodoItem()` component to:

1. Display if it's checked or not
2. Display some todo text

If `function TodoItem()` was a typical JavaScript function, we might translate those two requirements into the arguments:

```javascript
// - isChecked would be a `boolean`
// - text would be a  `string`
function TodoItem(isChecked, text) {}
```

However components _are not regular functions_ and they're not called the same way. To achieve this with components, we must edit `function TodoItem()` to take in a singular object instead of a list of arguments.

```javascript
// - isChecked would be a `boolean`
// - text would be a  `string`
function TodoItem(props) {
  let isChecked = props.isChecked;
  let text = props.text;
}
```

That object contains a series of fields which we call **props**. We pass props into components as such:

```jsx
<TodoItem isChecked={false} text={"Go to basketball game."} />
```

However, be careful with the _JSX_ syntax here. Notice how the JavaScript values `false` and `"Go to basketball"` have curly braces around them. That's an important rule that we must follow.

Right now, our component doesn't use the props passed into it to render the view. Let's change that. Edit your `function TodoItem()` to contain a checkbox adjacent to some text.

```javascript
// - isChecked would be a `boolean`
// - text would be a  `string`
function TodoItem(props) {
  let isChecked = props.isChecked;
  let text = props.text;

  return (
    <div>
      <input type="checkbox" />
      <span>This is some text</span>
    </div>
  );
}
```

Next, lets take our prop values and add them to our view. Aforementioned, we add JavaScript values to our _JSX_ by using curly braces.

```javascript
function TodoItem(props) {
  let isChecked = props.isChecked;
  let text = props.text;

  return (
    <div>
      <input type="checkbox" checked={isChecked} />
      <span>{text}</span>
    </div>
  );
}
```

Now that our component is capable of displaying props, we can pass some props into our `function TodoItem()` component.

```jsx
<div className="App">
  <TodoItem checked={false} text={"Go to basketball game."} />
</div>
```

Notice how the names of the props that we pass inside of `<App />`(`isChecked` and `text`) match the names of the fields on the `props` object that we recieve in our component function. This is true for every component that we will create.

Also notice how we're using curly braces in this example—very important. Now, going back to our component code...

```javascript
function TodoItem(props) {
  let isChecked = props.isChecked;
  let text = props.text;

  return (
    <div>
      <input type="checkbox" checked={isChecked} />
      <span>{text}</span>
    </div>
  );
}
```

If you haven't noticed already, `{text}` and `{isChecked}` are acting as fill-ins for the values that we eventually pass into our component as props. Although it's useful to think about props as arguments and components as function, be sure to follow the rules of React and _JSX_.

## State and Events

Our app doesn't have live data yet, like the [finished product](https://codesandbox.io/s/self-guided-project-react-to-do-app-v3ju1) does. We hardcoded the props that our first component took (`<TodoItem checked={false} text={"Go to basketball game."} />`). In reality, we want our props to contain actual data from our user. We'll be dealing with different types of data from different types of user interactions, namely:

1. Entering new todo text into an input box,
2. Adding new todo items to a list of todo items,
3. Checking and unchecking each todo item.

This means that we'll need:

- The current value of the input box,
- A list of every todo item and tis `isChecked` and `text` values,
- A method for modifying a specific todo item's `isChecked` value when we click on it.

### Entering new todo text into an input box

We'll store our input text inside of our **state**.

**state** is data that will eventually update in our application. React is clever, so every time that we update state data, those updates will be immediately reflected in the view that we see on screen. To update state and access state, we use the React hook pattern.

Add `{useState}` to the imports at the top of your code and add the following code to the top of `function App()`.

```jsx
// Add `{useState}` to the top of your imports.
import React, {useState} from "react";
import "./styles.css";

export default function App() {
  // Add this code.
  const [input, setInput] = useState("");

  return (
    <div className="App">
      <TodoItem isChecked={false} text={"Go to basketball game."} />
    </div>
  );
}
```

Next, let's add an input box and an adjacent add button.

```jsx
export default function App() {
  // Add this code.
  const [input, setInput] = useState("");

  return (
    <div className="App">
      <div>
        <input type="text" />
        <button>Add</button>
      </div>
      <TodoItem isChecked={false} text={"Go to basketball game."} />
    </div>
  );
}
```

```javascript
const [input, setInput] = useState("");
```

Every time that `setInput` is called with a new value, `function App()` is called again, and `input` is replaced with the new value.

`useState("")` is used to set the default value of the `input`. This is what `input` will be equal to before we update it with `setInput`.

The next step is to actually use `setInput` and `input` to update our input. To acheive this, we must learn a bit about events.

**events** allow us to respond to user interaction on a specific element. They allow us to run a specific function every time that a user interacts with an element in a specific way.

Every time that the user inputs text on `<input type="text" />`, we want to respond by updating the `input` state. To acheive this, we can pass a function to the `onChange` event.

```jsx
import React, { useState } from "react";

export default function App() {
  const [input, setInput] = useState("");

  return (
    <div className="App">
      <div>
        <input
          type="text"
          value={input}
          onChange={function(event) {
            const value = event.target.value;
            setInput(value);
          }}
        />
        <button>Add</button>
      </div>
      <TodoItem isChecked={false} text={"Go to basketball game."} />
    </div>
  );
}
```

JavaScript happens to internally store the current value of an input element in the `event` object on the field `event.target.value`. Every time that the inputs text changes, we call `setInput` which updates the `input` state accordingly. We also set the value to that input with `value={input}` so that the new input values updates are reflected in the input box.

To re-iterate:

- `input` is a value and `setInput` is a function used to modify that value.
- `function App()` is called at the beginning of every program.
- The `""` inside of `useState` is just the default value of `item`. This is what `item` is equal to at the beginning of every program.
- Every time that `setInput` is called with a new value, `function App()` is called agian, and `input` contains the new value.
- We called `setInput` inside of `onChange` to update its value whenever the input box changes in value.

Create a new paragraph element above the `input` containing `{input}` to preview the `input` state's current value. It should update when you type in the input box!

```jsx
import React, { useState } from "react";

export default function App() {
  const [input, setInput] = useState("");

  return (
    <div className="App">
      <div>
        <p>{input}</p>
        <input
          type="text"
          onInput={function(event) {
            const value = event.target.value;
            setInput(value);
          }}
        />
        <button>Add</button>
      </div>
      <TodoItem isChecked={false} text={"Go to basketball game."} />
    </div>
  );
}
```

React developers call the `const [value, setValue] = useState(defaultValue)` pattern "React hooks". They're just a clean way of updating and managing values (state) and keeping them consistent with our view (what we see).

## Adding new todo items

We still need a way of creating new items. We'll be storing our items in an array, which will contain no elements at the start. 
```jsx
import React, { useState } from "react";

export default function App() {
  const [input, setInput] = useState("");
  const [items, setItems] = useState([]);

  return (
    <div className="App">
      <div>
        <p>{input}</p>
        <input
          type="text"
          onInput={function(event) {
            const value = event.target.value;
            setInput(value);
          }}
        />
        <button>Add</button>
      </div>
      <TodoItem isChecked={false} text={"Go to basketball game."} />
    </div>
  );
}
}
```

To achieve this, we create state to contain our items.

Similar to `setInput`, every time that `setItems` is called with a new value, `function App()` is called again, and `items` is replaced with the new value. `useState([])` is used to set the default value of `items`.

We'll be adding todo items when users "click" on the "Add" button. Let's add an `onClick` event for this.

```jsx
import React, { useState } from "react";

export default function App() {
  const [input, setInput] = useState("");
  const [items, setItems] = useState([]);

  return (
    <div className="App">
      <div>
        <p>{input}</p>
        <input
          type="text"
          onInput={function(event) {
            const value = event.target.value;
            setInput(value);
          }}
        />
        <button
          onClick={function(event) {
            // setItems()
          }}
        >
          Add
        </button>
      </div>
      <TodoItem isChecked={false} text={"Go to basketball game."} />
    </div>
  );
}
```

Inside of this function, we want to create a new array with a new item containing our input at the end. We also want to set out `input` state back to an empty string.

To create a new array with a our new item at the end, we can use the JavaScript spread operator.

```jsx
const newItem = { text: input, isChecked: false };

// `...` is the "spread operator"
setItems([...items, newItem]);
```

This allows us to fill our new array with the previous value of `input` and add our new object at the end.

```jsx
import React, { useState } from "react";

export default function App() {
  const [input, setInput] = useState("");
  const [items, setItems] = useState([]);

  return (
    <div className="App">
      <div>
        <p>{input}</p>
        <input
          type="text"
          onInput={function(event) {
            const value = event.target.value;
            setInput(value);
          }}
        />
        <button
          onClick={function(event) {
            const newItem = { text: input, isChecked: false };

            // `...` is the "spread operator"
            setItems([...items, newItem]);

            // set input back to empty string
            setInput("");
          }}
        >
          Add
        </button>
      </div>
      <TodoItem isChecked={false} text={"Go to basketball game."} />
    </div>
  );
}
```

### Displaying items

Now we have a list of items each containing `isClicked` and `text` properties and are capable of modifying that list to add new itmes.

```javascript
// Our `items` list might look something like this. 
[
  { text: "Do this.", isChecked: false },
  { text: "Do this other thing.", isChecked: true }
];
```

Next, we have to pass each one of these elements in our list as props to our `<TodoItem />` components.

```jsx
import React, { useState } from "react";

export default function App() {
  const [input, setInput] = useState("");
  const [items, setItems] = useState([]);

  return (
    <div className="App">
      <div>
        <p>{input}</p>
        <input
          type="text"
          onInput={function(event) {
            const value = event.target.value;
            setInput(value);
          }}
        />
        <button
          onClick={function(event) {
            const newItem = { text: input, isChecked: false };

            // `...` is the "spread operator"
            setItems([...items, newItem]);

            // set input back to empty string
            setInput("");
          }}
        >
          Add
        </button>
      </div>
      {/* Pass elements in list as props */}
      {items.map(function(item) {
        return <TodoItem isChecked={item.isChecked} text={item.text} />;
      })}
    </div>
  );
}
```

The way that we acheive this is with the JavaScript `map` function. Calling `map` on the `items` array allows us to iterate through every element in the array and return a new object in it's place. In this case, we're using the JavaScript `map` function to iterate though the `items` array and return a react component instance in it's place.

Almost every application contains large a variety of lists, this pattern is one of the most important in React.

### Checking and Unchecking items

Notice how everytime that you click on a checkbox, it's value does not update.

This is because clicking on a checkbox doesn't modify our state, we have to modify it ourselves. This means that if our a specific `<TodoItem />` in the todo item list is clicked on, we need to set items to a new list containing the opposite value for that item. (If the item is clicked it becomes unclicked, if it is clicked it becomes unclicked.)

We can achieve this, we need to listen to when our checkbox is clicked and modify our `items` array accordingly.

```javascript
function TodoItem(props) {
  let isChecked = props.isChecked;
  let text = props.text;

  return (
    <div>
      <input
        type="checkbox"
        isChecked={isChecked}
        onClick={function() {
          // Do something here
        }}
      />
      <span>{text}</span>
    </div>
  );
}
```

Unfortunately, this approach won't give us access to `items` because the `onClick` event handler is nested within `function TodoItem()`. A better approach is to pass the `onClick` function as a prop and define it in our `<App />` component.

```javascript
function TodoItem(props) {
  let isChecked = props.isChecked;
  let text = props.text;
  let onClick = props.onClick;

  return (
    <div>
      <input type="checkbox" checked={isChecked} onClick={onClick} />
      <span>{text}</span>
    </div>
  );
}
```

```jsx
import React, { useState } from "react";

export default function App() {
  const [input, setInput] = setState("");
  const [items, setItems] = useState([]);

  return (
    <div className="App">
      <div>
        <input
          type="text"
          onInput={function() {
            setInput(input);
          }}
        />
        <button
          onClick={function() {
            setItems([...items, { text: input, isChecked: false }]);
          }}
        >
          Add
        </button>
      </div>
      {items.map(item => (
        <TodoItem
          isChecked={item.isChecked}
          text={item.text}
          onClick={function() {
            // this function is passed in
          }}
        />
      ))}
    </div>
  );
}
```

One issue with this is that we have no way of uniquely identifying every element. We can get a unique identifier for every item in the `items` list by using **JavaScript Symbols**. JavaScript Symbols allow us to create unique indentifiers on the fly. Add the following code to the "Add" button's `onClick` function.

```jsx
<button
  onClick={function() {
    setItems([
      ...items,
      {
        id: Symbol(),
        text: input,
        isChecked: false
      }
    ]);
  }}
>
  Add
</button>
```

Now every single added item has an `id`, `text` and `isChecked`. The `id` Symbol is unique (that's the magic of symbols) and it will allow us to reference that specific item. Next we need to modify the `TodoItem` `onClick` handler to check or uncheck the `isChecked` field every time that the function is called.

```jsx
{
  items.map(function(item) {
    return (
      <TodoItem
        isChecked={item.isChecked}
        text={item.text}
        onClick={function() {
          const newItems = items.map(function(oldItem) {
            let newItem = oldItem;

            if (oldItem.id == item.id) {
              newItem.isChecked = !oldItem.isChecked;
            }

            return newItem;
          });

          setItems(newItems);
        }}
      />
    );
  });
}
```

Here, whenever a todo item is clicked, we iterate through every single item in the items array and once we encouter the item in the items array, we negate `isChecked`.

## Colophon

### React

- JSX
- Components
  - State
  - Props

### JavaScript

- Events
- Spread Operator
- Symbols

We organized our app into components, each of which take props. Props describe how a component should behave. We then discussed how every component has a state, and how to communicate state changes beween components. Lastly we discussed how events work and how they relate to interactivity.

I can only teach so much! Some resources that I recommend are:

- [React Tic-Tac-Toe](https://reactjs.org/tutorial/tutorial.html)
- [React For Beginners](https://tylermcginnis.com/reactjs-tutorial-a-comprehensive-guide-to-building-apps-with-react/)

Hope that this was fun!

## Next: Styled Components

This is cool, but it isn't visually interesting. In the next tutorial, we'll be adding styling to our To-Do application with a library called [styled-components](https://styled-components.com/). Stay tuned!


