#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Constant values used in LSV2"""

# TNC drive names
DRIVE_TNC = 'TNC:'
DRIVE_PLC = 'PLC:'
DRIVE_LOG = 'LOG:'
DRIVE_LOG = 'SYS:'

# Majour control types
TYPE_MILL_NEW_STYLE = 1
TYPE_MILL_OLD_STYLE = 2
TYPE_LATHE_NEW_STYLE = 3
TYPE_UNKNOWN = -1

# files system attributes
FS_ENTRY_IS_HIDDEN = 0x08
FS_ENTRY_IS_DRIVE = 0x10
FS_ENTRY_IS_DIRECTORY = 0x20
FS_ENTRY_IS_PROTCTED = 0x40
FS_ENTRY_IS_IN_USE = 0x80

# const for login
LOGIN_INSPECT = 'INSPECT'  # login for read only functions
LOGIN_DIAG = 'DIAGNOSTICS'  # Logbuch / Recover
LOGIN_PLCDEBUG = 'PLCDEBUG'  # write access to PLC
LOGIN_FILETRANSFER = 'FILE'  # filesystem access to tnc drive
LOGIN_MONITOR = 'MONITOR'  # TNC remote access and screen dump
LOGIN_DSP = 'DSP'  # DSP functions
LOGIN_DNC = 'DNC'  # DNC functions
LOGIN_SCOPE = 'OSZI'  # Remote Scope
LOGIN_STREAMAXES = 'STREAMAXES'  # Streaming of axis data
LOGIN_FILEPLC = 'FILEPLC'  # file system access to plc drive
LOGIN_FILESYS = 'FILESYS'  # file system access to sys drive

# Memory types for reading from PLC memory
PLC_MEM_TYPE_MARKER = 1
PLC_MEM_TYPE_INPUT = 2
PLC_MEM_TYPE_OUTPUT = 3
PLC_MEM_TYPE_COUNTER = 4
PLC_MEM_TYPE_TIMER = 5
PLC_MEM_TYPE_BYTE = 6
PLC_MEM_TYPE_WORD = 7
PLC_MEM_TYPE_DWORD = 8
PLC_MEM_TYPE_STRING = 9
PLC_MEM_TYPE_INPUT_WORD = 10
PLC_MEM_TYPE_OUTPUT_WORD = 11

# const for relegram R_RI
RUN_INFO_EXEC_STATE = 23
RUN_INFO_SELECTED_PGM = 24
RUN_INFO_PGM_STATE = 26
RUN_INFO_CURRENT_TOOL = 51
RUN_INFO_OVERRIDE = 25
RUN_INFO_FIRST_ERROR = 27
RUN_INFO_NEXT_ERROR = 28

# known program states
PGM_STATE_STARTED = 0
PGM_STATE_STOPPED = 1
PGM_STATE_FINISHED = 2
PGM_STATE_CANCELLED = 3
PGM_STATE_INTERRUPTED = 4
PGM_STATE_ERROR = 5
PGM_STATE_ERROR_CLEARED = 6
PGM_STATE_IDLE = 7
PGM_STATE_UNDEFINED = 8

# known execution states
EXEC_STATE_MANUAL = 0
EXEC_STATE_MDI = 1
EXEC_STATE_PASS_REFERENCES = 2
EXEC_STATE_SINGLE_STEP = 3
EXEC_STATE_AUTOMATIC = 4
EXEC_STATE_UNDEFINED = 5

# key codes
KEY_LOWER_A = 0x0061
KEY_LOWER_B = 0x0062
KEY_LOWER_C = 0x0063
KEY_LOWER_D = 0x0064
KEY_LOWER_E = 0x0065
KEY_LOWER_F = 0x0066
KEY_LOWER_G = 0x0067
KEY_LOWER_H = 0x0068
KEY_LOWER_I = 0x0069
KEY_LOWER_J = 0x006A
KEY_LOWER_K = 0x006B
KEY_LOWER_L = 0x006C
KEY_LOWER_M = 0x006D
KEY_LOWER_N = 0x006E
KEY_LOWER_O = 0x006F
KEY_LOWER_P = 0x0070
KEY_LOWER_Q = 0x0071
KEY_LOWER_R = 0x0072
KEY_LOWER_S = 0x0073
KEY_LOWER_T = 0x0074
KEY_LOWER_U = 0x0075
KEY_LOWER_V = 0x0076
KEY_LOWER_W = 0x0077
KEY_LOWER_X = 0x0078
KEY_LOWER_Y = 0x0079
KEY_LOWER_Z = 0x007A

