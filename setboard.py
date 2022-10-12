from sys import implementation
envVars["_implementation"] = implementation.name.upper()
if implementation.name.upper() == "MICROPYTHON":
    from os import uname
    envVars["_boardID"] = uname().machine
elif implementation.name.upper() == "CIRCUITPYTHON":
    import board
    envVars["_boardID"] = board.board_id