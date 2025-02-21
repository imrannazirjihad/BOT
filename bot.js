const express = require("express");
const app = express();
const port = process.env.PORT || 3000;

app.get("/", (req, res) => res.send("Bot is running!"));
app.listen(port, () => console.log(`Server is listening on port ${port}`));

// Add your existing bot code below
require("dotenv").config();
const TelegramBot = require("node-telegram-bot-api");
const axios = require("axios");

const TOKEN = process.env.BOT_TOKEN;
const bot = new TelegramBot(TOKEN, { polling: true });
console.log("Bot is running...");

bot.on("message", async (msg) => {
  const chatId = msg.chat.id;
  const userMessage = msg.text;

  if (userMessage.toLowerCase() === "hi") {
    bot.sendMessage(chatId, "Hello !😍");
  } else if (userMessage.startsWith("http://") || userMessage.startsWith("https://")) {
    const apiResponse = await visitUrlAndRespond(userMessage);
    bot.sendMessage(chatId, `Response:\n${apiResponse}`);
  } else {
    bot.sendMessage(chatId, "You can Chat With ME ✔");
  }
});

const visitUrlAndRespond = async (url) => {
  try {
    const response = await axios.get(url);
    let responseData = '';
    if (response.headers["content-type"].includes("application/json")) {
      responseData = JSON.stringify(response.data, null, 2);
    } else {
      responseData = response.data;
    }
    if (responseData.length > 3000) {
      responseData = responseData.substring(0, 3000) + "...";
    }
    return responseData;
  } catch (error) {
    console.error("Error fetching URL:", error);
    return "Sorry, I couldn't fetch the data at the moment.";
  }
};
