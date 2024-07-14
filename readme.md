# 실행

```shell
celery -A app.celery.celery_app worker --loglevel=info
poetry run uvicorn app.cmd.api:app --host 0.0.0.0 --port 8000 --reload
```


# 참고
- [How To Use Celery](https://medium.com/@kasperjuunge/how-to-use-celery-c34310e6bcba)



