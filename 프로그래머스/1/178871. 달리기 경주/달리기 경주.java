import java.io.*;
import java.util.*;


class Solution {
    public String[] solution(String[] players, String[] callings) {

        HashMap<String, Integer> st = new HashMap<>();
        for(int i=0; i<players.length; i++){
         st.put(players[i], i);
        }

        for(int i = 0; i<callings.length; i++){
            int a = st.get(callings[i]);

            String temp = players[a-1];
            players[a-1] =  players[a];
            players[a] = temp; 

            st.put(players[a], a);
            st.put(players[a-1], a-1);
        }
        
        return players;
    }
}