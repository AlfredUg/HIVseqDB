#!/bin/sh

until cd /app/hivseqdb
do
    echo "Waiting for server volume..."
done

# run a worker :)
celery -A hivseqdb worker --loglevel=info --concurrency 1 -E