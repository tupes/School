import java.io.*;

public class Sarsa {
	
	//FileWriter fstream = new FileWriter("out.txt");
	//BufferedWriter out = new BufferedWriter(fstream);
	final static double alpha = 0.1;
	final static int nepisodes = 1000;
	final static int nruns = 100;

	public static void main(String[] arg) {
		try {
			BufferedWriter outResults = new BufferedWriter(new FileWriter("outResults.txt"));
			BufferedWriter outPolicy = new BufferedWriter(new FileWriter("outPolicy.txt"));
			//FileWriter fstream = new FileWriter("out.txt");
			//PrintWriter out = new PrintWriter(fstream);

			//System.err.println("Error");
			//return null;
		
			double ret = 0.0;
			double reward = 0;
			double maxValue = 0.0;
			double value = 0.0;
			double nextValue = 0.0;
			int state = 0;
			int nextState = 0;
			int numActions = 0;
			int action = 0;
			// Initialize action values
			int NUM_STATES = 10;
			int NUM_ACTIONS = 3;
			double episodeAvgs[] = new double[nepisodes];
			for (int i=0; i < nepisodes; i++) {
				episodeAvgs[i] = 0.0;
			}
			double policyValues[] = new double[NUM_STATES + 1];
			double actionValues[][] = new double[NUM_STATES][NUM_ACTIONS];
			
			for (int run=0; run < nruns; run++) {
				// reset values for a new run
				for (int s=0; s < NUM_STATES; s++) {
					policyValues[s] = 6.5;
					for (int a=0; a < NUM_ACTIONS; a++) {
						actionValues[s][a] = 6.5;
					}
				}
				policyValues[NUM_STATES] = 0;
				// start a new episode
				for (int epi = 0; epi < nepisodes; epi++) {
					//System.out.println("Episode: " + epi);
					state = Party.init(); //System.out.println("State: " + state);
					ret = 0.0;
					while (state != -1) {
						numActions = Party.numActions(state); //System.out.println("Number actions: " + numActions);
						// get action greedily
						action = 0;
						maxValue = actionValues[state][0];
						for (int a = 1; a < numActions; a++) {
							value = actionValues[state][a];
							if (value > maxValue) {
								policyValues[state] = value;
								action = a;
								maxValue = value;
							}
						}
						//System.out.println("Action: " + action);
						//System.out.println("Max Value: " + maxValue);
						// get outcome
						nextState = Party.transition(state, action); //System.out.println("Next state: " + nextState);
						reward = Party.reward(state, action, nextState); //System.out.println("Reward: " + reward);
						ret += reward; //System.out.println("Total return: " + ret);
						// update action and policy values
						if (nextState == -1) nextValue = 0;
						else nextValue = policyValues[nextState];
						actionValues[state][action] += alpha * (reward + nextValue - actionValues[state][action]);
						state = nextState;
					}
					episodeAvgs[epi] += ret;
					//System.out.println("Return: " + ret);
				}
			}
			for (int s=0; s < NUM_STATES; s++) {
				numActions = Party.numActions(s);
				action = 0;
				maxValue = actionValues[s][0];
				for (int a = 1; a < numActions; a++) {
					value = actionValues[s][a];
					if (value > maxValue) {
						action = a;
						maxValue = value;
					}
				}
				outPolicy.write("State " + s + ": " + action + "\n");
			}
			outPolicy.close();
			for (int i=0; i < nepisodes; i++) {
				episodeAvgs[i] /= nruns;
				outResults.write(episodeAvgs[i] + "\n");
			}
			outResults.close();
		} catch (IOException e) {
			e.printStackTrace();
		}
	} // main
	//~ try {
	//~ out.close();
	//~ } catch (Exception e) {
		//~ System.err.println("Error");
	//~ }
} // class
