# **<span style="text-decoration:underline;">Stalemate: A Python UCI Engine</span>**


# <span style="text-decoration:underline;">Introduction</span>

**What’s a UCI Engine?**

A UCI Engine is GUI (Graphical User Interface) Independent, It works on standard input and output. The Input usually is in form of FEN (Forsyth–Edwards Notation). 

**Features and Functionalities:**



1. It will identify itself with a UCI Command.
2. It will receive the board position as FEN and will spend at max 2000 ms to search for the best move.
3. The best move might change with time and as the graph of the search tree increases. 
4. The engine will also generate a list of moves for both sides, this list is called principal variation. 





# <span style="text-decoration:underline;">Components of the engine:</span>



1. **<span style="text-decoration:underline;">Board:</span>** Stores the current state of the board, past moves made on the board, side to move, en-passant permission, castle permission and pawn promotion permissions. 
2. **<span style="text-decoration:underline;">Legal Moves (Moves Generator):</span>** Generates all valid/ legal moves based on the current board position. Legal moves include en-passant, castling, pawn promotion, capture, check and other special moves. 
3. **<span style="text-decoration:underline;">Evaluation:</span>** Evaluates the position based on the position table of each piece and calculates a score based on the piece value and positions. This is the brain and heart of the engine and tells the strength of the engine. 
4. **<span style="text-decoration:underline;">Search:</span>** All valid moves will be arranged in form of a tree of a certain depth based on the strength of the CPU being used. The tree will search for a move with the highest positive score for white pieces and the largest negative score for black pieces, this step will occur recursively for a certain depth based on user preference or the CPU strength. 
5. **<span style="text-decoration:underline;">Framework:</span>** To integrate all components as one package. 
