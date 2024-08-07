
import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.util.StringTokenizer;



public class Main {

		
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer st =  new StringTokenizer(br.readLine(), " ");
		int N = Integer.parseInt(st.nextToken());
		
		st =  new StringTokenizer(br.readLine(), " "); // 거리
		int[] d = new int[N-1];
		for (int i = 0; i < N-1; i++) {
			d[i] = Integer.parseInt(st.nextToken());
		}
		
		st =  new StringTokenizer(br.readLine(), " ");// 가역
		int[] w = new int[N];
		for (int i = 0; i < N; i++) {
			w[i] = Integer.parseInt(st.nextToken());
		}
		
		
		//구현
		int C = 0;
		for (int i = 0; i < N-1; i++) {
			int j = i+1;
			while(w[i]<w[j]) {
				if(j==N-1) {
					break;
				}
				C = C + w[j]*d[j];
				j++;
			}
			if(w[i]>=w[i+1]) {
				C = C + w[i]*d[i];
			}

		}
		System.out.println(C);
		br.close();
	}}