import java.io.*;
import java.util.*;


public class Main {
	static int[] di = {-1,0,1,0};
	static int[] dj = {0,1,0,-1};
	static int[][] A;
	static int N, L, R;
	static boolean[][] v;
	static boolean[][] move;
	static boolean check;

	static int find (int i , int j){
		ArrayDeque<int[]> dq = new ArrayDeque<>();
		v[i][j] = true;
		dq.offer(new int[]{i,j});
		int sum = 0;
		int C = 0;
		while(!dq.isEmpty()){
			int[] ij = dq.poll();
			i = ij[0];
			j = ij[1];
			sum += A[i][j];
			C++;
			for(int d = 0; d < 4; d++){
				int ni = i+di[d];
				int nj = j+dj[d];
				if(0<=ni&&ni<N && 0<=nj && nj<N && !v[ni][nj]){
					if(Math.abs(A[i][j] - A[ni][nj]) >=L && Math.abs(A[i][j] - A[ni][nj])<=R ){
						check = true;
						move[i][j] = true;
						move[ni][nj] = true;
						v[ni][nj] = true;
						dq.offer(new int[]{ni,nj});
					}
				}
			}
		}
		int avg = sum / C;
		return avg;
	}

	static void move(int avg){
		for(int i = 0; i<N; i++){
			for(int j = 0; j<N; j++){
				if(v[i][j] && move[i][j]){
					A[i][j] = avg;
					move[i][j] = false;
				}
			}
		}
	}


	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;			
		st = new StringTokenizer(br.readLine(), " ");
		N = Integer.parseInt(st.nextToken());
		L = Integer.parseInt(st.nextToken());
		R = Integer.parseInt(st.nextToken());
		A = new int[N][N];

		for(int r =0; r<N; r++) {
			st = new StringTokenizer(br.readLine(), " ");
			for (int c = 0; c< N; c++) {
				A[r][c] = Integer.parseInt(st.nextToken());
			}
		}
		int ans = 0;
		while(true){
			check = false;
			v = new boolean[N][N];
			move = new boolean[N][N];
			for(int i = 0; i<N; i++){
				for(int j = 0; j<N; j++){
					if(!v[i][j]){
						int avg = find(i,j);
						if(move[i][j]) {
							move(avg);
						}
					}
				}
			}
			if(!check){
				break;
			}
			ans ++;
		}
		System.out.println(ans);
		}
}
