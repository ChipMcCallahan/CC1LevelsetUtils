# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cc1_levelset_utils.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='cc1_levelset_utils.proto',
  package='cc1_levelset_utils',
  syntax='proto3',
  serialized_pb=_b('\n\x18\x63\x63\x31_levelset_utils.proto\x12\x12\x63\x63\x31_levelset_utils\"\xc9\x01\n\x08Levelset\x12\x0c\n\x04name\x18\x01 \x01(\t\x12)\n\x06levels\x18\x02 \x03(\x0b\x32\x19.cc1_levelset_utils.Level\x12\x33\n\x07stories\x18\x03 \x03(\x0b\x32\".cc1_levelset_utils.Levelset.Story\x1aO\n\x05Story\x12\x14\n\x0clevel_number\x18\x01 \x01(\x05\x12\x0c\n\x04text\x18\x02 \x03(\t\"\"\n\x04Type\x12\x0c\n\x08PROLOGUE\x10\x00\x12\x0c\n\x08\x45PILOGUE\x10\x01\"\x99\x01\n\x05Level\x12\r\n\x05title\x18\x01 \x01(\t\x12\x0e\n\x06\x61uthor\x18\x02 \x01(\t\x12\x0e\n\x06number\x18\x03 \x01(\x05\x12\x0c\n\x04time\x18\x04 \x01(\x05\x12\r\n\x05\x63hips\x18\x05 \x01(\x05\x12\x0c\n\x04hint\x18\x06 \x01(\t\x12\x10\n\x08password\x18\x07 \x01(\t\x12$\n\x03map\x18\x08 \x01(\x0b\x32\x17.cc1_levelset_utils.Map\"\x84\x01\n\x03Map\x12\x31\n\x05tiles\x18\x01 \x03(\x0b\x32\".cc1_levelset_utils.Map.TilesEntry\x1aJ\n\nTilesEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12+\n\x05value\x18\x02 \x01(\x0b\x32\x1c.cc1_levelset_utils.TileSpec:\x02\x38\x01\"\x1b\n\x03Pos\x12\t\n\x01x\x18\x01 \x01(\x05\x12\t\n\x01y\x18\x02 \x01(\x05\"i\n\x08TileSpec\x12,\n\x03top\x18\x01 \x01(\x0e\x32\x1f.cc1_levelset_utils.CC1TileCode\x12/\n\x06\x62ottom\x18\x02 \x01(\x0e\x32\x1f.cc1_levelset_utils.CC1TileCode*\xe0\x0c\n\x0b\x43\x43\x31TileCode\x12\t\n\x05\x46LOOR\x10\x00\x12\x08\n\x04WALL\x10\x01\x12\x08\n\x04\x43HIP\x10\x02\x12\t\n\x05WATER\x10\x03\x12\x08\n\x04\x46IRE\x10\x04\x12\x11\n\rINV_WALL_PERM\x10\x05\x12\x0b\n\x07PANEL_N\x10\x06\x12\x0b\n\x07PANEL_W\x10\x07\x12\x0b\n\x07PANEL_S\x10\x08\x12\x0b\n\x07PANEL_E\x10\t\x12\t\n\x05\x42LOCK\x10\n\x12\x08\n\x04\x44IRT\x10\x0b\x12\x07\n\x03ICE\x10\x0c\x12\x0b\n\x07\x46ORCE_S\x10\r\x12\x11\n\rCLONE_BLOCK_N\x10\x0e\x12\x11\n\rCLONE_BLOCK_W\x10\x0f\x12\x11\n\rCLONE_BLOCK_S\x10\x10\x12\x11\n\rCLONE_BLOCK_E\x10\x11\x12\x0b\n\x07\x46ORCE_N\x10\x12\x12\x0b\n\x07\x46ORCE_E\x10\x13\x12\x0b\n\x07\x46ORCE_W\x10\x14\x12\x08\n\x04\x45XIT\x10\x15\x12\r\n\tBLUE_DOOR\x10\x16\x12\x0c\n\x08RED_DOOR\x10\x17\x12\x0e\n\nGREEN_DOOR\x10\x18\x12\x0f\n\x0bYELLOW_DOOR\x10\x19\x12\n\n\x06ICE_SE\x10\x1a\x12\n\n\x06ICE_SW\x10\x1b\x12\n\n\x06ICE_NW\x10\x1c\x12\n\n\x06ICE_NE\x10\x1d\x12\x12\n\x0e\x42LUE_WALL_FAKE\x10\x1e\x12\x12\n\x0e\x42LUE_WALL_REAL\x10\x1f\x12\x0e\n\nNOT_USED_0\x10 \x12\t\n\x05THIEF\x10!\x12\n\n\x06SOCKET\x10\"\x12\x10\n\x0cGREEN_BUTTON\x10#\x12\x10\n\x0c\x43LONE_BUTTON\x10$\x12\x0f\n\x0bTOGGLE_WALL\x10%\x12\x10\n\x0cTOGGLE_FLOOR\x10&\x12\x0f\n\x0bTRAP_BUTTON\x10\'\x12\x0f\n\x0bTANK_BUTTON\x10(\x12\x0c\n\x08TELEPORT\x10)\x12\x08\n\x04\x42OMB\x10*\x12\x08\n\x04TRAP\x10+\x12\x10\n\x0cINV_WALL_APP\x10,\x12\n\n\x06GRAVEL\x10-\x12\x0f\n\x0bPOP_UP_WALL\x10.\x12\x08\n\x04HINT\x10/\x12\x0c\n\x08PANEL_SE\x10\x30\x12\n\n\x06\x43LONER\x10\x31\x12\x10\n\x0c\x46ORCE_RANDOM\x10\x32\x12\x0e\n\nDROWN_CHIP\x10\x33\x12\x10\n\x0c\x42URNED_CHIP0\x10\x34\x12\x10\n\x0c\x42URNED_CHIP1\x10\x35\x12\x0e\n\nNOT_USED_1\x10\x36\x12\x0e\n\nNOT_USED_2\x10\x37\x12\x0e\n\nNOT_USED_3\x10\x38\x12\r\n\tCHIP_EXIT\x10\x39\x12\x11\n\rUNUSED_EXIT_0\x10:\x12\x11\n\rUNUSED_EXIT_1\x10;\x12\x13\n\x0f\x43HIP_SWIMMING_N\x10<\x12\x13\n\x0f\x43HIP_SWIMMING_W\x10=\x12\x13\n\x0f\x43HIP_SWIMMING_S\x10>\x12\x13\n\x0f\x43HIP_SWIMMING_E\x10?\x12\t\n\x05\x41NT_N\x10@\x12\t\n\x05\x41NT_W\x10\x41\x12\t\n\x05\x41NT_S\x10\x42\x12\t\n\x05\x41NT_E\x10\x43\x12\x0e\n\nFIREBALL_N\x10\x44\x12\x0e\n\nFIREBALL_W\x10\x45\x12\x0e\n\nFIREBALL_S\x10\x46\x12\x0e\n\nFIREBALL_E\x10G\x12\n\n\x06\x42\x41LL_N\x10H\x12\n\n\x06\x42\x41LL_W\x10I\x12\n\n\x06\x42\x41LL_S\x10J\x12\n\n\x06\x42\x41LL_E\x10K\x12\n\n\x06TANK_N\x10L\x12\n\n\x06TANK_W\x10M\x12\n\n\x06TANK_S\x10N\x12\n\n\x06TANK_E\x10O\x12\x0c\n\x08GLIDER_N\x10P\x12\x0c\n\x08GLIDER_W\x10Q\x12\x0c\n\x08GLIDER_S\x10R\x12\x0c\n\x08GLIDER_E\x10S\x12\x0b\n\x07TEETH_N\x10T\x12\x0b\n\x07TEETH_W\x10U\x12\x0b\n\x07TEETH_S\x10V\x12\x0b\n\x07TEETH_E\x10W\x12\x0c\n\x08WALKER_N\x10X\x12\x0c\n\x08WALKER_W\x10Y\x12\x0c\n\x08WALKER_S\x10Z\x12\x0c\n\x08WALKER_E\x10[\x12\n\n\x06\x42LOB_N\x10\\\x12\n\n\x06\x42LOB_W\x10]\x12\n\n\x06\x42LOB_S\x10^\x12\n\n\x06\x42LOB_E\x10_\x12\x10\n\x0cPARAMECIUM_N\x10`\x12\x10\n\x0cPARAMECIUM_W\x10\x61\x12\x10\n\x0cPARAMECIUM_S\x10\x62\x12\x10\n\x0cPARAMECIUM_E\x10\x63\x12\x0c\n\x08\x42LUE_KEY\x10\x64\x12\x0b\n\x07RED_KEY\x10\x65\x12\r\n\tGREEN_KEY\x10\x66\x12\x0e\n\nYELLOW_KEY\x10g\x12\x0c\n\x08\x46LIPPERS\x10h\x12\r\n\tFIREBOOTS\x10i\x12\n\n\x06SKATES\x10j\x12\x11\n\rSUCTION_BOOTS\x10k\x12\x0c\n\x08PLAYER_N\x10l\x12\x0c\n\x08PLAYER_W\x10m\x12\x0c\n\x08PLAYER_S\x10n\x12\x0c\n\x08PLAYER_E\x10ob\x06proto3')
)