KEY_UPPER_A = 0x0041
KEY_UPPER_B = 0x0042
KEY_UPPER_C = 0x0043
KEY_UPPER_D = 0x0044
KEY_UPPER_E = 0x0045
KEY_UPPER_F = 0x0046
KEY_UPPER_G = 0x0047
KEY_UPPER_H = 0x0048
KEY_UPPER_I = 0x0049
KEY_UPPER_J = 0x004A
KEY_UPPER_K = 0x004B
KEY_UPPER_L = 0x004C
KEY_UPPER_M = 0x004D
KEY_UPPER_N = 0x004E
KEY_UPPER_O = 0x004F
KEY_UPPER_P = 0x0050
KEY_UPPER_Q = 0x0051
KEY_UPPER_R = 0x0052
KEY_UPPER_S = 0x0053
KEY_UPPER_T = 0x0054
KEY_UPPER_U = 0x0055
KEY_UPPER_V = 0x0056
KEY_UPPER_W = 0x0057
KEY_UPPER_X = 0x0058
KEY_UPPER_Y = 0x0059
KEY_UPPER_Z = 0x005A

KEY_NUMBER_0 = 0x0030
KEY_NUMBER_1 = 0x0031
KEY_NUMBER_2 = 0x0032
KEY_NUMBER_3 = 0x0033
KEY_NUMBER_4 = 0x0034
KEY_NUMBER_5 = 0x0035
KEY_NUMBER_6 = 0x0036
KEY_NUMBER_7 = 0x0037
KEY_NUMBER_8 = 0x0038
KEY_NUMBER_9 = 0x0039

KEY_BOTTOM_SK0 = 0x0180
KEY_BOTTOM_SK1 = 0x0181
KEY_BOTTOM_SK2 = 0x0182
KEY_BOTTOM_SK3 = 0x0183
KEY_BOTTOM_SK4 = 0x0184
KEY_BOTTOM_SK5 = 0x0185
KEY_BOTTOM_SK6 = 0x0186
KEY_BOTTOM_SK7 = 0x0187
KEY_BOTTOM_SK8 = 0x0188
KEY_BOTTOM_SK9 = 0x0189

KEY_RIGHT_SK0 = 0x0160
KEY_RIGHT_SK1 = 0x0161
KEY_RIGHT_SK2 = 0x0162
KEY_RIGHT_SK3 = 0x0163
KEY_RIGHT_SK4 = 0x0164
KEY_RIGHT_SK5 = 0x0165
KEY_RIGHT_SK6 = 0x0166
KEY_RIGHT_SK7 = 0x0167
KEY_RIGHT_SK8 = 0x0168

KEY_LEFT_SK0 = 0x0150
KEY_LEFT_SK1 = 0x0151
KEY_LEFT_SK2 = 0x0152
KEY_LEFT_SK3 = 0x0153
KEY_LEFT_SK4 = 0x0154
KEY_LEFT_SK5 = 0x0155
KEY_LEFT_SK6 = 0x0156
KEY_LEFT_SK7 = 0x0157
KEY_LEFT_SK8 = 0x0158
KEY_LEFT_SK9 = 0x0159

KEY_BACKSPACE = 0x0008
KEY_LINE_FEED = 0x000A
KEY_CARIDGE_RETURN = 0x000D
KEY_SPACE = 0x020
KEY_COLON = 0x03A
KEY_ZIF0 = 0x030

KEY_SK_NEXT = 0x019D
KEY_SK_PREVIOUS = 0x019E
KEY_ARROW_UP = 0x01A0

