import os
import sys

path = str(sys.argv[1])
print("Folder file Path {0}".format(path))

for filename in os.listdir(path):
    input_path = os.path.join(path,filename)
    output_name = filename[:-4]
    output_path = os.path.join(path,output_name)

    if filename.endswith(".mp4"):
        #print("ffmpeg -i {0} -c:v prores_ks -profile:v -1 -c:a pcm_s32le {1}.mov".format(input_path, output_name))
        os.system("ffmpeg -i {0} -c:v prores_ks -profile:v -1 -c:a pcm_s32le {1}.mov".format(input_path, output_path))
        print(filename)
    else:
        continue

print("complete.")
    