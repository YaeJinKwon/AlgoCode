import java.io.*;
import java.util.*;

class Solution {
    boolean[][] out;
    char[][] map;
    int[] di = {-1,0,1,0};
    int[] dj = {0,1,0,-1};
    
    
    void one(int i, int j, char alp){
        ArrayDeque<int[]> dq = new ArrayDeque<>();
        boolean[][] v = new boolean[map.length][map[0].length];
        dq.offer(new int[]{i,j});
        v[i][j] = true;
        while(!dq.isEmpty()){
            int[] ij = dq.poll();
            i = ij[0];
            j = ij[1];
            if(map[i][j] == alp){
                map[i][j] ='x';
            }
            for(int k =0; k<4; k++){
                int ni = i+di[k];
                int nj = j+dj[k];
                if(0<=ni && ni<map.length && 0<=nj && nj<map[0].length && !v[ni][nj]){
                    if(ni == 0 || nj == 0 || ni == map.length -1 || nj == map[0].length -1 || out[i][j]){
                        v[ni][nj] = true;
                        dq.offer(new int[]{ni,nj});  
                    }
                }

            }
        }
        
    }
    void checkOut(){
        for(int i =0; i<map.length; i++){
            for (int k = 0; k<map[0].length; k++){
                if(map[i][k] == 'x'){
                    out[i][k] = true;
                }
            }
        }
    }

    void two(int i, int j, char alp){
        ArrayDeque<int[]> dq = new ArrayDeque<>();
        boolean[][] v = new boolean[map.length][map[0].length];
        dq.offer(new int[]{i,j});
        v[i][j] = true;
        while(!dq.isEmpty()){
            int[] ij = dq.poll();
            i = ij[0];
            j = ij[1];
            if(map[i][j] == alp){
                map[i][j] ='x';
            }
            for(int k =0; k<4; k++){
                int ni = i+di[k];
                int nj = j+dj[k];
                if(0<=ni && ni<map.length && 0<=nj && nj<map[0].length && !v[ni][nj]){
                    v[ni][nj] = true;
                    dq.offer(new int[]{ni,nj});  
                }

            }
        }
        
    }
    

    public int solution(String[] storage, String[] requests) {
        int answer = 0;
        map = new char[storage.length][storage[0].length()];
        out = new boolean[storage.length][storage[0].length()];
        
        
        for(int i =0; i<storage.length; i++){
            for (int k = 0; k<storage[0].length(); k++){
                map[i][k] = storage[i].charAt(k);
            }
        }
        
        
        for(int i =0; i<requests.length; i++){
            if(requests[i].length() == 2){
                two(0,0,requests[i].charAt(0));
                checkOut();
            }else{
                one(0,0,requests[i].charAt(0));
                checkOut();
            }
        }

        for(int i =0; i<map.length; i++){
            for (int k = 0; k<map[0].length; k++){
                if(map[i][k] != 'x'){
                    answer++;
                }
            }
        }
        
        
        
        return answer;
    }
}