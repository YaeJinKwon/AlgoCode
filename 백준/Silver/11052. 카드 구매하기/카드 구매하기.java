import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;


public class Main {


	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = null;
		

		int N = Integer.parseInt(br.readLine());
		int[] card = new int [N+1];
		st = new StringTokenizer(br.readLine());
		for (int i = 1; i <= N; i++) {
			card[i] = Integer.parseInt(st.nextToken());
		}

		int[] dp = new int[N+1];
		
		for (int i = 1; i < N+1 ; i++) {
			for(int h= 1; h<= i; h++)  {
				dp[i]= Math.max(dp[i], card[h] + dp[i-h]);
			}
		}
	
		System.out.println(dp[N]);
		
	}
	
}
