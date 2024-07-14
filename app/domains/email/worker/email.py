from app.celery.celery_app import celery


@celery.task(bind=True, max_retries=3)
def send_welcome_email(self, email: str):
    try:
        print("메일을 발송했습니다: ", email)
        return f"메일 발송 성공, {email}"
    except Exception as e:
        print("메일 발송 실패: ", e)
        raise self.retry(exc=e, countdown=60)