_CC1TILECODE = _descriptor.EnumDescriptor(
  name='CC1TileCode',
  full_name='cc1_levelset_utils.CC1TileCode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='FLOOR', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WALL', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHIP', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WATER', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FIRE', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INV_WALL_PERM', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PANEL_N', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PANEL_W', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PANEL_S', index=8, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PANEL_E', index=9, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BLOCK', index=10, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DIRT', index=11, number=11,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ICE', index=12, number=12,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FORCE_S', index=13, number=13,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CLONE_BLOCK_N', index=14, number=14,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CLONE_BLOCK_W', index=15, number=15,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CLONE_BLOCK_S', index=16, number=16,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CLONE_BLOCK_E', index=17, number=17,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FORCE_N', index=18, number=18,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FORCE_E', index=19, number=19,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FORCE_W', index=20, number=20,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EXIT', index=21, number=21,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BLUE_DOOR', index=22, number=22,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RED_DOOR', index=23, number=23,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GREEN_DOOR', index=24, number=24,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='YELLOW_DOOR', index=25, number=25,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ICE_SE', index=26, number=26,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ICE_SW', index=27, number=27,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ICE_NW', index=28, number=28,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ICE_NE', index=29, number=29,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BLUE_WALL_FAKE', index=30, number=30,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BLUE_WALL_REAL', index=31, number=31,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NOT_USED_0', index=32, number=32,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='THIEF', index=33, number=33,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SOCKET', index=34, number=34,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GREEN_BUTTON', index=35, number=35,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CLONE_BUTTON', index=36, number=36,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TOGGLE_WALL', index=37, number=37,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TOGGLE_FLOOR', index=38, number=38,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TRAP_BUTTON', index=39, number=39,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TANK_BUTTON', index=40, number=40,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TELEPORT', index=41, number=41,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BOMB', index=42, number=42,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TRAP', index=43, number=43,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INV_WALL_APP', index=44, number=44,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GRAVEL', index=45, number=45,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POP_UP_WALL', index=46, number=46,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HINT', index=47, number=47,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PANEL_SE', index=48, number=48,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CLONER', index=49, number=49,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FORCE_RANDOM', index=50, number=50,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DROWN_CHIP', index=51, number=51,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BURNED_CHIP0', index=52, number=52,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BURNED_CHIP1', index=53, number=53,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NOT_USED_1', index=54, number=54,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NOT_USED_2', index=55, number=55,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NOT_USED_3', index=56, number=56,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHIP_EXIT', index=57, number=57,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNUSED_EXIT_0', index=58, number=58,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNUSED_EXIT_1', index=59, number=59,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHIP_SWIMMING_N', index=60, number=60,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHIP_SWIMMING_W', index=61, number=61,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHIP_SWIMMING_S', index=62, number=62,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHIP_SWIMMING_E', index=63, number=63,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ANT_N', index=64, number=64,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ANT_W', index=65, number=65,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ANT_S', index=66, number=66,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ANT_E', index=67, number=67,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FIREBALL_N', index=68, number=68,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FIREBALL_W', index=69, number=69,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FIREBALL_S', index=70, number=70,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FIREBALL_E', index=71, number=71,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BALL_N', index=72, number=72,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BALL_W', index=73, number=73,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BALL_S', index=74, number=74,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BALL_E', index=75, number=75,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TANK_N', index=76, number=76,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TANK_W', index=77, number=77,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TANK_S', index=78, number=78,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TANK_E', index=79, number=79,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GLIDER_N', index=80, number=80,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GLIDER_W', index=81, number=81,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GLIDER_S', index=82, number=82,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GLIDER_E', index=83, number=83,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TEETH_N', index=84, number=84,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TEETH_W', index=85, number=85,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TEETH_S', index=86, number=86,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TEETH_E', index=87, number=87,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WALKER_N', index=88, number=88,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WALKER_W', index=89, number=89,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WALKER_S', index=90, number=90,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WALKER_E', index=91, number=91,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BLOB_N', index=92, number=92,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BLOB_W', index=93, number=93,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BLOB_S', index=94, number=94,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BLOB_E', index=95, number=95,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PARAMECIUM_N', index=96, number=96,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PARAMECIUM_W', index=97, number=97,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PARAMECIUM_S', index=98, number=98,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PARAMECIUM_E', index=99, number=99,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BLUE_KEY', index=100, number=100,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RED_KEY', index=101, number=101,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GREEN_KEY', index=102, number=102,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='YELLOW_KEY', index=103, number=103,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FLIPPERS', index=104, number=104,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FIREBOOTS', index=105, number=105,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SKATES', index=106, number=106,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUCTION_BOOTS', index=107, number=107,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PLAYER_N', index=108, number=108,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PLAYER_W', index=109, number=109,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PLAYER_S', index=110, number=110,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PLAYER_E', index=111, number=111,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=680,
  serialized_end=2312,
)
_sym_db.RegisterEnumDescriptor(_CC1TILECODE)

