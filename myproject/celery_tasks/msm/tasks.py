from .utils.yuntongxun.sms import CCP
from celery_tasks.main import celery_app
import logging


log = logging.getLogger('django')

@celery_app.task(name='send_msg_code')
def send_msg_code(phone,msg_code,expire,temp_id):
    try:
        ccp = CCP()
        ret = ccp.send_template_sms(phone,[msg_code,expire],temp_id)
        print(ret)
    except Exception as e:
        print('-------------------->发送短信验证码异常')

    else:
        if ret == 0:
            print('发送短信成功')
        else:
            print('发送失败')