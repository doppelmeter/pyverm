########################################################################
#                                                                      #
# Copyright (C) 2018,  Marius Hürzeler                                 #
#                                                                      #
# This file is part of PyVerm.                                         #
#                                                                      #
# PyVerm is free software: you can redistribute it and/or modify       #
# it under the terms of the GNU General Public License as published by #
# the Free Software Foundation, either version 3 of the License, or    #
# (at your option) any later version.                                  #
#                                                                      #
# PyVerm is distributed in the hope that it will be useful,            #
# but WITHOUT ANY WARRANTY; without even the implied warranty of       #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the        #
# GNU General Public License for more details.                         #
#                                                                      #
# You should have received a copy of the GNU General Public License    #
# along with Foobar.  If not, see <http://www.gnu.org/licenses/>.      #
#                                                                      #
########################################################################

"""
module settings


"""

__all__ = ["Point", "Database"]

__author__ = "Marius Hürzler"
__copyright__ = "Copyright (C) 2018, Marius Hürzeler"
__license__ = "GNU GPLv3"


import logging



# logger
logger = logging.getLogger(__name__)

decimal_precision = 20
report_always_on = False


# import configparser
# import logging
#
# import os
#
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)
# #logger.setLevel(level=logging.DEBUG)
#
# _is_loaded = False
# _config = configparser.ConfigParser()
#
#
# if not _is_loaded:
#     loaded_files = _config.read([os.getcwd()+"\pyverm_settings.ini", "pyverm.ini"], encoding="UTF-8")
#     if loaded_files != []:
#         for each in loaded_files:
#             logger.info("loaded settings from %s",each)
#     _is_loaded = True
#
# def save():
#     filename = os.getcwd()+"\pyverm_settings.ini"
#     file = open(filename,"w", encoding="UTF-(")
#     _config.write(file)
#     logger.info("current settings are saved to %s", filename)
#     file.close()
#
#
#
# def get_decimal_precision():
#     decimal_precision = _config.getint("calculations","decimal_precision", fallback="10")
#     return(decimal_precision)
#
# def set_decimal_precision(decimal_precision):
#     _config.set("calculations","decimal_precision", str(decimal_precision))
#     logger.info("setting calculations->decimal_precision is changed to %s", str(decimal_precision))
#
###################################################
# file pyverm_settings.ini
#--------------------------------------------------
# [meta]
# settings_version = 0.0.0
# auto_save_settings_changes = False
# test = hallo welt
#
# [calculations]
# decimal_precision = 10
###################################################


