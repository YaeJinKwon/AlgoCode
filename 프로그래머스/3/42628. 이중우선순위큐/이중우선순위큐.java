import java.io.*;
import java.util.*;
class Solution {
    public int[] solution(String[] operations) {
        PriorityQueue<Integer> pqMin = new PriorityQueue<>((a,b)->a-b);
        PriorityQueue<Integer> pqMax = new PriorityQueue<>((a,b)->b-a);
        
        for(int i = 0; i<operations.length; i++){
            if(operations[i].charAt(0) == 'I'){
                pqMin.add(Integer.parseInt(operations[i].substring(2)));
                pqMax.add(Integer.parseInt(operations[i].substring(2)));

            }else if(operations[i].equals("D -1")&&!pqMin.isEmpty()){
                int min = pqMin.poll();
                pqMax.remove(min);
            }else if(operations[i].equals("D 1")&&!pqMax.isEmpty()){
                int max = pqMax.poll();
                pqMin.remove(max);
            }
        }
        
        if(!pqMax.isEmpty()){
            int min = pqMin.poll();
            int max = pqMax.poll();
            int[] answer ={max,min};
            return answer;
        }
    
        int[] answer = {0,0};
        return answer;
    }
}