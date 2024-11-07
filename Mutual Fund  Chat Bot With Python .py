#!/usr/bin/env python
# coding: utf-8

# Creating a mutual fund-oriented chatbot in Python requires a combination of natural language processing (NLP) techniques, a well-structured handling of mutual fund related queries, and possibly integration with a financial data API for real-time information. Below is a simplified version that utilizes basic Python structure and logic. This chatbot will be able to handle a few common user queries regarding mutual funds.

# In[ ]:


import random

class MutualFundChatBot:
    def __init__(self):
        self.greetings = ["Hello! How can I assist you today?", "Hi there! What do you want to know about mutual funds?", "Greetings! I'm here to help you with mutual fund queries."]
        self.fund_types = ["Equity Fund", "Debt Fund", "Hybrid Fund", "Index Fund", "Sector Fund"]
        self.questions = {
            "What are mutual funds?": "Mutual funds are investment vehicles that pool money from many investors to purchase securities like stocks and bonds.",
            "What types of mutual funds are there?": f"The common types of mutual funds are: {', '.join(self.fund_types)}.",
            "How to invest in mutual funds?": "You can invest in mutual funds through a financial advisor, directly through the fund house, or through online platforms."
        }
        self.farewells = ["Thank you for chatting! Have a great day!", "Goodbye! Hope I helped you with your queries.", "See you next time!"]

    def greet(self):
        return random.choice(self.greetings)

    def farewell(self):
        return random.choice(self.farewells)

    def handle_query(self, query):
        query = query.strip().capitalize()
        return self.questions.get(query, "I'm sorry, I don't have information on that. Can you ask something else?")

    def chat(self):
        print(self.greet())
        while True:
            user_input = input("You: ")
            if user_input.lower() in ("exit", "quit"):
                print(self.farewell())
                break
            response = self.handle_query(user_input)
            print(f"Bot: {response}")

if __name__ == "__main__":
    bot = MutualFundChatBot()
    bot.chat()


# # How the Chatbot Works:
# Initialization:
# 
# The bot initializes with predefined greetings, a list of mutual fund types, a dictionary of common questions and responses, and farewells.
# Greeting and Farewells:
# 
# The bot greets the user upon starting. It will respond with a random greeting each time. Similarly, it says farewell with a random message when the user decides to exit.
# Handling Queries:
# 
# The bot listens for user input and responds to predefined questions. For any query that isn’t recognized, it provides a fallback message.
# Possible Outputs:
# User Input: "What are mutual funds?"
# 
# Bot Response: "Mutual funds are investment vehicles that pool money from many investors to purchase securities like stocks and bonds."
# User Input: "What types of mutual funds are there?"
# 
# Bot Response: "The common types of mutual funds are: Equity Fund, Debt Fund, Hybrid Fund, Index Fund, Sector Fund."
# User Input: "How to invest in mutual funds?"
# 
# Bot Response: "You can invest in mutual funds through a financial advisor, directly through the fund house, or through online platforms."
# User Input: "Tell me about SIP."
# 
# Bot Response: "I'm sorry, I don't have information on that. Can you ask something else?"
# User Input: "exit"
# 
# Bot Response: "Goodbye! Hope I helped you with your queries."
# Future Improvements:
# Natural Language Processing: To understand more varied queries.
# Integration with Financial APIs: For real-time data on mutual funds, NAVs, etc.
# User Profiles: To provide personalized recommendations based on user preferences.
# Logging and Analytics: To analyze user interactions for better performance and training.
# This basic framework can be expanded and improved based on specific user needs and capabilities required for a full mutual fund chatbot

# In[ ]:




