import java.io.*;
import java.util.*;


class Solution {
    public int[] solution(int N, int[] stages) {
        
        int P = stages.length;
        int[] c = new int[N+2];
        
        
        for (int i = 0; i<stages.length; i++){
            c[stages[i]] +=1;
        }
        
        HashMap<Integer, Double >fail = new HashMap<>();
        for(int i = 1; i <= N; i++){
            if(c[i] == 0){
               fail.put(i, 0.);
            }
            else{
            fail.put(i, (double) c[i]/P);
            P = P-c[i];
            }

        }
        

        return fail.entrySet().stream().sorted((o1, o2) ->
                                               o1.getValue().equals(o2.getValue())? Integer.compare(o1.getKey(), o2.getKey()) : Double.compare(o2.getValue(), o1.getValue())).mapToInt(HashMap.Entry::getKey).toArray();
    }
}