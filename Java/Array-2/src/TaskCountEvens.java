public class TaskCountEvens {

    public static int countEvens(int[] nums) {
        int cnt = 0;
        for (int num: nums) {
            if (num % 2 == 0) cnt++;
        }
        return cnt;
    } 

    public static void main(String[] args) throws Exception {
        System.out.println(countEvens(new int[]{2, 1, 2, 3, 4}));
        System.out.println(countEvens(new int[]{2, 2, 0}));
        System.out.println(countEvens(new int[]{1, 3, 5}));
    }
}
