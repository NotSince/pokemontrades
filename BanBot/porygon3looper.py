import time
import Porygon3noloop

already_done = set()

while True:
    try:
        Porygon3noloop.main()
    except Exception, e:
        print "couldn't Reddit: %s" % str(e)
        time.sleep(30)
        pass
    time.sleep(60)
