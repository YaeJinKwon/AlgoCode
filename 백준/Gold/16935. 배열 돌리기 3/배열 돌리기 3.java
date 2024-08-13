import java.io.*;
import java.lang.reflect.Array;
import java.util.*;

public class Main {
	static int[][] arr;
	static int[][] ans;
	static int N , M;

	static void first (){
		int a = arr.length;
		int b = arr[0].length;
		int[][] temp = new int [a][b];
		for(int i=0;i<a;i++){
			temp[i] = arr[a-i-1];
		}
		arr = temp;
	}
	static void second (){
		int a = arr.length;
		int b = arr[0].length;
		int[][] temp = new int [a][b];
		for(int i=0;i<a;i++){
			for(int j=0;j<b;j++){
				temp[i][j] = arr[i][b-j-1];
			}
		}
		arr = temp;
	}
	static void third (){
		if(arr.length == N){
		int [][] temp = new int [M][N];
		for(int i=0;i<M;i++){
			for(int j=0;j<N;j++){
				temp[i][j] = arr[N-j-1][i];
			}
		}
		arr = temp;}
		else{
			int [][] temp = new int [N][M];
			for(int i=0;i<N;i++){
				for(int j=0;j<M;j++){
					temp[i][j] = arr[M-j-1][i];
				}
			}
			arr = temp;
		}
	}

	static void four (){
		if(arr.length == N){
		int [][] temp = new int [M][N];
		for(int i=0;i<M;i++){
			for(int j=0;j<N;j++){
				temp[i][j] = arr[j][M-i-1];
			}
		}
		arr = temp;}

		else {
				int [][] temp = new int [N][M];
				for(int i=0;i<N;i++){
					for(int j=0;j<M;j++){
						temp[i][j] = arr[j][N-i-1];
					}
				}
				arr = temp;
			}
	}
	static void five (){
		int a = arr.length;
		int b = arr[0].length;
		int[][] temp = new int [a][b];
		for(int i=0;i<a/2;i++){
			for(int j=0;j<b/2;j++){
				temp[i][j] = arr[a/2 + i][j];
				temp[i][b/2 + j ] = arr[i][j];
				temp[a/2 + i][j] = arr[a/2 + i][b/2 + j];
				temp[a/2 + i][b/2 + j] = arr[i][b/2 + j];
			}
		}
		arr = temp;
	}
	static void six (){
		int a = arr.length;
		int b = arr[0].length;
		int[][] temp = new int [a][b];
		for(int i=0;i<a/2;i++){
			for(int j=0;j<b/2;j++){
				temp[i][j] = arr[i][b/2+j];
				temp[i][b/2 + j ] =  arr[a/2 + i][b/2 + j];
				temp[a/2 + i][j] =arr[i][j];
				temp[a/2 + i][b/2 + j] = arr[a/2 + i][j];
			}
		}
		arr = temp;
	}
	public static void main(String[] args)	throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); // 알고리즘 풀때 무조건 이거 써야함
		StringTokenizer st = null;

		st = new StringTokenizer(br.readLine(), " ");
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		int R = Integer.parseInt(st.nextToken());

		arr = new int[N][M];

		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine(), " ");
			for (int j = 0; j < M; j++) {
				arr[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		st = new StringTokenizer(br.readLine(), " ");
		for (int i = 0; i < R; i++) {
			int a = Integer.parseInt(st.nextToken());
			if(a == 1){
				first();
			}
			else if(a == 2){
				second();
			}
			else if(a == 3){
				third();
			}
			else if(a == 4){
				four();
			}
			else if(a == 5){
				five();
			}
			else if(a == 6){
				six();
			}
		}
		StringBuilder sb = new StringBuilder();
        for (int[] i : arr) {
            for (int anInt : i) {
                sb.append(anInt).append(" ");
            }
            sb.append("\n");
        }
		System.out.println(sb.toString());

	}
}
