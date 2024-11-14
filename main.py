import os
from openai import OpenAI


OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
CONTENT_FILE_PATH = ".\\plik.txt"

client = OpenAI(
    api_key=OPENAI_API_KEY
)

with open(CONTENT_FILE_PATH, 'r', encoding='utf-8') as content_file:
    content_from_file = content_file.read()
    prompt = f"""
Transform the following text into an HTML structure that meets these guidelines:
- Use appropriate HTML tags to structure the content.
- Identify places where it would be appropriate to insert images and mark these spots using the <img> tag with the attribute src="image_placeholder.jpg". Add an alt attribute to each image with a detailed prompt that can be used to generate an image.
- Place captions below the images using the appropriate HTML tags.
- Do not add any CSS or JavaScript. The code should only contain content to be inserted between the <body> and </body> tags. Do not include <html>, <head>, or <body> tags.
- Please remember to skip any formatting addtions from generating. No html addition at top and any other additional chars. Generate only ready to use content for html file

Text to transform:
{content_from_file}
"""

completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a proffessional HTML creator. Your job is to create good tags and images to from my file."},
        {
            "role": "user",
            "content": prompt
        }
    ]
)

with open("artykul.html", 'w', encoding="utf-8") as html_file:
    html_file.write(completion.choices[0].message.content)

