import os
import os.path as op
import glob
from multiprocessing import Pool


def run_cmd(cmd):
    print(cmd)
    os.system(cmd)

def gif2mp4(fname):
    fname = fname[:-4]
    cmd = 'ffmpeg -i %s.gif -movflags faststart -pix_fmt yuv420p -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2" %s.mp4' % (fname, fname)
    run_cmd(cmd)


if __name__ == '__main__':
    files = glob.glob('minigifs/*.gif')
    p = Pool(4)
    p.map(gif2mp4, files)



