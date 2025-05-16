import java.io.*;
import java.util.*;

class Solution {
    public int solution(int[][] targets) {
        if(targets.length == 1) {
            return 1;
        }
        
        PriorityQueue<int[]> dq = new PriorityQueue<>((a,b)-> a[1]-b[1]);
        
        for(int i =0 ; i< targets.length; i++){
            dq.offer(targets[i]);
        }
        
        int[] start = dq.poll();
        int[] end = dq.poll();
        int answer = 0;
        
        while(!dq.isEmpty()){
           if(start[1] <= end[0]){
               answer++;
               start = Arrays.copyOf(end,2);
           }
            end = dq.poll();
       }
        
        if(start[1] <= end[0]){
               answer++;
           }
        
        return answer + 1;
    }
}
