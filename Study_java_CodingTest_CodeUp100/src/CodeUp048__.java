import java.util.Scanner;

//a를 2의 n승만큼 곱한값 출력 (비트시프트 연산)
public class CodeUp048__ {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        String[] arr = sc.nextLine().split(" ");
        int a = Integer.parseInt(arr[0]);
        int b = Integer.parseInt(arr[1]);

        System.out.println(a << b);
    }
}
