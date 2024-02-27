from setting import client
from Chat_GPT_Video_filtre import article_1 , article_2 ,article_3 ,article_4 , article_5


data1 = article_1
data2 = article_2
data3 = article_3
data4 = article_4
data5 = article_5

instruction = """crée 1 mot clée tres generique en anglais  liée a cette article """


response = client.chat.completions.create(model="gpt-3.5-turbo", # Specify the model
messages=[
      {"role": "system", "content": instruction },
      {"role": "user", "content": data1}
  ],
    temperature=0,
    top_p=0,
    frequency_penalty=0,
    presence_penalty=0.0
  )

mots_clée_1 = str(response.choices[0].message.content)

response = client.chat.completions.create(model="gpt-3.5-turbo", # Specify the model
messages=[
      {"role": "system", "content": instruction },
      {"role": "user", "content": data2}
  ],
    temperature=0,
    top_p=0,
    frequency_penalty=0,
    presence_penalty=0.0
  )

mots_clée_2 = str(response.choices[0].message.content)


response = client.chat.completions.create(model="gpt-3.5-turbo", # Specify the model
messages=[
      {"role": "system", "content": instruction },
      {"role": "user", "content": data3}
  ],
    temperature=0,
    top_p=0,
    frequency_penalty=0,
    presence_penalty=0.0
  )

mots_clée_3 = str(response.choices[0].message.content)

response = client.chat.completions.create(model="gpt-3.5-turbo", # Specify the model
messages=[
      {"role": "system", "content": instruction },
      {"role": "user", "content": data4}
  ],
    temperature=0,
    top_p=0,
    frequency_penalty=0,
    presence_penalty=0.0
  )

mots_clée_4 = str(response.choices[0].message.content)

response = client.chat.completions.create(model="gpt-3.5-turbo", # Specify the model
messages=[
      {"role": "system", "content": instruction },
      {"role": "user", "content": data5}
  ],
    temperature=0,
    top_p=0,
    frequency_penalty=0,
    presence_penalty=0.0
  )

mots_clée_5 = str(response.choices[0].message.content)




print(mots_clée_1)
print(mots_clée_2)
print(mots_clée_3)
print(mots_clée_4)
print(mots_clée_5)


