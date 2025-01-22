#Un tablero de ajedrez es una matriz de 8x8. En vez de representar solo las casillas blancas y negras, podemos representar las piezas de ajedrez. Usaremos letras para representar las piezas: P para peón, R para torre, N para caballo (knight), B para alfil, Q para reina y K para rey. Las piezas negras se representan con letras minúsculas y las blancas con letras mayúsculas.


chess_board = [
['r1','n1','b1','q','k','b2','n2','r2'],
['p1','p2','p3','p4','p5','p6','p7','p8'],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
['P1','P2','P3','P4','P5','P6','P7','P8'],
['R2','N2','b2','Q','K','B1','N1','R1'],
]
print(chess_board)

'''Por ejemplo, si el caballo blanco está en la posición (7, 1) (segunda casilla de la última fila), las posiciones posibles a las que puede moverse son:
(5, 0)
(5, 2)
(6, 3)
Es importante verificar que estas posiciones estén dentro de los límites del tablero y no contengan piezas blancas.

Si movemos el caballo negro moverse adelante y a la derecha, el tablero se vería así:'''

chess_board[0][2] = 0 #original location of the horse is now empty
chess_board[2][1] = 'b1' #New location of the horse
print(chess_board)

'''Resoult

[['r1', 'n1', 0, 'q', 'k', 'b2', 'n2', 'r2'], 
 ['p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8'], 
 [0, 'b1', 0, 0, 0, 0, 0, 0], 
 [0, 0, 0, 0, 0, 0, 0, 0], 
 [0, 0, 0, 0, 0, 0, 0, 0], 
 [0, 0, 0, 0, 0, 0, 0, 0], 
 ['P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8'], 
 ['R2', 'N2', 'b2', 'Q', 'K', 'B1', 'N1', 'R1']]'''