KEY_ARROW_DOWN = 0x01A1
KEY_ARROW_LEFT = 0x01A2
KEY_ARROW_RIGHT = 0x01A3

KEY_SPEC_ENT = 0x01A8
KEY_SPEC_NOENT = 0x01A9
KEY_SPEC_DEL = 0x01AB
KEY_SPEC_END = 0x01AC
KEY_SPEC_GOTO = 0x01AD
KEY_SPEC_CE = 0x01AE

KEY_AXIS_X = 0x01B0
KEY_AXIS_Y = 0x01B1
KEY_AXIS_Z = 0x01B2
KEY_ANGULAR_AXIS_1 = 0x01B3
KEY_ANGULAR_AXIS_2 = 0x01B4
KEY_TOGGEL_POLAR = 0x01B8
KEY_TOGGEL_INC = 0x01B9
KEY_PROG_Q = 0x01BA
KEY_ACTPOS = 0x01BB
KEY_TOGGEL_SIGN = 0x01BC
KEY_DECIMAL_POINT = 0x01BD
KEY_PROG_PGM_CALL = 0x01D0
KEY_PROG_TOOL_DEF = 0x01D1
KEY_PROG_TOOL_CALL = 0x01D2
KEY_PROG_CYC_DEF = 0x01D3
KEY_PROG_CYC_CAL = 0x01D4
KEY_PROG_LBL = 0x01D5
KEY_PROG_LBL_CALL = 0x01D6
KEY_PROG_L = 0x01D7
KEY_PROG_C = 0x01D8
KEY_PROG_CR = 0x01D9
KEY_PROG_CT = 0x01DA
KEY_PROG_CC = 0x01DB
KEY_PROG_RND = 0x01DC
KEY_PROG_CHF = 0x01DD
KEY_PROG_FK = 0x01DE
KEY_PROG_TOUCH_PROBE = 0x01DF
KEY_PROG_STOP = 0x01E0
KEY_PROG_APPR_DEP = 0x01E1

KEY_MODE_MANUAL = 0x01C0
KEY_MODE_SINGLE_STEP = 0x01C2
KEY_MODE_AUTOMATIC = 0x01C3
KEY_MODE_PGM_EDIT = 0x01C4
KEY_MODE_HANDWHEEL = 0x01C5
KEY_MODE_PGM_SIMULATION = 0x01C6
KEY_MOD_DIALOG = 0x01C7
KEY_PGMMGT = 0x01CB

KEY_TI = 0x01C1
KEY_HELP = 0x01ED
KEY_INFO = 0x01EE
KEY_CALC = 0x01EF

