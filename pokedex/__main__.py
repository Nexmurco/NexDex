import curses
from pokedex.menu import Menu
from pokedex.calculator import Calculator
from pokedex.pokedex_menu import PokedexMenu
from pokedex.battle_menu import BattleMenu
from pokedex.main_menu import MainMenu
import math
import json
import os
import pytesseract
from PIL import Image
from PIL import ImageGrab
import win32gui
from time import sleep
import datetime
import re
from enum import Enum
import cv2
import numpy
import imagehash



nature_bonus = {}
nature_bonus["negative"] = 0.9
nature_bonus["netural"] = 1.0
nature_bonus["positive"] = 1.1

HAMMING_THRESHOLD = 5

DS_WIDTH = 256
DS_HEIGHT = 384

CHAR_A_UPPER_HASH = "8929f6f634b409cb"
CHAR_B_UPPER_HASH = "8909f636d4b636c9"
CHAR_C_UPPER_HASH = "8909fc7c90b6b4cb"
CHAR_D_UPPER_HASH = "8909f636c9f436c9"
CHAR_E_UPPER_HASH = "8101fc7cd47c7cd2"
CHAR_F_UPPER_HASH = "8321fcc97c7cb4c1"
CHAR_G_UPPER_HASH = "8903f47c49f6b683"
CHAR_H_UPPER_HASH = "8909f6cbb4b434d6"
CHAR_I_UPPER_HASH = "b131ce2ccbce2cc3"
CHAR_J_UPPER_HASH = "e949b63683f63483"
CHAR_K_UPPER_HASH = "8323fccde6b019b8"
CHAR_L_UPPER_HASH = "8303fc7cd0fc78d0"
CHAR_M_UPPER_HASH = "8909f6c3f3f02cac"
CHAR_N_UPPER_HASH = "8909f4c7e6f0999c"
CHAR_O_UPPER_HASH = "8909f634cbf434cb"
CHAR_P_UPPER_HASH = "8329fc96b4b4f0c9"
CHAR_Q_UPPER_HASH = "890bf63496de34c3"
CHAR_R_UPPER_HASH = "8921f4c936b6d9c9"
CHAR_S_UPPER_HASH = "a901967cf9f43683"
CHAR_T_UPPER_HASH = "b131ce0c0eced3d6"
CHAR_U_UPPER_HASH = "1010101010101010"
CHAR_V_UPPER_HASH = "8909c3b0bcccf3f4"
CHAR_W_UPPER_HASH = "8909f63e33f68c34"
CHAR_X_UPPER_HASH = "ac2cc34bb4f0d1bc"
CHAR_Y_UPPER_HASH = "a90dc9f1b0bcb4b4"
CHAR_Z_UPPER_HASH = "ac6cc30b98f327c6"
CHAR_A_LOWER_HASH = "a9b6d60949fc3c83"
CHAR_B_LOWER_HASH = "8301f4f8c9fc34f8"
CHAR_C_LOWER_HASH = "a900f40083007c00"
CHAR_D_LOWER_HASH = "e969f69483963496"
CHAR_E_LOWER_HASH = "a996d63c0bc93c36"
CHAR_F_LOWER_HASH = "b82dc7d2d2c70707"
CHAR_G_LOWER_HASH = "a983b6f9830b7934"
CHAR_H_LOWER_HASH = "8906f6c9c9fc3c34"
CHAR_I_LOWER_HASH = "9d1de2871de21ce2"
CHAR_J_LOWER_HASH = "b2e79832cd18e798"
CHAR_K_LOWER_HASH = "8303dee334fc4ce1"
CHAR_L_LOWER_HASH = "b131ce0e8ecef8c4"
CHAR_M_LOWER_HASH = "a336dccb49342736"
CHAR_N_LOWER_HASH = "8b36f6c9493c23e2"
CHAR_O_LOWER_HASH = "a900f6004b003400"
CHAR_P_LOWER_HASH = "83fcf686490b3636"
CHAR_Q_LOWER_HASH = "e9b4f4e901497c3c"
CHAR_R_LOWER_HASH = "836afc97096923f2"
CHAR_S_LOWER_HASH = "a929d6c9cbb62c49"
CHAR_T_LOWER_HASH = "bc1cc3e3dcc3231c"
CHAR_U_LOWER_HASH = "8983f67c0bcb2b83"
CHAR_V_LOWER_HASH = "a94fd3b03c4f034d"
CHAR_W_LOWER_HASH = "8bcbf63603cf0c43"
CHAR_X_LOWER_HASH = "ab00c60034000e00"
CHAR_Y_LOWER_HASH = "a983f67c830bc936"
CHAR_Z_LOWER_HASH = "a94bd6b4f44b29b0"
CHAR_SPACE_HASH = "8000000000000000"
CHAR_NUM_ZERO = "8b89f6b4c3f149c1" 
CHAR_NUM_ONE = "e6be1be6c1c441c3" 
CHAR_NUM_TWO = "a9c924b4f4e49cd9" 
CHAR_NUM_THREE = "e9a9348cf4b489dc" 
CHAR_NUM_FOUR = "a6bef97181c419cc" 
CHAR_NUM_FIVE = "898474e97c34c9fc" 
CHAR_NUM_SIX = "8984fce936b4c9d4" 
CHAR_NUM_SEVEN = "eb491bb321ae44d9" 
CHAR_NUM_EIGHT = "8b8bf4a4b6b4c9c1" 
CHAR_NUM_NINE = "a909b4f87434c9fc" 

#8b0bf434d131cbd3
#8b0bf434d131cbd3

class PokeType(Enum):
    NORMAL = 1
    FIRE = 2
    WATER = 3
    GRASS = 4
    ELECTRIC = 5
    ICE = 6
    FIGHTING = 7
    POISON = 8
    GROUND = 9
    FLYING = 10
    PSYCHIC = 11
    BUG = 12
    ROCK = 13
    GHOST = 14
    DRAGON = 15
    DARK = 16
    STEEL = 17

class Character(Enum):
    CHAR_A_UPPER = 1
    CHAR_B_UPPER = 2
    CHAR_C_UPPER = 3
    CHAR_D_UPPER = 4
    CHAR_E_UPPER = 5
    CHAR_F_UPPER = 6
    CHAR_G_UPPER = 7
    CHAR_H_UPPER = 8
    CHAR_I_UPPER = 9
    CHAR_J_UPPER = 10
    CHAR_K_UPPER = 11
    CHAR_L_UPPER = 12
    CHAR_M_UPPER = 13
    CHAR_N_UPPER = 14
    CHAR_O_UPPER = 15
    CHAR_P_UPPER = 16
    CHAR_Q_UPPER = 17
    CHAR_R_UPPER = 18
    CHAR_S_UPPER = 19
    CHAR_T_UPPER = 20
    CHAR_U_UPPER = 21
    CHAR_V_UPPER = 22
    CHAR_W_UPPER = 23
    CHAR_X_UPPER = 24
    CHAR_Y_UPPER = 25
    CHAR_Z_UPPER = 26
    CHAR_A_LOWER = 27
    CHAR_B_LOWER = 28
    CHAR_C_LOWER = 29
    CHAR_D_LOWER = 30
    CHAR_E_LOWER = 31
    CHAR_F_LOWER = 32
    CHAR_G_LOWER = 33
    CHAR_H_LOWER = 34
    CHAR_I_LOWER = 35
    CHAR_J_LOWER = 36
    CHAR_K_LOWER = 37
    CHAR_L_LOWER = 38
    CHAR_M_LOWER = 39
    CHAR_N_LOWER = 40
    CHAR_O_LOWER = 41
    CHAR_P_LOWER = 42
    CHAR_Q_LOWER = 43
    CHAR_R_LOWER = 44
    CHAR_S_LOWER = 45
    CHAR_T_LOWER = 46
    CHAR_U_LOWER = 47
    CHAR_V_LOWER = 48
    CHAR_W_LOWER = 49
    CHAR_X_LOWER = 50
    CHAR_Y_LOWER = 51
    CHAR_Z_LOWER = 52
    CHAR_SPACE =53
    CHAR_DASH =54
    CHAR_COMMA =55
    CHAR_PERIOD =56
    CHAR_COLON =57
    CHAR_SEMI_COLON =58
    CHAR_EXCLAMATION_POINT =59
    CHAR_QUESTION_MARK =60
    CHAR_QUOTATION_LEFT =61
    CHAR_QUOTATION_RIGHT =62
    CHAR_APOSTRAPHE_LEFT =63
    CHAR_APOSTRAPHE_RIGHT =64
    CHAR_PARENTHESIS_LEFT =65
    CHAR_PARENTHESIS_RIGHT =66
    CHAR_ELLIPSIS =67
    CHAR_BULLET =68
    CHAR_TILDE =69
    CHAR_AT_SIGN =70
    CHAR_GENDER_MALE =71
    CHAR_GENDER_FEMALE =72
    CHAR_HASH =73
    CHAR_PERCENT =74
    CHAR_PLUS =75
    CHAR_MINUS =76
    CHAR_ASTERISK =77
    CHAR_SLASH =78
    CHAR_EQUAL =79
    CHAR_SHAPE_TARGET =80
    CHAR_SHAPE_CIRCLE =81
    CHAR_SHAPE_SQUARE =82
    CHAR_SHAPE_TRIANGLE =83
    CHAR_SHAPE_KITE =84
    CHAR_SHAPE_SPADE =85
    CHAR_SHAPE_HEART =86
    CHAR_SHAPE_DIAMOND =87
    CHAR_SHAPE_CLUB =88
    CHAR_SHAPE_STAR =89
    CHAR_SHAPE_SUN =90
    CHAR_SHAPE_CLOUD =91
    CHAR_SHAPE_UMBRELLA =92
    CHAR_SHAPE_SNOWMAN =93
    CHAR_EMOTE_SMILE =94
    CHAR_EMOTE_LAUGH =95
    CHAR_EMOTE_YELL =96
    CHAR_EMOTE_ANGRY =97
    CHAR_EMOTE_SLEEP =98
    CHAR_SHAPE_ARROW_UP =99
    CHAR_SHAPE_ARROW_DOWN = 100
    CHAR_SHAPE_MUSIC_NOTE =101
    CHAR_NUM_ZERO = 102
    CHAR_NUM_ONE = 103
    CHAR_NUM_TWO = 104
    CHAR_NUM_THREE = 105
    CHAR_NUM_FOUR = 106
    CHAR_NUM_FIVE = 107
    CHAR_NUM_SIX = 108
    CHAR_NUM_SEVEN = 109
    CHAR_NUM_EIGHT = 110
    CHAR_NUM_NINE = 111

dict_char2str ={
    Character.CHAR_A_UPPER: "A",
    Character.CHAR_B_UPPER: "B",
    Character.CHAR_C_UPPER: "C",
    Character.CHAR_D_UPPER: "D",
    Character.CHAR_E_UPPER: "E",
    Character.CHAR_F_UPPER: "F",
    Character.CHAR_G_UPPER: "G",
    Character.CHAR_H_UPPER: "H",
    Character.CHAR_I_UPPER: "I",
    Character.CHAR_J_UPPER: "J",
    Character.CHAR_K_UPPER: "K",
    Character.CHAR_L_UPPER: "L",
    Character.CHAR_M_UPPER: "M",
    Character.CHAR_N_UPPER: "N",
    Character.CHAR_O_UPPER: "O",
    Character.CHAR_P_UPPER: "P",
    Character.CHAR_Q_UPPER: "Q",
    Character.CHAR_R_UPPER: "R",
    Character.CHAR_S_UPPER: "S",
    Character.CHAR_T_UPPER: "T",
    Character.CHAR_U_UPPER: "U",
    Character.CHAR_V_UPPER: "V",
    Character.CHAR_W_UPPER: "W",
    Character.CHAR_X_UPPER: "X",
    Character.CHAR_Y_UPPER: "Y",
    Character.CHAR_Z_UPPER: "Z",
    Character.CHAR_A_LOWER: "a",
    Character.CHAR_B_LOWER: "b",
    Character.CHAR_C_LOWER: "c",
    Character.CHAR_D_LOWER: "d",
    Character.CHAR_E_LOWER: "e",
    Character.CHAR_F_LOWER: "f",
    Character.CHAR_G_LOWER: "g",
    Character.CHAR_H_LOWER: "h",
    Character.CHAR_I_LOWER: "i",
    Character.CHAR_J_LOWER: "j",
    Character.CHAR_K_LOWER: "k",
    Character.CHAR_L_LOWER: "l",
    Character.CHAR_M_LOWER: "m",
    Character.CHAR_N_LOWER: "n",
    Character.CHAR_O_LOWER: "o",
    Character.CHAR_P_LOWER: "p",
    Character.CHAR_Q_LOWER: "q",
    Character.CHAR_R_LOWER: "r",
    Character.CHAR_S_LOWER: "s",
    Character.CHAR_T_LOWER: "t",
    Character.CHAR_U_LOWER: "u",
    Character.CHAR_V_LOWER: "v",
    Character.CHAR_W_LOWER: "w",
    Character.CHAR_X_LOWER: "x",
    Character.CHAR_Y_LOWER: "y",
    Character.CHAR_Z_LOWER: "z",
    Character.CHAR_NUM_ZERO: "0",
    Character.CHAR_NUM_ONE: "1",
    Character.CHAR_NUM_TWO: "2",
    Character.CHAR_NUM_THREE: "3",
    Character.CHAR_NUM_FOUR: "4",
    Character.CHAR_NUM_FIVE: "5",
    Character.CHAR_NUM_SIX: "6",
    Character.CHAR_NUM_SEVEN: "7",
    Character.CHAR_NUM_EIGHT: "8",
    Character.CHAR_NUM_NINE: "9",
    Character.CHAR_SPACE: " ",
    Character.CHAR_DASH: "-",
    Character.CHAR_COMMA: ",",
    Character.CHAR_PERIOD: ".",
    Character.CHAR_COLON: ":",
    Character.CHAR_SEMI_COLON: ";",
    Character.CHAR_EXCLAMATION_POINT: "!",
    Character.CHAR_QUESTION_MARK: "?",
    Character.CHAR_QUOTATION_LEFT: "\"",
    Character.CHAR_QUOTATION_RIGHT: "\"",
    Character.CHAR_APOSTRAPHE_LEFT: "'",
    Character.CHAR_APOSTRAPHE_RIGHT: "'",
    Character.CHAR_PARENTHESIS_LEFT: "(",
    Character.CHAR_PARENTHESIS_RIGHT: ")",
    Character.CHAR_ELLIPSIS: "…",
    Character.CHAR_BULLET: "•",
    Character.CHAR_TILDE: "~",
    Character.CHAR_AT_SIGN: "@",
    Character.CHAR_GENDER_MALE: "♂",
    Character.CHAR_GENDER_FEMALE: "♀",
    Character.CHAR_HASH: "#",
    Character.CHAR_PERCENT: "%",
    Character.CHAR_PLUS: "+",
    Character.CHAR_MINUS: "-",
    Character.CHAR_ASTERISK: "*",
    Character.CHAR_SLASH: "/",
    Character.CHAR_EQUAL: "=",
    Character.CHAR_SHAPE_TARGET: "⨀",
    Character.CHAR_SHAPE_CIRCLE: "○",
    Character.CHAR_SHAPE_SQUARE: "□",
    Character.CHAR_SHAPE_TRIANGLE: "△",
    Character.CHAR_SHAPE_KITE: "◇",
    Character.CHAR_SHAPE_SPADE: "♠",
    Character.CHAR_SHAPE_HEART: "♥",
    Character.CHAR_SHAPE_DIAMOND: "♦",
    Character.CHAR_SHAPE_CLUB: "♣",
    Character.CHAR_SHAPE_STAR: "★",
    Character.CHAR_SHAPE_SUN: "☼",
    Character.CHAR_SHAPE_CLOUD: "☁",
    Character.CHAR_SHAPE_UMBRELLA: "☂",
    Character.CHAR_SHAPE_SNOWMAN: "❆",
    Character.CHAR_EMOTE_SMILE: ":)",
    Character.CHAR_EMOTE_LAUGH: ":D",
    Character.CHAR_EMOTE_YELL: ":O",
    Character.CHAR_EMOTE_ANGRY: ">:|",
    Character.CHAR_EMOTE_SLEEP: "zZz",
    Character.CHAR_SHAPE_ARROW_UP: "↑",
    Character.CHAR_SHAPE_ARROW_DOWN: "↓",
    Character.CHAR_SHAPE_MUSIC_NOTE: "♪"
}