CC1TileCode = enum_type_wrapper.EnumTypeWrapper(_CC1TILECODE)
FLOOR = 0
WALL = 1
CHIP = 2
WATER = 3
FIRE = 4
INV_WALL_PERM = 5
PANEL_N = 6
PANEL_W = 7
PANEL_S = 8
PANEL_E = 9
BLOCK = 10
DIRT = 11
ICE = 12
FORCE_S = 13
CLONE_BLOCK_N = 14
CLONE_BLOCK_W = 15
CLONE_BLOCK_S = 16
CLONE_BLOCK_E = 17
FORCE_N = 18
FORCE_E = 19
FORCE_W = 20
EXIT = 21
BLUE_DOOR = 22
RED_DOOR = 23
GREEN_DOOR = 24
YELLOW_DOOR = 25
ICE_SE = 26
ICE_SW = 27
ICE_NW = 28
ICE_NE = 29
BLUE_WALL_FAKE = 30
BLUE_WALL_REAL = 31
NOT_USED_0 = 32
THIEF = 33
SOCKET = 34
GREEN_BUTTON = 35
CLONE_BUTTON = 36
TOGGLE_WALL = 37
TOGGLE_FLOOR = 38
TRAP_BUTTON = 39
TANK_BUTTON = 40
TELEPORT = 41
BOMB = 42
TRAP = 43
INV_WALL_APP = 44
GRAVEL = 45
POP_UP_WALL = 46
HINT = 47
PANEL_SE = 48
CLONER = 49
FORCE_RANDOM = 50
DROWN_CHIP = 51
BURNED_CHIP0 = 52
BURNED_CHIP1 = 53
NOT_USED_1 = 54
NOT_USED_2 = 55
NOT_USED_3 = 56
CHIP_EXIT = 57
UNUSED_EXIT_0 = 58
UNUSED_EXIT_1 = 59
CHIP_SWIMMING_N = 60
CHIP_SWIMMING_W = 61
CHIP_SWIMMING_S = 62
CHIP_SWIMMING_E = 63
ANT_N = 64
ANT_W = 65
ANT_S = 66
ANT_E = 67
FIREBALL_N = 68
FIREBALL_W = 69
FIREBALL_S = 70
FIREBALL_E = 71
BALL_N = 72
BALL_W = 73
BALL_S = 74
BALL_E = 75
TANK_N = 76
TANK_W = 77
TANK_S = 78
TANK_E = 79
GLIDER_N = 80
GLIDER_W = 81
GLIDER_S = 82
GLIDER_E = 83
TEETH_N = 84
TEETH_W = 85
TEETH_S = 86
TEETH_E = 87
WALKER_N = 88
WALKER_W = 89
WALKER_S = 90
WALKER_E = 91
BLOB_N = 92
BLOB_W = 93
BLOB_S = 94
BLOB_E = 95
PARAMECIUM_N = 96
PARAMECIUM_W = 97
PARAMECIUM_S = 98
PARAMECIUM_E = 99
BLUE_KEY = 100
RED_KEY = 101
GREEN_KEY = 102
YELLOW_KEY = 103
FLIPPERS = 104
FIREBOOTS = 105
SKATES = 106
SUCTION_BOOTS = 107
PLAYER_N = 108
PLAYER_W = 109
PLAYER_S = 110
PLAYER_E = 111


