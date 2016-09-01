import logging

import djcelery
import subprocess

from django.utils import log
from djcelery.app import app

from .models import Video

logger = logging.getLogger(__name__)  # assuming you have set up logging elsewhere


@app.task
def convert_video(video_id):
    video = Video.objects.filter(id=2).get()
    pathConverted = 'C:\\Users\\diego\\Documents\\GitHub\\convertido.mp4'
    cmd = ['ffmpeg', '-i ', video.original_video.path, ' -b 1500k -vcodec libx264 -g 30', pathConverted]
    print('Ejecutando... ', ' '.join(cmd))

    # proc = subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    try:
        proc = subprocess.run(cmd, stdout=subprocess.PIPE)
        proc.subprocess.wait()
    except subprocess.CalledProcessError as e:
        raise RuntimeError("command '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))

    print("Esta convertido? " + video.converted)

    if proc.returncode != 0:
        print('Falló algo en command failed with ret val %s', proc.returncode)
        print(proc.stderr)
        print(proc.stdout)
    else:
        video.converted = True
        video.save()
        print.info('Video convertido ok')
