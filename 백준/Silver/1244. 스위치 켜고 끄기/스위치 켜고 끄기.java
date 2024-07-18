import java.io.*;
import java.lang.reflect.Array;
import java.util.*;

public class Main{
	static int[]s;
	public static void main(String[] args)	throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); // 알고리즘 풀때 무조건 이거 써야함
		StringTokenizer sw = null; // 단순하게 자를때


		int N = Integer.parseInt(br.readLine());
		s = new int[N];
			
		sw = new StringTokenizer(br.readLine(), " ");
		for (int i = 0; i < N; i++) {
			s[i] = Integer.parseInt(sw.nextToken());		
		}
			
		int S = Integer.parseInt(br.readLine());
		int[][] bg = new int[S][2];
		for (int i = 0; i < S; i++) {
			sw = new StringTokenizer(br.readLine(), " "); // 
			bg[i][0] = Integer.parseInt(sw.nextToken());
			bg[i][1] = Integer.parseInt(sw.nextToken());
		}
		for (int i = 0; i < S; i++) {
			if(bg[i][0]==1) {
				Boy(N,bg[i][1]);
			}else {
				Girl(N,bg[i][1]);
			}
		}
		StringBuilder sb = new StringBuilder();
		int cnt=0 ;
		for (int i = 0; i < N; i++) {
			sb.append(s[i]+" ");
			if(i == 19+cnt) {
				sb.append("\n");
				cnt = cnt+ 20;
				}
			
			}
		System.out.print(sb);
		br.close();
		
	}

	static void Girl(int size, int i) {
		i = i-1;
		if(s[i] == 1) {
			s[i] = 0;
		}else {
			s[i] = 1;
		}
		int i_left = i-1;
		int i_right = i+1;
		while(i_left >= 0 && i_right < size) {
			if(s[i_left] == s[i_right]) {
				if(s[i_right] == 1) {
					s[i_left] = 0;
					s[i_right] = 0;
				}else {
					s[i_left] = 1;
					s[i_right] = 1;
					}
			}if(s[i_left] != s[i_right]){
					break;
				}
			i_left --;
			i_right ++;
		}
		
	}

	static void Boy(int size, int i) {
		int c = 1;
		int a = i;
		while(i <= size) {
			if(s[i-1] == 1) {
				s[i-1] = 0;
			}else {
				s[i-1] = 1;
			}
			c++;
			i = a * c;
		}
	}

}