_LEVELSET_STORY_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='cc1_levelset_utils.Levelset.Story.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PROLOGUE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EPILOGUE', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=216,
  serialized_end=250,
)
_sym_db.RegisterEnumDescriptor(_LEVELSET_STORY_TYPE)


_LEVELSET_STORY = _descriptor.Descriptor(
  name='Story',
  full_name='cc1_levelset_utils.Levelset.Story',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='level_number', full_name='cc1_levelset_utils.Levelset.Story.level_number', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='text', full_name='cc1_levelset_utils.Levelset.Story.text', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _LEVELSET_STORY_TYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=171,
  serialized_end=250,
)

_LEVELSET = _descriptor.Descriptor(
  name='Levelset',
  full_name='cc1_levelset_utils.Levelset',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='cc1_levelset_utils.Levelset.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='levels', full_name='cc1_levelset_utils.Levelset.levels', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stories', full_name='cc1_levelset_utils.Levelset.stories', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_LEVELSET_STORY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=49,
  serialized_end=250,
)


_LEVEL = _descriptor.Descriptor(
  name='Level',
  full_name='cc1_levelset_utils.Level',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='title', full_name='cc1_levelset_utils.Level.title', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='author', full_name='cc1_levelset_utils.Level.author', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='number', full_name='cc1_levelset_utils.Level.number', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='time', full_name='cc1_levelset_utils.Level.time', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='chips', full_name='cc1_levelset_utils.Level.chips', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hint', full_name='cc1_levelset_utils.Level.hint', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='password', full_name='cc1_levelset_utils.Level.password', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='map', full_name='cc1_levelset_utils.Level.map', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=253,
  serialized_end=406,
)


