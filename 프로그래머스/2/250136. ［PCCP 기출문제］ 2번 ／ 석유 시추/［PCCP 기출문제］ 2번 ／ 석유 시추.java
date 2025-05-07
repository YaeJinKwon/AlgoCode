import java.io.*;
import java.util.*;

class Solution {
    int[] di = {0, 1, 0, -1};
    int[] dj = {-1, 0, 1, 0};
    int N, M;
    int[] oil;
    boolean[][] v;
        
    void bfs(int i, int j, int[][] land){
        ArrayDeque<int[]> dq = new ArrayDeque<>();
        Set<Integer> cols = new HashSet<>();
        dq.add(new int[]{i , j});
        v[i][j] = true;
        int C = 0;
        while(!dq.isEmpty()){
            int[] ij = dq.poll();
            i = ij[0];
            j = ij[1];
            cols.add(j);
            C++;
            for(int k = 0; k<4; k++){
                int ni = i + di[k];
                int nj = j + dj[k];
                if(0<=ni && ni <N && 0<=nj && nj< M && !v[ni][nj] && land[ni][nj] == 1){
                    v[ni][nj] = true;
                    dq.offer(new int[]{ni,nj});
                }
            }
        }
        
        for(int col : cols){
            oil[col] += C;
        }
        
        
        
    }
    
    public int solution(int[][] land) {
        N = land.length;
        M = land[0].length;
        int answer = 0;
        oil = new int[M];
        v = new boolean[N][M];
        
        
        for(int m = 0; m<M; m++){
            for(int n = 0; n<N; n++){
                if(!v[n][m]&&land[n][m]==1){
                bfs(n,m,land);
                }
            }
        }
        
        for(int max : oil){
            answer = Math.max(max, answer);
        }

        return answer;
    }
}