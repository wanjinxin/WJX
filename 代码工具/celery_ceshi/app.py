from celery import Celery
import celery_conf


celery_app = Celery('task', broker='redis://127.0.0.1:6379/7')
celery_app.config_from_object(celery_conf)


if __name__ == '__main__':
    print('start task')
    celery_app.worker_main()
