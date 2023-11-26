import os
import time
from random import random
from time import sleep

from neetbox.daemon import action
from neetbox.logging import logger
from neetbox.pipeline import listen, watch


@watch("train", initiative=True)
def train(epoch):
    loss, acc = random(), random()
    return {"loss": loss, "acc": acc}


@listen("train")
def print_to_console(metrix):
    logger.log(f"metrix from train: {metrix}")


@watch("log-some-prefix", interval=5.0)
def log_with_some_prefix():
    logger.ok("some ok")
    logger.info("some info")
    logger.debug("some debug")
    logger.warn("some warn")
    logger.err("some error")


@action(name="action-1")
def action_1(text: str):
    """take action 1

    Args:
        text (string): print this string to console as log
    """

    logger.log(f"action 1 triggered. text = {text}")


val = 0


def def_plus_1():
    @action(name="plus1", description=f"val={val}")
    def plus_1():
        global val
        val += 1
        def_plus_1()


def_plus_1()


@action(name="action-2")
def action_2(text1, text2):
    logger.log(f"action 2 triggered. text1 = {text1}, text2 = {text2}")


@action(name="wait-for-sec", blocking=True)
def action_2(sec):
    sec = int(sec)
    logger.log(f"wait for {sec} sec.")
    time.sleep(sec)


@action(name="eval")
def eval_code(code: str):
    logger.log(f"running code {code}")
    logger.info("eval result: ", eval(code))


_id_indexer = 0


@action()
def new_action(id: int):
    global _id_indexer

    @action(name=f"new_action_{_id_indexer}")
    def action_():
        pass

    _id_indexer += 1


@action(name="shutdown", description="shutdown your process", blocking=True)
def sys_exit():
    logger.log("shutdown received, shutting down immediately.")
    os._exit(0)


for i in range(99999):
    sleep(1)
    train(i)
