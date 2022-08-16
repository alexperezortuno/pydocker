# !/usr/src/env python
# -*- coding: utf-8 -*-
import sys
import docker
from docker.models.images import Image


class Container:
    client = docker.from_env()

    def list(self):
        for container in self.client.containers.list(all=True):
            image: Image = container.image
            sys.stdout.write(f"Name: {container.name}\t\t\tImage:{image.tags[0]}\tshort_id:{container.short_id}\n")

    def run(self, param: str):
        if param.lower() == "list" or param.lower() == "ls":
            self.list()
