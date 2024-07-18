import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args)	throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); // 알고리즘 풀때 무조건 이거 써야함
		StringTokenizer st = null; // 단순하게 자를때

		
			int N = Integer.parseInt(br.readLine());
			int[][] a = new int[N][2];

			for (int i = 0; i < N; i++) {
				st = new StringTokenizer(br.readLine(), " "); // 
				a[i][0] = Integer.parseInt(st.nextToken());
				a[i][1] = Integer.parseInt(st.nextToken());
			}
			
			Arrays.sort(a, (o1, o2) -> o1[1] == o2[1] ? o1[0] - o2[0] : o1[1] - o2[1]);
			
			int ans = 0;
			int cnt = 0;
			for (int i = 0; i <N-1; i++) {
				if(a[i+1][0]>=a[cnt][1]) {
					cnt = i+1;
					ans++;
				}
			}
			
			System.out.println(ans+1);
			
		
		br.close();
		
	}

}
