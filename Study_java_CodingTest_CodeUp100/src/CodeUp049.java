import java.util.Scanner;

//두 정수 입력받아 비교
public class CodeUp049 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        String[] arr = sc.nextLine().split(" ");

        int a = Integer.parseInt(arr[0]);
        int b = Integer.parseInt(arr[1]);

        System.out.println(a>b?1:0);
    }
}
