import logging

def say_hello(msg):
    return 'Hello ' + msg

# logger 생성
root_logger = logging.getLogger()

# log level 설정
root_logger.setLevel(logging.DEBUG)

# logger file Handler 생성
fileHandler = logging.FileHandler('test.log', 'w', 'utf-8')

# logger console Handler 생성
streamHandler = logging.StreamHandler()


formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(filename)s : %(lineno)s - %(message)s')

# FileHandler에 file_formatter 설정
fileHandler.setFormatter(file_formatter)
streamHandler.setFormatter(formatter)

# logger 객체에 fileHandler와 streamHandler를 등록
root_logger.addHandler(fileHandler)
root_logger.addHandler(streamHandler)

root_logger.debug('Start of Program')
root_logger.debug(say_hello('debug 모드'))
root_logger.info(say_hello('info 모드'))
root_logger.warning(say_hello('warning 모드'))
root_logger.error(say_hello('error 모드'))
root_logger.debug('End of Program')


'''
2020-07-17 16:35:23,220 - DEBUG - Start of Program
2020-07-17 16:35:23,220 - DEBUG - Hello debug 모드
2020-07-17 16:35:23,220 - INFO - Hello info 모드
2020-07-17 16:35:23,220 - ERROR - Hello error 모드
2020-07-17 16:35:23,220 - DEBUG - End of Program
'''
