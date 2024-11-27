import java.util.Scanner;

class Hello{
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter num1: ");
        double num1 = sc.nextDouble();
        System.out.print("Enter num2: ");
        double num2 = sc.nextDouble();

        System.out.print("Enter the operation: ");
        char operator = sc.next().charAt(0);

        double ans = 0;
        switch(operator){
            case '+':
            ans = num1 + num2;
            break;

            case '-':
            ans = num1 - num2;
            break;

            case '%':
            ans = num1 % num2;
            break;

            case '*':
            ans = num1 * num2;
            break;

            case '/':
            if(num2 == 0){
                System.out.println("Division by zero not possible");
                break;
            }
            else{
                ans = num1/num2;
                break;
            }

            default:
            System.out.println("Invalid operator");
            break;
        }
        System.out.println(ans);

    }
}