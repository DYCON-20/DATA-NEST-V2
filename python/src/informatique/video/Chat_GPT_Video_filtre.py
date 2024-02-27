from local import client
from Thread.Thread_recup import threads_resultat_str


data = threads_resultat_str

instruction = '''Filtre et affiche seulement 5 articles pour une veille informatique 
la reponse doit ètre scruture comme :


articles 1 

articles 2 

articles 3 

articles 4 

articles 5 

''' 

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

result_filtre_filme = str(response.choices[0].message.content)

#print(result_filtre_filme)

delimiter = "\n\n"  # Update this based on the actual response format
articles = result_filtre_filme.strip().split(delimiter)

if len(articles) >= 5:
    # Assuming the first split part might not be an article
    article_1 = articles[0]
    article_2 = articles[1]
    article_3 = articles[2]
    article_4 = articles[3]
    article_5 = articles[4]

    # Print articles to verify
else:
    print("Not enough articles found. Found only:", len(articles) - 1)  # Adjusting count for potential empty first element