#!/usr/bin/env python
# -*- coding: utf-8 -*-

subtable = {}

for i in range(200):
    for j in range(200):
        subtable.update({"{}{}".format(i,j) : i - j})

print(subtable["1608"])
