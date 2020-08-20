from app import celery_app


@celery_app.task
def my_task():
    print('hello')


if __name__ == '__main__':
    my_task()
