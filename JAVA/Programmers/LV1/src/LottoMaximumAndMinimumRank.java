public class LottoMaximumAndMinimumRank {
    public int[] solution(int[] lottos, int[] win_nums) {
        int[] answer = new int[2];
        int minimum = 0;
        int maximum = 0;

        for (int i = 0; i < lottos.length; i++) {
            if (lottos[i] == 0) {
                maximum++;
            }
            for (int j = 0; j < win_nums.length; j++) {
                if (win_nums[i] == lottos[j]) {
                        minimum++;
                        maximum++;
                }
            }
        }
        System.out.println(minimum, maximum);
        return answer;
    }

}