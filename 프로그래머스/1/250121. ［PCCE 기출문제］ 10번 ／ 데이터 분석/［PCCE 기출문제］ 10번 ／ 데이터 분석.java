import java.io.*;
import java.util.*;


class Solution {
    
    int check (String string){
        if(string.equals("code")){
            return 0;
            
        }else if(string.equals("date")){
            return 1;
            
        }else if(string.equals("maximum")){
            return 2;
            
        }else{
            return 3;   
        }    
        
    }
    
    public int[][] solution(int[][] data, String ext, int val_ext, String sort_by) {
        ArrayList<int[]> ans = new ArrayList<>();
        
        int extN = check(ext);
        for(int i = 0; i<data.length; i++){
            if(data[i][extN] < val_ext){
                ans.add(data[i]);
            }
        }        
        
        int[][] answer = new int[ans.size()][4];
        for(int i = 0; i<ans.size(); i++){
            answer[i] = ans.get(i);
        }
        int sort = check(sort_by);
        Arrays.sort(answer, (a, b) -> a[sort] - b[sort]);
        
        return answer;
    }
}