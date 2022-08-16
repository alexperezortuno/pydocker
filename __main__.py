#!/usr/src/env python
# -*- coding: utf-8 -*-
import getopt
import sys

from core.container import Container
from core.image import Image
from logger import logger
from sql_app.containers import check_table_containers
from sql_app.settings import check_table_settings


def doc_help():
    print("""
    Usage:
        python pydocker [options]
    Options:
    -h, --help                 Print this help message
    -t, --create-tables        Create tables
    -c, --container           Container operations
    """)


def run_standalone():
    try:
        logger.debug("Pydocker version: 0.0.1")
        opts, args = getopt.getopt(sys.argv[1:], "htc:i:", [
            "help",
            "create-tables",
            "container=",
            "image="])
        for opt, arg in opts:
            if opt == "-h" or opt == "--help":
                print(doc_help())
                sys.exit(0)
            elif opt == "-t" or opt == "--create-tables":
                check_table_settings()
                check_table_containers()
                sys.exit(0)
            elif opt == "-c" or opt == "--container":
                logger.debug(f"Container: {arg}")
                Container().run(arg)
                sys.exit(0)
            elif opt == "-i" or opt == "--image":
                logger.debug(f"Image: {arg}")
                Image().run(arg)
                sys.exit(0)
    except Exception as e:
        logger.error(e)
        doc_help()
        sys.exit(1)


if __name__ == "__main__":
    run_standalone()
    check_table_settings()
    check_table_containers()
