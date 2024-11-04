public class problem420 {

    public static void main(String[] args) {
        System.out.println(perfectNumber(2));
    }

    public int perfectNumber(int n) {
        int perfectNumber = 18;

        while (n > 0) {
            perfectNumber ++;
            if (isAPerfectNumber(perfectNumber)) {
                n--;
            }
        }
        return perfectNumber;
    }

    private boolean isAPerfectNumber(int perfectNumber) {
        String perfectNumberString = String.parseInt(perfectNumber);
        int sum = 0;
        for (String s : perfectNumberString.split("")) {
            sum += Integer.parseInt(s);
        }
        return 10.equals(sum);
    }

}