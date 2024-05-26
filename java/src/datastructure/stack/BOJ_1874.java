package datastructure.stack;

import java.util.Scanner;
import java.util.Stack;

public class BOJ_1874 {

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int N = sc.nextInt();
    int A[] = new int[N];
    for (int i = 0; i < N; i++) {
      A[i] = sc.nextInt();
    }
    Stack<Integer> stack = new Stack<>();
    int num = 1;
    StringBuffer bf = new StringBuffer();
    for (int i = 0; i < A.length; i++) {
      int su = A[i];
      if (su >= num) {
        while (su >= num) {
          stack.push(num++);
          bf.append("+\n");
        }
        stack.pop();
        bf.append("-\n");
      } else {
        int n = stack.pop();
        if (n > su) {
          System.out.println("No");

        }
      }
    }
  }
}
