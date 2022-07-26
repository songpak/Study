package CodeUp100;

import java.util.Scanner;

//정수 2개 입력 후 합 출력
public class CodeUp038 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        String[] a = sc.nextLine().split(" ");
        int a1 = Integer.parseInt(a[0]);
        int a2 = Integer.parseInt(a[1]);

        System.out.print(a1+a2);
    }
}
