
import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;



public class Main {
		static int[][] a;
		static int N, ans,cnt;
		static boolean[][] v;
		static int [] di = {-1,0,1,0}; // 상우하좌
		static int [] dj = {0,1,0,-1}; //
				
		static void dfs(int i, int j)
		{
			if(a[i][j]==1) {
				v[i][j] = true;
				cnt ++;}
			else {
				return;
			}
			for(int d = 0; d<4; d++) {
				int ni = i + di[d];
				int nj = j + dj[d];
				if(0<=ni&&ni<N && 0<=nj&& nj < N &&!v[ni][nj]) {

					dfs(ni,nj);

				}
			}
		}
		
		public static void main(String[] args) throws Exception {
			BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

			N = Integer.parseInt(br.readLine());
			a = new int[N][N];
				
			for (int i = 0; i < N; i++) {
				String st = br.readLine();
				for (int j = 0; j < N; j++) {
					a[i][j] = st.charAt(j) -'0';
					}
				}

			ArrayList<Integer> count = new ArrayList<Integer>();
			v = new boolean[N][N];
			for (int j = 0; j < N; j++) {
				for (int k = 0; k < N; k++) {
					cnt = 0;
						if(!v[j][k] && a[j][k]==1) {
							dfs(j,k);
							ans++;
							count.add(cnt);
						}
						
						
					}
				}
			Collections.sort(count);
	
			StringBuilder sb = new StringBuilder();
			sb.append(ans).append("\n");
			for (int i = 0; i < ans; i++) {
				sb.append(count.get(i)).append("\n");
			}
			System.out.println(sb);
			br.close();
		}
	}
