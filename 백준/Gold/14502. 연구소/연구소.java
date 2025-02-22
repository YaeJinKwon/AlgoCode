import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Iterator;
import java.util.LinkedList;
import java.util.List;
import java.util.StringTokenizer;


public class Main {
	static int N, M;
	static int[][] map;
	static int[] di = {-1, 0 , 1 ,0};
	static int[] dj = {0, 1, 0, -1};
	static boolean[][] visitWall;
	static boolean[][] visit;
	static ArrayList<int[]> virus;
	static int min;

	static int spread(){
		visit = new boolean[N][M];
		int count = 0;
		int R = virus.size();

		for(int n = 0; n <R; n++) {
			int[] ij = virus.get(n);
			int i = ij[0];
			int j = ij[1];
			ArrayDeque<int[]> dq = new ArrayDeque<>();
			visit[i][j] = true;
			dq.offer(new int[]{i, j});
			while (!dq.isEmpty()) {
				ij = dq.poll();
				i = ij[0];
				j = ij[1];
				for (int k = 0; k < 4; k++) {
					int ni = i + di[k];
					int nj = j + dj[k];
					if (0 <= ni && ni < N && 0 <= nj && nj < M && !visit[ni][nj] && map[ni][nj] == 0) {
						visit[ni][nj] = true;
						count++;
						dq.offer(new int[]{ni, nj});
					}
				}
			}
		}
		return count;
	}

	static void makeWall(int countWall){
		if(countWall == 3){
			int cnt = spread();
			min = Math.min(cnt, min);
			return;
		}
		for(int i = 0; i<N; i++){
			for(int j =0; j<M; j++) {
				if(map[i][j] != 0){
					continue;
				}
				visitWall[i][j] = true;
				map[i][j] = 1;
				makeWall(countWall + 1);
				map[i][j] = 0;
				visitWall[i][j] = false;
			}
		}
	}



	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		map = new int[N][M];
		visitWall = new boolean[N][M];
		virus = new ArrayList<>();
		int cntZero = 0;

		for(int i = 0; i<N; i++){
			st = new StringTokenizer(br.readLine()," ");
			for(int j = 0; j<M; j++){
				map[i][j] = Integer.parseInt(st.nextToken());
				if(map[i][j] == 0){
					cntZero++;
				}else if (map[i][j] == 2 ){
					virus.add(new int[]{i, j});
				}
				// 0은 빈칸, 1은 벽, 2는 바이러스
			}
		}
		min = Integer.MAX_VALUE;
		makeWall(0);
		System.out.println(cntZero - 3 - min);

		
	}
	
}

