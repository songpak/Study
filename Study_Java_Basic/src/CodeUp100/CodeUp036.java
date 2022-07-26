package CodeUp100;

import java.util.Scanner;

//영문자 1개를 10진수로 출력
public class CodeUp036 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        char a = sc.next().charAt(0);

        System.out.print((int)a);
    }
}
