import java.io.*;
import java.util.*;

class Solution {
    public int solution(int[] schedules, int[][] timelogs, int startday) {
        int[] least = new int[schedules.length];
        int answer = 0;
        
        
        for(int i = 0; i<schedules.length; i++){
            if(schedules[i]%100 + 10 >= 60){
                least[i] = schedules[i] + 110 - 60;
            }else{
                least[i] = schedules[i] + 10;
            }
        }
        
        for(int i = 0; i<schedules.length; i++){
            int c = 0;
            int day = startday;
            for(int j = 0; j<7; j++){
                if(day == 6 || day == 7){
                    day ++;  
                    continue;
                }
                if(day > 7){
                    day = 1;
                }  
                
                if(least[i]<timelogs[i][j]){
                    break;
                }
                c++;
                day ++;              
 
            }
            if (c==5){
                answer++;
            }
        }
        
        return answer;
    }
}