dict_char2hash ={
    Character.CHAR_A_UPPER: CHAR_A_UPPER_HASH,
    Character.CHAR_B_UPPER: CHAR_B_UPPER_HASH,
    Character.CHAR_C_UPPER: CHAR_C_UPPER_HASH,
    Character.CHAR_D_UPPER: CHAR_D_UPPER_HASH,
    Character.CHAR_E_UPPER: CHAR_E_UPPER_HASH,
    Character.CHAR_F_UPPER: CHAR_F_UPPER_HASH,
    Character.CHAR_G_UPPER: CHAR_G_UPPER_HASH,
    Character.CHAR_H_UPPER: CHAR_H_UPPER_HASH,
    Character.CHAR_I_UPPER: CHAR_I_UPPER_HASH,
    Character.CHAR_J_UPPER: CHAR_J_UPPER_HASH,
    Character.CHAR_K_UPPER: CHAR_K_UPPER_HASH,
    Character.CHAR_L_UPPER: CHAR_L_UPPER_HASH,
    Character.CHAR_M_UPPER: CHAR_M_UPPER_HASH,
    Character.CHAR_N_UPPER: CHAR_N_UPPER_HASH,
    Character.CHAR_O_UPPER: CHAR_O_UPPER_HASH,
    Character.CHAR_P_UPPER: CHAR_P_UPPER_HASH,
    Character.CHAR_Q_UPPER: CHAR_Q_UPPER_HASH,
    Character.CHAR_R_UPPER: CHAR_R_UPPER_HASH,
    Character.CHAR_S_UPPER: CHAR_S_UPPER_HASH,
    Character.CHAR_T_UPPER: CHAR_T_UPPER_HASH,
    Character.CHAR_U_UPPER: CHAR_U_UPPER_HASH,
    Character.CHAR_V_UPPER: CHAR_V_UPPER_HASH,
    Character.CHAR_W_UPPER: CHAR_W_UPPER_HASH,
    Character.CHAR_X_UPPER: CHAR_X_UPPER_HASH,
    Character.CHAR_Y_UPPER: CHAR_Y_UPPER_HASH,
    Character.CHAR_Z_UPPER: CHAR_Z_UPPER_HASH,
    Character.CHAR_A_LOWER: CHAR_A_LOWER_HASH,
    Character.CHAR_B_LOWER: CHAR_B_LOWER_HASH,
    Character.CHAR_C_LOWER: CHAR_C_LOWER_HASH,
    Character.CHAR_D_LOWER: CHAR_D_LOWER_HASH,
    Character.CHAR_E_LOWER: CHAR_E_LOWER_HASH,
    Character.CHAR_F_LOWER: CHAR_F_LOWER_HASH,
    Character.CHAR_G_LOWER: CHAR_G_LOWER_HASH,
    Character.CHAR_H_LOWER: CHAR_H_LOWER_HASH,
    Character.CHAR_I_LOWER: CHAR_I_LOWER_HASH,
    Character.CHAR_J_LOWER: CHAR_J_LOWER_HASH,
    Character.CHAR_K_LOWER: CHAR_K_LOWER_HASH,
    Character.CHAR_L_LOWER: CHAR_L_LOWER_HASH,
    Character.CHAR_M_LOWER: CHAR_M_LOWER_HASH,
    Character.CHAR_N_LOWER: CHAR_N_LOWER_HASH,
    Character.CHAR_O_LOWER: CHAR_O_LOWER_HASH,
    Character.CHAR_P_LOWER: CHAR_P_LOWER_HASH,
    Character.CHAR_Q_LOWER: CHAR_Q_LOWER_HASH,
    Character.CHAR_R_LOWER: CHAR_R_LOWER_HASH,
    Character.CHAR_S_LOWER: CHAR_S_LOWER_HASH,
    Character.CHAR_T_LOWER: CHAR_T_LOWER_HASH,
    Character.CHAR_U_LOWER: CHAR_U_LOWER_HASH,
    Character.CHAR_V_LOWER: CHAR_V_LOWER_HASH,
    Character.CHAR_W_LOWER: CHAR_W_LOWER_HASH,
    Character.CHAR_X_LOWER: CHAR_X_LOWER_HASH,
    Character.CHAR_Y_LOWER: CHAR_Y_LOWER_HASH,
    Character.CHAR_Z_LOWER: CHAR_Z_LOWER_HASH,
    Character.CHAR_SPACE: CHAR_SPACE_HASH,
    Character.CHAR_NUM_ZERO: CHAR_NUM_ZERO,
    Character.CHAR_NUM_ONE: CHAR_NUM_ONE,
    Character.CHAR_NUM_TWO: CHAR_NUM_TWO,
    Character.CHAR_NUM_THREE: CHAR_NUM_THREE,
    Character.CHAR_NUM_FOUR: CHAR_NUM_FOUR,
    Character.CHAR_NUM_FIVE: CHAR_NUM_FIVE,
    Character.CHAR_NUM_SIX: CHAR_NUM_SIX,
    Character.CHAR_NUM_SEVEN: CHAR_NUM_SEVEN,
    Character.CHAR_NUM_EIGHT: CHAR_NUM_EIGHT,
    Character.CHAR_NUM_NINE: CHAR_NUM_NINE,
    Character.CHAR_DASH: "-",
    Character.CHAR_COMMA: ",",
    Character.CHAR_PERIOD: ".",
    Character.CHAR_COLON: ":",
    Character.CHAR_SEMI_COLON: ";",
    Character.CHAR_EXCLAMATION_POINT: "!",
    Character.CHAR_QUESTION_MARK: "?",
    Character.CHAR_QUOTATION_LEFT: "\"",
    Character.CHAR_QUOTATION_RIGHT: "\"",
    Character.CHAR_APOSTRAPHE_LEFT: "'",
    Character.CHAR_APOSTRAPHE_RIGHT: "'",
    Character.CHAR_PARENTHESIS_LEFT: "(",
    Character.CHAR_PARENTHESIS_RIGHT: ")",
    Character.CHAR_ELLIPSIS: "…",
    Character.CHAR_BULLET: "•",
    Character.CHAR_TILDE: "~",
    Character.CHAR_AT_SIGN: "@",
    Character.CHAR_GENDER_MALE: "♂",
    Character.CHAR_GENDER_FEMALE: "♀",
    Character.CHAR_HASH: "#",
    Character.CHAR_PERCENT: "%",
    Character.CHAR_PLUS: "+",
    Character.CHAR_MINUS: "-",
    Character.CHAR_ASTERISK: "*",
    Character.CHAR_SLASH: "/",
    Character.CHAR_EQUAL: "=",
    Character.CHAR_SHAPE_TARGET: "⨀",
    Character.CHAR_SHAPE_CIRCLE: "○",
    Character.CHAR_SHAPE_SQUARE: "□",
    Character.CHAR_SHAPE_TRIANGLE: "△",
    Character.CHAR_SHAPE_KITE: "◇",
    Character.CHAR_SHAPE_SPADE: "♠",
    Character.CHAR_SHAPE_HEART: "♥",
    Character.CHAR_SHAPE_DIAMOND: "♦",
    Character.CHAR_SHAPE_CLUB: "♣",
    Character.CHAR_SHAPE_STAR: "★",
    Character.CHAR_SHAPE_SUN: "☼",
    Character.CHAR_SHAPE_CLOUD: "☁",
    Character.CHAR_SHAPE_UMBRELLA: "☂",
    Character.CHAR_SHAPE_SNOWMAN: "❆",
    Character.CHAR_EMOTE_SMILE: ":)",
    Character.CHAR_EMOTE_LAUGH: ":D",
    Character.CHAR_EMOTE_YELL: ":O",
    Character.CHAR_EMOTE_ANGRY: ">:|",
    Character.CHAR_EMOTE_SLEEP: "zZz",
    Character.CHAR_SHAPE_ARROW_UP: "↑",
    Character.CHAR_SHAPE_ARROW_DOWN: "↓",
    Character.CHAR_SHAPE_MUSIC_NOTE: "♪"
}

dict_width2charhash = {
    3: [
        CHAR_I_LOWER_HASH
    ],

    4: [
        CHAR_L_LOWER_HASH,
        CHAR_SPACE_HASH
    ],
    5: [
        CHAR_J_LOWER_HASH,
        CHAR_F_LOWER_HASH
    ],
    6: [
        CHAR_SPACE_HASH,
        CHAR_A_UPPER_HASH,
        CHAR_B_UPPER_HASH,
        CHAR_C_UPPER_HASH,
        CHAR_D_UPPER_HASH,
        CHAR_E_UPPER_HASH,
        CHAR_F_UPPER_HASH,
        CHAR_G_UPPER_HASH,
        CHAR_H_UPPER_HASH,
        CHAR_I_UPPER_HASH,
        CHAR_J_UPPER_HASH,
        CHAR_K_UPPER_HASH,
        CHAR_L_UPPER_HASH,
        CHAR_M_UPPER_HASH,
        CHAR_N_UPPER_HASH,
        CHAR_O_UPPER_HASH,
        CHAR_P_UPPER_HASH,
        CHAR_Q_UPPER_HASH,
        CHAR_R_UPPER_HASH,
        CHAR_S_UPPER_HASH,
        CHAR_T_UPPER_HASH,
        CHAR_U_UPPER_HASH,
        CHAR_V_UPPER_HASH,
        CHAR_W_UPPER_HASH,
        CHAR_X_UPPER_HASH,
        CHAR_Y_UPPER_HASH,
        CHAR_Z_UPPER_HASH,
        CHAR_A_LOWER_HASH,
        CHAR_B_LOWER_HASH,
        CHAR_C_LOWER_HASH,
        CHAR_D_LOWER_HASH,
        CHAR_E_LOWER_HASH,
        CHAR_G_LOWER_HASH,
        CHAR_H_LOWER_HASH,
        CHAR_K_LOWER_HASH,
        CHAR_M_LOWER_HASH,
        CHAR_N_LOWER_HASH,
        CHAR_O_LOWER_HASH,
        CHAR_P_LOWER_HASH,
        CHAR_Q_LOWER_HASH,
        CHAR_R_LOWER_HASH,
        CHAR_S_LOWER_HASH,
        CHAR_T_LOWER_HASH,
        CHAR_U_LOWER_HASH,
        CHAR_V_LOWER_HASH,
        CHAR_W_LOWER_HASH,
        CHAR_X_LOWER_HASH,
        CHAR_Y_LOWER_HASH,
        CHAR_Z_LOWER_HASH,
        CHAR_NUM_ZERO,
        CHAR_NUM_ONE,
        CHAR_NUM_TWO,
        CHAR_NUM_THREE,
        CHAR_NUM_FOUR,
        CHAR_NUM_FIVE,
        CHAR_NUM_SIX,
        CHAR_NUM_SEVEN,
        CHAR_NUM_EIGHT,
        CHAR_NUM_NINE,
    ]
}

dict_hash2char = {
    CHAR_A_UPPER_HASH: Character.CHAR_A_UPPER,
    CHAR_B_UPPER_HASH: Character.CHAR_B_UPPER,
    CHAR_C_UPPER_HASH: Character.CHAR_C_UPPER,
    CHAR_D_UPPER_HASH: Character.CHAR_D_UPPER,
    CHAR_E_UPPER_HASH: Character.CHAR_E_UPPER,
    CHAR_F_UPPER_HASH: Character.CHAR_F_UPPER,
    CHAR_G_UPPER_HASH: Character.CHAR_G_UPPER,
    CHAR_H_UPPER_HASH: Character.CHAR_H_UPPER,
    CHAR_I_UPPER_HASH: Character.CHAR_I_UPPER,
    CHAR_J_UPPER_HASH: Character.CHAR_J_UPPER,
    CHAR_K_UPPER_HASH: Character.CHAR_K_UPPER,
    CHAR_L_UPPER_HASH: Character.CHAR_L_UPPER,
    CHAR_M_UPPER_HASH: Character.CHAR_M_UPPER,
    CHAR_N_UPPER_HASH: Character.CHAR_N_UPPER,
    CHAR_O_UPPER_HASH: Character.CHAR_O_UPPER,
    CHAR_P_UPPER_HASH: Character.CHAR_P_UPPER,
    CHAR_Q_UPPER_HASH: Character.CHAR_Q_UPPER,
    CHAR_R_UPPER_HASH: Character.CHAR_R_UPPER,
    CHAR_S_UPPER_HASH: Character.CHAR_S_UPPER,
    CHAR_T_UPPER_HASH: Character.CHAR_T_UPPER,
    CHAR_U_UPPER_HASH: Character.CHAR_U_UPPER,
    CHAR_V_UPPER_HASH: Character.CHAR_V_UPPER,
    CHAR_W_UPPER_HASH: Character.CHAR_W_UPPER,
    CHAR_X_UPPER_HASH: Character.CHAR_X_UPPER,
    CHAR_Y_UPPER_HASH: Character.CHAR_Y_UPPER,
    CHAR_Z_UPPER_HASH: Character.CHAR_Z_UPPER,
    CHAR_A_LOWER_HASH: Character.CHAR_A_LOWER,
    CHAR_B_LOWER_HASH: Character.CHAR_B_LOWER,
    CHAR_C_LOWER_HASH: Character.CHAR_C_LOWER,
    CHAR_D_LOWER_HASH: Character.CHAR_D_LOWER,
    CHAR_E_LOWER_HASH: Character.CHAR_E_LOWER,
    CHAR_F_LOWER_HASH: Character.CHAR_F_LOWER,
    CHAR_G_LOWER_HASH: Character.CHAR_G_LOWER,
    CHAR_H_LOWER_HASH: Character.CHAR_H_LOWER,
    CHAR_I_LOWER_HASH: Character.CHAR_I_LOWER,
    CHAR_J_LOWER_HASH: Character.CHAR_J_LOWER,
    CHAR_K_LOWER_HASH: Character.CHAR_K_LOWER,
    CHAR_L_LOWER_HASH: Character.CHAR_L_LOWER,
    CHAR_M_LOWER_HASH: Character.CHAR_M_LOWER,
    CHAR_N_LOWER_HASH: Character.CHAR_N_LOWER,
    CHAR_O_LOWER_HASH: Character.CHAR_O_LOWER,
    CHAR_P_LOWER_HASH: Character.CHAR_P_LOWER,
    CHAR_Q_LOWER_HASH: Character.CHAR_Q_LOWER,
    CHAR_R_LOWER_HASH: Character.CHAR_R_LOWER,
    CHAR_S_LOWER_HASH: Character.CHAR_S_LOWER,
    CHAR_T_LOWER_HASH: Character.CHAR_T_LOWER,
    CHAR_U_LOWER_HASH: Character.CHAR_U_LOWER,
    CHAR_V_LOWER_HASH: Character.CHAR_V_LOWER,
    CHAR_W_LOWER_HASH: Character.CHAR_W_LOWER,
    CHAR_X_LOWER_HASH: Character.CHAR_X_LOWER,
    CHAR_Y_LOWER_HASH: Character.CHAR_Y_LOWER,
    CHAR_Z_LOWER_HASH: Character.CHAR_Z_LOWER,
    CHAR_SPACE_HASH: Character.CHAR_SPACE,
    CHAR_NUM_ZERO: Character.CHAR_NUM_ZERO,
    CHAR_NUM_ONE: Character.CHAR_NUM_ONE,
    CHAR_NUM_TWO: Character.CHAR_NUM_TWO,
    CHAR_NUM_THREE: Character.CHAR_NUM_THREE,
    CHAR_NUM_FOUR: Character.CHAR_NUM_FOUR,
    CHAR_NUM_FIVE: Character.CHAR_NUM_FIVE,
    CHAR_NUM_SIX: Character.CHAR_NUM_SIX,
    CHAR_NUM_SEVEN: Character.CHAR_NUM_SEVEN,
    CHAR_NUM_EIGHT: Character.CHAR_NUM_EIGHT,
    CHAR_NUM_NINE: Character.CHAR_NUM_NINE,
}

'''
    "": Character.CHAR_SPACE,
    "": Character.CHAR_DASH,
    "": Character.CHAR_COMMA,
    "": Character.CHAR_PERIOD,
    "": Character.CHAR_COLON,
    "": Character.CHAR_SEMI_COLON,
    "": Character.CHAR_EXCLAMATION_POINT,
    "": Character.CHAR_QUESTION_MARK,
    "": Character.CHAR_QUOTATION_LEFT,
    "": Character.CHAR_QUOTATION_RIGHT,
    "": Character.CHAR_APOSTRAPHE_LEFT,
    "": Character.CHAR_APOSTRAPHE_RIGHT,
    "": Character.CHAR_PARENTHESIS_LEFT,
    "": Character.CHAR_PARENTHESIS_RIGHT,
    "": Character.CHAR_ELLIPSIS,
    "": Character.CHAR_BULLET,
    "": Character.CHAR_TILDE,
    "": Character.CHAR_AT_SIGN,
    "": Character.CHAR_GENDER_MALE,
    "": Character.CHAR_GENDER_FEMALE,
    "": Character.CHAR_HASH,
    "": Character.CHAR_PERCENT,
    "": Character.CHAR_PLUS,
    "": Character.CHAR_MINUS,
    "": Character.CHAR_ASTERISK,
    "": Character.CHAR_SLASH,
    "": Character.CHAR_EQUAL,
    "": Character.CHAR_SHAPE_TARGET,
    "": Character.CHAR_SHAPE_CIRCLE,
    "": Character.CHAR_SHAPE_SQUARE,
    "": Character.CHAR_SHAPE_TRIANGLE,
    "": Character.CHAR_SHAPE_KITE,
    "": Character.CHAR_SHAPE_SPADE,
    "": Character.CHAR_SHAPE_HEART,
    "": Character.CHAR_SHAPE_DIAMOND,
    "": Character.CHAR_SHAPE_CLUB,
    "": Character.CHAR_SHAPE_STAR,
    "": Character.CHAR_SHAPE_SUN,
    "": Character.CHAR_SHAPE_CLOUD,
    "": Character.CHAR_SHAPE_UMBRELLA,
    "": Character.CHAR_SHAPE_SNOWMAN,
    "": Character.CHAR_EMOTE_SMILE,
    "": Character.CHAR_EMOTE_LAUGH,
    "": Character.CHAR_EMOTE_YELL,
    "": Character.CHAR_EMOTE_ANGRY,
    "": Character.CHAR_EMOTE_SLEEP,
    "": Character.CHAR_SHAPE_ARROW_UP,
    "": Character.CHAR_SHAPE_ARROW_DOWN,
    "": Character.CHAR_SHAPE_MUSIC_NOTE
'''

class Gamestate(Enum):
    BATTLE = 1
    OVERWORLD = 2
    MENU_POKEMON = 3
    MENU_BLUE = 4
    MENU_RED = 5
    MENU_YELLOW = 6

gamestate_name_dict = {
    Gamestate.BATTLE: "Battle", 
    Gamestate.OVERWORLD: "Overworld",
    Gamestate.MENU_POKEMON: "Pokemon Menu",
    Gamestate.MENU_BLUE: "Info Menu",
    Gamestate.MENU_RED: "Moves Menu",
    Gamestate.MENU_YELLOW: "Ribbon Menu"
}

#(Left, Top, Right, Bottom)
#percentage scaling in terms of width and height
dict_types2hash = {
    PokeType.NORMAL: "dfd02aa0f6d989c4",
    PokeType.FIRE: "d0c02faebbb19ec0",
    PokeType.WATER: "d5953ae2e4ad91c4",
    PokeType.GRASS: "c0c13bb8cdfe3a81",
    PokeType.ELECTRIC: "ff8488d081ad6f93",
    PokeType.ICE: "ebc29cb585ad62c1",
    PokeType.FIGHTING: "90c16f8ebaba8e85",
    PokeType.POISON: "85e07a8fbbe18e90",
    PokeType.GROUND: "f79068ad92923f94",
    PokeType.FLYING: "97946bc1b694cb94",
    PokeType.PSYCHIC: "b5f46a83b6d48983",
    PokeType.BUG: "c2c33fa49f88ea94",
    PokeType.ROCK: "c0c03bbbe6e49f90",
    PokeType.GHOST: "c0943feaeacb9894",
    PokeType.DRAGON: "e5e17a9a8981f6c4",
    PokeType.DARK: "d0d12fa4eebbb084",
    PokeType.STEEL: "eec1619417ec3cc5",
}

dict_types2string = {
    PokeType.NORMAL: "NORMAL",
    PokeType.FIRE: "FIRE",
    PokeType.WATER: "WATER",
    PokeType.GRASS: "GRASS",
    PokeType.ELECTRIC: "ELECTRIC",
    PokeType.ICE: "ICE",
    PokeType.FIGHTING: "FIGHTING",
    PokeType.POISON: "POISON",
    PokeType.GROUND: "GROUND",
    PokeType.FLYING: "FLYING",
    PokeType.PSYCHIC: "PSYCHIC",
    PokeType.BUG: "BUG",
    PokeType.ROCK: "ROCK",
    PokeType.GHOST: "GHOST",
    PokeType.DRAGON: "DRAGON",
    PokeType.DARK: "DARK",
    PokeType.STEEL: "STEEL",
}

#level 8943f636d3338b13
#stats 890bb434d333cbd3

dict_int2hash = {
    "0": "890bb434d333cbd3",
    "1": "e43c9966dbe4c1c4",
    "2": "a9690d36f464dc39",
    "3": "a96b3409f434cb7c",
    "4": "a434f87983e33b62",
    "5": "a90334697c36cb7c",
    "6": "8b07fc693436c3b4",
    "7": "a96b0b3b232c273b",
    "8": "a90bb60bb434cb3e",
    "9": "a909b67cf434c3b4",
    "": "8000000000000000"
}

dict_hash2int = {
    "890bb434d333cbd3": "0",
    "e43c9966dbe4c1c4": "1",
    "a9690d36f464dc39": "2",
    "a96b3409f434cb7c": "3",
    "a434f87983e33b62": "4",
    "a90334697c36cb7c": "5",
    "8b07fc693436c3b4": "6",
    "a96b0b3b232c273b": "7",
    "a90bb60bb434cb3e": "8",
    "a909b67cf434c3b4": "9",
    "8000000000000000": ""
}

dict_gender2hash = {
    "Male": "a333b54afc34c383",
    "Female": "a34edc353cb50c33",
    "None": "8000000000000000",
}

dict_hash2gender = {
    "a333b54afc34c383": "Male",
    "a34edc353cb50c33": "Female",
    "8000000000000000": "None"
}

dict_hash2ball = {
    "c663b9343091e6cf": "Poke Ball",
    "c62eb9653191e6ca": "Great Ball",
    "1010101010101011": "Ultra Ball",
    "6969696969696969": "Master Ball",
    "c36bbe24309166cf": "Safari Ball",
    "c3313e4c3991e69b": "Level Ball",
    "1010101010101012": "Moon Ball",
    "1010101010101013": "Lure Ball",
    "1010101010101014": "Dive Ball",
    "1010101010101015": "Friend Ball",
    "c6d83f94744b92d8": "Luxury Ball",
    "1010101010101016": "Cherish Ball",
    "1010101010101017": "Love Ball",
    "c3913f6e3191e41b": "Premier Ball",
    "1010101010101018": "Heavy Ball",
    "c7a5ba643491e68b": "Fast Ball",
    "1010101010101019": "Repeat Ball",
    "c2722e4dd1d1671b": "Timer Ball",
    "1010101010101010": "Nest Ball",
    "1010101010101020": "Net Ball",
    "c2b43b4e3191e69b": "Quick Ball",
    "c0cb3f663490679b": "Heal Ball",
    "1010101010101021": "Dusk Ball",
    "1010101010101022": "Park Ball"
}

dict_ball2hash = {
    "Poke Ball": "c663b9343091e6cf",
    "Great Ball": "c62eb9653191e6ca",
    "Ultra Ball": "",
    "Master Ball": "",
    "Safari Ball": "c36bbe24309166cf",
    "Level Ball": "c3313e4c3991e69b",
    "Moon Ball": "",
    "Lure Ball": "",
    "Dive Ball": "",
    "Friend Ball": "",
    "Luxury Ball": "c6d83f94744b92d8",
    "Cherish Ball": "",
    "Love Ball": "",
    "Premier Ball": "c3913f6e3191e41b",
    "Heavy Ball": "",
    "Fast Ball": "c7a5ba643491e68b",
    "Repeat Ball": "",
    "Timer Ball": "c2722e4dd1d1671b",
    "Nest Ball": "",
    "Net Ball": "",
    "Quick Ball": "c2b43b4e3191e69b",
    "Heal Ball": "c0cb3f663490679b",
    "Dusk Ball": "",
    "Park Ball": ""
}

