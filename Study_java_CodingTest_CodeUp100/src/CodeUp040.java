import java.util.Scanner;

//정수 1개 입력후 부호 바꿔서 출력
public class CodeUp040 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        int a = sc.nextInt();

        System.out.print(a*-1);
    }
}
