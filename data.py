### [GENERAL DATA] ###

# Set your decomp assets path here
decompPath = "../oot/assets"

# Add types here
fileTypes = [".h", ".c"]

# -------------------------------------------------------

### [FIX TYPES MODE] ###

# Format: ``"OLD": "NEW"``

camData = {
    "CamData": "BgCamInfo",
}

curveData = {
    "TransformData": "CurveInterpKnot",
    "TransformUpdateIndex": "CurveAnimationHeader",
    "SkelCurveLimbList": "CurveSkeletonHeader",
}

roomData = {
    "PolygonDlist": "RoomShapeDListsEntry",
    "PolygonType0": "RoomShapeNormal",
    "MeshHeader1Single": "RoomShapeImageSingle",
    "BgImage": "RoomShapeImageMultiBgEntry",
    "MeshHeader1Multi": "RoomShapeImageMulti",
    "PolygonDlist2": "RoomShapeCullableEntry",
    "PolygonType2": "RoomShapeCullable",
    "SCENE_CMD_MESH": "SCENE_CMD_ROOM_SHAPE",
}

skinData = {
    "Struct_800A57C0": "SkinVertex",
    "Struct_800A598C_2": "SkinTransformation",
    "Struct_800A5E28": "SkinAnimatedLimbData",
    "Struct_800A598C": "SkinLimbModif",
}

# Add or remove dictionnaries to this list to replace types
dataToFix = [
    camData,
    curveData,
    roomData,
    skinData,
]

# -------------------------------------------------------

