# Decompilation Assets Fixer (DAF)
The tool used for extract the assets ([ZAPD](https://github.com/zeldaret/ZAPD)) needs to be updated because it's using old names for structs and macros, this project is a workaround attempt until the main tool is updated.

## Usage
- Change the decomp path in ``data.py``
- Run ``daf.py`` (tested under Python 3.10, should work with 3.9+)
- If you have any issues when compiling the decomp, try ``make clean && make -j``, if it's not working feel free to open an issue on this repo

### Operating modes:
- ``daf.py -m (--mode) fix_types``, this will update types and macros, intended to be used after using ZAPD
- ``daf.py -m (--mode) name_entrances``, this will remove hex numbers from exit lists
- ``daf.py -m (--mode) fix_segments``, this will add casts to segment symbols inside room lists

### ROM should build OK
```
f0b7f35375f9cc8ca1b2d59d78e35405  zelda_ocarina_mq_dbg.z64
zelda_ocarina_mq_dbg.z64: OK
```

## Add More Data
If you need to add more data to change, add a dictionnary with the following format: ``"OLD": "NEW"``, then add your dictionnary to ``dataToFix``.

Next, run ``daf.py`` and it should make the changes.

## Contributions are welcome!
