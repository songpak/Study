import java.util.Scanner;

public class CodeUp027 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        String[] a = sc.nextLine().split("\\.");

        int dd = Integer.parseInt(a[2]);
        int mm = Integer.parseInt(a[1]);
        int yyyy = Integer.parseInt(a[0]);

        int[] b = new int[a.length];
        System.out.printf("%02d-%02d-%04d",dd,mm,yyyy);
    }
}
