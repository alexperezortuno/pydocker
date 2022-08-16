#!/usr/src/env python
# -*- coding: utf-8 -*-
import json
from json import JSONEncoder
from typing import Optional


class ContainerType:
    def __init__(self, name: Optional[str] = None,
                 image: Optional[str] = None,
                 status: Optional[int] = None,
                 ports: Optional[str] = None,
                 created: Optional[str] = None,
                 started: Optional[str] = None,
                 finished: Optional[str] = None,
                 duration: Optional[str] = None,
                 command: Optional[str] = None,
                 args: Optional[str] = None,
                 env: Optional[str] = None,
                 volumes: Optional[str] = None,
                 networks: Optional[str] = None):
        super().__init__()
        if name is not None:
            self.name = name
        if image is not None:
            self.image = image
        if status is not None:
            self.status = status
        if ports is not None:
            self.ports = ports
        if created is not None:
            self.created = created
        if started is not None:
            self.started = started
        if finished is not None:
            self.finished = finished
        if duration is not None:
            self.duration = duration
        if command is not None:
            self.command = command
        if args is not None:
            self.args = args
        if env is not None:
            self.env = env
        if volumes is not None:
            self.volumes = volumes
        if networks is not None:
            self.networks = networks

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.__hash__() == other.__hash__()

    def __hash__(self):
        return hash((self.name,
                    self.image,
                    self.status,
                    self.ports,
                    self.created,
                    self.started,
                    self.finished,
                    self.duration,
                    self.command,
                    self.args,
                    self.env,
                    self.volumes,
                    self.networks))

    def __str__(self):
        return json.dumps(self,
                          default=lambda o: o.__dict__,
                          sort_keys=True,
                          indent=2,
                          ensure_ascii=False).encode('utf-8')

    def to_json(self):
        return self.__str__()


class ContainerTypeEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__
