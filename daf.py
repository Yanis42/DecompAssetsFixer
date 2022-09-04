import argparse

try:
    from data import fileTypes, decompPath
    from functions import replaceOldData, replaceEntranceHex
except:
    print("ERROR: Files are missing. Make sure everything is in the same folder.")
    quit()

parser = argparse.ArgumentParser(description="Fix various things related to assets for the OoT Decomp")

parser.add_argument(
    "-m", "--mode", dest="mode", type=str, default="", help="available modes: `fix_types`, `name_entrances`"
)

args = parser.parse_args()

if args.mode == "":
    print("Usage: daf.py -h (--help)")
    quit()

if args.mode == "fix_types":
    for type in fileTypes:
        replaceOldData(f"{decompPath}/assets/", type)

if args.mode == "name_entrances":
    replaceEntranceHex(decompPath)
