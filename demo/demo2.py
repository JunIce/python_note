#!/bin/bash/
# coding: utf-8
import math


def cash(x):
  a = {100: 0.01, 60: 0.015, 40: 0.03, 20: 0.05, 10: 0.075, 0: 0.1}
  r = 0

  for i in a.keys():
    if x > i:
      r+=(x - i) * a.get(i)
      x = i
  return r


