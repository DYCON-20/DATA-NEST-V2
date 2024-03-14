import discord
import asyncio

from discord.ext import commands, tasks
from discord.ext import commands
from discord.ui import Button, View
from datetime import time
from setting import connect_db  
from datetime import datetime, timedelta

from setting import Theme
from video.setup_video import  setup

from video.setup_video import  setup
from Thread.Thread import recuperation 
from Article.Chat_GPT_filtre import generer_filtre_veille 
from Article.Chat_GPT_Article import generer_article_veille 
from video.Chat_GPT_Video_mot import  création_mot_video
from video.Chat_GPT_Video_Script import creation_script_video 

from video.Recuperation_Video import  recuperation_videos


from video.Voice_script import  voice_videos

from video.Montage_Video_1 import  ajustement_rush
from video.Montage_Video_2 import  assamblage_rush
from video.Montage_Video_3 import  crated_subtitle
from video.Montage_Video_4 import  assamblage_sous_titre_rush


# Créez le bot
bot = commands.Bot(command_prefix='!')
MODE_DEV = True





# Exécutez cette fonction lorsque le bot est prêt
# Définissez une vue contenant plusieurs boutons
class MultipleScriptButtonView(View):
    def __init__(self, channel):
        super().__init__(timeout=None)  # Timeout=None pour que la vue reste active indéfiniment
        self.channel = channel
        self.script4_button_clicked = False  # Initialise l'état de clic du bouton 4 à False
        self.wait_and_execute = asyncio.create_task(self.wait_then_execute_script4())

    @discord.ui.button(label="Régénérer le thread", style=discord.ButtonStyle.blurple)
    async def script1_button_callback(self, button, interaction):
        # Action pour le premier bouton
        await self.channel.send("Régénérer le thread")
        button.disabled = True
        await interaction.response.edit_message(view=self)
        
    @discord.ui.button(label="Régénérer la vidéo", style=discord.ButtonStyle.blurple)
    async def script2_button_callback(self, button, interaction):
        # Action pour le second bouton
        await self.channel.send("Le script 2 a été exécuté.")
        button.disabled = True
        await interaction.response.edit_message(view=self)

    @discord.ui.button(label="Régénérer la vidéo", style=discord.ButtonStyle.blurple, custom_id="script3_button")
    async def script3_button_callback(self, button, interaction):
        # Action pour le troisième bouton
        await self.channel.send("Le script 3 a été exécuté.")
        button.disabled = True
        await interaction.response.edit_message(view=self)

    @discord.ui.button(label="Valider l'envoie", style=discord.ButtonStyle.red, custom_id="script4_button")
    async def script4_button_callback(self, button, interaction):
        self.script4_button_clicked = True
        # Votre logique ici
        self.message = interaction.message  # Stocke une référence au message
        # Le reste de votre logique


    async def wait_then_execute_script4(self):
        await asyncio.sleep(5)  # Remplacez 5 par 3600 pour une heure
        if not self.script4_button_clicked:
            # Exécute le script ici si le bouton n'a pas été cliqué
            await self.channel.send("Le script 4 a été exécuté automatiquement après 1 heure.")
            for item in self.children:
                if item.custom_id == "script4_button":
                    item.disabled = True
            # Met à jour le message pour refléter l'état désactivé du bouton
            if hasattr(self, 'message'):
                await self.message.edit(view=self)

    

@bot.event
async def on_ready():
    print(f'{bot.user.name} a démarré avec succès.')

    if MODE_DEV:
        # Si en mode développement, exécutez immédiatement
        bot.loop.create_task(envoyer_message())
    else:
        # Sinon, planifiez l'exécution à 8h chaque jour
        envoyer_message.start()



# Une tâche planifiée pour envoyer un message à 8h chaque jour
@tasks.loop(time=time(hour=8))
async def envoyer_message():
    channel_id = '1215410000009240647'  # Remplacez par l'ID du canal où envoyer le message
    channel = bot.get_channel(int(channel_id))
    datetime_Monitoring = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')

    #
    await bot.loop.run_in_executor(None, setup)
    await channel.send("{datetime_Monitoring} Le script `setup` a terminé son exécution.")
    #

    #
    await bot.loop.run_in_executor(None, recuperation)
    await channel.send("{datetime_Monitoring} Le script `recuperation` a terminé son exécution.")
    #

    #
    await bot.loop.run_in_executor(None, generer_filtre_veille)
    await channel.send("{datetime_Monitoring} Le script `generer_filtre_veille` a terminé son exécution.")
    #
    #
    await bot.loop.run_in_executor(None, generer_article_veille)
    await channel.send("{datetime_Monitoring} Le script `generer_article_veille` a terminé son exécution.")
    #
   
    #
    await bot.loop.run_in_executor(None, création_mot_video)
    await channel.send("{datetime_Monitoring} Le script `création_mot_video` a terminé son exécution.")
    #
    
    #
    await bot.loop.run_in_executor(None, creation_script_video)
    await channel.send("{datetime_Monitoring} Le script `creation_script_video` a terminé son exécution.")
    #     

    #
    await bot.loop.run_in_executor(None, recuperation_videos)
    await channel.send("{datetime_Monitoring} Le script `recuperation_videos` a terminé son exécution.")
    #    
    #
    await bot.loop.run_in_executor(None, voice_videos)
    await channel.send("{datetime_Monitoring} Le script `voice_videos` a terminé son exécution.")
    #      
    #
    await bot.loop.run_in_executor(None, ajustement_rush)
    await channel.send("{datetime_Monitoring} Le script `ajustement_rush` a terminé son exécution.")
    #     
    #
    await bot.loop.run_in_executor(None, assamblage_rush)
    await channel.send("{datetime_Monitoring} Le script `assamblage_rush` a terminé son exécution.")
    #    
    #
    await bot.loop.run_in_executor(None, crated_subtitle)
    await channel.send("{datetime_Monitoring} Le script `crated_subtitle` a terminé son exécution.")
    #
    #
    await bot.loop.run_in_executor(None, assamblage_sous_titre_rush)
    await channel.send("{datetime_Monitoring} Le script  `assamblage_sous_titre_rush` a terminé son exécution.")
    #          

    conn = connect_db()
    c = conn.cursor()
    
    datetime_Monitoring = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
    c.execute('SELECT Article_resultat FROM Article_final WHERE date = %s', (datetime_Monitoring,))
    resultat = c.fetchone()
    c.close()
    conn.close()   

    MESSAGE = resultat[0]
    Apart1 = MESSAGE[:2000]
    Apart2 = MESSAGE[2000:]
    await channel.send(Apart1)
    await channel.send(Apart2)

    # Envoi de la vidéo
    VIDEO_PATH = f"./python/data/Monitoring/{Theme}/{Theme}_monitoring_{datetime_Monitoring}/{datetime_Monitoring}_{Theme}_monitoring_.mp4"
    await channel.send(file=discord.File(VIDEO_PATH))

    view = MultipleScriptButtonView(channel)
    await channel.send("Cliquez sur un des boutons pour exécuter un script.", view=view)
