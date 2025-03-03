import java.util.*;

class Solution {
    int[][] linked;
    boolean[] v;
    int count;
    
    public void dfs(int i, int n){
        v[i] = true;
        count++;
        for(int j=1; j<=n; j++){
            if(!v[j] && linked[i][j]==1){
                dfs(j,n);
            }
        }
    }
    public int solution(int n, int[][] wires) {
        int answer = -1;
        
        linked = new int[n+1][n+1];
        
        for(int i = 0; i<n-1; i++){
            linked[wires[i][0]][wires[i][1]] = 1; 
            linked[wires[i][1]][wires[i][0]] = 1; 
        }    
        
        int min = 1000;
        for(int i = 0; i<n-1; i++){
            v = new boolean[n+1];;         
            linked[wires[i][0]][wires[i][1]] = 0; 
            linked[wires[i][1]][wires[i][0]] = 0; 
            
            count = 0;
            dfs(wires[i][0], n);
            int a = count;
            
            count = 0;
            dfs(wires[i][1], n);
            int b = count;
            
            linked[wires[i][0]][wires[i][1]] = 1; 
            linked[wires[i][1]][wires[i][0]] = 1; 
            
            int cal = Math.abs(a - b);
            
            min = Math.min(min,cal);
        }
        answer = min;

        return answer;
    }
}