dict_hash2types = {
    "d7d02aa0f6d9a9c4": PokeType.NORMAL,
    "d0c02fa6bbb19ec1": PokeType.FIRE,
    "d1953ae2e4ad93c4": PokeType.WATER,
    "c0c13fb8cdee3a81": PokeType.GRASS,
    "ff8488d081ad6f93": PokeType.ELECTRIC,
    "ebd29ca487ad62c1": PokeType.ICE,
    "90c16f8ebaba8e85": PokeType.FIGHTING,
    "85e07a8fbbe18e90": PokeType.POISON,
    "b79069ad92923f94": PokeType.GROUND,
    "97946bc1b694cb94": PokeType.FLYING,
    "b5f46a83b6d48983": PokeType.PSYCHIC,
    "c2c33fb49b88ea94": PokeType.BUG,
    "c0c03b9fe6e49f90": PokeType.ROCK,
    "c0843feaeecb9894": PokeType.GHOST,
    "e5c17a9aa981f6c4": PokeType.DRAGON,
    "d0d13fa4eeb3b084": PokeType.DARK,
    "eec1619417ec3cc5": PokeType.STEEL,
}

image_inversion_dictionary ={
    Gamestate.BATTLE: True,
    Gamestate.OVERWORLD: False,
    Gamestate.MENU_POKEMON: True,
    Gamestate.MENU_BLUE: False,
    Gamestate.MENU_RED: False,
    Gamestate.MENU_YELLOW: True
}

pokemon_box_overview_offset_dict = {
    "Nickname": (8, 58, 68, 71)
}



class MenuSetting(Enum):
    OFFSET = 1
    INVERT_BOOL = 2
    THRESHOLD_BINARIZE = 3
    IS_TEXT = 4
    DEBUG = 5
    IS_ACTIVE = 6
    IS_GRAYSCALE = 7
    IS_BINARIZE = 8
    THRESHOLD_HAMMING = 9
    TEXT_LENGTH = 10
    NAME = 11
    HASH_DICT = 12
    ALIGN_CENTER = 13

class MenuRedPOI(Enum):
    STAT_HP_CUR_0 = 1
    STAT_HP_CUR_1 = 10
    STAT_HP_CUR_2 = 100
    STAT_HP_MAX_0 = 2
    STAT_HP_MAX_1 = 20
    STAT_HP_MAX_2 = 200
    STAT_ATK_0 = 3
    STAT_ATK_1 = 30
    STAT_ATK_2 = 300
    STAT_DEF_0 = 4
    STAT_DEF_1 = 40
    STAT_DEF_2 = 400
    STAT_SPEC_ATK_0 = 5
    STAT_SPEC_ATK_1 = 50
    STAT_SPEC_ATK_2 = 500
    STAT_SPEC_DEF_0 = 6
    STAT_SPEC_DEF_1 = 60
    STAT_SPEC_DEF_2 = 600
    STAT_SPEED_0 = 26
    STAT_SPEED_1 = 260
    STAT_SPEED_2 = 2600
    ABILITY_NAME = 7
    ABILITY_DESC_1 = 8
    ABILITY_DESC_2 = 9
    MOVE_1_NAME = 10
    MOVE_1_TYPE = 11
    MOVE_1_PP_CUR_0 = 12
    MOVE_1_PP_CUR_1 = 120
    MOVE_1_PP_CUR_2 = 1200
    MOVE_1_PP_MAX_0 = 13
    MOVE_1_PP_MAX_1 = 130
    MOVE_1_PP_MAX_2 = 1300
    MOVE_2_NAME = 14
    MOVE_2_TYPE = 15
    MOVE_2_PP_CUR_0 = 16
    MOVE_2_PP_CUR_1 = 160
    MOVE_2_PP_CUR_2 = 1600
    MOVE_2_PP_MAX_0 = 17
    MOVE_2_PP_MAX_1 = 170
    MOVE_2_PP_MAX_2 = 1700
    MOVE_3_NAME = 18
    MOVE_3_TYPE = 19
    MOVE_3_PP_CUR_0 = 20
    MOVE_3_PP_CUR_1 = 200
    MOVE_3_PP_CUR_2 = 2000
    MOVE_3_PP_MAX_0 = 21
    MOVE_3_PP_MAX_1 = 210
    MOVE_3_PP_MAX_2 = 2100
    MOVE_4_NAME = 22
    MOVE_4_TYPE = 23
    MOVE_4_PP_CUR_0 = 24
    MOVE_4_PP_CUR_1 = 240
    MOVE_4_PP_CUR_2 = 2400
    MOVE_4_PP_MAX_0 = 25
    MOVE_4_PP_MAX_1 = 250
    MOVE_4_PP_MAX_2 = 2500
    

class MenuBluePOI(Enum):
    NATURE = 1
    CATCH_DATE = 2
    CATCH_LOCATION = 3
    CATCH_LEVEL_0 = 4
    CATCH_LEVEL_1 = 4
    CATCH_LEVEL_2 = 4
    PERSONALITY = 5
    DEX_NUMBER = 6
    DEX_NAME = 7
    TYPE_MONO = 8
    TYPE_SPLIT_1 = 9
    TYPE_SPLIT_2 = 10
    TRAINER_NAME = 11
    TRAINER_ID = 12
    EXP_CUR = 13
    EXP_NXT = 14

class MenuAllPOI(Enum):
    POKEBALL = 1
    NICKNAME = 2
    GENDER = 3
    IMAGE = 4
    ITEM = 5
    MARKINGS = 6
    POKERUS_INFECTED = 7
    POKERUS_IMMUNE = 8
    LEVEL_0 = 9
    LEVEL_1 = 10
    LEVEL_2 = 11

class GamestateSetting(Enum):
    ADJACENCIES = 1
    OFFSET = 2
    HASH_DICT = 3
    NAME = 4
    SCANS = 5
    THRESHOLD_HAMMING = 6
    IS_ACTIVE = 7



HAMMING_THRESHOLD_NUMBERS = 10

