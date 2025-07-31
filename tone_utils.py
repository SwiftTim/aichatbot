from openai import OpenAI
import os

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY environment variable not set.")
client = OpenAI(api_key=api_key)

def generate_tone_matched_reply(message):
    prompt = f"""
    Analyze the tone, style, and formality of the following message, then respond in a matching way.

    User: {message}
    Assistant:
    """
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",

            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.8,
            max_tokens=100
        )
        reply = response.choices[0].message.content.strip()
        return reply
    except Exception as e:
        # Optionally log the exception here for
         return f"[Error: {e}]"