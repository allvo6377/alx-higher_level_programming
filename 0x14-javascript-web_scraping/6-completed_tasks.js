#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];

request(apiUrl, (err, res, body) => {
  if (err) {
    console.error(err);
  } else {
    const todos = JSON.parse(body);
    const completedTasks = {};

    for (const todo of todos) {
      if (todo.completed) {
        if (completedTasks.hasOwnProperty(todo.userId)) {
          completedTasks[todo.userId] += 1;
        } else {
          completedTasks[todo.userId] = 1;
        }
      }
    }

    for (const userId in completedTasks) {
      console.log(`User ${userId} completed ${completedTasks[userId]} tasks`);
    }
  }
});

