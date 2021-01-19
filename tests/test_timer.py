# -*- coding: utf-8 -*-

import time

from .timer import timer_start, timer_stop, timer_get_time


def test_timer_get_time_1():
    timer_name = 'foo'
    timer_start(timer_name)
    time.sleep(10)
    current_time = timer_get_time(timer_name)
    assert 10 < current_time < 11
    timer_stop(timer_name)


def test_generic_timer_1():
    timer_name = timer_start()
    time.sleep(10)
    elapsed_time = timer_stop(timer_name)
    assert elapsed_time > 10
    assert elapsed_time < 11


def test_named_timer_1():
    timer_name = timer_start()
    timer_start(timer_name)
    time.sleep(10)

    generic_elapsed_time = timer_stop(timer_name)
    assert 10 < generic_elapsed_time < 11

    timer_start('bar')
    time.sleep(3)
    generic_elapsed_time = timer_stop(timer_name)
    bar_elapsed_time = timer_stop('bar')
    assert generic_elapsed_time > 13
    assert generic_elapsed_time < 14
    assert bar_elapsed_time > 3
    assert bar_elapsed_time < 4