pokemon_menu_red_dict = {

    MenuRedPOI.STAT_HP_MAX_0: {
        MenuSetting.OFFSET: (119,27,125,37),
        MenuSetting.DEBUG: False,
        MenuSetting.IS_TEXT: True,
        MenuSetting.IS_ACTIVE: True,

        MenuSetting.IS_GRAYSCALE: True,

        MenuSetting.IS_BINARIZE: True,
        MenuSetting.THRESHOLD_BINARIZE: 100,
        MenuSetting.INVERT_BOOL: False,

        MenuSetting.THRESHOLD_HAMMING: HAMMING_THRESHOLD_NUMBERS,
        MenuSetting.HASH_DICT: dict_hash2int
    },
        MenuRedPOI.STAT_HP_MAX_1: {
        MenuSetting.OFFSET: (125,27,131,37),
        MenuSetting.DEBUG: False,
        MenuSetting.IS_TEXT: True,
        MenuSetting.IS_ACTIVE: True,

        MenuSetting.IS_GRAYSCALE: True,

        MenuSetting.IS_BINARIZE: True,
        MenuSetting.THRESHOLD_BINARIZE: 100,
        MenuSetting.INVERT_BOOL: False,

        MenuSetting.THRESHOLD_HAMMING: HAMMING_THRESHOLD_NUMBERS,
        MenuSetting.HASH_DICT: dict_hash2int
    },
        MenuRedPOI.STAT_HP_MAX_2: {
        MenuSetting.OFFSET: (131,27,137,37),
        MenuSetting.DEBUG: False,
        MenuSetting.IS_TEXT: True,
        MenuSetting.IS_ACTIVE: True,

        MenuSetting.IS_GRAYSCALE: True,

        MenuSetting.IS_BINARIZE: True,
        MenuSetting.THRESHOLD_BINARIZE: 100,
        MenuSetting.INVERT_BOOL: False,

        MenuSetting.THRESHOLD_HAMMING: HAMMING_THRESHOLD_NUMBERS,
        MenuSetting.HASH_DICT: dict_hash2int
    },

        MenuRedPOI.STAT_HP_CUR_0: {
        MenuSetting.OFFSET: (95,27,101,37),
        MenuSetting.DEBUG: False,
        MenuSetting.IS_TEXT: True,
        MenuSetting.IS_ACTIVE: True,

        MenuSetting.IS_GRAYSCALE: True,

        MenuSetting.IS_BINARIZE: True,
        MenuSetting.THRESHOLD_BINARIZE: 100,
        MenuSetting.INVERT_BOOL: False,

        MenuSetting.THRESHOLD_HAMMING: HAMMING_THRESHOLD_NUMBERS,
        MenuSetting.HASH_DICT: dict_hash2int
    },
        MenuRedPOI.STAT_HP_CUR_1: {
        MenuSetting.OFFSET: (101,27,107,37),
        MenuSetting.DEBUG: False,
        MenuSetting.IS_TEXT: True,
        MenuSetting.IS_ACTIVE: True,

        MenuSetting.IS_GRAYSCALE: True,

        MenuSetting.IS_BINARIZE: True,
        MenuSetting.THRESHOLD_BINARIZE: 100,
        MenuSetting.INVERT_BOOL: False,

        MenuSetting.THRESHOLD_HAMMING: HAMMING_THRESHOLD_NUMBERS,
        MenuSetting.HASH_DICT: dict_hash2int
    },
        MenuRedPOI.STAT_HP_CUR_2: {
        MenuSetting.OFFSET: (107,27,113,37),
        MenuSetting.DEBUG: False,
        MenuSetting.IS_TEXT: True,
        MenuSetting.IS_ACTIVE: True,

        MenuSetting.IS_GRAYSCALE: True,

        MenuSetting.IS_BINARIZE: True,
        MenuSetting.THRESHOLD_BINARIZE: 100,
        MenuSetting.INVERT_BOOL: False,

        MenuSetting.THRESHOLD_HAMMING: HAMMING_THRESHOLD_NUMBERS,
        MenuSetting.HASH_DICT: dict_hash2int
    },


    MenuRedPOI.STAT_ATK_0: {
        MenuSetting.OFFSET: (110,51,116,61),
        MenuSetting.DEBUG: False,
        MenuSetting.IS_TEXT: True,
        MenuSetting.IS_ACTIVE: True,

        MenuSetting.IS_GRAYSCALE: True,

        MenuSetting.IS_BINARIZE: True,
        MenuSetting.THRESHOLD_BINARIZE: 100,
        MenuSetting.INVERT_BOOL: False,

        MenuSetting.THRESHOLD_HAMMING: HAMMING_THRESHOLD_NUMBERS,
        MenuSetting.HASH_DICT: dict_hash2int
    },
        MenuRedPOI.STAT_ATK_1: {
        MenuSetting.OFFSET: (116,51,122,61),
        MenuSetting.DEBUG: False,
        MenuSetting.IS_TEXT: True,
        MenuSetting.IS_ACTIVE: True,

        MenuSetting.IS_GRAYSCALE: True,

        MenuSetting.IS_BINARIZE: True,
        MenuSetting.THRESHOLD_BINARIZE: 100,
        MenuSetting.INVERT_BOOL: False,

        MenuSetting.THRESHOLD_HAMMING: HAMMING_THRESHOLD_NUMBERS,
        MenuSetting.HASH_DICT: dict_hash2int
    },
        MenuRedPOI.STAT_ATK_2: {
        MenuSetting.OFFSET: (122,51,128,61),
        MenuSetting.DEBUG: False,
        MenuSetting.IS_TEXT: True,
        MenuSetting.IS_ACTIVE: True,

        MenuSetting.IS_GRAYSCALE: True,

        MenuSetting.IS_BINARIZE: True,
        MenuSetting.THRESHOLD_BINARIZE: 100,
        MenuSetting.INVERT_BOOL: False,

        MenuSetting.THRESHOLD_HAMMING: HAMMING_THRESHOLD_NUMBERS,
        MenuSetting.HASH_DICT: dict_hash2int
    },

    MenuRedPOI.STAT_DEF_0: {
        MenuSetting.OFFSET: (110,67,116,77),
        MenuSetting.DEBUG: False,
        MenuSetting.IS_TEXT: True,
        MenuSetting.IS_ACTIVE: True,

        MenuSetting.IS_GRAYSCALE: True,

        MenuSetting.IS_BINARIZE: True,
        MenuSetting.THRESHOLD_BINARIZE: 100,
        MenuSetting.INVERT_BOOL: False,

        MenuSetting.THRESHOLD_HAMMING: HAMMING_THRESHOLD_NUMBERS,
        MenuSetting.HASH_DICT: dict_hash2int
    },
        MenuRedPOI.STAT_DEF_1: {
        MenuSetting.OFFSET: (116,67,122,77),
        MenuSetting.DEBUG: False,
        MenuSetting.IS_TEXT: True,
        MenuSetting.IS_ACTIVE: True,

        MenuSetting.IS_GRAYSCALE: True,

        MenuSetting.IS_BINARIZE: True,
        MenuSetting.THRESHOLD_BINARIZE: 100,
        MenuSetting.INVERT_BOOL: False,

        MenuSetting.THRESHOLD_HAMMING: HAMMING_THRESHOLD_NUMBERS,
        MenuSetting.HASH_DICT: dict_hash2int
    },
        MenuRedPOI.STAT_DEF_2: {
        MenuSetting.OFFSET: (122,67,128,77),
        MenuSetting.DEBUG: False,
        MenuSetting.IS_TEXT: True,
        MenuSetting.IS_ACTIVE: True,

        MenuSetting.IS_GRAYSCALE: True,

        MenuSetting.IS_BINARIZE: True,
        MenuSetting.THRESHOLD_BINARIZE: 100,
        MenuSetting.INVERT_BOOL: False,

        MenuSetting.THRESHOLD_HAMMING: HAMMING_THRESHOLD_NUMBERS,
        MenuSetting.HASH_DICT: dict_hash2int
    },

        MenuRedPOI.STAT_SPEC_ATK_0: {
        MenuSetting.OFFSET: (110,83,116,93),
        MenuSetting.DEBUG: False,
        MenuSetting.IS_TEXT: True,
        MenuSetting.IS_ACTIVE: True,

        MenuSetting.IS_GRAYSCALE: True,

        MenuSetting.IS_BINARIZE: True,
        MenuSetting.THRESHOLD_BINARIZE: 100,
        MenuSetting.INVERT_BOOL: False,

        MenuSetting.THRESHOLD_HAMMING: HAMMING_THRESHOLD_NUMBERS,
        MenuSetting.HASH_DICT: dict_hash2int
    },
        MenuRedPOI.STAT_SPEC_ATK_1: {
        MenuSetting.OFFSET: (116,83,122,93),
        MenuSetting.DEBUG: False,
        MenuSetting.IS_TEXT: True,
        MenuSetting.IS_ACTIVE: True,

        MenuSetting.IS_GRAYSCALE: True,

        MenuSetting.IS_BINARIZE: True,
        MenuSetting.THRESHOLD_BINARIZE: 100,
        MenuSetting.INVERT_BOOL: False,

        MenuSetting.THRESHOLD_HAMMING: HAMMING_THRESHOLD_NUMBERS,
        MenuSetting.HASH_DICT: dict_hash2int
    },
        MenuRedPOI.STAT_SPEC_ATK_2: {
        MenuSetting.OFFSET: (122,83,128,93),
        MenuSetting.DEBUG: False,
        MenuSetting.IS_TEXT: True,
        MenuSetting.IS_ACTIVE: True,

        MenuSetting.IS_GRAYSCALE: True,

        MenuSetting.IS_BINARIZE: True,
        MenuSetting.THRESHOLD_BINARIZE: 100,
        MenuSetting.INVERT_BOOL: False,

        MenuSetting.THRESHOLD_HAMMING: HAMMING_THRESHOLD_NUMBERS,
        MenuSetting.HASH_DICT: dict_hash2int
    },

    MenuRedPOI.STAT_SPEC_DEF_0: {
        MenuSetting.OFFSET: (110,99,116,109),
        MenuSetting.DEBUG: False,
        MenuSetting.IS_TEXT: True,
        MenuSetting.IS_ACTIVE: True,

        MenuSetting.IS_GRAYSCALE: True,

        MenuSetting.IS_BINARIZE: True,
        MenuSetting.THRESHOLD_BINARIZE: 100,
        MenuSetting.INVERT_BOOL: False,

        MenuSetting.THRESHOLD_HAMMING: HAMMING_THRESHOLD_NUMBERS,
        MenuSetting.HASH_DICT: dict_hash2int
    },
        MenuRedPOI.STAT_SPEC_DEF_1: {
        MenuSetting.OFFSET: (116,99,122,109),
        MenuSetting.DEBUG: False,
        MenuSetting.IS_TEXT: True,
        MenuSetting.IS_ACTIVE: True,

        MenuSetting.IS_GRAYSCALE: True,

        MenuSetting.IS_BINARIZE: True,
        MenuSetting.THRESHOLD_BINARIZE: 100,
        MenuSetting.INVERT_BOOL: False,

        MenuSetting.THRESHOLD_HAMMING: HAMMING_THRESHOLD_NUMBERS,
        MenuSetting.HASH_DICT: dict_hash2int
    },
        MenuRedPOI.STAT_SPEC_DEF_2: {
        MenuSetting.OFFSET: (122,99,128,109),
        MenuSetting.DEBUG: False,
        MenuSetting.IS_TEXT: True,
        MenuSetting.IS_ACTIVE: True,

        MenuSetting.IS_GRAYSCALE: True,

        MenuSetting.IS_BINARIZE: True,
        MenuSetting.THRESHOLD_BINARIZE: 100,
        MenuSetting.INVERT_BOOL: False,

        MenuSetting.THRESHOLD_HAMMING: HAMMING_THRESHOLD_NUMBERS,
        MenuSetting.HASH_DICT: dict_hash2int
    },

    MenuRedPOI.STAT_SPEED_0: {
        MenuSetting.OFFSET: (110,115,116,125),
        MenuSetting.DEBUG: False,
        MenuSetting.IS_TEXT: True,
        MenuSetting.IS_ACTIVE: True,

        MenuSetting.IS_GRAYSCALE: True,

        MenuSetting.IS_BINARIZE: True,
        MenuSetting.THRESHOLD_BINARIZE: 100,
        MenuSetting.INVERT_BOOL: False,

        MenuSetting.THRESHOLD_HAMMING: HAMMING_THRESHOLD_NUMBERS,
        MenuSetting.HASH_DICT: dict_hash2int
    },
        MenuRedPOI.STAT_SPEED_1: {
        MenuSetting.OFFSET: (116,115,122,125),
        MenuSetting.DEBUG: False,
        MenuSetting.IS_TEXT: True,
        MenuSetting.IS_ACTIVE: True,

        MenuSetting.IS_GRAYSCALE: True,

        MenuSetting.IS_BINARIZE: True,
        MenuSetting.THRESHOLD_BINARIZE: 100,
        MenuSetting.INVERT_BOOL: False,

        MenuSetting.THRESHOLD_HAMMING: HAMMING_THRESHOLD_NUMBERS,
        MenuSetting.HASH_DICT: dict_hash2int
    },
        MenuRedPOI.STAT_SPEED_2: {
        MenuSetting.OFFSET: (122,115,128,125),
        MenuSetting.DEBUG: False,
        MenuSetting.IS_TEXT: True,
        MenuSetting.IS_ACTIVE: True,

        MenuSetting.IS_GRAYSCALE: True,

        MenuSetting.IS_BINARIZE: True,
        MenuSetting.THRESHOLD_BINARIZE: 100,
        MenuSetting.INVERT_BOOL: False,

        MenuSetting.THRESHOLD_HAMMING: HAMMING_THRESHOLD_NUMBERS,
        MenuSetting.HASH_DICT: dict_hash2int
    },
    MenuRedPOI.ABILITY_NAME: {
        MenuSetting.NAME: "Ability Name",
        MenuSetting.IS_TEXT: True,
        MenuSetting.OFFSET: (72,138,150,152),
        MenuSetting.TEXT_LENGTH: 16,
        MenuSetting.IS_ACTIVE: True,
        MenuSetting.THRESHOLD_HAMMING: 5,
        MenuSetting.IS_GRAYSCALE: True,
        MenuSetting.IS_BINARIZE: True,
        MenuSetting.THRESHOLD_BINARIZE: 100,
        MenuSetting.INVERT_BOOL: False,
        MenuSetting.DEBUG: False
    },

    MenuRedPOI.ABILITY_DESC_1: {
        MenuSetting.NAME: "Ability Description 1",
        MenuSetting.IS_TEXT: True,
        MenuSetting.OFFSET: (3,154,150,168),
        MenuSetting.TEXT_LENGTH: 38,
        MenuSetting.IS_ACTIVE: True,
        MenuSetting.THRESHOLD_HAMMING: 5,
        MenuSetting.IS_GRAYSCALE: True,
        MenuSetting.IS_BINARIZE: True,
        MenuSetting.THRESHOLD_BINARIZE: 100,
        MenuSetting.INVERT_BOOL: False,
        MenuSetting.DEBUG: False
    },
    MenuRedPOI.ABILITY_DESC_2: {
        MenuSetting.NAME: "Ability Description 2",
        MenuSetting.IS_TEXT: True,
        MenuSetting.OFFSET: (3,170,150,184),
        MenuSetting.TEXT_LENGTH: 38,
        MenuSetting.IS_ACTIVE: True,
        MenuSetting.THRESHOLD_HAMMING: 5,
        MenuSetting.IS_GRAYSCALE: True,
        MenuSetting.IS_BINARIZE: True,
        MenuSetting.THRESHOLD_BINARIZE: 100,
        MenuSetting.INVERT_BOOL: False,
        MenuSetting.DEBUG: False
    }

}

pokemon_menu_blue_dict = {
#All natures are 7 characters, 8 including the space after the word
    MenuBluePOI.NATURE: {
        MenuSetting.NAME: "Nature",
        MenuSetting.OFFSET: (6,26,52,40),
        MenuSetting.DEBUG: False,
        MenuSetting.IS_TEXT: True,
        MenuSetting.TEXT_LENGTH: 8,

        MenuSetting.IS_ACTIVE: True,
        MenuSetting.THRESHOLD_HAMMING: 5,

        MenuSetting.IS_GRAYSCALE: True,

        MenuSetting.IS_BINARIZE: True,
        MenuSetting.THRESHOLD_BINARIZE: 150,
        MenuSetting.INVERT_BOOL: False
    },
    MenuBluePOI.CATCH_DATE: {
        MenuSetting.NAME: "Catch Date",
        MenuSetting.OFFSET: (6,42,90,56),
        MenuSetting.DEBUG: False,
        MenuSetting.IS_TEXT: True,
        MenuSetting.TEXT_LENGTH: 16,
        MenuSetting.IS_ACTIVE: True,

        MenuSetting.THRESHOLD_HAMMING: 5,

        MenuSetting.IS_GRAYSCALE: True,

        MenuSetting.IS_BINARIZE: True,
        MenuSetting.THRESHOLD_BINARIZE: 150,
        MenuSetting.INVERT_BOOL: False
    },
    MenuBluePOI.CATCH_LOCATION: {
        MenuSetting.NAME: "Catch Location",
        MenuSetting.OFFSET: (6,58,112,72),
        MenuSetting.DEBUG: False,
        MenuSetting.IS_TEXT: True,
        MenuSetting.TEXT_LENGTH: 16,
        MenuSetting.IS_ACTIVE: True,

        MenuSetting.IS_GRAYSCALE: True,
        MenuSetting.THRESHOLD_HAMMING: 5,

        MenuSetting.IS_BINARIZE: True,
        MenuSetting.THRESHOLD_BINARIZE: 150,
        MenuSetting.INVERT_BOOL: False
    },
    MenuBluePOI.CATCH_LEVEL_0: {
        MenuSetting.OFFSET: True,
        MenuSetting.INVERT_BOOL: True,
        MenuSetting.THRESHOLD_BINARIZE: 100,

    },
    MenuBluePOI.PERSONALITY: {
        MenuSetting.NAME: "Personality",
        MenuSetting.OFFSET: (6,106,142,120),
        MenuSetting.DEBUG: False,
        MenuSetting.IS_TEXT: True,
        MenuSetting.TEXT_LENGTH:25,
        MenuSetting.IS_ACTIVE: True,

        MenuSetting.IS_GRAYSCALE: True,
        MenuSetting.THRESHOLD_HAMMING: 5,

        MenuSetting.IS_BINARIZE: True,
        MenuSetting.THRESHOLD_BINARIZE: 150,
        MenuSetting.INVERT_BOOL: False
    },
    #Dex num and name not calibrated
        MenuBluePOI.DEX_NUMBER: {
        MenuSetting.NAME: "Number",
        MenuSetting.OFFSET: (95,195,118,220),
        MenuSetting.IS_TEXT: True,
        MenuSetting.IS_ACTIVE: False,

        MenuSetting.IS_GRAYSCALE: True,

        MenuSetting.IS_BINARIZE: True,
        MenuSetting.THRESHOLD_BINARIZE: 150,
        MenuSetting.INVERT_BOOL: False,
        MenuSetting.DEBUG: False
    },
    MenuBluePOI.DEX_NAME: {
        MenuSetting.NAME: "Name",
        MenuSetting.OFFSET: (74,218,142,232),
        MenuSetting.DEBUG: False,
        MenuSetting.IS_TEXT: True,
        MenuSetting.IS_ACTIVE: True,
        MenuSetting.TEXT_LENGTH: 12,

        MenuSetting.IS_GRAYSCALE: True,

        MenuSetting.IS_BINARIZE: True,
        MenuSetting.THRESHOLD_BINARIZE: 100,
        MenuSetting.THRESHOLD_HAMMING: 5,
        MenuSetting.INVERT_BOOL: False,
        MenuSetting.ALIGN_CENTER: True
    },

    MenuBluePOI.TYPE_MONO: {
        MenuSetting.NAME: "Type 0",
        MenuSetting.OFFSET: (92,233,124,247),
        MenuSetting.DEBUG: False,
        MenuSetting.IS_ACTIVE: True,
        MenuSetting.THRESHOLD_HAMMING: 5,
        MenuSetting.HASH_DICT: dict_hash2types
    },
    MenuBluePOI.TYPE_SPLIT_1: {
        MenuSetting.NAME: "Type 1",
        MenuSetting.OFFSET: (75,233,107,247),
        MenuSetting.DEBUG: False,
        MenuSetting.IS_ACTIVE: True,
        MenuSetting.THRESHOLD_HAMMING: 5,
        MenuSetting.HASH_DICT: dict_hash2types
    },
    MenuBluePOI.TYPE_SPLIT_2: {
        MenuSetting.NAME: "Type 2",
        MenuSetting.OFFSET: (109,233,141,247),
        MenuSetting.DEBUG: False,
        MenuSetting.IS_ACTIVE: True,
        MenuSetting.THRESHOLD_HAMMING: 5,
        MenuSetting.HASH_DICT: dict_hash2types
    },
    #Trainer name, id, and both exp values not calibrated
    MenuBluePOI.TRAINER_NAME: {
        MenuSetting.OFFSET: (80,248,130,268),
        MenuSetting.DEBUG: False,
        MenuSetting.IS_TEXT: True,
        MenuSetting.IS_ACTIVE: True,

        MenuSetting.IS_GRAYSCALE: True,

        MenuSetting.IS_BINARIZE: True,
        MenuSetting.THRESHOLD_BINARIZE: 150,
        MenuSetting.INVERT_BOOL: False
    },
    MenuBluePOI.TRAINER_ID: {
        MenuSetting.OFFSET: (80,248,130,268),
        MenuSetting.DEBUG: False,
        MenuSetting.IS_TEXT: True,
        MenuSetting.IS_ACTIVE: True,

        MenuSetting.IS_GRAYSCALE: True,

        MenuSetting.IS_BINARIZE: True,
        MenuSetting.THRESHOLD_BINARIZE: 150,
        MenuSetting.INVERT_BOOL: False
    },
    MenuBluePOI.EXP_CUR: {
        MenuSetting.OFFSET: (80,248,130,268),
        MenuSetting.DEBUG: False,
        MenuSetting.IS_TEXT: True,
        MenuSetting.IS_ACTIVE: True,

        MenuSetting.IS_GRAYSCALE: True,

        MenuSetting.IS_BINARIZE: True,
        MenuSetting.THRESHOLD_BINARIZE: 150,
        MenuSetting.INVERT_BOOL: False
    },
    MenuBluePOI.EXP_NXT: {
        MenuSetting.OFFSET: (80,248,130,268),
        MenuSetting.DEBUG: False,
        MenuSetting.IS_TEXT: True,
        MenuSetting.IS_ACTIVE: True,

        MenuSetting.IS_GRAYSCALE: True,

        MenuSetting.IS_BINARIZE: True,
        MenuSetting.THRESHOLD_BINARIZE: 150,
        MenuSetting.INVERT_BOOL: False
    }
}

