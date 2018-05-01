'''
Module specific config
'''
import configparser
import os.path
import json
from threadsafeLogger import ThreadsafeLogger

def load(loggingQueue):
    """ Load module specific config into dictionary, return it"""    
    logger = ThreadsafeLogger(loggingQueue, "websocketServerLoader")
    thisConfig = {}
    configParser = configparser.ConfigParser()

    thisConfig = loadSecrets(thisConfig, logger, configParser)
    thisConfig = loadModule(thisConfig, logger, configParser)
    return thisConfig

def loadSecrets(thisConfig, logger, configParser):
    """ Load module specific secrets """
    try:
        with open("/secrets.conf") as f:
            configParser.readfp(f)
    except IOError:
        configParser.read(os.path.join(os.path.dirname(__file__),"config/secrets.conf"))
        exit

    return thisConfig

def loadModule(thisConfig, logger, configParser):
    """ Load module config """
    try:
        with open("/collectionPoint.conf") as f:
            configParser.readfp(f)
    except IOError:
        configParser.read(os.path.join(os.path.dirname(__file__),"config/collectionPoint.conf"))
        exit

    """websocket host"""
    try:
        configValue=configParser.get('ModuleConfig','websocket_host')
    except:
        configValue = '127.0.0.1'
    logger.info("Websocket server host : %s" % configValue)
    thisConfig['WebsocketHost'] = configValue

    """websocket port"""
    try:
        configValue=configParser.getint('ModuleConfig','websocket_port')
    except:
        configValue = 13254
    logger.info("Websocket server port : %s" % configValue)
    thisConfig['WebsocketPort'] = configValue

    return thisConfig