_MAP_TILESENTRY = _descriptor.Descriptor(
  name='TilesEntry',
  full_name='cc1_levelset_utils.Map.TilesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='cc1_levelset_utils.Map.TilesEntry.key', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='cc1_levelset_utils.Map.TilesEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=467,
  serialized_end=541,
)

_MAP = _descriptor.Descriptor(
  name='Map',
  full_name='cc1_levelset_utils.Map',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tiles', full_name='cc1_levelset_utils.Map.tiles', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_MAP_TILESENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=409,
  serialized_end=541,
)


_POS = _descriptor.Descriptor(
  name='Pos',
  full_name='cc1_levelset_utils.Pos',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='cc1_levelset_utils.Pos.x', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='y', full_name='cc1_levelset_utils.Pos.y', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=543,
  serialized_end=570,
)


_TILESPEC = _descriptor.Descriptor(
  name='TileSpec',
  full_name='cc1_levelset_utils.TileSpec',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='top', full_name='cc1_levelset_utils.TileSpec.top', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bottom', full_name='cc1_levelset_utils.TileSpec.bottom', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=572,
  serialized_end=677,
)

_LEVELSET_STORY.containing_type = _LEVELSET
_LEVELSET_STORY_TYPE.containing_type = _LEVELSET_STORY
_LEVELSET.fields_by_name['levels'].message_type = _LEVEL
_LEVELSET.fields_by_name['stories'].message_type = _LEVELSET_STORY
_LEVEL.fields_by_name['map'].message_type = _MAP
_MAP_TILESENTRY.fields_by_name['value'].message_type = _TILESPEC
_MAP_TILESENTRY.containing_type = _MAP
_MAP.fields_by_name['tiles'].message_type = _MAP_TILESENTRY
_TILESPEC.fields_by_name['top'].enum_type = _CC1TILECODE
_TILESPEC.fields_by_name['bottom'].enum_type = _CC1TILECODE
DESCRIPTOR.message_types_by_name['Levelset'] = _LEVELSET
DESCRIPTOR.message_types_by_name['Level'] = _LEVEL
DESCRIPTOR.message_types_by_name['Map'] = _MAP
DESCRIPTOR.message_types_by_name['Pos'] = _POS
DESCRIPTOR.message_types_by_name['TileSpec'] = _TILESPEC
DESCRIPTOR.enum_types_by_name['CC1TileCode'] = _CC1TILECODE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Levelset = _reflection.GeneratedProtocolMessageType('Levelset', (_message.Message,), dict(

  Story = _reflection.GeneratedProtocolMessageType('Story', (_message.Message,), dict(
    DESCRIPTOR = _LEVELSET_STORY,
    __module__ = 'cc1_levelset_utils_pb2'
    # @@protoc_insertion_point(class_scope:cc1_levelset_utils.Levelset.Story)
    ))
  ,
  DESCRIPTOR = _LEVELSET,
  __module__ = 'cc1_levelset_utils_pb2'
  # @@protoc_insertion_point(class_scope:cc1_levelset_utils.Levelset)
  ))
