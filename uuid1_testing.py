"""I had some concerns about uuid1 conflicts as mentioned e.g. here:
https://www.reddit.com/r/Python/comments/1hbx2z/python_1204_lts_273_uuid1_collisions/

But looking into the source the issue has been addressed by having a global timestamp variable that will always be
incremented to be larger than the last one used. So there is no chance of conflicts by generating the uuids in a single
thread (unique timestamp) even if on multiple machines (different mac adresses + unique timestamp per mac address).
"""
# code below from https://gist.github.com/devdave/5892749
from uuid import uuid1
from time import time

def main():
    test = dict()
    limit = 10 ** 10
    while limit:
        limit -= 1
        x = {n:uuid1().hex for n in range(15)}
        if len(set(x.values())) != len(x.keys()):
            print "Collision"
            return

if __name__ == '__main__':
    start = time()
    main()
print time() - start