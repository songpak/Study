
import java.util.Scanner;

public class CodeUp019 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        String[] a = sc.nextLine().split("\\.");

       int[] arr = new int[3];

       for (int i=0; i<arr.length; i++){
           arr[i] = Integer.parseInt(a[i]);
       }

       System.out.printf("%04d.%02d.%02d",arr[0],arr[1],arr[2]);
    }
}