pokemon_menu_all_dict = {
    MenuAllPOI.POKEBALL: {
        MenuSetting.OFFSET: (160,31,175,47),
        MenuSetting.DEBUG: False,
        MenuSetting.IS_ACTIVE: True,
        MenuSetting.THRESHOLD_HAMMING: 5,
        MenuSetting.HASH_DICT: dict_hash2ball
    },
    MenuAllPOI.NICKNAME: {
        MenuSetting.NAME: "Nickname",
        MenuSetting.OFFSET: (176,34,240,48),
        MenuSetting.DEBUG: False,
        MenuSetting.IS_TEXT: True,
        MenuSetting.TEXT_LENGTH: 10,
        MenuSetting.IS_ACTIVE: True,
        MenuSetting.THRESHOLD_HAMMING: 5,

        MenuSetting.IS_GRAYSCALE: True,

        MenuSetting.IS_BINARIZE: True,
        MenuSetting.THRESHOLD_BINARIZE: 200,
        MenuSetting.INVERT_BOOL: True
    },
    MenuAllPOI.GENDER: {
        MenuSetting.NAME: "Gender",
        MenuSetting.OFFSET: (242,35,248,45),
        MenuSetting.IS_ACTIVE: True,
        MenuSetting.DEBUG: False,
        MenuSetting.THRESHOLD_HAMMING: 5,
        MenuSetting.HASH_DICT: dict_hash2gender
    },
    MenuAllPOI.LEVEL_0: {
        MenuSetting.OFFSET: (176,51,182,61),
        MenuSetting.DEBUG: False,
        MenuSetting.IS_TEXT: True,
        MenuSetting.IS_ACTIVE: True,

        MenuSetting.THRESHOLD_HAMMING: HAMMING_THRESHOLD_NUMBERS,

        MenuSetting.IS_GRAYSCALE: True,

        MenuSetting.IS_BINARIZE: True,
        MenuSetting.THRESHOLD_BINARIZE: 100,
        MenuSetting.INVERT_BOOL: False,

        MenuSetting.THRESHOLD_HAMMING: 5,
        MenuSetting.HASH_DICT: dict_hash2int
    },
    MenuAllPOI.LEVEL_1: {
        MenuSetting.OFFSET: (182,51,188,61),
        MenuSetting.DEBUG: False,
        MenuSetting.IS_TEXT: True,
        MenuSetting.IS_ACTIVE: True,

        MenuSetting.IS_GRAYSCALE: True,
        MenuSetting.THRESHOLD_HAMMING: HAMMING_THRESHOLD_NUMBERS,

        MenuSetting.IS_BINARIZE: True,
        MenuSetting.THRESHOLD_BINARIZE: 100,
        MenuSetting.INVERT_BOOL: False,

        MenuSetting.THRESHOLD_HAMMING: 5,
        MenuSetting.HASH_DICT: dict_hash2int
    },
    MenuAllPOI.LEVEL_2: {
        MenuSetting.OFFSET: (188,51,194,61),
        MenuSetting.DEBUG: False,
        MenuSetting.IS_TEXT: True,
        MenuSetting.IS_ACTIVE: True,

        MenuSetting.IS_GRAYSCALE: True,
        MenuSetting.THRESHOLD_HAMMING: HAMMING_THRESHOLD_NUMBERS,

        MenuSetting.IS_BINARIZE: True,
        MenuSetting.THRESHOLD_BINARIZE: 100,
        MenuSetting.INVERT_BOOL: False,

        MenuSetting.THRESHOLD_HAMMING: 5,
        MenuSetting.HASH_DICT: dict_hash2int
    },
    MenuAllPOI.IMAGE: {
        MenuSetting.OFFSET: True,
        MenuSetting.INVERT_BOOL: True,
        MenuSetting.THRESHOLD_BINARIZE: 100
    },
#Items can potentially be 16 characters
    MenuAllPOI.ITEM: {
        MenuSetting.NAME: "Item",
        MenuSetting.OFFSET: (160,178,240,192),
        MenuSetting.DEBUG: False,
        MenuSetting.IS_TEXT: True,
        MenuSetting.IS_ACTIVE: True,
        MenuSetting.TEXT_LENGTH: 16,
        MenuSetting.THRESHOLD_HAMMING: 5,

        MenuSetting.IS_GRAYSCALE: True,

        MenuSetting.IS_BINARIZE: True,
        MenuSetting.THRESHOLD_BINARIZE: 100,
        MenuSetting.INVERT_BOOL: False
    },
    MenuAllPOI.MARKINGS: {
        MenuSetting.OFFSET: True,
        MenuSetting.INVERT_BOOL: True,
        MenuSetting.THRESHOLD_BINARIZE: 100
    },
    MenuAllPOI.POKERUS_INFECTED: {
        MenuSetting.OFFSET: True,
        MenuSetting.INVERT_BOOL: True,
        MenuSetting.THRESHOLD_BINARIZE: 100
    },
    MenuAllPOI.POKERUS_IMMUNE: {
        MenuSetting.OFFSET: True,
        MenuSetting.INVERT_BOOL: True,
        MenuSetting.THRESHOLD_BINARIZE: 100
    }
}



state_dict = {
    Gamestate.BATTLE: {
        GamestateSetting.ADJACENCIES: [Gamestate.OVERWORLD],
        GamestateSetting.NAME: "Battle",
        GamestateSetting.HASH_DICT: {"a0220a8808202282": Gamestate.BATTLE},
        GamestateSetting.SCANS: [],
        GamestateSetting.OFFSET: (0,192,256,384),
        GamestateSetting.IS_ACTIVE: True,
        GamestateSetting.THRESHOLD_HAMMING: 8
    },
    Gamestate.OVERWORLD: {
        GamestateSetting.ADJACENCIES: [Gamestate.BATTLE, Gamestate.MENU_POKEMON],
        GamestateSetting.NAME: "Overworld",
        GamestateSetting.HASH_DICT: {"853d5a185f4b1f4a": Gamestate.OVERWORLD},
        GamestateSetting.SCANS: [],
        GamestateSetting.OFFSET: (0, 192, 153, 384),
        GamestateSetting.IS_ACTIVE: True,
        GamestateSetting.THRESHOLD_HAMMING: 8
    },
    Gamestate.MENU_POKEMON: {
        GamestateSetting.ADJACENCIES: [Gamestate.OVERWORLD, Gamestate.MENU_BLUE],
        GamestateSetting.NAME: "Pokemon Menu",
        GamestateSetting.HASH_DICT: {"c091264a3be66eeb": Gamestate.MENU_POKEMON},
        GamestateSetting.SCANS: [],
        GamestateSetting.OFFSET: (0,0,256,192),
        GamestateSetting.IS_ACTIVE: True,
        GamestateSetting.THRESHOLD_HAMMING: 8
    },
    Gamestate.MENU_BLUE: {
        GamestateSetting.ADJACENCIES: [Gamestate.MENU_POKEMON, Gamestate.MENU_RED, Gamestate.MENU_YELLOW],
        GamestateSetting.NAME: "Blue Menu",
        GamestateSetting.HASH_DICT: {"d5d5add1d03d2628": Gamestate.MENU_BLUE},
        GamestateSetting.OFFSET: (153,0,256,27),
        GamestateSetting.SCANS: [pokemon_menu_all_dict, pokemon_menu_blue_dict],
        GamestateSetting.IS_ACTIVE: True,
        GamestateSetting.THRESHOLD_HAMMING: 8
    },
    Gamestate.MENU_RED: {
        GamestateSetting.ADJACENCIES: [Gamestate.MENU_POKEMON, Gamestate.MENU_BLUE, Gamestate.MENU_YELLOW],
        GamestateSetting.NAME: "Red Menu",
        GamestateSetting.HASH_DICT: {"d5959fd5d4154238": Gamestate.MENU_RED},
        GamestateSetting.OFFSET: (153,0,256,27),
        GamestateSetting.SCANS: [pokemon_menu_all_dict, pokemon_menu_red_dict],
        GamestateSetting.IS_ACTIVE: True,
        GamestateSetting.THRESHOLD_HAMMING: 8
    },
    Gamestate.MENU_YELLOW: {
        GamestateSetting.ADJACENCIES: [Gamestate.MENU_POKEMON, Gamestate.MENU_BLUE, Gamestate.MENU_RED],
        GamestateSetting.NAME: "Yellow Menu",
        GamestateSetting.HASH_DICT: {"d5c0aad5dcd5330a": Gamestate.MENU_YELLOW},
        GamestateSetting.OFFSET: (0,0,256,384),
        GamestateSetting.SCANS: [pokemon_menu_all_dict],
        GamestateSetting.IS_ACTIVE: True,
        GamestateSetting.THRESHOLD_HAMMING: 8
    }

}


def generate_hp_data(forward = True, backward = True):
    stat_dict_forward = {}
    stat_dict_reverse = {}


    for level in range(1, 101):
        level_dict = {}
        stat_dict_reverse[level] = {}
        for base_stat in range(10, 256):
            base_stat_dict = {}
                
            #calc low and high
            low = Calculator.stat_calc(base_stat, level, 0, 0)
            high = Calculator.stat_calc(base_stat, level, 31, 255)
            #add to forward lookup


            for stat in range(low, high+1):
                if stat not in stat_dict_reverse[level]:
                    stat_dict_reverse[level][stat] = {}
                if "unknown" not in stat_dict_reverse[level][stat]:
                    stat_dict_reverse[level][stat]["unknown"] = {"low": math.inf, "high": 0}
                
                '''if base_stat < stat_dict_reverse[level][stat][nature]["low"]:
                    stat_dict_reverse[level][stat][nature]["low"] = base_stat
                if base_stat > stat_dict_reverse[level][stat][nature]["high"]:
                    stat_dict_reverse[level][stat][nature]["high"] = base_stat'''
                
                if base_stat < stat_dict_reverse[level][stat]["unknown"]["low"]:
                    stat_dict_reverse[level][stat]["unknown"]["low"] = base_stat
                if base_stat > stat_dict_reverse[level][stat]["unknown"]["high"]:
                    stat_dict_reverse[level][stat]["unknown"]["high"] = base_stat
                    
            level_dict[base_stat] = base_stat_dict
        stat_dict_forward[level] = level_dict

    if forward:
        with open('level_data_fwd.json', 'w') as f1:
            json.dump(stat_dict_forward, f1)

    if backward:
        with open('level_data_rev.json', 'w') as f2:
            json.dump(stat_dict_reverse, f2)

def generate_level_data(forward = True, backward = True):
    stat_dict_forward = {}
    stat_dict_reverse = {}


    for level in range(1, 101):
        level_dict = {}
        stat_dict_reverse[level] = {}
        for base_stat in range(10, 256):
            base_stat_dict = {}
            for nature in nature_bonus:
                nature_dict = {}
                
                #calc low and high
                low = Calculator.stat_calc(base_stat, level, 0, 0, nature_bonus[nature])
                high = Calculator.stat_calc(base_stat, level, 31, 0, nature_bonus[nature])
                #add to forward lookup
                nature_dict["low"] = low
                nature_dict["high"] = high

                for stat in range(low, high+1):
                    if stat not in stat_dict_reverse[level]:
                        stat_dict_reverse[level][stat] = {}
                    if "unknown" not in stat_dict_reverse[level][stat]:
                        stat_dict_reverse[level][stat]["unknown"] = {"low": math.inf, "high": 0}
                    if nature not in stat_dict_reverse[level][stat]:
                        stat_dict_reverse[level][stat][nature] = {"low": math.inf, "high": 0}
                    
                    if base_stat < stat_dict_reverse[level][stat][nature]["low"]:
                        stat_dict_reverse[level][stat][nature]["low"] = base_stat
                    if base_stat > stat_dict_reverse[level][stat][nature]["high"]:
                        stat_dict_reverse[level][stat][nature]["high"] = base_stat
                    
                    if base_stat < stat_dict_reverse[level][stat]["unknown"]["low"]:
                        stat_dict_reverse[level][stat]["unknown"]["low"] = base_stat
                    if base_stat > stat_dict_reverse[level][stat]["unknown"]["high"]:
                        stat_dict_reverse[level][stat]["unknown"]["high"] = base_stat
                    
                base_stat_dict[nature] = nature_dict
            level_dict[base_stat] = base_stat_dict
        stat_dict_forward[level] = level_dict


    if forward:
        with open('level_data_fwd.json', 'w') as f1:
            json.dump(stat_dict_forward, f1)

    if backward:
        with open('level_data_rev.json', 'w') as f2:
            json.dump(stat_dict_reverse, f2)

