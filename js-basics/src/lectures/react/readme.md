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

### Part 4 (Completing the Game)

* Lifting State Up
* Why Immutability Is Important
    1. Complex Features Become Simple
    2. Detecting Changes
    3. Determining When to Re-Render in React
* Function Component (Square is being converted)
* Taking Turns
* Declaring a Winner

### Part 5 (Adding Time Travel)

* Storing a History of Moves
* Lifting State Up, Again
* Showing the Past Moves
* Picking a Key
* Implementing Time Travel

### Wrapping Up
Congratulations! You’ve created a tic-tac-toe game that:

* Lets you play tic-tac-toe,
* Indicates when a player has won the game,
* Stores a game’s history as a game progresses,
* Allows players to review a game’s history and see previous
* versions of a game’s board.

If you have extra time or want to practice your new React skills, here are some ideas for improvements that you could make to the tic-tac-toe game which are listed in order of increasing difficulty:

1. Display the location for each move in the format (col, row) in the move history list.
2. Bold the currently selected item in the move list.
3. Rewrite Board to use two loops to make the squares instead of hardcoding them.
4. Add a toggle button that lets you sort the moves in either ascending or descending order.
5. When someone wins, highlight the three squares that caused the win.
6. When no one wins, display a message about the result being a draw.
