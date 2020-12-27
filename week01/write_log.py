import time
import logging


# def w_log():
#     now_time = time.strftime("%Y-%m-%d %X", time.localtime())
#     print(now_time)
#
#
# w_log()


def my_log():
    logging.basicConfig(filename="test.log",
                        level=logging.DEBUG,
                        datefmt="%Y-%m-%d %H:%M:%S",
                        format="%(asctime)s %(name)-8s %(levelname)-8s [line: %(lineno)d] %(message)s"
                        )
    logging.info("test_demo")


my_log()
