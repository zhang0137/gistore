# -*- coding: utf-8 -*-
#
# gistore -- Backup files using DVCS, such as git.
# Copyright (C) 2010 Jiang Xin <jiangxin@ossxp.com>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#

import sys

LOG_DEBUG=5
LOG_INFO=4
LOG_NOTICE=3
LOG_WARNING=2
LOG_ERR=1
LOG_NONE=0

GISTORE_CONFIG_DIR=".gistore"

class DefaultConfig(object):
    sys_config_dir = '/etc/gistore'
    backend = "git"
    root_only = True
    log_level = LOG_WARNING
    task = None
    store_list = {'default': None }

def getConfig():
    try:
        # load custom config file in /etc/gistore/local_config.py
        sys.path.insert(0, DefaultConfig.sys_config_dir);
        module = __import__('local_config', globals(), {})
        configClass = getattr(module, 'Config')
        cfg = configClass()
    except ImportError:
        cfg = DefaultConfig()

    return cfg

cfg = getConfig()

# vim: et ts=4 sw=4
