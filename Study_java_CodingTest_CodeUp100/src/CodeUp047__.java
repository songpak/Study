import java.util.Scanner;

//비트시프트 연산 2배 곱하기
public class CodeUp047__ {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        int a  =sc.nextInt();

        System.out.println(a << 1);

        //a >> 1 : a를 2로 나눈 값
        //a << 2 : a를 4배한 값
        //a >> 2 : a를 4로 나눈 값 (반의 반)
    }
}
