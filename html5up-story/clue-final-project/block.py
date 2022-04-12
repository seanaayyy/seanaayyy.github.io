# block class for clue
# this is the space the players move on

class Block:
    def __init__(self, x, y, room=None):
        self.player = None  # color of player or None if there is no player there
        self.x = x
        self.y = y
        self.room = room  # what room the space is an entrance to (if any)

    def get_coordinates(self):
        return [self.x, self.y]

    def get_room(self):
        return self.room

    # sets the player if there isn't a player already there
    def set_player(self, player):
        if self.player is None:
            self.player = player
            return True
        return False

    # sets room if block is an entrance to that room
    def set_room(self, room):
        self.room = room

    # Be careful in using this as players could get lost, but this may be useful in certain cases
    def remove_player(self):
        if self.player is None:
            return False
        self.player = None
        return True

    def get_player(self):
        return self.player

    def has_player(self):
        if self.player is not None:
            return True
        return False

    def enter_room(self):
        if self.room is not None and not self.room.has_player(self.player):
            self.room.add_player(self.player)
            self.player = None
            return True
        return False

    def move_player(self, block):
        if block.get_player() is None:
            block.set_player(self.player)
            self.player = None
            return True
        return False

    def load_blocks(self):
        rows = 22
        columns = 23
        # create 2d list with rows and columns to match the board
        block_grid = [[Block(None, None, None) for j in range(columns)] for i in range(rows)]
        A4 = Block(77, 163, None)
        B4 = Block(103, 163, None)
        C4 = Block(130, 163, None)
        D4 = Block(156, 163, None)
        E4 = Block(183, 163, None)
        A5 = Block(77, 190, None)
        B5 = Block(103, 190, None)
        C5 = Block(130, 190, None)
        D5 = Block(156, 190, None)
        E5 = Block(183, 190, None)
        A11 = Block(77, 349, None)
        B11 = Block(103, 349, None)
        C11 = Block(130, 349, None)
        D11 = Block(156, 349, None)
        E11 = Block(183, 349, None)
        A17 = Block(77, 509, None)
        B17 = Block(103, 509, None)
        C17 = Block(130, 509, None)
        D17 = Block(156, 509, None)
        A18 = Block(77, 535, None)
        B18 = Block(103, 535, None)
        C18 = Block(130, 535, None)
        D18 = Block(156, 535, None)
        E17 = Block(183, 509, None)
        E18 = Block(183, 535, None)
        E19 = Block(183, 562, None)
        F4 = Block(210, 163, None)
        F5 = Block(210, 190, None)
        F6 = Block(210, 217, None)
        F10 = Block(210, 323, None)
        F11 = Block(210, 349, None)
        F12 = Block(210, 376, None)
        F13 = Block(210, 402, None)
        F14 = Block(210, 429, None)
        F15 = Block(210, 455, None)
        F16 = Block(210, 482, None)
        F17 = Block(210, 509, None)
        F18 = Block(210, 535, None)
        F19 = Block(210, 562, None)
        F20 = Block(210, 588, None)
        F21 = Block(210, 615, None)
        F22 = Block(210, 641, None)
        G1 = Block(236, 84, None)
        G2 = Block(236, 110, None)
        G3 = Block(236, 137, None)
        G4 = Block(236, 163, None)
        G5 = Block(236, 190, None)
        G6 = Block(236, 217, None)
        G7 = Block(236, 243, None)
        G8 = Block(236, 270, None)
        G9 = Block(236, 296, None)
        G10 = Block(236, 323, None)
        G11 = Block(236, 349, None)
        G12 = Block(236, 376, None)
        G13 = Block(236, 402, None)
        G14 = Block(236, 429, None)
        G15 = Block(236, 455, None)
        G16 = Block(236, 482, None)
        G17 = Block(236, 509, None)
        G18 = Block(236, 535, None)
        G19 = Block(236, 562, None)
        G20 = Block(236, 588, None)
        G21 = Block(236, 615, None)
        G22 = Block(236, 641, None)
        G23 = Block(236, 668, None)
        H1 = Block(263, 84, None)
        H2 = Block(263, 110, None)
        H3 = Block(263, 137, None)
        H4 = Block(263, 163, None)
        H5 = Block(263, 190, None)
        H6 = Block(263, 217, None)
        H7 = Block(263, 243, None)
        H8 = Block(263, 270, None)
        H9 = Block(263, 296, None)
        H10 = Block(263, 323, None)
        H11 = Block(263, 349, None)
        H12 = Block(263, 376, None)
        H13 = Block(263, 402, None)
        H14 = Block(263, 429, None)
        H15 = Block(263, 455, None)
        H16 = Block(263, 482, None)
        H23 = Block(263, 668, None)
        I23 = Block(289, 668, None)
        I7 = Block(289, 243, None)
        J7 = Block(316, 243, None)
        K7 = Block(342, 243, None)
        L7 = Block(369, 243, None)
        M7 = Block(395, 243, None)
        I15 = Block(289, 455, None)
        J15 = Block(316, 455, None)
        K15 = Block(342, 455, None)
        L15 = Block(369, 455, None)
        M15 = Block(395, 455, None)
        I16 = Block(289, 482, None)
        J16 = Block(316, 482, None)
        K16 = Block(342, 482, None)
        L16 = Block(369, 482, None)
        M16 = Block(395, 482, None)
        N7 = Block(422, 243, None)
        N8 = Block(422, 270, None)
        N9 = Block(422, 296, None)
        N10 = Block(422, 323, None)
        N11 = Block(422, 349, None)
        N12 = Block(422, 376, None)
        N13 = Block(422, 402, None)
        N14 = Block(422, 429, None)
        N15 = Block(422, 455, None)
        N16 = Block(422, 482, None)
        N23 = Block(422, 668, None)
        O23 = Block(448, 668, None)
        O1 = Block(448, 84, None)
        O2 = Block(448, 110, None)
        O3 = Block(448, 137, None)
        O4 = Block(448, 163, None)
        O5 = Block(448, 190, None)
        O6 = Block(448, 217, None)
        O7 = Block(448, 243, None)
        O8 = Block(448, 270, None)
        O9 = Block(448, 296, None)
        O10 = Block(448, 323, None)
        O11 = Block(448, 349, None)
        O12 = Block(448, 376, None)
        O13 = Block(448, 402, None)
        O14 = Block(448, 429, None)
        O15 = Block(448, 455, None)
        O16 = Block(448, 482, None)
        P1 = Block(475, 84, None)
        P2 = Block(475, 110, None)
        P3 = Block(475, 137, None)
        P4 = Block(475, 163, None)
        P5 = Block(475, 190, None)
        P6 = Block(475, 217, None)
        P7 = Block(475, 243, None)
        P8 = Block(475, 270, None)
        P15 = Block(475, 455, None)
        P16 = Block(475, 482, None)
        P17 = Block(475, 509, None)
        P18 = Block(475, 535, None)
        P19 = Block(475, 562, None)
        P20 = Block(475, 588, None)
        P21 = Block(475, 615, None)
        P22 = Block(475, 641, None)
        P23 = Block(475, 668, None)
        Q6 = Block(502, 217, None)
        R6 = Block(528, 217, None)
        S6 = Block(555, 217, None)
        T6 = Block(581, 217, None)
        U6 = Block(608, 217, None)
        V6 = Block(634, 217, None)
        Q7 = Block(502, 243, None)
        R7 = Block(528, 243, None)
        S7 = Block(555, 243, None)
        T7 = Block(581, 243, None)
        U7 = Block(608, 243, None)
        V7 = Block(634, 243, None)
        Q8 = Block(502, 270, None)
        R8 = Block(528, 270, None)
        S8 = Block(555, 270, None)
        T8 = Block(581, 270, None)
        U8 = Block(608, 270, None)
        V8 = Block(634, 270, None)
        Q15 = Block(502, 455, None)
        Q16 = Block(502, 482, None)
        Q17 = Block(502, 509, None)
        Q18 = Block(502, 535, None)
        Q19 = Block(502, 562, None)
        Q20 = Block(502, 588, None)
        Q21 = Block(502, 615, None)
        Q22 = Block(502, 641, None)
        R15 = Block(528, 455, None)
        R16 = Block(528, 482, None)
        R17 = Block(528, 509, None)
        S16 = Block(555, 482, None)
        T16 = Block(581, 482, None)
        U16 = Block(608, 482, None)
        V16 = Block(634, 482, None)
        S17 = Block(555, 509, None)
        T17 = Block(581, 509, None)
        U17 = Block(608, 509, None)
        V17 = Block(634, 509, None)

        block_grid[0][3] = A4
        block_grid[4][3] = E4
        block_grid[1][3] = B4
        block_grid[2][3] = C4
        block_grid[3][3] = D4
        block_grid[0][4] = A5
        block_grid[1][4] = B5
        block_grid[2][4] = C5
        block_grid[3][4] = D5
        block_grid[4][4] = E5
        block_grid[5][3] = F4
        block_grid[5][4] = F5
        block_grid[5][5] = F6
        block_grid[5][9] = F10
        block_grid[5][10] = F11
        block_grid[5][11] = F12
        block_grid[5][12] = F13
        block_grid[5][13] = F14
        block_grid[5][14] = F15
        block_grid[5][15] = F16
        block_grid[5][16] = F17
        block_grid[5][17] = F18
        block_grid[5][18] = F19
        block_grid[5][19] = F20
        block_grid[5][20] = F21
        block_grid[5][21] = F22
        block_grid[0][10] = A11
        block_grid[1][10] = B11
        block_grid[2][10] = C11
        block_grid[3][10] = D11
        block_grid[4][10] = E11
        block_grid[0][16] = A17
        block_grid[1][16] = B17
        block_grid[2][16] = C17
        block_grid[3][16] = D17
        block_grid[4][16] = E17
        block_grid[0][17] = A18
        block_grid[1][17] = B18
        block_grid[2][17] = C18
        block_grid[3][17] = D18
        block_grid[4][17] = E18
        block_grid[4][18] = E19
        block_grid[6][0] = G1
        block_grid[6][1] = G2
        block_grid[6][2] = G3
        block_grid[6][3] = G4
        block_grid[6][4] = G5
        block_grid[6][5] = G6
        block_grid[6][6] = G7
        block_grid[6][7] = G8
        block_grid[6][8] = G9
        block_grid[6][9] = G10
        block_grid[6][10] = G11
        block_grid[6][11] = G12
        block_grid[6][12] = G13
        block_grid[6][13] = G14
        block_grid[6][14] = G15
        block_grid[6][15] = G16
        block_grid[6][16] = G17
        block_grid[6][17] = G18
        block_grid[6][18] = G19
        block_grid[6][19] = G20
        block_grid[6][20] = G21
        block_grid[6][21] = G22
        block_grid[6][22] = G23
        block_grid[7][0] = H1
        block_grid[7][1] = H2
        block_grid[7][2] = H3
        block_grid[7][3] = H4
        block_grid[7][4] = H5
        block_grid[7][5] = H6
        block_grid[7][6] = H7
        block_grid[7][7] = H8
        block_grid[7][8] = H9
        block_grid[7][9] = H10
        block_grid[7][10] = H11
        block_grid[7][11] = H12
        block_grid[7][12] = H13
        block_grid[7][13] = H14
        block_grid[7][14] = H15
        block_grid[7][15] = H16
        block_grid[7][22] = H23
        block_grid[8][22] = I23
        block_grid[8][6] = I7
        block_grid[9][6] = J7
        block_grid[10][6] = K7
        block_grid[11][6] = L7
        block_grid[12][6] = M7
        block_grid[8][14] = I15
        block_grid[9][14] = J15
        block_grid[10][14] = K15
        block_grid[11][14] = L15
        block_grid[12][14] = M15
        block_grid[8][15] = I16
        block_grid[9][15] = J16
        block_grid[10][15] = K16
        block_grid[11][15] = L16
        block_grid[12][15] = M16
        block_grid[13][6] = N7
        block_grid[13][7] = N8
        block_grid[13][8] = N9
        block_grid[13][9] = N10
        block_grid[13][10] = N11
        block_grid[13][11] = N12
        block_grid[13][12] = N13
        block_grid[13][13] = N14
        block_grid[13][14] = N15
        block_grid[13][15] = N16
        block_grid[13][22] = N23
        block_grid[14][22] = O23
        block_grid[14][0] = O1
        block_grid[14][1] = O2
        block_grid[14][2] = O3
        block_grid[14][3] = O4
        block_grid[14][4] = O5
        block_grid[14][5] = O6
        block_grid[14][6] = O7
        block_grid[14][7] = O8
        block_grid[14][8] = O9
        block_grid[14][9] = O10
        block_grid[14][10] = O11
        block_grid[14][11] = O12
        block_grid[14][12] = O13
        block_grid[14][13] = O14
        block_grid[14][14] = O15
        block_grid[14][15] = O16
        block_grid[15][0] = P1
        block_grid[15][1] = P2
        block_grid[15][2] = P3
        block_grid[15][3] = P4
        block_grid[15][4] = P5
        block_grid[15][5] = P6
        block_grid[15][6] = P7
        block_grid[15][7] = P8
        block_grid[15][14] = P15
        block_grid[15][15] = P16
        block_grid[15][16] = P17
        block_grid[15][17] = P18
        block_grid[15][18] = P19
        block_grid[15][19] = P20
        block_grid[15][20] = P21
        block_grid[15][21] = P22
        block_grid[15][22] = P23
        block_grid[16][5] = Q6
        block_grid[17][5] = R6
        block_grid[18][5] = S6
        block_grid[19][5] = T6
        block_grid[20][5] = U6
        block_grid[21][5] = V6
        block_grid[16][6] = Q7
        block_grid[17][6] = R7
        block_grid[18][6] = S7
        block_grid[19][6] = T7
        block_grid[20][6] = U7
        block_grid[21][6] = V7
        block_grid[16][7] = Q8
        block_grid[17][7] = R8
        block_grid[18][7] = S8
        block_grid[19][7] = T8
        block_grid[20][7] = U8
        block_grid[21][7] = V8
        block_grid[16][14] = Q15
        block_grid[16][15] = Q16
        block_grid[16][16] = Q17
        block_grid[16][17] = Q18
        block_grid[16][18] = Q19
        block_grid[16][19] = Q20
        block_grid[16][20] = Q21
        block_grid[16][21] = Q22
        block_grid[17][14] = R15
        block_grid[17][15] = R16
        block_grid[17][16] = R17
        block_grid[18][15] = S16
        block_grid[19][15] = T16
        block_grid[20][15] = U16
        block_grid[21][15] = V16
        block_grid[18][16] = S17
        block_grid[19][16] = T17
        block_grid[20][16] = U17
        block_grid[21][16] = V17

        return block_grid


