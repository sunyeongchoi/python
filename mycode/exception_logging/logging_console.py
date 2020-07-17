import logging

def say_hello(msg):
    return 'Hello' + msg

# logging 설정
logging.basicConfig(level=logging.INFO, \
                    format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of Program')
logging.debug(say_hello('디버그 모드'))
logging.info(say_hello('인포 모드'))
logging.debug('End of Program')

'''
2020-07-17 16:13:17,390 - INFO - Hello인포 모드
'''

