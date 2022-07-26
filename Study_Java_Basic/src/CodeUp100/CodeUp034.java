package CodeUp100;

import java.util.Scanner;

//8진수를 10진수로 출력
public class CodeUp034 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        String a  = sc.next();
        int b = Integer.parseInt(a,8);

        System.out.print(b);
    }
}
