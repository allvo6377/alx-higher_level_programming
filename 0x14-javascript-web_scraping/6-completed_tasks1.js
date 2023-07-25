#!/usr/bin/node

const requests = require("requests");

function getCompletedTasks(apiUrl) {
  const response = requests.get(apiUrl);
  if (response.statusCode === 200) {
    const data = response.json();
    const completedTasks = [];
    for (const task of data) {
      if (task.completed) {
        completedTasks.push(task);
      }
    }
    return completedTasks;
  } else {
    console.log(`Error: ${response.statusCode}`);
  }
}

function getNumberOfCompletedTasksByUserId(completedTasks, userId) {
  let count = 0;
  for (const task of completedTasks) {
    if (task.userId === userId) {
      count++;
    }
  }
  return count;
}

if (require.main === module) {
  const apiUrl = "https://jsonplaceholder.typicode.com/todos";
  const completedTasks = getCompletedTasks(apiUrl);
  const userId = 1;
  const count = getNumberOfCompletedTasksByUserId(completedTasks, userId);
  console.log(`User ${userId} has ${count} completed tasks`);
}

