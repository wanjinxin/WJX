from celery.schedules import crontab


backend = 'redis://localhost:6379/8'
timezone = 'Asia/Shanghai'
enable_utc = True

imports = [
    'test',
]

beat_schedule = {
    'my_task': {
        'task': 'test.my_task',
        'schedule': crontab(minute='*')
    }
}


if __name__ == '__main__':
    pass
