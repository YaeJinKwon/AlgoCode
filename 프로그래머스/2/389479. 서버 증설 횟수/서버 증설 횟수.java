import java.io.*;
import java.util.*;


class Solution {
    
        
    public int solution(int[] players, int m, int k) {
        int answer = 0;
        int[] sub = new int[players.length];
        
        for(int i =0; i<players.length; i++){
            if(players[i] >= m && players[i] >= sub[i] * m){
                while((sub[i] +1) * m <= players[i]){
                    answer++;
                    for(int l = 0; l<k; l++){
                        if(i+l>= players.length){
                            break;
                        }
                        sub[i+l] += 1;
                    }
                }
            }
            
            
        }
    
        return answer;
    }
}