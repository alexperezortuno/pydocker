#!/usr/src/env python
# -*- coding: utf-8 -*-
import sys
import docker


class Image:
    client = docker.from_env()

    def list(self):
        for image in self.client.images.list(all=True):
            sys.stdout.write(f"Tag: {image.tags[0]}\tshort_id:{image.id}\n")

    def run(self, param: str):
        if param.lower() == "list" or param.lower() == "ls":
            self.list()
