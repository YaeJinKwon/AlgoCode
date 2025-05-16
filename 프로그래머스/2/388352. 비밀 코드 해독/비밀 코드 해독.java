import java.io.*;
import java.util.*;

class Solution {
    int[] b = new int[5];
    int answer = 0;
    
    void make (int n, int c, int start, int[][] q, int[] ans){
        if(c == 5){
            check(q, b, ans);
            return;
        }
        for(int i = start; i<= n; i++){
            b[c] = i;
            make(n, c+1 , i + 1, q, ans);   
        }
          
    }
    
    void check(int[][] q, int[] b, int[] ans){
        int c = 0;
        for(int i =0; i<q.length; i++){
            int cnt = 0;
            for(int k =0; k<5; k++){
                 for(int j =0; j<5; j++){
                     if(q[i][k] == b[j]){
                          cnt++;
                     }
                 }
            }
            if(cnt != ans[i]){
                break;
            }
            c++;
        }
        if(c==ans.length){
            answer++;
        }
        
    }
    public int solution(int n, int[][] q, int[] ans) {


        make(n, 0, 1, q, ans);

        
        
        return answer;
    }
}