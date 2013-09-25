import java.util.Random;

public class RandomPolicy {

	static Random generator = new Random();
	final static int nepisodes = 20;

	public static void main(String[] arg) {
		double ret = 0.0;
		double total = 0.0;
		int state = 0;
		int next_state = 0;
		int numActions = 0;
		int action = 0;
		
		for (int epi = 0; epi < nepisodes; epi++) {
			state = Party.init();
			ret = 0.0;
			while (state != -1) {
				numActions = Party.numActions(state);
				action = generator.nextInt(numActions);
				next_state = Party.transition(state, action);
				ret += Party.reward(state, action, next_state);
				state = next_state;
			}
			System.out.println("Episode: " + epi);
			System.out.println("Return: " + ret);
			total += ret;
		}
		System.out.println("Average Return:" + (total / nepisodes));
	}
}
