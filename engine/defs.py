import math

class defs():
    def __init__(self):
        self.PIECES = {'EMPTY': 0, 'wP': 1, 'wN': 2, 'wB': 3, 'wR': 4, 'wQ': 5, 'wK': 6,
                    'bP': 7, 'bN': 8, 'bB': 9, 'bR': 10, 'bQ': 11, 'bK': 12}

        self.BRD_SQ_NUM = 120

        self.FILES = {'FILE_A': 0, 'FILE_B': 1, 'FILE_C': 2, 'FILE_D': 3,
            'FILE_E': 4, 'FILE_F': 5, 'FILE_G': 6, 'FILE_H': 7, 'FILE_NONE': 8}

        self.RANKS = {'RANK_1': 0, 'RANK_2': 1, 'RANK_3': 2, 'RANK_4': 3,
            'RANK_5': 4, 'RANK_6': 5, 'RANK_7': 6, 'RANK_8': 7, 'RANK_NONE': 8}

        self.COLOURS = {'WHITE': 0, 'BLACK': 1, 'BOTH': 2}

        self.CASTLEBIT = {'WKCA': 1, 'WQCA': 2, 'BKCA': 4, 'BQCA': 8}

        self.SQUARES = {
        'A1': 21, 'B1': 22, 'C1': 23, 'D1': 24, 'E1': 25, 'F1': 26, 'G1': 27, 'H1': 28,
        'A8': 91, 'B8': 92, 'C8': 93, 'D8': 94, 'E8': 95, 'F8': 96, 'G8': 97, 'H8': 98,
        'NO_SQ': 99, 'OFFBOARD': 100
        }


        self.MAXGAMEMOVES = 2048
        self.MAXPOSITIONMOVES = 256
        self.MAXDEPTH = 64
        self.INFINITE = 30000
        self.MATE = 29000
        self.PVENTRIES = 10000

        self.FilesBrd = [0] * (self.BRD_SQ_NUM)
        self.RanksBrd = [0] * (self.BRD_SQ_NUM)

        self.START_FEN = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"

        self.PceChar = ".PNBRQKpnbrqk"
        self.SideChar = "wb-"
        self.RankChar = "12345678"
        self.FileChar = "abcdefgh"


        def FR2SQ(self, f, r):
            return ((21 + (f)) + ((r) * 10))


        self.PieceBig = [0, 0, 1, 1, 1, 1,
            1, 0, 1, 1, 1, 1, 1]
        self.PieceMaj = [0, 0, 0, 0, 1, 1,
            1, 0, 0, 0, 1, 1, 1]
        self.PieceMin = [0, 0, 1, 1, 0, 0,
            0, 0, 1, 1, 0, 0, 0]
        self.PieceVal = [0, 100, 325, 325, 550, 1000,
            50000, 100, 325, 325, 550, 1000, 50000]
        self.PieceCol = [self.COLOURS['BOTH'], self.COLOURS['WHITE'], self.COLOURS['WHITE'], self.COLOURS['WHITE'], self.COLOURS['WHITE'], self.COLOURS['WHITE'], self.COLOURS['WHITE'],
            self.COLOURS['BLACK'], self.COLOURS['BLACK'], self.COLOURS['BLACK'], self.COLOURS['BLACK'], self.COLOURS['BLACK'], self.COLOURS['BLACK']]

        self.PiecePawn = [0, 1, 0, 0, 0, 0,
            0, 1, 0, 0, 0, 0, 0]
        self.PieceKnight = [0, 0, 1, 0, 0, 0,
            0, 0, 1, 0, 0, 0, 0]
        self.PieceKing = [0, 0, 0, 0, 0, 0,
            1, 0, 0, 0, 0, 0, 1]
        self.PieceRookQueen = [0, 0, 0, 0, 1, 1,
            0, 0, 0, 0, 1, 1, 0]
        self.PieceBishopQueen = [0, 0, 0, 1, 0, 1,
            0, 0, 0, 1, 0, 1, 0]
        self.PieceSlides = [0, 0, 0, 1, 1, 1,
            0, 0, 0, 1, 1, 1, 0]

        self.KnDir = [-8, -19,	-21, -12, 8, 19, 21, 12]
        self.RkDir = [-1, -10,	1, 10]
        self.BiDir = [-9, -11, 11, 9]
        self.KiDir = [-1, -10,	1, 10, -9, -11, 11, 9]

        self.DirNum = [0, 0, 8, 4, 4, 8, 8, 0, 8, 4, 4, 8, 8]
        self.PceDir = [0, 0, self.KnDir, self.BiDir, self.RkDir, self.KiDir,
            self.KiDir, 0, self.KnDir, self.BiDir, self.RkDir, self.KiDir, self.KiDir]
        self.LoopNonSlidePce = [self.PIECES['wN'], self.PIECES['wK'],
            0, self.PIECES['bN'], self.PIECES['bK'], 0]
        self.LoopNonSlideIndex = [0, 3]
        self.LoopSlidePce = [self.PIECES['wB'], self.PIECES['wR'], self.PIECES['wQ'],
            0, self.PIECES['bB'], self.PIECES['bR'], self.PIECES['bQ'], 0]
        self.LoopSlideIndex = [0, 4]

        self.PieceKeys = [[0] * 14] * 120
        self.SideKey = None
        self.CastleKeys = [0] * 16

        self.Sq120ToSq64 = [0]*self.BRD_SQ_NUM
        self.Sq64ToSq120 = [0]*64


        def RAND_32(self):
            return (math.floor((math.random()*255)+1) << 23) or (math.floor((math.random()*255)+1) << 16) or (math.floor((math.random()*255)+1) << 8) or math.floor((math.random()*255)+1)


        self.Mirror64 = [


        56	,	57	,	58	,	59	,	60	,	61	,	62	,	63	,
        48	,	49	,	50	,	51	,	52	,	53	,	54	,	55	,
        40	,	41	,	42	,	43	,	44	,	45	,	46	,	47	,
        32	,	33	,	34	,	35	,	36	,	37	,	38	,	39	,
        24	,	25	,	26	,	27	,	28	,	29	,	30	,	31	,
        16	,	17	,	18	,	19	,	20	,	21	,	22	,	23	,
        8	,	9	,	10	,	11	,	12	,	13	,	14	,	15	,
        0	,	1	,	2	,	3	,	4	,	5	,	6	,	7
        ]


        def SQ64(self, sq120):
            return self.Sq120ToSq64[(sq120)]


        def SQ120(self, sq64):
            return self.Sq64ToSq120[(sq64)]


        def PCEINDEX(self, pce, pceNum):
            return (pce * 10 + pceNum)


        def MIRROR64(self, sq):
            return self.Mirror64[sq]


        self.Kings = [self.PIECES['wK'], self.PIECES['bK']]
        self.CastlePerm = [
            15, 15, 15, 15, 15, 15, 15, 15, 15, 15,
            15, 15, 15, 15, 15, 15, 15, 15, 15, 15,
            15, 13, 15, 15, 15, 12, 15, 15, 14, 15,
            15, 15, 15, 15, 15, 15, 15, 15, 15, 15,
            15, 15, 15, 15, 15, 15, 15, 15, 15, 15,
            15, 15, 15, 15, 15, 15, 15, 15, 15, 15,
            15, 15, 15, 15, 15, 15, 15, 15, 15, 15,
            15, 15, 15, 15, 15, 15, 15, 15, 15, 15,
            15, 15, 15, 15, 15, 15, 15, 15, 15, 15,
            15,  7, 15, 15, 15,  3, 15, 15, 11, 15,
            15, 15, 15, 15, 15, 15, 15, 15, 15, 15,
            15, 15, 15, 15, 15, 15, 15, 15, 15, 15
        ]


        '''
        0000 0000 0000 0000 0000 0111 1111 -> From 0x7F
        0000 0000 0000 0011 1111 1000 0000 -> To >> 7, 0x7F
        0000 0000 0011 1100 0000 0000 0000 -> Captured >> 14, 0xF
        0000 0000 0100 0000 0000 0000 0000 -> EP 0x40000
        0000 0000 1000 0000 0000 0000 0000 -> Pawn Start 0x80000
        0000 1111 0000 0000 0000 0000 0000 -> Promoted Piece >> 20, 0xF
        0001 0000 0000 0000 0000 0000 0000 -> Castle 0x1000000
        '''


        def FROMSQ(self, m):
            return (m & 0x7F)


        def TOSQ(self, m):
            return ((m >> 7) & 0x7F)


        def CAPTURED(self, m):
            return ((m >> 14) & 0xF)


        def PROMOTED(self, m):
            return ((m >> 20) & 0xF)

        self.MFLAGEP = 0x40000
        self.MFLAGPS = 0x80000
        self.MFLAGCA = 0x1000000

        self.MFLAGCAP = 0x7C000
        self.MFLAGPROM = 0xF00000

        self.NOMOVE = 0

        def SQOFFBOARD(sq):
            if(self.FilesBrd['sq'] == self.SQUARES['OFFBOARD']):
                    return 1
            return 0	

        '''def HASH_PCE(pce, sq): 
            GameBoard.posKey ^= PieceKeys[(pce * 120) + sq]


        def HASH_CA():
            GameBoard.posKey ^= CastleKeys[GameBoard.castlePerm]
        def HASH_SIDE():
            GameBoard.posKey ^= SideKey
        def HASH_EP():
            GameBoard.posKey ^= PieceKeys[GameBoard.enPas]'''


class GameController():
    def __init__(self):
        self.defs_obj = defs()
        self.EngineSide = self.defs_obj.COLOURS['BOTH']
        self.PlayerSide = self.defs_obj.COLOURS['BOTH']
        self.BoardFlipped = 0
        self.GameOver = 0
