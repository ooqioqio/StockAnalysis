#!/usr/bin/env python
#coding=utf-8
from django.http import HttpResponse
import sys
import imp
imp.reload(sys) 
import logging
# 引用django日志实例
def logDemo(request):
    logger = logging.getLogger(__name__)
    logger.debug("debug level log")
    logger.warning("warning level log")
    logger.info("info level log")
    logger.error("error level log")
    return HttpResponse("Demo Log.")
# 引用errorOnly日志实例
def errorOnlyDemo(request):
    logger = logging.getLogger('errorOnly')
    logger.debug("debug level log")
    logger.warning("warning level log")
    logger.info("info level log")
    logger.error("error level log")
    return HttpResponse("Only display error log.")