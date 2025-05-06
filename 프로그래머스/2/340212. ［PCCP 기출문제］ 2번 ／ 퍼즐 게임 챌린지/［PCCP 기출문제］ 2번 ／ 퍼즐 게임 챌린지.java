import java.io.*;
import java.util.*;

class Solution {
    public int solution(int[] diffs, int[] times, long limit) {
        long time = limit+1;
        int max = 100000;
        int min = 1;
        
        int level = 0;
        while(max >= min){
            level = (max + min) / 2;
            time = 0;
            for(int i = 0; i<diffs.length; i++){
                int l = diffs[i] - level;
                if(l <= 0){
                    time += times[i];
                }else{
                    time += (times[i-1] + times[i]) *l + times[i];
                }
            }
            
            if (time > limit){
                min = level + 1;
            }else{
                max = level - 1 ;
            }

        }

        int answer = min;
        return answer;
    }
}