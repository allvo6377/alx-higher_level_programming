#!/usr/bin/node
const request = require('request');
const api_url = 'https://jsonplaceholder.typicode.com/todos';

request(api_url, function (error, response, body) {
    if (!error && response.statusCode == 200) {
        const data = JSON.parse(body);
        let completedTasks = {};
        data.forEach(task => {
            if (task.completed) {
                if (completedTasks[task.userId]) {
                    completedTasks[task.userId] += 1;
                } else {
                    completedTasks[task.userId] = 1;
                }
            }
        });
        for (let userId in completedTasks) {
            console.log(`User ${userId} completed ${completedTasks[userId]} tasks`);
        }
    }
});
