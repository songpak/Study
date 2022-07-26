package CodeUp100;

import java.util.Scanner;

public class CodeUp025 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        char[] a = sc.nextLine().toCharArray();

        for (int i=0; i<a.length; i++){
            System.out.print("["+a[i]);
            for (int j=0; j<a.length-i-1; j++){
                System.out.print("0");
            }
            System.out.println("]");
        }
    }
}
