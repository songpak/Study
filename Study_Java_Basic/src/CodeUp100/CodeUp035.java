package CodeUp100;

import java.util.Scanner;

//16진수를 8진수로
public class CodeUp035 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        String a = sc.nextLine();

        int b = Integer.parseInt(a, 16);

        System.out.printf("%o",b);
    }
}
