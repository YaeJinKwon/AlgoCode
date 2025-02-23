import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
	static int N, M, min;
	static boolean[] visit ;
	static ArrayList<int[]> house;
	static ArrayList<int[]> chicken;
	static int[][] maxChicken;

	static int find(){
		int sum = 0;

		for(int i =0; i<house.size(); i++) {
			int[] ij = house.get(i);
			int mindis = Integer.MAX_VALUE;
			for(int j = 0; j<M; j++){
				int dis = Math.abs(ij[0] - maxChicken[j][0]) + Math.abs(ij[1] - maxChicken[j][1]);
				mindis = Math.min(dis,mindis);
			}
			sum += mindis;
		}
		return sum;
	}

	static void maxchic(int cnt, int size){
		if(cnt == M){
			int sum = find();
			min = Math.min(sum, min);
			return;
		}
		for(int k = size; k<chicken.size(); k++){
			if(visit[k]){
				continue;
			}
			visit[k] = true;
			maxChicken[cnt][0] = chicken.get(k)[0];
			maxChicken[cnt][1] = chicken.get(k)[1];
			maxchic(cnt +1, size+1);
			visit[k] = false;

		}
	}

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = null;
		st = new StringTokenizer(br.readLine(), " ");
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		house = new ArrayList<>();
		chicken = new ArrayList<>();
		min = Integer.MAX_VALUE;


		for(int i =0; i<N; i++){
			st = new StringTokenizer(br.readLine(), " ");
			for(int j = 0; j<N; j++){
				 int a  = Integer.parseInt(st.nextToken());
				 if(a == 1){
					 house.add(new int[] {i,j});
				 }
				 else if (a == 2){
					 chicken.add(new int[]{i,j});
				 }
			}
		}

		visit = new boolean[chicken.size()];
		maxChicken = new int[M][2];
		maxchic(0,0);

		System.out.println(min);
	}
}
