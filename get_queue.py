#!/usr/bin/env python
# -*- coding: utf-8 -*-

import posix_ipc as ipc

from time import sleep


def main():

    mq = ipc.MessageQueue(
        # '/my_q01', ipc.O_CREAT, 0666, 10, 1024, True, False
        '/my_q01', ipc.O_CREAT
    )

    while True:
        data = mq.receive()
        print(data)
        # print("data: %s" % data)

        sleep(1)


if __name__ == "__main__":
    main()