_sym_db.RegisterMessage(Levelset)
_sym_db.RegisterMessage(Levelset.Story)

Level = _reflection.GeneratedProtocolMessageType('Level', (_message.Message,), dict(
  DESCRIPTOR = _LEVEL,
  __module__ = 'cc1_levelset_utils_pb2'
  # @@protoc_insertion_point(class_scope:cc1_levelset_utils.Level)
  ))
_sym_db.RegisterMessage(Level)

Map = _reflection.GeneratedProtocolMessageType('Map', (_message.Message,), dict(

  TilesEntry = _reflection.GeneratedProtocolMessageType('TilesEntry', (_message.Message,), dict(
    DESCRIPTOR = _MAP_TILESENTRY,
    __module__ = 'cc1_levelset_utils_pb2'
    # @@protoc_insertion_point(class_scope:cc1_levelset_utils.Map.TilesEntry)
    ))
  ,
  DESCRIPTOR = _MAP,
  __module__ = 'cc1_levelset_utils_pb2'
  # @@protoc_insertion_point(class_scope:cc1_levelset_utils.Map)
  ))
_sym_db.RegisterMessage(Map)
_sym_db.RegisterMessage(Map.TilesEntry)

Pos = _reflection.GeneratedProtocolMessageType('Pos', (_message.Message,), dict(
  DESCRIPTOR = _POS,
  __module__ = 'cc1_levelset_utils_pb2'
  # @@protoc_insertion_point(class_scope:cc1_levelset_utils.Pos)
  ))
_sym_db.RegisterMessage(Pos)

TileSpec = _reflection.GeneratedProtocolMessageType('TileSpec', (_message.Message,), dict(
  DESCRIPTOR = _TILESPEC,
  __module__ = 'cc1_levelset_utils_pb2'
  # @@protoc_insertion_point(class_scope:cc1_levelset_utils.TileSpec)
  ))
_sym_db.RegisterMessage(TileSpec)


_MAP_TILESENTRY.has_options = True
_MAP_TILESENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
# @@protoc_insertion_point(module_scope)
