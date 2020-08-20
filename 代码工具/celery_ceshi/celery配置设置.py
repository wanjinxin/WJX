from celery import Celery

# broker设置
BROKEN_URL = 'redis://127.0.0.1:6379/7'

# 存储任务结果
CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/8'

# celery任务结果有效期
CELERY_TASK_RESULT_EXPIRES = 18000

# 任务系列化结构
CELERY_TASK_SERIALIZER = 'json'

# 结果序列化结构
CELERY_RESULT_SERIALIZER = 'json'

# celery接收内容类型
CELERY_ACCEPT_CONTENT = ['json']

# celery使用的时区
CELERY_TIMEZONE = 'Asia/Shanghai'

# 启动时区设置
CELERY_ENABLE_UTC = True

#