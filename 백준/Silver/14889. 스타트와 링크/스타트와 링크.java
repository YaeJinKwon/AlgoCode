import java.io.*;
import java.util.*;


public class Main {
	static int[] b;
	static boolean[] v;
	static int[][] s;
	static int N;
	static int min = Integer.MAX_VALUE;
	static void comb(int cnt, int start) {
		if(cnt == N/2) {
			min = Math.min(min,check());
			return;
		}
		for(int i = start; i<N; i++) {
			v[i] = true;
			b[cnt] = i;
			comb(cnt+1, i+1);
			v[i]=false;
		}		
	}
	static int check() {
		int start = 0;
		int link = 0;
		
		for (int i = 0; i < N; i++) {
			for (int j = 0; j <N; j++) {
			if(v[i]== true && v[j] == true) {
					start += s[i][j];
			}else if(v[i]== false && v[j] == false) {
					link += s[i][j];
				}
			}
		}
		
		return Math.abs(start - link);
		
	}
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = null;
		
		N = Integer.parseInt(br.readLine());
		s = new int [N][N]; 
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine()," ");
			for (int j = 0; j < N; j++) {
				s[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		b = new int[N/2];
		v = new boolean[N];
		comb(0,0);
		
		System.out.println(min);

	}
}
