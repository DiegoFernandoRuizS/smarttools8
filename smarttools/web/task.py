import logging

import djcelery
import subprocess

from django.utils import log
from djcelery.app import app

from .models import Video

logger = logging.getLogger(__name__)  # assuming you have set up logging elsewhere


@app.task
def convert_video(video_id):
    video = Video.objects.get(video_id)
    print("Llego al proceso background....")
    print(video.name)
    cmd = ['ffmpeg',  '-i', video.original_video.path, video.convertido.path]
    log.info('Ejecutando... %s', ' '.join(cmd))
    proc = subprocess.Popen(cmd)
    proc.subprocess.wait()

    if proc.returncode != 0:
        log.error('Falló algo en command failed with ret val %s', proc.returncode)
        log.info(proc.stderr)
        log.info(proc.stdout)
    else:
        video.converted = True
        video.save()
        log.info('Video convertido ok')