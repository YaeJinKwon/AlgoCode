import java.io.*;
import java.util.*;

class Solution {
    int[] di = {-1, 0, 1 ,0};
    int[] dj = {0, 1, 0, -1};
    
    int bfs(int h, int w, String[][] board){
        ArrayDeque<int[]> dq = new ArrayDeque<>();
        boolean[][] v = new boolean[board.length][board[0].length];
        dq.offer(new int[]{h,w});
        v[h][w] = true;
        String color = board[h][w];
        int ans = 0;
        while(!dq.isEmpty()){
            int[] hw = dq.poll();
            h = hw[0];
            w = hw[1];
            for(int k=0; k<4; k++){
                int nh = h+di[k];
                int nw = w+dj[k];
                if(0<=nh && nh<board.length && 0<= nw && nw <board[0].length && board[nh][nw].equals(color) && !v[nh][nw]){
                    v[nh][nw] = true;
                    ans++;
                }
            }
        }
        return ans;
    }
    
    public int solution(String[][] board, int h, int w) {
        int answer = bfs(h, w, board);
        
        return answer;
    }
}