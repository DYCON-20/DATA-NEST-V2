#rejouter fonction nom+date
#rajouter supresion rush 


from moviepy.editor import VideoFileClip, concatenate_videoclips

clip1 = VideoFileClip("python/src/informatique/Video_traitement/video_informatique_1.mp4")
clip2 = VideoFileClip("python/src/informatique/Video_traitement/video_informatique_2.mp4")


clip_final = concatenate_videoclips([clip1, clip2])


clip_final.write_videofile("python/src/informatique/Video_final/video_informatique.mp4")
