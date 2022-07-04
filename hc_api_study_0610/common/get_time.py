import time
def get_time_strftime():
    return time.strftime("%Y%m%d%H%M%S",time.localtime())


if __name__ == '__main__':
    print(get_time_strftime())