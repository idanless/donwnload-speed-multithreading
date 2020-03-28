import threading
import requests
import time
from termcolor import colored

class geturl:
    # size file you download
    filesize = 100

    # url default download
    def __init__(self,url='http://main.com'):
        self.url = url
    def pyaload_get(self):
        return self.url

    def show_url(self):
        ourput = str(self.url)
        print(ourput)


class multi:
    def __init__(self):
        self.run = threading.Thread(name='speed', target=payload)
        self.count = threading.active_count()

    def active_count(self):
        return self.count


def payload():
    start = time.perf_counter()
    # run default url
    run = geturl()
    #change url here
   # run = geturl('http://demo.com')
    url = str(run.pyaload_get())
    requests.get(url)
    end = time.perf_counter()
    sum = end - start
    print()
    print("sum of speed on megabit:",colored(int((int(run.filesize) /sum)*8), 'green'))



def check_threads(max):
    while True:
        thread = multi()
        if thread.count >= max:
            print(colored('Reach to limit Threads', 'red'),colored(thread.count-1, 'white'))
            time.sleep(2)
        else:
            threads()



def threads():
    thread = multi()
    thread.run.start()

if __name__ == '__main__':
    threads()
    # number of  thread (the max will be run)
    check_threads(2)

