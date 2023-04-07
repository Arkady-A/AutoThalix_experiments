from thales_remote.connection import ThalesRemoteConnection
from thales_remote.script_wrapper import ThalesRemoteScriptWrapper


def initialize_experiment(run_name):
    zennium_connection = ThalesRemoteConnection()
    zennium_connection.connectToTerm("localhost", "ScriptRemote")  # do not change to anything besides localhost
    zahner_zennium = ThalesRemoteScriptWrapper(zennium_connection)
    zahner_zennium.forceThalesIntoRemoteScript()
    zahner_zennium.calibrateOffsets()
    return zennium_connection, zahner_zennium
