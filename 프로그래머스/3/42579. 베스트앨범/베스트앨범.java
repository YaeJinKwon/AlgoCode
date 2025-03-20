import java.io.*;
import java.util.*;

class Solution {
    public int[] solution(String[] genres, int[] plays) {
        HashMap<Integer, String> hashGen = new HashMap();
        HashMap<String, Integer> hashGenSum= new HashMap();
        HashMap<Integer, Integer> hashPlay = new HashMap();
        
        for(int i = 0; i<plays.length; i++){
            hashPlay.put(i,plays[i]);
            hashGen.put(i,genres[i]);
        }
        
        for(int i = 0; i<genres.length; i++){
            if(hashGenSum.containsKey(genres[i])){
            hashGenSum.put(genres[i], plays[i]+hashGenSum.get(genres[i]));
            }
        
            else{
               hashGenSum.put(genres[i], plays[i]);
            }
        }
        List<Integer> sortGen = new ArrayList<>(hashGenSum.values());
        sortGen.sort((a,b)->b-a);
        
        List<Integer> ans = new ArrayList<>();
        
        for(int i = 0; i<sortGen.size(); i++){
            for(String key : hashGenSum.keySet()){
                if(sortGen.get(i) == hashGenSum.get(key)){
                    List<Integer> sortNum = new ArrayList<>();
                    for(Integer num : hashGen.keySet()){
                        if(hashGen.get(num).equals(key)){
                            sortNum.add(plays[num]);
                        }
                    }
                    sortNum.sort((a,b)->b-a);
                    int C = 0;
                    for(int k : sortNum){
                        for(int j = 0; j<plays.length; j++){
                            if(k == plays[j]){
                                ans.add(j);
                                C++;
                            }
                        }
                        if(C==2){
                            break;
                        }
                        
               
                    }       
                }       
                        
            }                
        }
       
        int[] answer = new int[ans.size()];
        for(int i = 0; i<ans.size(); i++){
            answer[i] = ans.get(i);
        }
        return answer;
    }
}