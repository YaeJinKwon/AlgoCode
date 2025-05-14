import java.io.*;
import java.util.*;

class Solution {
    public int solution(String[] friends, String[] gifts) {
        int answer = 0;
        int[][] gift = new int[friends.length][friends.length];
        HashMap<String, Integer> num = new HashMap<>();
        
        for(int i = 0; i<friends.length; i++){
            num.put(friends[i], i);
        }
        
        for(int i = 0; i<gifts.length; i++){
            String[] give = gifts[i].split(" ");
            gift[num.get(give[0])][num.get(give[1])]++;       
        }
        
        int[] giftNum = new int[friends.length];
        
        for(int i = 0; i<gift.length; i++){
            int m =0;
            int a =0;
            for(int j=0; j<gift.length; j++){
                a += gift[i][j];
                m += gift[j][i];
            }
            giftNum[i] = a-m;
        }
        

        
        for(int i=0; i<gift.length; i++){
            int c = 0;
            for(int j=0; j<gift.length; j++){
                if(gift[i][j] > gift[j][i]){
                    c++;
                }else if(gift[i][j] == gift[j][i] || gift[i][j] == 0 && gift[j][i] == 0){
                    if(giftNum[i]> giftNum[j]){
                        c++;
                    }
                }
            }
            answer = Math.max(c,answer);
        }
        
        
        
        
        
        return answer;
    }
}