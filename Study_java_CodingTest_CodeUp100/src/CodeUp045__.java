import java.util.Scanner;

public class CodeUp045__ {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        String[] arr = sc.nextLine().split(" ");

        int a = Integer.parseInt(arr[0]);
        int b = Integer.parseInt(arr[1]);

        System.out.println(a+b);
        System.out.println(Math.abs(a-b));
        System.out.println(a*b);
        System.out.println(a>b?(int)a/b:(int)b/a);
        System.out.println(a>b?a%b:b%a);
        System.out.printf("%.2f",a>b?(float)a/b:(float)b/a);
    }
}
