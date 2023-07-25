#!/usr/bin/node

// Import the request module
const request = require('request');

// Define the API URL as the first argument
const apiUrl = process.argv[2];

// Define a function that takes a response body and prints the number of tasks completed by user id
function printCompletedTasks(body) {
  // Parse the body as a JSON array
  const todos = JSON.parse(body);

  // Create an empty object to store the counts
  const counts = {};

  // Loop through each todo item
  for (const todo of todos) {
    // Get the user id and the completed status
    const userId = todo.userId;
    const completed = todo.completed;

    // If the user id is not in the counts object, initialize it to zero
    if (!counts[userId]) {
      counts[userId] = 0;
    }

    // If the completed status is true, increment the count by one
    if (completed) {
      counts[userId]++;
    }
  }

  // Loop through the counts object and print only the users with completed tasks
  for (const userId in counts) {
    // Get the count for the user id
    const count = counts[userId];

    // If the count is greater than zero, print the user id and the count
    if (count > 0) {
      console.log(`User ${userId} has completed ${count} tasks`);
    }
  }
}

// Make a GET request to the API URL and pass the printCompletedTasks function as a callback
request(apiUrl, (error, response, body) => {
  // If there is no error and the status code is 200, call the printCompletedTasks function with the body
  if (!error && response.statusCode === 200) {
    printCompletedTasks(body);
  } else {
    // Otherwise, print the error or the status code
    console.error(error || response.statusCode);
  }
});

