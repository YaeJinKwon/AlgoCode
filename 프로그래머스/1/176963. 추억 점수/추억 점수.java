import java.io.*;
import java.util.*;

class Solution {
    public int[] solution(String[] name, int[] yearning, String[][] photo) {
        HashMap<String, Integer> map = new HashMap<>();
        
        for(int i =0; i<name.length; i++){
            map.put(name[i], yearning[i]);
        }
        
        int[] answer = new int[photo.length];
        
        for(int i =0; i<photo.length; i++){
            int a = 0;
            for(int k =0; k<photo[i].length; k++){
                if(map.containsKey(photo[i][k])){
                a += map.get(photo[i][k]);}
            }
            answer[i] = a;
        }
        
        

        return answer;
    }
}