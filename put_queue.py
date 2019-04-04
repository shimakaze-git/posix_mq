#!/usr/bin/env python
# -*- coding: utf-8 -*-

import posix_ipc as ipc
import json

from time import sleep


def main():
    mq = ipc.MessageQueue(
        # '/my_q01', ipc.O_CREAT, 666, 10, 1024, False, True
        '/my_q01', ipc.O_CREAT
    )
    cnt = 0

    try:
        while True:
            cnt += 1
            obj = {
                "counter": cnt
            }
            mq.send(json.dumps(obj))
            print("pushed: %d" % cnt)
            print("obj: %s" % obj)
            print("[--------------------------------------]")

            sleep(1)
    except KeyboardInterrupt:
        mq.unlink()


if __name__ == "__main__":
    main()
