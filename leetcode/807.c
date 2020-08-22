int maxIncreaseKeepingSkyline(int** grid, int gridSize, int* gridColSize){
    int maxTop=0, maxLeft=0;
    int total=0, value=0;
    int* topBottom=(int*)malloc(sizeof(int)*gridSize+1);
    int* leftRight=(int*)malloc(sizeof(int)*gridSize+1);
    
    //skyline viewed from left or right
    for(int i=0; i<gridSize; i++){
        maxTop=0;
        maxLeft=0;
        for(int j=0; j<gridSize; j++){
            if(grid[i][j]>maxTop)
                maxTop=grid[i][j];
            if(grid[j][i]>maxLeft)
                maxLeft=grid[j][i];
        }
        topBottom[i]=maxLeft;
        leftRight[i]=maxTop;
    } 
        
    for(int i=0; i<gridSize; i++){
        for(int j=0; j<gridSize; j++){
            value=(topBottom[j] <= leftRight[i]) ? topBottom[j] : leftRight[i];
            total += value-grid[i][j];
        }
    }
    return total;
}