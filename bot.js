require("dotenv").config();
const TelegramBot = require("node-telegram-bot-api");
const axios = require("axios");

// Initialize the bot with your token
const TOKEN = process.env.BOT_TOKEN;
const bot = new TelegramBot(TOKEN, { polling: true });
console.log("Bot is running...");

// Listen for messages
bot.on("message", async (msg) => {
  const chatId = msg.chat.id;
  const userMessage = msg.text.trim();

  if (userMessage.toLowerCase() === "hi") {
    bot.sendMessage(chatId, "Send me a URL to visit.");
  } else if (userMessage.startsWith("http://") || userMessage.startsWith("https://")) {
    // If the message is a URL, visit it and respond
    const apiResponse = await visitUrlAndRespond(userMessage);
    bot.sendMessage(chatId, `Response:\n${apiResponse}`);
  } else {
    bot.sendMessage(chatId, "Please send a valid URL.");
  }
});


// Function to visit the URL and handle the response
const visitUrlAndRespond = async (url) => {
  try {
    const response = await axios.get(url); // Visit the URL

    // Check if the response is JSON (status code 200 and valid JSON)
    let responseData = '';

    if (response.headers["content-type"].includes("application/json")) {
      // Return the JSON response stringified and formatted
      responseData = JSON.stringify(response.data, null, 2);
    } else {
      // Return the raw HTML or other response
      responseData = response.data;
    }

    // Check if the response length is greater than 4096 characters
    if (responseData.length > 3000) {
      // Truncate to 4090 characters and add ellipsis
      responseData = responseData.substring(0, 3000) + "...";
    }

    return responseData; // Return the response to be sent
  } catch (error) {
    console.error("Error fetching URL:", error);
    return "Sorry, I couldn't fetch the data at the moment.";  // Fallback message
  }
};


