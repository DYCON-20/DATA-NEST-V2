from local import client
from Chat_GPT_filtre import result_filtre


data = result_filtre

instruction = """
Bonjour je m’appelle dycon est tu es programme qui récupère des textes et tu dois les analyser et créer un résumé dans un article de veille informatique 

Pour créer l’article suis cette template

(Utilise Pas de lien)

☕️ Hello There, Bienvenue sur m’a veille technologique voici différentes info sur ce qui c’est passé hier 

[Emoji avec un lien de l’article] Resumé de l’article 

🔗 Sources :
[Inclure ici la liste complète des nom  source]

🗣️ Votre Avis  Qu’en pensez-vous ? 

📱N'hésitez pas à partager vos propres découvertes ou à poser des questions. La veille technologique est un voyage collectif!

#VeilleInformatique #Technologie #Innovation #SécuritéInformatique #AI #ML
[Insérer plusieurs hashtag lié au sujet]
Restez connectés pour plus d'informations demain!
"""


response = client.chat.completions.create(model="gpt-4", # Specify the model
messages=[
      {"role": "system", "content": instruction },
      {"role": "user", "content": data}
  ],
    temperature=0,
    top_p=0,
    frequency_penalty=0,
    presence_penalty=0.0
  )

result_article = str(response.choices[0].message.content)

print(result_article)