# AI Chatbot Tone Matcher

This project is a simple Python chatbot utility that uses the OpenAI API to generate replies that match the tone, style, and formality of a user's message.

## Features

- Uses OpenAI's GPT model to analyze and mimic the tone of user input.
- Simple function interface for integration into other Python projects.

## Requirements

- Python 3.11+
- [OpenAI Python SDK v1.x](https://github.com/openai/openai-python)

## Setup

1. **Install dependencies:**

   ```
   pip install openai
   ```

2. **Set your OpenAI API key:**

   On Windows Command Prompt:
   ```
   set OPENAI_API_KEY=sk-your-openai-key-here
   ```

   Replace `sk-your-openai-key-here` with your actual OpenAI API key.

3. **Run your bot:**

   ```
   python bot.py
   ```

## Usage

The main function is `generate_tone_matched_reply(message)` in `tone_utils.py`.  
It takes a user message as input and returns a tone-matched reply.

Example:
```python
from tone_utils import generate_tone_matched_reply

reply = generate_tone_matched_reply("Hey, what's up?")
print(reply)
```

## File Structure

- `tone_utils.py` — Contains the tone-matching reply function.
- `bot.py` — Example bot script (not shown here).

## Notes

- Make sure your OpenAI API key is kept secret.
- The model used is `gpt-3.5-turbo` by default, but you can change it in the code.

## License

MIT License 