# Error map
LSV2_ERROR_T_ER_BAD_FORMAT = 20
LSV2_ERROR_T_ER_UNEXPECTED_TELE = 21
LSV2_ERROR_T_ER_UNKNOWN_TELE = 22
LSV2_ERROR_T_ER_NO_PRIV = 23
LSV2_ERROR_T_ER_WRONG_PARA = 24
LSV2_ERROR_T_ER_BREAK = 25
LSV2_ERROR_T_ER_BAD_KEY = 30
LSV2_ERROR_T_ER_BAD_FNAME = 31
LSV2_ERROR_T_ER_NO_FILE = 32
LSV2_ERROR_T_ER_OPEN_FILE = 33
LSV2_ERROR_T_ER_FILE_EXISTS = 34
LSV2_ERROR_T_ER_BAD_FILE = 35
LSV2_ERROR_T_ER_NO_DELETE = 36
LSV2_ERROR_T_ER_NO_NEW_FILE = 37
LSV2_ERROR_T_ER_NO_CHANGE_ATT = 38
LSV2_ERROR_T_ER_BAD_EMULATEKEY = 39
LSV2_ERROR_T_ER_NO_MP = 40
LSV2_ERROR_T_ER_NO_WIN = 41
LSV2_ERROR_T_ER_WIN_NOT_AKTIV = 42
LSV2_ERROR_T_ER_ANZ = 43
LSV2_ERROR_T_ER_FONT_NOT_DEFINED = 44
LSV2_ERROR_T_ER_FILE_ACCESS = 45
LSV2_ERROR_T_ER_WRONG_DNC_STATUS = 46
LSV2_ERROR_T_ER_CHANGE_PATH = 47
LSV2_ERROR_T_ER_NO_RENAME = 48
LSV2_ERROR_T_ER_NO_LOGIN = 49
LSV2_ERROR_T_ER_BAD_PARAMETER = 50
LSV2_ERROR_T_ER_BAD_NUMBER_FORMAT = 51
LSV2_ERROR_T_ER_BAD_MEMADR = 52
LSV2_ERROR_T_ER_NO_FREE_SPACE = 53
LSV2_ERROR_T_ER_DEL_DIR = 54
LSV2_ERROR_T_ER_NO_DIR = 55
LSV2_ERROR_T_ER_OPERATING_MODE = 56
LSV2_ERROR_T_ER_NO_NEXT_ERROR = 57
LSV2_ERROR_T_ER_ACCESS_TIMEOUT = 58
LSV2_ERROR_T_ER_NO_WRITE_ACCESS = 59
LSV2_ERROR_T_ER_STIB = 60
LSV2_ERROR_T_ER_REF_NECESSARY = 61
LSV2_ERROR_T_ER_PLC_BUF_FULL = 62
LSV2_ERROR_T_ER_NOT_FOUND = 63
LSV2_ERROR_T_ER_WRONG_FILE = 64
LSV2_ERROR_T_ER_NO_MATCH = 65
LSV2_ERROR_T_ER_TOO_MANY_TPTS = 66
LSV2_ERROR_T_ER_NOT_ACTIVATED = 67
LSV2_ERROR_T_ER_DSP_CHANNEL = 70
LSV2_ERROR_T_ER_DSP_PARA = 71
LSV2_ERROR_T_ER_OUT_OF_RANGE = 72
LSV2_ERROR_T_ER_INVALID_AXIS = 73
LSV2_ERROR_T_ER_STREAMING_ACTIVE = 74
LSV2_ERROR_T_ER_NO_STREAMING_ACTIVE = 75
LSV2_ERROR_T_ER_TO_MANY_OPEN_TCP = 80
LSV2_ERROR_T_ER_NO_FREE_HANDLE = 81
LSV2_ERROR_T_ER_PLCMEMREMA_CLEAR = 82
LSV2_ERROR_T_ER_OSZI_CHSEL = 83
LSV2_ERROR_LSV2_BUSY = 90
LSV2_ERROR_LSV2_X_BUSY = 91
LSV2_ERROR_LSV2_NOCONNECT = 92
LSV2_ERROR_LSV2_BAD_BACKUP_FILE = 93
LSV2_ERROR_LSV2_RESTORE_NOT_FOUND = 94
LSV2_ERROR_LSV2_DLL_NOT_INSTALLED = 95
LSV2_ERROR_LSV2_BAD_CONVERT_DLL = 96
LSV2_ERROR_LSV2_BAD_BACKUP_LIST = 97
LSV2_ERROR_LSV2_UNKNOWN_ERROR = 99
LSV2_ERROR_T_BD_NO_NEW_FILE = 100
LSV2_ERROR_T_BD_NO_FREE_SPACE = 101
LSV2_ERROR_T_BD_FILE_NOT_ALLOWED = 102
LSV2_ERROR_T_BD_BAD_FORMAT = 103
LSV2_ERROR_T_BD_BAD_BLOCK = 104
LSV2_ERROR_T_BD_END_PGM = 105
LSV2_ERROR_T_BD_ANZ = 106
LSV2_ERROR_T_BD_WIN_NOT_DEFINED = 107
LSV2_ERROR_T_BD_WIN_CHANGED = 108
LSV2_ERROR_T_BD_DNC_WAIT = 110
LSV2_ERROR_T_BD_CANCELLED = 111
LSV2_ERROR_T_BD_OSZI_OVERRUN = 112
LSV2_ERROR_T_BD_FD = 200
LSV2_ERROR_T_USER_ERROR = 255
