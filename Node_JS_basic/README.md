# Node.js Basics

This project introduces the fundamentals of backend development using Node.js and Express.js.

The goal of this project is to understand how JavaScript can run outside the browser, interact with the file system, process user input, and create HTTP servers.

---

# Learning Objectives

By the end of this project, you should be able to explain:

- How to run JavaScript using Node.js
- How Node.js modules work
- The difference between CommonJS and ES6 modules
- How to use the `fs` module to read files
- How to use `process`
- How to access command line arguments
- How to use standard input/output streams
- How to create an HTTP server using Node.js
- How to create an HTTP server using Express
- How routing works in Express
- How to organize backend applications using controllers and routes
- How asynchronous I/O works in Node.js
- The difference between synchronous and asynchronous operations
- How MVC-like backend architecture works

---

# Requirements

- Ubuntu 20.04 LTS
- Node.js 20.x.x
- npm 9.x.x or higher
- All files must end with a new line
- All code must pass ESLint validation
- Tests are executed using Jest

---

# Setup

## Install Node.js

```bash id="f4n8qp"
curl -sL https://deb.nodesource.com/setup_20.x -o nodesource_setup.sh
sudo bash nodesource_setup.sh
sudo apt install nodejs -y
```

Check installation:

```bash id="r7m2vx"
node -v
npm -v
```

---

# Install Dependencies

```bash id="u9k5qa"
npm install
```

---

# Important Packages

| Package    | Purpose             |
| ---------- | ------------------- |
| express    | HTTP framework      |
| nodemon    | Auto-restart server |
| babel-node | ES6 support         |
| jest       | Testing             |
| eslint     | Linting             |

---

# Project Structure

```text id="y6v1we"
Node_JS_basic/
│
├── 0-console.js
├── 1-stdin.js
├── 2-read_file.js
├── 3-read_file_async.js
├── 4-http.js
├── 5-http.js
├── 6-http_express.js
├── 7-http_express.js
│
├── full_server/
│   ├── controllers/
│   │   ├── AppController.js
│   │   └── StudentsController.js
│   │
│   ├── routes/
│   │   └── index.js
│   │
│   ├── utils.js
│   └── server.js
│
├── database.csv
├── package.json
├── babel.config.js
├── .eslintrc.js
└── README.md
```

---

# CommonJS vs ES6 Modules

## CommonJS

```js id="m3q8ze"
const fs = require("fs");

module.exports = myFunction;
```

---

# ES6 Modules

```js id="n7v2wr"
import fs from "fs";

export default myFunction;
```

---

# File System

Using Node.js `fs` module:

```js id="h2x9pa"
const fs = require("fs");
```

---

# Synchronous Read

```js id="p5m4ke"
fs.readFileSync(path, "utf8");
```

Blocks execution until reading finishes.

---

# Asynchronous Read

```js id="k8n1vx"
fs.readFile(path, "utf8", callback);
```

Non-blocking operation.

---

# Process Object

## Command line arguments

```js id="w1q7re"
process.argv;
```

---

# Standard Input

```js id="c6m3pa"
process.stdin;
```

---

# Standard Output

```js id="s9x2we"
process.stdout;
```

---

# Basic HTTP Server

Using built-in `http` module:

```js id="t4k8vn"
const http = require("http");

const server = http.createServer((req, res) => {
  res.end("Hello");
});
```

---

# Express Server

Using Express:

```js id="b7q5mx"
const express = require("express");

const app = express();

app.get("/", (req, res) => {
  res.send("Hello");
});
```

---

# Express Routing

```js id="e1m9qa"
app.get("/students", controllerMethod);
```

Routes connect URLs to controller logic.

---

# MVC-like Architecture

This project introduces a layered backend structure:

```text id="d5x4wr"
Server
   ↓
Routes
   ↓
Controllers
   ↓
Utilities / Services
```

---

# Controllers

Controllers contain application logic.

Example:

```js id="j9n2vp"
class AppController {
  static getHomepage(req, res) {
    res.send("Hello Holberton School!");
  }
}
```

---

# Routes

Routes map URLs to controllers.

```js id="g3m7ke"
router.get("/", AppController.getHomepage);
```

---

# Utilities

Reusable helper logic such as database reading.

---

# Running the Project

## Run a single file

```bash id="x4v1pa"
node 4-http.js
```

---

# Run Express Server

```bash id="q7k8wr"
npm run dev
```

---

# Test Endpoints

```bash id="u5n2mx"
curl localhost:1245
```

```bash id="p8x4qa"
curl localhost:1245/students
```

---

# CSV Database Example

```csv id="m1v9re"
firstname,lastname,age,field
Johann,Kerbrou,30,CS
Guillaume,Salou,30,SWE
```

---

# Key Concepts Learned

- Event-driven programming
- Non-blocking I/O
- HTTP fundamentals
- REST-style routing
- Backend architecture organization
- Separation of concerns
- Express middleware flow

---

# Author

Salman Al-Mutairi
