import urllib
from urllib.parse import quote

from celery import Celery
from kombu import Queue, Exchange

AWS_SECRET_ACCESS_KEY = "AWS_SECRET_ACCESS_KEY"
AWS_ACCESS_KEY_ID = "AWS_ACCESS_KEY_ID"
SQS_QUEUE_URL = "https://sqs.ap-northeast-2.amazonaws.com/USER_ID/QUEUE_TASK"
encoded_secret_key = urllib.parse.quote(AWS_SECRET_ACCESS_KEY, safe='')

celery = Celery(
    broker_url=f'sqs://{AWS_ACCESS_KEY_ID}:{encoded_secret_key}@',
    broker_transport_options={
        'region': 'ap-northeast-2',
        'visibility_timeout': 3600,
        'polling_interval': 1,
    },
    task_default_queue='QUEUE_TASK',  # 기본 대기열 설정
    task_queues=(
        Queue('QUEUE_TASK', Exchange('celery'), routing_key='QUEUE_TASK'),
    ),
    result_backend=None,
    task_create_missing_queues=False,
    include=['app.domains.email.worker.email']
)

celery.conf.update(
    result_expires=3600,
    task_serializer='json',
    accept_content=['json'],
    result_serializer='json',
)

celery.conf.broker_connection_retry_on_startup = True
