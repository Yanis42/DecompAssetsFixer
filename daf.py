from time import time

try:
    from data import fileTypes, decompPath
    from functions import replaceOldData, replaceEntranceHex, fixSegments, getArguments
except:
    print("[DAF:Error]: Files are missing. Make sure everything is in the same folder.")
    quit()

# verbose settings
fixTypeTime = entranceTime = segmentsTime = None
dashAmount = 60
infoPrefix = "[DAF:Info]"

# general things
args, parser = getArguments()
hasArgs = False
runTime = time()

if args.mode == "fix_types" or args.run_all:
    startingTime = time()

    if args.verbose:
        print(f"{infoPrefix}: Fixing types and macros...")

    hasArgs = True
    for type in fileTypes:
        replaceOldData(f"{decompPath}/assets/", type)

    if args.verbose:
        print(f"{infoPrefix}: Done in {(time() - startingTime):.2f}s!\n{'-' * dashAmount}")

if args.mode == "name_entrances" or args.run_all:
    startingTime = time()

    if args.verbose:
        print(f"{infoPrefix}: Removing hexadecimal from exit lists...")
    hasArgs = True
    replaceEntranceHex(decompPath)

    if args.verbose:
        print(f"{infoPrefix}: Done in {(time() - startingTime):.2f}s!\n{'-' * dashAmount}")

if args.mode == "fix_segments" or args.run_all:
    startingTime = time()

    if args.verbose:
        print(f"{infoPrefix}: Adding missing casts to rooms symbols...")
    hasArgs = True
    fixSegments(decompPath)

    if args.verbose:
        print(f"{infoPrefix}: Done in {(time() - startingTime):.2f}s!\n{'-' * dashAmount}")

if hasArgs and args.verbose:
    print(f"{infoPrefix}: All Done in {(time() - runTime):.2f}s!")

if not hasArgs:
    parser.print_help()
    quit()
