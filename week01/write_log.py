
import logging
import os
import time as times


def write_log(path):
    # 获取文件路径
    log_path = os.path.dirname(path)
    # 获取当前日期
    file_dir = "python-" + times.strftime("%Y%m%d", times.localtime())
    # 拼接路径
    real_path = os.path.join(log_path, file_dir)
    # 判断路径是否存在，不存在则创建
    is_exists = os.path.exists(real_path)
    if not is_exists:
        os.makedirs(real_path)
    # 获取文件名称
    file_name = os.path.basename(path)

    # 拼接成路径+文件名
    final_path = os.path.join(real_path, file_name)

    logging.basicConfig(filename=final_path,
                        level=logging.DEBUG,
                        datefmt="%Y-%m-%d %H:%M:%S",
                        format="%(asctime)s"
                        )
    logging.info("test_demo")


write_log(r"E:/WeGame/my_log.txt")
