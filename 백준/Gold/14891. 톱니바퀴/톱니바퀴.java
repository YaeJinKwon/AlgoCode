import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	static int[] turn;
	static int[][] tb = new int[4][8];

	static void find(int num){
		int dir = turn[num];
		for(int j = num; j<=2; j++){
			if(tb[j][2] != tb[j+1][6]){
				dir *= -1;
				turn[j+1] = dir;
			}else{
				break;
			}
		}
		dir = turn[num];
		for(int j = num; j>=1; j--){
			if(tb[j][6] != tb[j-1][2]){
				dir *= -1;
				turn[j-1] = dir;
			}else{
				break;
			}
		}
	}
	static void clock(int n){
		int temp = tb[n][7];
		for(int i = 7; i>0; i--){
			tb[n][i] = tb[n][i-1];
		}
		tb[n][0] = temp;
	}
	static void anticlock(int n){
		int temp = tb[n][0];
		for(int i = 0; i<7; i++){
			tb[n][i] = tb[n][i+1];
		}
		tb[n][7] = temp;
	}

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = null;

		for(int i = 0; i<4; i++){
			 String s = br.readLine();
			for(int j =0; j<8; j++){
				tb[i][j] = s.charAt(j) -'0';
			}
		}
		int K  = Integer.parseInt(br.readLine());


		for(int i =0; i < K; i++){
			st = new StringTokenizer(br.readLine(), " ");
			int num = Integer.parseInt(st.nextToken()) -1;
			int dir = Integer.parseInt(st.nextToken());
			turn = new int[4];
			turn [num] = dir;
			find(num);
			for(int j = 0; j<4; j++){
				if(turn[j] == 1){
					clock(j);
				}
				else if(turn[j] == -1){
					anticlock(j);
				}
			}
		}
		int ans = 0;
		for(int i = 0; i<4; i++){
			if(tb[i][0] == 1){
				ans += Math.pow(2,i);
			}
		}
		System.out.println(ans);

		}
	}
