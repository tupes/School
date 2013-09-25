import java.io.*;

public class Sarsa {
	
	final static double ALPHA = 0.1;
	final static double OPTIMISTIC = 6.0;
	final static int NUM_STATES = 10;
	final static int NUM_ACTIONS = 3;
	
	public static void initValues(double policyValues[], double actionValues[][]) {
		for (int s=0; s < NUM_STATES; s++) {
			policyValues[s] = OPTIMISTIC + Math.random();
			for (int a=0; a < NUM_ACTIONS; a++) {
				actionValues[s][a] = OPTIMISTIC + Math.random();
			}
		}
		policyValues[NUM_STATES] = 0;
	}
	
	// returns the action determined by the greey policy
	public static int getAction(int state, double policyValues[], double actionValues[][]) {
		int numActions = Party.numActions(state);
		int action = 0;
		double value = 0.0;
		double maxValue = actionValues[state][0];
		for (int a = 1; a < numActions; a++) {
			value = actionValues[state][a];
			if (value > maxValue) {
				policyValues[state] = value;
				action = a;
				maxValue = value;
			}
		}
		return action;
	}
	
	public static void main(String[] args) {
		try {
			// get arguments for the number of runs and episodes
			int numRuns = Integer.parseInt(args[0]);
			int numEpisodes = Integer.parseInt(args[1]);
			// declare variables
			BufferedWriter resultsFile = new BufferedWriter(new FileWriter("outResults.txt"));
			BufferedWriter policyFile = new BufferedWriter(new FileWriter("outPolicy.txt"));
			double ret = 0.0; double reward = 0.0;
			double nextValue = 0.0;
			int state = 0; int nextState = 0; int action = 0;
			double policyValues[] = new double[NUM_STATES + 1];
			double actionValues[][] = new double[NUM_STATES][NUM_ACTIONS];
			double episodeAvgs[] = new double[numEpisodes];
			// Initialize episode average returns
			for (int i=0; i < numEpisodes; i++) {
				episodeAvgs[i] = 0.0;
			}
			
			// Execute each run
			for (int run=0; run < numRuns; run++) {
				initValues(policyValues, actionValues);
				// Execute each episode
				for (int epi = 0; epi < numEpisodes; epi++) {
					state = Party.init();
					ret = 0.0;
					// Execute actions until terminal state is reached
					while (state != -1) {
						action = getAction(state, policyValues, actionValues);
						// get outcome
						nextState = Party.transition(state, action); 
						reward = Party.reward(state, action, nextState);
						ret += reward; 
						if (nextState == -1) nextValue = 0;
						else nextValue = policyValues[nextState];
						// update action value and state
						actionValues[state][action] += ALPHA * (reward + nextValue - actionValues[state][action]);
						state = nextState;
					}
					// keep a running total of return for each episode
					episodeAvgs[epi] += ret;
				}
			}
			
			// write the policy to a file
			for (int s=0; s < NUM_STATES; s++) {
				action = getAction(s, policyValues, actionValues);
				policyFile.write("State " + s + ": " + action + "\n");
			}
			policyFile.close();
			
			// get the average return for each episode and write it to a file
			for (int i=0; i < numEpisodes; i++) {
				episodeAvgs[i] /= numRuns;
				resultsFile.write(episodeAvgs[i] + "\n");
			}
			resultsFile.close();
			
		} catch (IOException e) {
			e.printStackTrace();
		}
	} // main
} // class
