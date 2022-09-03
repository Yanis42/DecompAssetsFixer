import argparse

try:
    from functions import replaceOldData, fileTypes, decompPath
except:
    print("ERROR: ``functions.py`` not found! Make sure everything is in the same folder.")
    quit()

parser = argparse.ArgumentParser(
    description = "Fix various things related to assets for the OoT Decomp"
)

parser.add_argument(
    "-m",
    "--mode",
    dest = "mode",
    type = str,
    default = "",
    help = "available modes: `fix_types`, `name_entrances`"
)

args = parser.parse_args()

if args.mode == "":
    print("Usage: daf.py -h (--help)")
    quit()

if args.mode == "fix_types":
    for type in fileTypes:
        replaceOldData(decompPath, type)