def convert_move_data():
    with open('pokedex//move_data.txt') as f:
        moves_name = {}
        moves_id = {}
        lines = f.readlines()
        for line in lines:
            split_text = line.split(' 	', -1)
            id = split_text[0]
            moves_id[id] = {}
            moves_id[id]["id"] = split_text[0]
            moves_id[id]["name"] = split_text[1]
            moves_id[id]["type"] = split_text[2]
            moves_id[id]["category"] = split_text[3]
            moves_id[id]["pp"] = split_text[4]
            moves_id[id]["power"] = split_text[5]
            moves_id[id]["accuracy"] = split_text[6]
        for line in lines:
            split_text = line.split(' 	', -1)
            name = split_text[1]
            moves_name[name] = {}
            moves_name[name]["id"] = split_text[0]
            moves_name[name]["name"] = split_text[1]
            moves_name[name]["type"] = split_text[2]
            moves_name[name]["category"] = split_text[3]
            moves_name[name]["pp"] = split_text[4]
            moves_name[name]["power"] = split_text[5]
            moves_name[name]["accuracy"] = split_text[6]
    
    with open('move_data_id.json', 'w') as f:
        json.dump(moves_id, f)
    with open('move_data_name.json', 'w') as f:
        json.dump(moves_name, f)

def damage_calc_test():
    hp_lost = [60, 72]
    attack = 140
    defense = 100
    type1 = 1
    type2 = 1
    stab = 1.5
    crit = 1
    base_power = 100
    level = 50

    print("attack: " + str(attack))
    min = 0
    max = math.inf

    print()
    for key, dmg in Calculator.damage_calc(level, base_power, attack, defense, stab, type1, type2).items():
        print("dmg: " + str(dmg))
        print()
        attacks = Calculator.reverse_calc_attack(dmg, defense, type1, type2, stab, crit, base_power, level)
        print(Calculator.reverse_calc_attack(dmg, defense, type1, type2, stab, crit, base_power, level))
        lo = attacks["low"]
        hi = attacks["high"] 
        if lo > min:
            min = lo
        if hi < max:
            max = hi
        
        
    print()

    print("min: " + str(min))
    print("max: " + str(max))

    for x in range(min, max+1):
        print(str(x) + ": ")
        nature = 0.9
        for y in range(3):
            print(str(nature) + ": " + str(Calculator.base_stat_calc(x, nature, level)))
            nature += 0.1

def menu_test():
    main_menu = MainMenu()
    battle_vision_menu = BattleMenu()
    pokedex_menu = PokedexMenu()

    main_menu.add_menu_dict_option("Pokedex", pokedex_menu.run)
    main_menu.add_menu_dict_option("Battle Vision", battle_vision_menu.run)
    battle_vision_menu.add_menu_dict_option("Back", main_menu.run)
    pokedex_menu.add_menu_dict_option("Back", main_menu.run)

    curses.wrapper(main_menu.run)

def calc_bst_change():
    total = 0
    plus = 0
    minus = 0
    same = 0
    count = 1000000
    for i in range(count):
        if i % int(count/100) == 0:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(str(int(i/(count/100))) + "%")
        with open('raw_resources//pokemon_bst.txt') as f:
            for line in f.readlines():
                total += 1
                bst_original = int(line)
                bst_new = Calculator.randomize_stats_within_bst(bst_original)
                
                if bst_new > bst_original:
                    plus += 1
                elif bst_new < bst_original:
                    minus += 1
                else:
                    same += 1
    os.system('cls' if os.name == 'nt' else 'clear')
    print("same: " + str(same) + "/" + str(total) + " = " + str(same/total))
    print("plus: " + str(plus) + "/" + str(total) + " = " + str(plus/total))
    print("minus: " + str(minus) + "/" + str(total) + " = " + str(minus/total))

def read_screen(key):
    pass
    #take screenshot of screen based on key data

SCALING_VALUE = 1

def calc_scaling(image):
    if isinstance(image, Image.Image):
        width = image.width
        height = image.height
    else:
        width = image[2]-image[0]
        height = image[3]-image[1]

    return round(min(height/DS_HEIGHT, width/DS_WIDTH))


def get_cropped_screen(image, item):

    scalar = calc_scaling(image)

    if MenuSetting.OFFSET in item:
        b0 = item[MenuSetting.OFFSET][0]*scalar
        b1 = item[MenuSetting.OFFSET][1]*scalar
        b2 = item[MenuSetting.OFFSET][2]*scalar
        b3 = item[MenuSetting.OFFSET][3]*scalar
    elif GamestateSetting.OFFSET in item:
        b0 = item[GamestateSetting.OFFSET][0]*scalar
        b1 = item[GamestateSetting.OFFSET][1]*scalar
        b2 = item[GamestateSetting.OFFSET][2]*scalar
        b3 = item[GamestateSetting.OFFSET][3]*scalar

    crop_image = image.crop((b0, b1, b2, b3))

    w = int((b2 - b0)/scalar)
    h = int((b3 - b1)/scalar)

    return crop_image.resize((w,h))

class DebugTag(Enum):
    NONE = 1
    ALL = 2
    DEFINED = 3
    IMAGE = 4
    TIME = 5

def is_whitespace_hash(hash, thresh):
    dist = hamming_distance(str(hash), CHAR_SPACE_HASH)
    
    if dist < thresh:
        return True
    
    return False

def extract_text(image, max_letters, hamming_threshold, debug = False, center_aligned = False):


    text = ""
    scalar = image.height / LETTER_HEIGHT
    next_width = 6
    starting_pixel = 0

    # color_image = cv2.cvtColor(numpy.array(image), cv2.COLOR_RGB2BGR)
    # cv2.imshow("Image Preview " + str(datetime.datetime.now()), color_image)
    # cv2.waitKey(500)

    if center_aligned is True:
        #skip white space
        is_whitespace = True
        while is_whitespace:
            #check if the space is white space, if it is, skip forward, when it's not, keep trying letters moving up one pixel at a time
            
            #get subshot
            hash = subshot_with_hash(image, starting_pixel, 6)
            #check if it's whitespace
            if not is_whitespace_hash(hash, 5):
                is_whitespace = False
            else:
                starting_pixel += 6
    
    #find what the first letter is, moving up 1 px at a time
        is_unknown_char = True
        while is_unknown_char:
            for w in range(6,2,-1):
                hash = subshot_with_hash(image, starting_pixel, w, debug)
                char_info = get_char_from_hash(hash, hamming_threshold, w)
                if char_info[1] < math.inf:
                    is_unknown_char = False
                    break
            if is_unknown_char:
                starting_pixel += 1
                if starting_pixel >= max_letters*6:
                    return text



    for i in range(0,max_letters):
        results = ({math.inf: []}, math.inf)
        next_width = 6

        for w in range(6, 2, -1):
            hash = subshot_with_hash(image, starting_pixel, w)
            char_info = get_char_from_hash(hash, hamming_threshold, w)
            if char_info[1] < results[1]:
                results = char_info
                next_width = w

        # print("Found the following letters with distance of " + str(results[1]) + ": ")
        # print(results[0])

        if results[1] < math.inf:
            letter = results[0][0]
        else:
            letter = "▞"

        text += letter
        starting_pixel += next_width*scalar
        
    return text

def extract_data(image, item):
    
    data = None

    #check for rgb vs grayscale
    if MenuSetting.IS_GRAYSCALE in item and item[MenuSetting.IS_GRAYSCALE] is True:
        image = image.convert('L')

    #check for binarize
    if MenuSetting.IS_BINARIZE in item and MenuSetting.THRESHOLD_BINARIZE in item and item[MenuSetting.IS_BINARIZE] is True:
        invert = False
        if MenuSetting.INVERT_BOOL in item:
            invert = item[MenuSetting.INVERT_BOOL]
        image = pillow_binarize(image, item[MenuSetting.THRESHOLD_BINARIZE], invert)

    debug = False
    if MenuSetting.DEBUG in item and item[MenuSetting.DEBUG] is True:
        debug = True
    
    if debug is True:
        color_image = cv2.cvtColor(numpy.array(image), cv2.COLOR_RGB2BGR)
        cv2.imshow("Image Preview " + str(datetime.datetime.now()), color_image)
        cv2.waitKey(500)


    if (MenuSetting.IS_TEXT in item and item[MenuSetting.IS_TEXT] is True and 
        MenuSetting.TEXT_LENGTH in item and MenuSetting.THRESHOLD_HAMMING in item):
            align_c = False
            if MenuSetting.ALIGN_CENTER in item:
                align_c = True
            data = str(extract_text(image, item[MenuSetting.TEXT_LENGTH], item[MenuSetting.THRESHOLD_HAMMING], debug, align_c))
    else:
        #for the item compare it against each hash entry in the corresponding hash dict
        hash_d = {}
        if MenuSetting.HASH_DICT in item:
            hash_d = item[MenuSetting.HASH_DICT]
        elif GamestateSetting.HASH_DICT in item:
            hash_d = item[GamestateSetting.HASH_DICT]

        hamming_thresh = math.inf
        if MenuSetting.THRESHOLD_HAMMING in item:
            hamming_thresh = item[MenuSetting.THRESHOLD_HAMMING]
        elif GamestateSetting.THRESHOLD_HAMMING in item:
            hamming_thresh = item[GamestateSetting.THRESHOLD_HAMMING]
        
        #empty dict evaluates to false
        dist_min = math.inf
        hash = None

        if hash_d and (hamming_thresh < math.inf):
            phash = str(imagehash.phash(image))
            #print("Hash: " + phash)
            for entry in hash_d:
                dist_hamming = hamming_distance(phash, entry)
                if (dist_hamming < dist_min and dist_hamming < hamming_thresh):
                    dist_min = dist_hamming
                    hash = entry

        if dist_min < math.inf:
            data = str(hash_d[hash])
    return (data, image)

def scan(hwnd, menu_dict, debug = [DebugTag.DEFINED]):

    data = {}
    images = {}

    original_image = get_screenshot(hwnd)

    #check for gamestates

        
    for key in menu_dict:
        if GamestateSetting.IS_ACTIVE in menu_dict[key] and menu_dict[key][GamestateSetting.IS_ACTIVE] is True:
            images[key] = get_cropped_screen(original_image, menu_dict[key])
        if MenuSetting.IS_ACTIVE in menu_dict[key] and menu_dict[key][MenuSetting.IS_ACTIVE] is True:
            images[key] = get_cropped_screen(original_image, menu_dict[key])

    #since the data is now loaded, compare it against each appropriate hash to collect what is needed

    for key in menu_dict:
        #print("Extracting " + str(key))
        if GamestateSetting.IS_ACTIVE in menu_dict[key] and menu_dict[key][GamestateSetting.IS_ACTIVE] is True:
            data[key], images[key] = extract_data(images[key], menu_dict[key])
        elif MenuSetting.IS_ACTIVE in menu_dict[key] and menu_dict[key][MenuSetting.IS_ACTIVE] is True:
            data[key], images[key] = extract_data(images[key], menu_dict[key])
            #if debug_level == DebugLevel.ALL or (debug_level == DebugLevel.DEFINED and MenuSetting.DEBUG in menu_dict[key] and menu_dict[key][MenuSetting.DEBUG] is True):
                #print(str(key) + ": " + str(data[key]))
                #color_image = cv2.cvtColor(numpy.array(images[key]), cv2.COLOR_RGB2BGR)
                #cv2.imshow("Image Preview " + str(window_snapshot_callback.counter), color_image)
                #cv2.waitKey(500)

    return data


def position_scaled(scalar, bbox, bbox_offset):
    new_bbox = []

    width = bbox[2] - bbox[0]
    height = bbox[3] - bbox[1]

    width_offset = round((width - (scalar * DS_WIDTH))/2)
    height_offset = round((height - (scalar * DS_HEIGHT))/2)
    
    new_bbox.append(bbox[0] + round(bbox_offset[0]*scalar) + width_offset)
    new_bbox.append(bbox[1] + round(bbox_offset[1]*scalar) + height_offset)
    new_bbox.append(bbox[2] - round((DS_WIDTH - bbox_offset[2])*scalar) - width_offset)
    new_bbox.append(bbox[3] - round((DS_HEIGHT - bbox_offset[3])*scalar) - height_offset)

    return new_bbox

def pillow_binarize(image, threshold, invert = False):
    if invert is True:
        img = image.point(lambda p: 0 if p > threshold else 255)
    else:
        img = image.point(lambda p: 255 if p > threshold else 0)
    return img


LETTER_HEIGHT = 14
def subshot_with_hash(image, starting_pixel, letter_width, debug = False):



    scalar = image.height/(LETTER_HEIGHT)

    crop_image = image.crop((starting_pixel, 0, starting_pixel + (letter_width*scalar), image.height))

    crop_image = crop_image.resize((letter_width, LETTER_HEIGHT))
    if debug:
        color_image = cv2.cvtColor(numpy.array(crop_image), cv2.COLOR_RGB2BGR)
        cv2.imshow("Image Preview " + str(datetime.datetime.now()), color_image)
        cv2.waitKey(500)
    
    hash = imagehash.phash(crop_image)
    #print(hash)
    return str(hash)

def bbox_shift(bbox, shift_old, shift_new):
    return (bbox[0]+shift_old, bbox[1], bbox[2]+shift_new, bbox[3])

def get_char_from_hash(hash, hamming_threshold, width):
    
    matches = {math.inf: []}
    lowest_dist = math.inf

    for h in dict_width2charhash[width]:
        dist = hamming_distance(h, hash)

        if dist <= hamming_threshold:

            if lowest_dist > dist:
                lowest_dist = dist

            if dist not in matches:
                matches[dist] = []
            
            matches[dist].append(dict_char2str[dict_hash2char[h]])

    return (matches[lowest_dist], lowest_dist)

