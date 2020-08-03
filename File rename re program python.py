from os import path
import re
import glob
import sys
import shutil
basedir='C:\\Users\\shash\\Videos\\Anime Videos series\\Anime\\Detective Conan'

for file in os.listdir(basedir):
    print(file)
#prints all the file and folder names

os.rename(os.path.join(basedir,'951-480p.mp4'), os.path.join(basedir,'951.mp4'))
# renames the file 951-480p.mp4 to 951.mp4

pattern= r"^(\d*)-480p(.*)\.mp4$"
sub_name = re.compile(pattern, flags=re.I).sub
for old_path in glob.glob(os.path.join(basedir, "*\.mp4$")):
    dirname, old_name = os.path.split(old_path)
    new_name = sub_name("\\1\\2.mp4", old_name)
    new_path = os.path.join(dirname, new_name)
    os.rename(old_path, new_path)

#removes -480p from the file name in the directory



#130-the stadium indiscriminate threatening case + ending.mp4
189 Ran suspects Shinichi Conan Desperate Revival Haibara Agasa Heiji convince Conan ❤️❤️❤️❤️.mp4
190-360.mp4
191-360.mp4
207.mp4
208.mp4
209.mp4
212.mp4
217.mp4
219.mp4
220.mp4
226 star.mp4
240.mp4
246 star.mp4
253 star.mp4
.
.
931-480p.mp4
935-480p.mp4
936-480p.mp4
937-480p.mp4
938-480p.mp4
939 filler fossil.mp4
940-480p.mp4
941-480p.mp4
942-480p❤️ CARASUMA RENYA reveal.mp4
943.mp4
944-480p.mp4
948-480p filler.mp4
949-480pretty good filler.mp4
950-480p filler.mp4
951-480p.mp4
#
