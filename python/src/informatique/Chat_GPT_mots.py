from local import client
from Chat_GPT_Article import result_article


data = result_article

instruction = """crée 3 mot clée tres generique en anglais  liée a cette article séparer par des virgule 

"""


response = client.chat.completions.create(model="gpt-3.5-turbo", # Specify the model
messages=[
      {"role": "system", "content": instruction },
      {"role": "user", "content": data}
  ],
    temperature=0,
    top_p=0,
    frequency_penalty=0,
    presence_penalty=0.0
  )

mots_clée = str(response.choices[0].message.content)

print(mots_clée)