def window_dimensions_adjusted(hwnd, offset_tuple):
    #windows uses invisible barrier, adjust window based on that
    #also djusting height for top window, and menu bar

    WINDOWS_BARRIER_THICKNESS = 8
    WINDOWS_TOP_BAR_COMBINED = 52

    rect = win32gui.GetWindowRect(hwnd)
    rect_adj = []
    rect_adj.append(rect[0] + WINDOWS_BARRIER_THICKNESS)
    rect_adj.append(rect[1] + WINDOWS_TOP_BAR_COMBINED)
    rect_adj.append(rect[2] - WINDOWS_BARRIER_THICKNESS)
    rect_adj.append(rect[3] - WINDOWS_BARRIER_THICKNESS)
    
    scalar = calc_scaling(rect_adj)

    rect_adj = position_scaled(scalar, rect_adj, offset_tuple)

    return rect_adj


def get_screenshot(hwnd, offset_tuple = (0, 0, DS_WIDTH, DS_HEIGHT)):
    box = window_dimensions_adjusted(hwnd, offset_tuple)
    start_time = datetime.datetime.now()
    image = ImageGrab.grab(bbox = box, all_screens = True)
    #print("Image Grab Time: " + str(datetime.datetime.now() - start_time))
    return image

def get_snapshot(hwnd, invert, threshold, offset_tuple = (0,0,0,0), debug = False):
    window_snapshot_callback.counter += 1
    rect = win32gui.GetWindowRect(hwnd)
    rect_adj = []
    rect_adj.append(rect[0]+8)
    rect_adj.append(rect[1]+52)
    rect_adj.append(rect[2]-8)
    rect_adj.append(rect[3]-8)


    width = rect_adj[2]-rect_adj[0]
    height = rect_adj[3]-rect_adj[1]
    
    scalar = round(min(height/DS_HEIGHT, width/DS_WIDTH))


    image_bbox = position_scaled(scalar, rect_adj, offset_tuple)
    
    image = ImageGrab.grab(bbox=image_bbox, all_screens=True).convert('L')


    width_regular = 6 * scalar
    width_t = 5 * scalar
    width_l = 4 * scalar
    width_i = 3 * scalar

    bbox_l = 0
    bbox_t = 0
    bbox_r = bbox_l
    bbox_b = image.height

    print("Showing Cropped Image")

    

    # e f g h i j k l m n
    # 6 5 6 6 3 5 6 4 6 6
        


    print(text)

    return



def gamestate_check(new_gamestate, regex_pattern, hwnd):
    offset_tuple = offset_dictionary[new_gamestate]
    inversion = image_inversion_dictionary[new_gamestate]
    grayscale_threshold = image_grayscale_threshold_dictionary[new_gamestate]
    threshold_type = image_threshold_type_dictionary[new_gamestate]
    
    #print("Gamestate: " + str(new_gamestate))
    results = window_snapshot_callback(hwnd,inversion, grayscale_threshold, threshold_type, offset_tuple, False)
    
    compare_hash = "1234567812345678"
    if new_gamestate in hash_dict_gamestates:
        compare_hash = hash_dict_gamestates[new_gamestate]

    #print(hamming_distance(results, compare_hash))
    #print("\n")

    if hamming_distance(results, compare_hash) < HAMMING_THRESHOLD:
        print("You are in state: " + gamestate_name_dict[new_gamestate])
        return new_gamestate

    '''if (results is not None) and re.match(regex_pattern, results) is not None:
        #os.system('cls' if os.name == 'nt' else 'clear')
        print("You are in state: " + gamestate_name_dict[new_gamestate])
        return new_gamestate
    '''
    
    return None

def hamming_distance(chaine1, chaine2):
    return sum(c1 != c2 for c1, c2 in zip(chaine1, chaine2))


#GET REGEX INTO GAMESTATE DEFINITIONS
pattern_battle = r".*wild.*"
pattern_overworld = r".*MENU.*"
pattern_menu_pokemon = r".*Choose.*"
pattern_menu_info = r".*INFO.*"
pattern_menu_moves = r".*MOVES.*"
pattern_program_title = r".*melonDS [0-9]+\.[0-9]+\.[0-9]*"

def number_concat_l2r(s1, s2, s3):
    if s3 != '':
        return number_concat_r2l(s1,s2,s3)
    elif s2 != '':
        return number_concat_r2l('', s1, s2)
    elif s1 != '':
        return number_concat_r2l('', '', s1)
    else:
        return ''


def number_concat_r2l(s1, s2, s3):
    if s3 == '':
        return ''
    
    ones = int(s3)
    tens = 0
    huns = 0

    if s2 != '':
        tens = int(s2)
        if s1 != '':
            huns = int(s1)
    
    value = (100*huns) + (10*tens) + ones
    return value

def process_data(data):
    processed_data = {}

    #check for gamestates
    for d in data:
        if isinstance(d, Gamestate) and data[d] is not None:
            processed_data["Next Gamestate"] = d
            return processed_data

    #Nickname
    if MenuAllPOI.NICKNAME in data:
        processed_data["Nickname"] = data[MenuAllPOI.NICKNAME].strip()

    #Pokeball
    if MenuAllPOI.POKEBALL in data:
        processed_data["Pokeball Type"] = data[MenuAllPOI.POKEBALL]
    
    #Pokedex Name
    if MenuBluePOI.DEX_NAME in data:
        processed_data["Name"] = data[MenuBluePOI.DEX_NAME].strip()

    if MenuBluePOI.TYPE_MONO in data and data[MenuBluePOI.TYPE_MONO] is not None:
        s1 = data[MenuBluePOI.TYPE_MONO]
        pos = s1.find(".")
        processed_data["Type1"] = s1[pos+1:]
        processed_data["Type2"] = None

    elif MenuBluePOI.TYPE_SPLIT_1 in data and data[MenuBluePOI.TYPE_SPLIT_1] is not None and MenuBluePOI.TYPE_SPLIT_2 in data and data[MenuBluePOI.TYPE_SPLIT_2] is not None:
        s1 = data[MenuBluePOI.TYPE_SPLIT_1]
        pos1 = s1.find(".")
        s2 = data[MenuBluePOI.TYPE_SPLIT_2]
        pos2 = s2.find(".")
        processed_data["Type1"] = s1[pos1+1:]
        processed_data["Type2"] = s2[pos2+1:]


    #Pokedex Number
    if MenuBluePOI.DEX_NUMBER in data:
        processed_data["Number"] = data[MenuBluePOI.DEX_NUMBER]

    #Gender
    if MenuAllPOI.GENDER in data:
        processed_data["Gender"] = data[MenuAllPOI.GENDER]
    
    #Level
    if MenuAllPOI.LEVEL_0 in data and MenuAllPOI.LEVEL_1 in data and MenuAllPOI.LEVEL_2 in data:
        processed_data["Level"] = number_concat_l2r(data[MenuAllPOI.LEVEL_0], data[MenuAllPOI.LEVEL_1], data[MenuAllPOI.LEVEL_2])        
    
    #Item
    if MenuAllPOI.ITEM in data:
        processed_data["Item"] = data[MenuAllPOI.ITEM].strip()

    #Nature
    if MenuBluePOI.NATURE in data:
        string = data[MenuBluePOI.NATURE]
        pos = string.find(" ")
        if pos > -1:
            string = string[:pos-len(string)]
        processed_data["Nature"] = string

    if MenuBluePOI.CATCH_LOCATION in data:
        processed_data["Location"] = data[MenuBluePOI.CATCH_LOCATION]
    
    # if MenuBluePOI.CATCH_LEVEL_0 in data and MenuBluePOI.CATCH_LEVEL_1 in data and MenuBluePOI.CATCH_LEVEL_2 in data:
    #     pass

    if MenuBluePOI.PERSONALITY in data:
        processed_data["Personality"] = data[MenuBluePOI.PERSONALITY].strip()


    #HP
    if  (MenuRedPOI.STAT_HP_CUR_0 in data and MenuRedPOI.STAT_HP_CUR_0 in data and MenuRedPOI.STAT_HP_CUR_0 in data and
        MenuRedPOI.STAT_HP_MAX_0 in data and MenuRedPOI.STAT_HP_MAX_0 in data and MenuRedPOI.STAT_HP_MAX_0 in data):
            processed_data["Max HP"] = number_concat_l2r(data[MenuRedPOI.STAT_HP_MAX_0], data[MenuRedPOI.STAT_HP_MAX_1], data[MenuRedPOI.STAT_HP_MAX_2])
            processed_data["Current HP"] = number_concat_r2l(data[MenuRedPOI.STAT_HP_CUR_0], data[MenuRedPOI.STAT_HP_CUR_1], data[MenuRedPOI.STAT_HP_CUR_2])
            
    
    #ATK
    if MenuRedPOI.STAT_ATK_0 in data and MenuRedPOI.STAT_ATK_1 in data and MenuRedPOI.STAT_ATK_2 in data:
        processed_data["Attack"] = number_concat_l2r(data[MenuRedPOI.STAT_ATK_0], data[MenuRedPOI.STAT_ATK_1], data[MenuRedPOI.STAT_ATK_2])        
    
    #DEF
    if MenuRedPOI.STAT_DEF_0 in data and MenuRedPOI.STAT_DEF_1 in data and MenuRedPOI.STAT_DEF_2 in data:
        processed_data["Defense"] = number_concat_l2r(data[MenuRedPOI.STAT_DEF_0], data[MenuRedPOI.STAT_DEF_1], data[MenuRedPOI.STAT_DEF_2]) 
    #SPATK
    if MenuRedPOI.STAT_SPEC_ATK_0 in data and MenuRedPOI.STAT_SPEC_ATK_1 in data and MenuRedPOI.STAT_SPEC_ATK_2 in data:
        processed_data["Special Attack"] = number_concat_l2r(data[MenuRedPOI.STAT_SPEC_ATK_0], data[MenuRedPOI.STAT_SPEC_ATK_1], data[MenuRedPOI.STAT_SPEC_ATK_2]) 
   
    #SPDEF
    if MenuRedPOI.STAT_SPEC_DEF_0 in data and MenuRedPOI.STAT_SPEC_DEF_1 in data and MenuRedPOI.STAT_SPEC_DEF_2 in data:
        processed_data["Special Defense"] = number_concat_l2r(data[MenuRedPOI.STAT_SPEC_DEF_0], data[MenuRedPOI.STAT_SPEC_DEF_1], data[MenuRedPOI.STAT_SPEC_DEF_2]) 
    #SPEED
    if MenuRedPOI.STAT_SPEED_0 in data and MenuRedPOI.STAT_SPEED_1 in data and MenuRedPOI.STAT_SPEED_2 in data:
        processed_data["Speed"] = number_concat_l2r(data[MenuRedPOI.STAT_SPEED_0], data[MenuRedPOI.STAT_SPEED_1], data[MenuRedPOI.STAT_SPEED_2]) 

    #ABILITY
    if MenuRedPOI.ABILITY_NAME in data:
        processed_data["Ability"] = data[MenuRedPOI.ABILITY_NAME]
    
    if MenuRedPOI.ABILITY_DESC_1 in data and MenuRedPOI.ABILITY_DESC_2 in data:
        processed_data["Ability Description"] = data[MenuRedPOI.ABILITY_DESC_1].strip() + " " + data[MenuRedPOI.ABILITY_DESC_2].strip()

    return processed_data

def super_gamestate_check(game_state, hwnd):
    #os.system('cls' if os.name == 'nt' else 'clear')

    scan_dict = {}

    #use our current gamestate and look up what gamestates we should be checking for
    other_gamestates = state_dict[game_state][GamestateSetting.ADJACENCIES]
    
    #add gamestate data for each adjacent gamestate
    for gamestate in other_gamestates:
        scan_dict[gamestate] = state_dict[gamestate]

    #add any additional scan info based on the current gamestate
    for scan_definition in state_dict[game_state][GamestateSetting.SCANS]:
        scan_dict = scan_dict|scan_definition

    results = scan(hwnd, scan_dict, DebugTag.ALL)

    os.system('cls' if os.name == 'nt' else 'clear')

    print("Gamestate: " + str(game_state))

    data = process_data(results)

    for d in data:
        print(str(d) + ": " + str(data[d]))

    if "Next Gamestate" in data:
        game_state = data["Next Gamestate"]

    return game_state

def gamestate_test():
    
    gamestate_test.windowClassName = "test"

    def callback(hwnd, ctx):
        if(re.match(pattern_program_title, win32gui.GetWindowText(hwnd))):
            gamestate_test.windowClassName = win32gui.GetClassName(hwnd)
            print(gamestate_test.windowClassName)
    
    win32gui.EnumWindows(callback, None)
    hwnd = win32gui.FindWindow(gamestate_test.windowClassName, None)

    game_state = Gamestate.MENU_BLUE


    #os.system('cls' if os.name == 'nt' else 'clear')
    print("You are in state: " + gamestate_name_dict[game_state] )   
    currTime = datetime.datetime.now()
    while True:
        prevTime = currTime
        currTime = datetime.datetime.now()
        delta = (currTime - prevTime).microseconds/1000000
        #os.system('cls' if os.name == 'nt' else 'clear')
        print("Delta: " + str(delta))
        if delta > 0:
            print("Iterations per Second: " + str(int(1/delta)))

        #Do thing

        game_state = super_gamestate_check(game_state, hwnd)
            
def main():
    try:
        #file = open('D:\Code\Pokedex\level_data_rev.json')
        #structure goes level->stat->nature->low/high
        print('Pokedex.')
        gamestate_test()
        
    except KeyboardInterrupt: 
        pass



if(__name__ == "__main__"):
    main()