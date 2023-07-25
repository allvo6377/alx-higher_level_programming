#!/usr/bin/node
const request = require('request')

const apiUrl = 'https://jsonplaceholder.typicode.com/todos'

request(apiUrl, (error, response, body) => {
  const todos = JSON.parse(body)

  const completedByUser = {}

  todos.forEach(todo => {
    if (todo.completed) {
      const userId = todo.userId
      if (completedByUser[userId]) {
        completedByUser[userId]++
      } else {
        completedByUser[userId] = 1
      } 
    }
  })

  Object.keys(completedByUser).forEach(userId => {
    console.log(`User ${userId} completed ${completedByUser[userId]} tasks`)
  })
})
