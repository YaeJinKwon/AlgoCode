import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Collections;
import java.util.Iterator;
import java.util.StringTokenizer;


public class Main {
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer sw = null;
	
		int N = Integer.parseInt(br.readLine());
		int[][] aa = new int[N][2];
		for (int i = 0; i < N; i++) {
			sw = new StringTokenizer(br.readLine(), " ");
			for (int j = 0; j < 2; j++) {
				aa[i][j] = Integer.parseInt(sw.nextToken());
				}
			}
		
		Arrays.sort(aa,(e1,e2) -> {
			if(e1[0] == e2[0]) {
				return e1[1]-e2[1];
			}else {
				return e1[0] - e2[0];
			}
		});
		
		
		
		for (int i = 0; i < N; i++) {
			System.out.println(aa[i][0] + " " + aa[i][1]);
		}
		br.close();

	}
}
