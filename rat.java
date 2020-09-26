class rat{

public static  int[][] solution = new int[4][4];

public static void sol(int[][] maze, int currow, int currcol){
if(maze[currow][currcol]==0)
return;
solution[currow][currcol]=1;
if(currow==3 && currcol==3)
return;
sol(maze,currow,currcol+1);
if(currow!=3 && currcol!=3)
sol(maze,currow+1,currcol);

}

public static void main(String[] args){

int[][]maze = {
		{1, 0, 0, 0},
		{1, 1, 0, 1},
		{0, 1, 0, 0},
		{1, 1, 1, 1}
	    };
int currcol=0;
int currow=0;
sol(maze,currcol,currow);

for(int i=0;i<4;i++){
for(int j=0;j<4;j++){
System.out.print(solution[i][j]);
}
System.out.println();
}


}}
