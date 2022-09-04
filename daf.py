import argparse

try:
    from data import fileTypes, decompPath
    from functions import replaceOldData, replaceEntranceHex, fixSegments
except:
    print("ERROR: Files are missing. Make sure everything is in the same folder.")
    quit()

parser = argparse.ArgumentParser(description="Fix various things related to assets for the OoT Decomp")

parser.add_argument(
    "-m",
    "--mode",
    dest="mode",
    type=str,
    default="",
    help="available modes: `fix_types`, `name_entrances`, `fix_segments`",
)

parser.add_argument(
    "-a",
    "--all",
    dest="run_all",
    default=False,
    action="store_true",
    help="run every mode",
)

args = parser.parse_args()

if args.mode == "fix_types" or args.run_all:
    for type in fileTypes:
        replaceOldData(f"{decompPath}/assets/", type)

elif args.mode == "name_entrances" or args.run_all:
    replaceEntranceHex(decompPath)

elif args.mode == "fix_segments" or args.run_all:
    fixSegments(decompPath)

else:
    parser.print_help()
    quit()
