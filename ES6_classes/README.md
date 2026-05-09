ES6 Basic
This project covers the fundamentals of modern JavaScript using ES6 (ECMAScript 2015) features.
The goal of this project is to understand the new syntax and concepts introduced in ES6 and how they improve JavaScript development.

Learning Objectives
By the end of this project, you should be able to explain:
•
What ES6 is
•
The new features introduced in ES6
•
The difference between var, let, and const
•
Block scope in JavaScript
•
Arrow functions
•
Default function parameters
•
Rest and spread operators
•
Template literals
•
Object property shorthand syntax
•
Computed property names
•
ES6 method properties
•
Iterators and for...of loops
•
How modules work using export and import

Requirements
•
Ubuntu 20.04 LTS
•
Node.js 20.x.x
•
npm 9.x.x or higher
•
All files must use the .js extension
•
Code should follow ESLint rules
•
Testing is done using Jest

Project Setup
Install Node.js
Bash
نسخ
curl -sL https://deb.nodesource.com/setup_20.x -o nodesource_setup.sh
sudo bash nodesource_setup.sh
sudo apt install nodejs -y
Check installation:
Bash
نسخ
node -v
npm -v

Install Dependencies
Inside the project directory:
Bash
نسخ
npm install
Or manually:
Bash
نسخ
npm install --save-dev jest
npm install --save-dev babel-jest @babel/core @babel/preset-env
npm install --save-dev eslint

Project Structure
نسخ
ES6_basic/
│
├── 0-constants.js
├── 1-block-scoped.js
├── 2-arrow.js
├── 3-default-parameter.js
├── 4-rest-parameter.js
├── 5-spread-operator.js
├── 6-string-interpolation.js
├── 7-getBudgetObject.js
├── 8-getBudgetCurrentYear.js
├── 9-getFullBudget.js
├── 10-loops.js
├── 11-createEmployeesObject.js
├── 12-createReportObject.js
│
├── package.json
├── babel.config.js
├── .eslintrc.js
└── README.md

ES6 Features Used
const and let
JavaScript
نسخ
const name = 'Salman';
let age = 25;

Arrow Functions
JavaScript
نسخ
const add = (a, b) => a + b;

Default Parameters
JavaScript
نسخ
function sum(a = 0, b = 0) {
return a + b;
}

Rest Parameters
JavaScript
نسخ
function test(...args) {
return args.length;
}

Spread Syntax
JavaScript
نسخ
const arr = [...array1, ...array2];

Template Literals
JavaScript
نسخ
const message = `Hello ${name}`;

Object Property Shorthand
JavaScript
نسخ
const user = { name, age };

Computed Property Names
JavaScript
نسخ
const obj = {
[`user-${id}`]: value,
};

ES6 Method Properties
JavaScript
نسخ
const obj = {
greet() {
return 'Hello';
},
};

for...of Loop
JavaScript
نسخ
for (const value of array) {
console.log(value);
}

Running the Files
Example:
Bash
نسخ
npm run dev 0-main.js

Example Output
نسخ
I prefer const when I can. But sometimes let is okay

Author
Salman Al-Mutairi
