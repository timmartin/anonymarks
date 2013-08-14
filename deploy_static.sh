#!/bin/bash

set -e

python manage.py collectstatic -c --noinput

rsync -r --delete static_tmp/* timm_anonymarksstatic@ssh.phx.nearlyfreespeech.net:/home/public/
