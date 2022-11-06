import java.util.Arrays;

public class Day1 {
    public static void main(String[] args) {

        // 짝수와 홀수
        Solution1 s1 = new Solution1();
        int[] input1 = {3, 4};
        String[] result1 = {"Odd", "Even"};
        System.out.println("짝수와 홀수");
        for (int i = 0; i < input1.length; i++) {
            System.out.printf("example %d", i+1);
            System.out.println("=".repeat(20));
            System.out.println("input: " + input1[i]);
            System.out.println("correct: " + result1[i]);
            System.out.println("my answer: " + s1.solution(input1[i]));
        }
        System.out.println();

        // 가운데 글자 가져오기
        Solution2 s2 = new Solution2();
        String[] input2 = {"abcde", "qwer"};
        String[] result2 = {"c", "we"};
        System.out.println("가운데 글자 가져오기");
        for (int i = 0; i < input2.length; i++) {
            System.out.printf("example %d", i+1);
            System.out.println("=".repeat(20));
            System.out.println("input: " + input2[i]);
            System.out.println("correct: " + result2[i]);
            System.out.println("my answer: " + s2.solution(input2[i]));
        }
        System.out.println();

        // 두 개 뽑아서 더하기
        Solution3 s3 = new Solution3();
        int[][] input3 = {{2,1,3,4,1}, {5,0,2,7}};
        int[][] result3 = {{2,3,4,5,6,7}, {2,5,7,9,12}};
        System.out.println("두 개 뽑아서 더하기");
        for (int i = 0; i < input3.length; i++) {
            System.out.printf("example %d", i+1);
            System.out.println("=".repeat(20));
            System.out.println("input: " + Arrays.toString(input3[i]));
            System.out.println("correct: " + Arrays.toString(result3[i]));
            System.out.println("my answer: " + Arrays.toString(s3.solution(input3[i])));
        }
        System.out.println();
    }
}

class Solution1 {
    public String solution(int num) {
        /*
        * 짝수와 홀수
        *
        * 풀이)
        * num을 2로 나눈 값이 0이면 짝수, 아니면 홀수
        * */
        return (num%2 == 0 ? "Even" : "Odd");
    }
}

class Solution2 {
    public String solution(String s) {
        /*
        * 가운데 글자 가져오기
        *
        * 풀이)
        * 1. 문자열의 길이 len와 중간 인덱스 mid 저장
        * 2. 문자열의 길이가 홀수이면 mid인덱스 값
        * 3. 문자열의 길이가 짝수이면 (mid-1)인덱스 값부터 2개
        * */
        String answer = "";
        int len = s.length();
        int mid = len / 2;
        if (len % 2 == 1)
            answer += s.charAt(mid);
        else
            answer += s.substring(mid-1, mid+1);
        return answer;
    }
}

class Solution3 {
    public int[] solution(int[] numbers) {
        /*
        * 두 개 뽑아서 더하기
        *
        * 풀이)
        * 1. for문 중첩해서 요소 하나하나에 접근
        * 2. 요소 두 개를 더한 값을 sum에 저장
        * 3. 길이가 (answer 배열의 길이 + 1) 배열 할당 후 answer 복사
        * 4. answer 배열에 sum 넣어줌 -> answer에 sum이 없을 때만!
        * */
        int[] answer = {};

        for (int i = 0; i < numbers.length - 1; i++) {
            for (int j = i + 1; j < numbers.length; j++) {
                int sum = numbers[i] + numbers[j];
                boolean isContain = false;
                for (int a : answer) {
                    if (a == sum) {
                        isContain = true;
                        break;
                    }
                }
                if (!isContain) {
                    answer = Arrays.copyOf(answer, answer.length + 1);
                    answer[answer.length - 1] = sum;
                }
            }
        }
        Arrays.sort(answer);
        return answer;
    }
}