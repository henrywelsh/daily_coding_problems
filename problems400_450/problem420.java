public class problem420 {

    public static void main(String[] args) {
        System.out.println(perfectNumber(2));
    }

    public static int perfectNumber(int n) {
        int perfectNumber = 18;

        while (n > 0) {
            perfectNumber ++;
            if (isAPerfectNumber(perfectNumber)) {
                n--;
            }
        }
        return perfectNumber;
    }

    private static boolean isAPerfectNumber(int perfectNumber) {
        int sum = 0;
        while (perfectNumber > 0) {
            sum += perfectNumber % 10;
            perfectNumber /= 10;
        }
        return 10 == sum;
    }

}