#include<stdio.h>
#include<stdlib.h>

#define C 12
#define R 12

int count = 0;
int num = 0;
int chessboard[R][C] ;
int move[8][2] = {{-1,-2} ,{-2,-1}, {-2,1}, {-1,2}, {1,2}, {2,1} , {2,-1}, {1,-2}};

void init_chessboard() {
	for(int i = 0; i < R; i++) {
		if(i==0 || i==1 || i==10 || i==11) {
			for(int j = 0; j < C; j++) {
				chessboard[i][j] = -1;
            }
    	}
		else {
			for(int j = 0; j < C; j++) {
				if(j==0 || j==1 || j==10 || j==11) {
					chessboard[i][j] = -1;
                } else {
					chessboard[i][j] = 0;
                }
			}
		}
	}
}

void horse(int x, int y) {
	chessboard [x] [y] = ++ count;
	if(count == 64) {
        printf ("%d solução: \n", ++num);
        for(int i = 2; i < R-2; i++) {
            for(int j = 2; j < C-2; j++) {
                printf("%3d", chessboard[i][j]);
            }
            printf("\n");
        }
        printf("-------------------------\n");
	}
	else {
		int a,b;
		for(int i = 0; i <8; i ++) {
			a = x + move[i][0];
			b = y + move[i][1];
			if(chessboard [a] [b] == 0)	{
				horse(a, b);
				chessboard [a] [b] = 0;
				--count;
			}
		}
	}
}

int main(void) {
	printf("Todas as soluções do problema do passeio do cavalo.");
	for(int i = 2; i < R-2; i++) {
		for(int j = 2; j < C-2; j++) {
			init_chessboard();
			count = 0;
			horse(i,j);
		}
	}
	printf("\nfim\n");
	return 0;
}
