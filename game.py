from chessAI import *

class Game():

    def __init__(self, boardStr):
        self.board = chess.Board(boardStr)

    def doAMove(self, movestr):
        move = chess.Move.from_uci(movestr)
        if (move in self.board.legal_moves):
            isPassant = self.board.is_en_passant(move)
            castlingSide = self.getSideofCastling(move)
            sanMove = str(self.board.san(move))
            self.board.push(move)


            if(isPassant):
                return ("PassantMove", sanMove)
            elif(castlingSide != ""):
                return (castlingSide, sanMove)
            return ("Moved", sanMove)
        else:
            return ("", "")

    def getSideofCastling(self, move):
        result = ""
        if(self.board.is_queenside_castling(move)):
            result = "queenside"
        elif(self.board.is_kingside_castling(move)):
            result = "kingside"
        return result

    def isCheckMate(self):
        return self.board.is_checkmate()

    def isStalemate(self):
        return self.board.is_stalemate()

    def isCheck(self):
        return self.board.is_check()

    def suggestedMove(self,starts):
        return negamaxRoot(5,self.board,starts)

    def isvalid(self):
        return self.board.is_valid() or self.isStalemate() or self.isCheckMate()
