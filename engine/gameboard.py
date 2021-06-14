import defs


class GameBoard():
    def __init__(self):
        self.definitions = defs.Defs()
        self.pieces = [0] * self.definitions.BRD_SQ_NUM
        self.side = self.definitions.COLOURS['WHITE']
        self.fiftyMove = 0
        self.hisPly = 0
        self.history = []
        self.ply = 0
        self.enPas = 0
        self.castlePerm = 0
        self.material = [0]*(2)  # WHITE,BLACK material of pieces
        self.pceNum = [0]*(13)  # indexed by Pce
        self.pList = [0]*(14 * 10)
        self.posKey = 0
        self.moveList = [0]*(self.definitions.MAXDEPTH *
                             self.definitions.MAXPOSITIONMOVES)
        self.moveScores = [0]*(self.definitions.MAXDEPTH *
                               self.definitions.MAXPOSITIONMOVES)
        self.moveListStart = [0]*(self.definitions.MAXDEPTH)
        self.PvTable = []
        self.PvArray = [0]*(self.definitions.MAXDEPTH)
        self.searchHistory = [0]*(14 * self.definitions.BRD_SQ_NUM)
        self.searchKillers = [0]*(3 * self.definitions.MAXDEPTH)

    def PCEINDEX(self, pce, pceNum):
        return (pce * 10 + pceNum)

    def CheckBoard(self):

        t_pceNum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        t_material = [0, 0]
        sq64, t_piece, t_pce_num, sq120, colour, pcount = 0

        for t_piece in range(self.PIECES['wP'], self.PIECES['bK']+1):
            for t_pce_num in range(0, self.pceNum[t_piece]):
                sq120 = self.pList[self.PCEINDEX(t_piece, t_pce_num)]
                if(self.pieces[sq120] != t_piece):
                    return 0

        for sq64 in range(0, 65):
            sq120 = self.definitions.SQ120(sq64)
            t_piece = self.pieces[sq120]
            t_pceNum[t_piece] += 1
            t_material[self.definitions.PieceCol[t_piece]
                ] += self.definitions.PieceVal[t_piece]

        for t_piece in range(self.definitions.PIECES['wP'], self.definitions.PIECES['bP']+1):
            if t_pceNum[t_piece] != self.pceNum[t_piece]:
                print('Error t_pceNum')
                return 0

        if t_material[self.definitions.COLOURS['WHITE']] != self.material[self.definitions.COLOURS['WHITE']] or t_material[self.definitions.COLOURS['BLACK']] != self.material[self.definitions.COLOURS['BLACK']]:
            print('Error t_material')
            return 0

        if self.side != self.definitions.COLOURS['WHITE'] and self.side != self.definitions.COLOURS['BLACK']:
            print('Error self.side')
            return 0

        if self.GeneratePosKey() != self.posKey:
            print('Error self.posKey')
            return 0
        return 1

    def PrintBoard(self):

        sq, file, rank, piece = None

        print("\nGame Board:\n")
        for rank in range(self.definitions.RANKS['RANK_8'], self.definitions.RANKS['RANK_1'], -1):
            line = (self.definitions.RankChar[rank] + "  ")
            for file in range(self.definitions.FILES['FILE_A'], self.definitions.FILES['FILE_H'], 1):
                sq = self.definitions.FR2SQ(file, rank)
                piece = self.pieces[sq]
                line += (" " + self.definitions.PceChar[piece] + " ")
            print(line)
        print("")
        line = "   "
        for file in range(self.definitions.FILES['FILE_A'], self.definitions.FILES['FILE_H']):
            line += (' '+self.definitions.FileChar[file] + ' ')
        print(line)
        print("side:" + self.definitions.SideChar[self.side])
        print("enPas:" + self.enPas)
        line = ""

        if(self.castlePerm & self.definitions.CASTLEBIT['WKCA']): line += 'K'
        if(self.castlePerm & self.definitions.CASTLEBIT['WQCA']): line += 'Q'
        if(self.castlePerm & self.definitions.CASTLEBIT['BKCA']): line += 'k'
        if(self.castlePerm & self.definitions.CASTLEBIT['BQCA']): line += 'q'
        print("castle:" + line)
        print("key:" + self.posKey.toString(16))

