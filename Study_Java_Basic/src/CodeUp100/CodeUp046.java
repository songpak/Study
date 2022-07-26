package CodeUp100;

import java.util.Scanner;

public class CodeUp046 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        String[] arr = sc.nextLine().split(" ");

        int a = Integer.parseInt(arr[0]);
        int b = Integer.parseInt(arr[1]);
        int c = Integer.parseInt(arr[2]);

        System.out.println(a+b+c);
        System.out.println((float) (a+b+c)/3);
    }
}
