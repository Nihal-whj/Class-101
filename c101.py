import time
seconds = input("Please enter the seconds : ")
def countdowntimer(seconds):
    while seconds>0:
        mins=int(seconds/60)
        sec=int(seconds%60)
        timer=f'{mins} : {sec}'
        print(timer)
        time.sleep(1)
        seconds-=1
countdowntimer(int(seconds))
