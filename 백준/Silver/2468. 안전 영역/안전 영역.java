import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Iterator;
import java.util.StringTokenizer;


public class Main {
	static int[][] a;
	static int N, ans;
	static boolean[][] v;
	static int [] di = {-1,0,1,0}; // 상우하좌
	static int [] dj = {0,1,0,-1}; //
			
	static void dfs(int i, int j, int C)
	{
		if(a[i][j]> C) {
			v[i][j] = true;}
		else {
			return;
		}
		for(int d = 0; d<4; d++) {
			int ni = i + di[d];
			int nj = j + dj[d];
			if(0<=ni&&ni<N && 0<=nj&& nj < N &&!v[ni][nj]) {
				dfs(ni,nj,C);

			}
		}
	}
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer sw = null;

		N = Integer.parseInt(br.readLine());
		a = new int[N][N];
			
		for (int i = 0; i < N; i++) {
			sw = new StringTokenizer(br.readLine(), " ");
			for (int j = 0; j < N; j++) {
				a[i][j] = Integer.parseInt(sw.nextToken());
				}
			}
		int max = 0;
		for (int i = 0; i < 100; i++) {
			ans = 0;
			v = new boolean[N][N];
			for (int j = 0; j < N; j++) {
				for (int k = 0; k < N; k++) {
					if(!v[j][k] && a[j][k]>i) {
						dfs(j,k,i);
						ans++;
					}
					
				}
			}
			max = Math.max(max,ans);
			}
		
		System.out.println(max);
		
		br.close();

	}
}