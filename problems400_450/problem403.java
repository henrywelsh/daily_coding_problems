public class problem403 {
    public int rand7() {
        int n = 25;
        do {
            n = ((rand5() - 1) * 5) + rand5() - 1;
        } while (n > 21);

        return (n % 7) + 1;
    }
}
