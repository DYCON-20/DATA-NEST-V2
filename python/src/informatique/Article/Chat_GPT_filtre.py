import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from setting import client
from source import Source


data = Source

instruction = "Filtre et affiche seulement les articles correspondant à ces critères : - Lié à l’informatique et à la technologie - Pas une pub (un podcast, une vidéo) - Nouveauté ou événement - Affiche les données avec cette template : User Texte Pas de lien"

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

result_filtre = str(response.choices[0].message.content)

print(result_filtre)

