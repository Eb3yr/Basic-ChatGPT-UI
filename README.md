# Basic-ChatGPT-UI
A simple UI that lets you interact with any OpenAI chat model.

You can edit any user message and assistant response, as well as set a system message that is inserted to the start of the conversation (though this system message is usually ignored in the gpt-3.5-turbo model).

Each message is preceded by "user: ", "assistant: " or "system: " and these are used to split the contents of the text box into each message. This is case-sensitive and the space following the colon is required. The program won't break if the number of user messages and assistant responses are out of sync, but you should probably try to maintain this. The system message isn't split, only read starting from the 9th character onwards, so it doesn't support sending multiple system messages.

Pressing send multiple times before the previous one has finished will work, but I wouldn't recommend it.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

REQUIREMENTS:

-Your own API key should be set manually on line 5 of the UI.py file.

-You will need the openai library installed. You can do this with "pip install openai" in cmd. 
