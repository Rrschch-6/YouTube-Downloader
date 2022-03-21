import pytube
import os
loc='C:/Users/Sasha/Documents/11-SRH Heidelberg/Big Data Programming Project/Practice/Downloads'
url='https://youtu.be/KGPn0KAEHrI'
youtube = pytube.YouTube(url)
video_list=youtube.streams.all()
for i in range(len(video_list)):
    print(i,".",video_list[i])

choice=int(input("Enter Stream Number:"))
out_file=video_list[choice].download(loc)

#for converting Audio to MP3
base, ext = os.path.splitext(out_file)
new_file = base + '.mp3'
os.rename(out_file, new_file)
print("Done")