package CodeUp100;

import java.util.Scanner;

public class CodeUp042__ {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        String[] arr = sc.nextLine().split(" ");
        int a = Integer.parseInt(arr[0]);
        int b = Integer.parseInt(arr[1]);

        System.out.println((int)(a/b));
    }
}
