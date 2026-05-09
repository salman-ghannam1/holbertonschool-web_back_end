ES6 Classes
This project focuses on Object-Oriented Programming (OOP) concepts in modern JavaScript using ES6 Classes.
The goal of this project is to understand how classes, inheritance, getters/setters, static methods, symbols, and metaprogramming work in JavaScript.

Learning Objectives
By the end of this project, you should be able to explain:
•
How to define a class
•
How to create objects from a class
•
How constructors work
•
How to add methods to a class
•
How getters and setters work
•
How static methods work
•
How inheritance works using extends
•
How to override methods
•
What abstract class behavior means in JavaScript
•
How Symbols work in ES6
•
How metaprogramming works in JavaScript

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
Code should pass ESLint validation
•
Tests are executed using Jest

Setup
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
ES6_classes/
│
├── 0-classroom.js
├── 1-make_classrooms.js
├── 2-hbtn_course.js
├── 3-currency.js
├── 4-pricing.js
├── 5-building.js
├── 6-sky_high.js
├── 7-airport.js
├── 8-hbtn_class.js
├── 9-hoisting.js
├── 10-car.js
│
├── package.json
├── babel.config.js
├── .eslintrc.js
└── README.md

Main Concepts
Classes
JavaScript
نسخ
class Person {
constructor(name) {
this.\_name = name;
}
}

Getters and Setters
JavaScript
نسخ
get name() {
return this.\_name;
}

set name(value) {
this.\_name = value;
}

Inheritance
JavaScript
نسخ
class Dog extends Animal {
}

Static Methods
JavaScript
نسخ
class MathHelper {
static add(a, b) {
return a + b;
}
}
Usage:
JavaScript
نسخ
MathHelper.add(1, 2);

Method Overriding
JavaScript
نسخ
class Animal {
speak() {
return 'sound';
}
}

class Dog extends Animal {
speak() {
return 'bark';
}
}

Symbols
JavaScript provides built-in Symbols used internally by the language.
Examples:
Symbol
Purpose
Symbol.iterator
Custom iteration
Symbol.toPrimitive
Object conversion
Symbol.toStringTag
Object description
Symbol.species
Object cloning
نسخ الجدول

Metaprogramming
Metaprogramming allows developers to customize how objects behave internally.
Example:
JavaScript
نسخ
[Symbol.toPrimitive](hint) {
return this.\_value;
}

Running Tests
Run a specific file:
Bash
نسخ
npm run dev 0-main.js
Run all tests:
Bash
نسخ
npm test
Run full project validation:
Bash
نسخ
npm run full-test

Example Output
نسخ
[
'Guillaume Salva - 2020 - San Francisco',
'John Doe - 2020 - San Francisco'
]

Author
Salman Al-Mutairi
