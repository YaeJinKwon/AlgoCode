import java.io.*;
import java.util.*;

class Solution {
    
    public int solution(int[] mats, String[][] park) {
        int answer = -1;

        for(int i = 0; i<park.length; i++){
            for(int j = 0; j<park[0].length; j++){
                if(!park[i][j].equals("-1")){
                    continue;
                }
                for(int l =0; l<mats.length; l++){
                    int c = mats[l];
                    boolean v = true;
                    loop1: 
                    for(int h = 0; h<c; h++){
                        for(int m =0; m<c; m++){
                            if(i+h>=park.length || j+m>=park[0].length){
                                v = false;
                                break loop1;
                            }
                            if(!park[i+h][j+m].equals("-1")){
                                v = false;
                                break loop1;
                            }
                        }
                    }
                    if(v){
                        answer = Math.max(c, answer);
                    }
                 
                }          
                       
                
            }
        }
        return answer;
    }
}