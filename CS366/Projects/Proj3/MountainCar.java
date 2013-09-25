public class MountainCar {
	
	// corrected version Nov 27, 2011

	public static double[] init() {
		return new double[] { Math.random() * 0.2 - 0.6, 0 };
		// position near bottom and zero velocity
	}

	public static int numActions(double[] state) {
		return 3;
	}

	public static double[] transition(double[] state, int action) {
		if (state == null || state.length < 2) {
			System.out.println("Invalid state!");
			System.exit(-1);
		}

		action = action - 1;
		if (action != 0 && action != -1 && action != +1) {
			System.out.println("Invalid action!");
			System.exit(-1);
		}

		double xt = state[0]; // first element is the position
		double xtdot = state[1]; // second element is the velocity
		double xtp1 = xt + xtdot;
		double xtdotp1 = xtdot + 0.001 * action + -0.0025 * Math.cos(3 * xt);

		if (xtdotp1 < -0.07) { // imposing maximum speed
			xtdotp1 = -0.07;
		} else if (xtdotp1 > 0.07)
			xtdotp1 = 0.07;

		if (xtp1 < -1.2) { // imposing the left bound for position
			xtp1 = -1.2;
			xtdotp1 = 0.0;
		}
		if (xtp1 >= 0.5)
			return null; // goal state reached
		return new double[] { xtp1, xtdotp1 };
	}

	public static double reward(double[] state, int action, double[] nextState) {
		return -1.0; // always -1
	}
}
