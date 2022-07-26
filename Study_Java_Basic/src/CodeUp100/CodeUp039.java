package CodeUp100;

import java.util.Scanner;

//정수 2개 입력받아 함 출력(Long Type)
public class CodeUp039 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        String[] arr = sc.nextLine().split(" ");
        long a = Long.parseLong(arr[0]);
        long b = Long.parseLong(arr[1]);

        System.out.print(a+b);
    }
}
