# React

## Theory

React at `w3schools.com` -> [Getting started](https://www.w3schools.com/react/react_getstarted.asp)

## Tutorial

Intro to React at `reactjs.org` -> [Tic Tac Toe](https://reactjs.org/tutorial/tutorial.html)<br>
Source Code at `codepen.io` -> [Starter Code](https://codepen.io/gaearon/pen/oWWQNa?editors=0010)

### Part 1

* Start terminal from this folder
* If `npx` is not on your system
    * `npm install -g npx​​​​​​​`
* Create react app
    * `npx create-react-app tic-tac-toe-game`
* Change directory and start the app
    * `cd tic-tac-toe-game`
    * `npm start`
* Execute the tests
    * `npm test`
* Open `App.js` and peplace all the content inside the `<div className="App">` with 
    * `<h1>Hello React!</h1>`
* Save the file and see the changes in the browser
* Execute the tests again --> oops!
* Open `App.test.js` and modify them accordingly
    * `const titleElement = screen.getByText(/Hello React!/i);`
    * `expect(titleElement).toBeInTheDocument();`
* Save the file and run the tests again

### Part 2

* Now delete all source files
    * `cd src`
    * `del *`
    * `cd ..`
* Add a file named `index.css` in the `src/` folder with [this CSS code](https://codepen.io/gaearon/pen/oWWQNa?editors=0100).
* Add a file named `index.js` in the `src/` folder with [this JS code](https://codepen.io/gaearon/pen/oWWQNa?editors=0010).
* Add these three lines to the top of `index.js` in the `src/` folder:
    * `import React from 'react';`
    * `import ReactDOM from 'react-dom';`
    * `import './index.css';`

### Part 3

* Passing Data Through Props
* Making an Interactive Component
* Developer Tools - React component tree
