import os
import glob
import shutil


dest1 = 'M:\\Programme\\Steamx64\\Default\\pics'
dest2 = 'M:\\Programme\\Steamx64\\Default\\jan'
dest3 = 'C:\\Users\\ukki\\Downloads\\pdf_files'
dest4 = 'C:\\Users\\ukki\\Downloads\\exe_files'

pics = ['jpg', 'jpeg', 'bmp', 'gif', 'png']
vids = ['webm', 'mpg', 'mp2', 'mpeg', 'mpe', 'mpv', 'ogg', 'mp4', 'm4p', 'm4v', 'flv']
exe = ['exe', 'xx']
pdf = ['pdf', 'xx']

def find_files(args):
    filelist = []
    all_files = glob.glob('C:\\Users\\ukki\\Downloads\\*')
    for file in all_files:
        for match in args:
            if file.endswith(match):
                filelist.append(file)
    return filelist


def move_files(here, there):
    for file in here:
        dest = file.replace('C:\\Users\\ukki\\Downloads', there)
        count = 0
        while os.path.exists(dest):
            replace = [n for n in range(9)]
            dest = dest.replace('.', '{}.'.format(replace[count]))
            count = count+1
        shutil.move(file, dest)
        print(dest.replace(there, ''))


pictures_list = find_files(pics)
move_files(pictures_list, dest1)
vid_list = find_files(vids)
move_files(vid_list, dest2)

pdf_files = find_files(pdf)
move_files(pdf_files, dest3)

exe_files = find_files(exe)
move_files(exe_files, dest4)
