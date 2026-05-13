ES6 Promises
This project focuses on asynchronous programming in modern JavaScript using ES6 Promises and async features.
The goal of this project is to understand how asynchronous operations work in JavaScript and how to properly handle success, failure, multiple promises, and errors.

Learning Objectives
By the end of this project, you should be able to explain:
•
What a Promise is
•
Why Promises are useful
•
Promise states:
•
pending
•
fulfilled
•
rejected
•
How to use:
•
then
•
catch
•
finally
•
How to use:
•
Promise.resolve
•
Promise.reject
•
Promise.all
•
Promise.allSettled
•
Promise.race
•
How error handling works using:
•
throw
•
try
•
catch
•
finally
•
How asynchronous JavaScript works
•
How to use async and await

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
All code must pass ESLint validation
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
npm install --save-dev babel-jest @babel/core @babel/preset-env @babel/cli
npm install --save-dev eslint

Project Structure
نسخ
ES6_promise/
│
├── 0-promise.js
├── 1-promise.js
├── 2-then.js
├── 3-all.js
├── 4-user-promise.js
├── 5-photo-reject.js
├── 6-final-user.js
├── 7-load_balancer.js
├── 8-try.js
├── 9-try.js
│
├── utils.js
├── package.json
├── babel.config.js
├── .eslintrc.js
└── README.md

Core Concepts
Promise
A Promise represents a future result of an asynchronous operation.
JavaScript
نسخ
const promise = new Promise((resolve, reject) => {
resolve('Success');
});

Promise States
State
Meaning
pending
Waiting
fulfilled
Success
rejected
Failed
نسخ الجدول

then / catch / finally
JavaScript
نسخ
promise
.then((result) => console.log(result))
.catch((error) => console.log(error))
.finally(() => console.log('Done'));

Promise.resolve
Creates a resolved promise.
JavaScript
نسخ
Promise.resolve('Success');

Promise.reject
Creates a rejected promise.
JavaScript
نسخ
Promise.reject(new Error('Failed'));

Promise.all
Waits for all promises.
JavaScript
نسخ
Promise.all([promise1, promise2]);

Promise.allSettled
Returns all results even if some fail.
JavaScript
نسخ
Promise.allSettled([promise1, promise2]);

Promise.race
Returns the first completed promise.
JavaScript
نسخ
Promise.race([promise1, promise2]);

Error Handling
Throwing Errors
JavaScript
نسخ
throw new Error('Something went wrong');

Try / Catch / Finally
JavaScript
نسخ
try {
riskyFunction();
} catch (error) {
console.log(error);
} finally {
console.log('Cleanup');
}

Example
JavaScript
نسخ
divideFunction(10, 2);
// 5
JavaScript
نسخ
divideFunction(10, 0);
// Error: cannot divide by 0

Running Tests
Run a specific file:
Bash
نسخ
npm run dev 0-main.js
Run all tests:
Bash
نسخ
npm test
Run full validation:
Bash
نسخ
npm run full-test

Notes
•
Promises are the foundation of modern JavaScript asynchronous programming.
•
Most APIs, databases, file systems, and network operations in Node.js use Promises.
•
Async/await is built on top of Promises.

Author
Salman Al-Mutairi
