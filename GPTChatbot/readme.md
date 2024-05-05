# OpenAI ChatGPT Chatbot with API

* To use this Chatbot you must have chatgpt API, and some funds deposited to your chatgpt account to spend. https://platform.openai.com/
* In project directory commands were run: 
npm init -y
npm install express openai
* Create file config.js in project directory and add your chatGPT API: 
module.exports = {
    OpenAIAPIKey: 'XXXXXXXXXXXXXXXXXXXXXXXXX'
};
* Start project with: node server.js
* Check on http://localhost:3000/
* Without funds deposited, every answer returns: "Sorry, I couldn't understand that." message: 'You exceeded your current quota, please check your plan and billing details. For more information on this error, read the docs: https://platform.openai.com/docs/guides/error-codes/api-errors.', type: 'insufficient_quota'..