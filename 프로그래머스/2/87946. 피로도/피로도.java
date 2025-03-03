import java.util.*;
class Solution {
    int N;
    boolean[] v;
    int[] t;
    int max;
    public int calculate(int k, int[][] dungeons){
        int result = 0;
        for(int i =0; i<N; i++){
            if(k<dungeons[t[i]][0]){
                break;
            }
            k = k-dungeons[t[i]][1];
            result++;
        }
        return result;
        
    }
    
    public void turn(int i, int[][] dungeons, int k){
        if(i == N){
            int result = calculate(k, dungeons);
            max = Math.max(result, max);
            return;
        }
        for(int j = 0; j<N; j++){
            if(v[j]) continue;
            v[j] = true;
            t[i] = j;
            turn(i+1, dungeons, k);
            v[j] = false;
            
        }
        
    }
    public int solution(int k, int[][] dungeons) {
        N = dungeons.length;
        v = new boolean[N];
        t = new int[N];
        max = 0;
        turn(0, dungeons, k);
        return max;
    }
}