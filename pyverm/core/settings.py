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


#imports from standard library
import logging



# logger
logger = logging.getLogger(__name__)

decimal_precision = 20

