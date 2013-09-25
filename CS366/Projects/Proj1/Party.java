import java.util.Random;

public class Party {

	private final static int RU_8p = 0;
	private final static int TU_10p = 1;
	private final static int RU_10p = 2;
	private final static int RD_10p = 3;
	private final static int RU_8a = 4;
	private final static int RD_8a = 5;
	private final static int TU_10a = 6;
	private final static int RU_10a = 7;
	private final static int RD_10a = 8;
	private final static int TD_10a = 9;
	private final static int TERMINAL_STATE = -1;
	private final static int INV = -100;

	private final static int[] numActions = { 3, 2, 3, 2, 3, 2, 3, 3, 3, 3 };

	private final static int P = 0;
	private final static int R = 1;
	private final static int S = 2;
	private static Random rnd = new Random(1);

	public static int init() {
		return RU_8p;
	}

	public static int numActions(int state) {
		if (state < 0 || state > 9) {
			System.err.println("Invalid state: " + state + "!!!");
			System.exit(INV);
			return INV;
		}
		return numActions[state];
	}

	public static int transition(int state, int action) {
		if (state == RU_8p) {
			if (action == P)
				return TU_10p;
			else if (action == R)
				return RU_10p;
			else if (action == S)
				return RD_10p;
			else {
				System.err.println("Invalid action: " + action + " at state: " + state + "!!!");
				System.exit(INV);
				return INV;
			}
		} else if (state == TU_10p) {
			if (action == P)
				return RU_10a;
			else if (action == R)
				return RU_8a;
			else {
				System.err.println("Invalid action: " + action + " at state: " + state + "!!!");
				System.exit(INV);
				return INV;
			}
		} else if (state == RU_10p) {
			if (action == P) {
				if (rnd.nextDouble() < 0.5)
					return RU_8a;
				else
					return RU_10a;
			} else if (action == R)
				return RU_8a;
			else if (action == S)
				return RD_8a;
			else {
				System.err.println("Invalid action: " + action + " at state: " + state + "!!!");
				System.exit(INV);
				return INV;
			}
		} else if (state == RD_10p) {
			if (action == P) {
				if (rnd.nextDouble() < 0.5)
					return RD_8a;
				else
					return RD_10a;
			} else if (action == R)
				return RD_8a;
			else {
				System.err.println("Invalid action: " + action + " at state: " + state + "!!!");
				System.exit(INV);
				return INV;
			}
		} else if (state == RU_8a) {
			if (action == P)
				return TU_10a;
			else if (action == R)
				return RU_10a;
			else if (action == S)
				return RD_10a;
			else {
				System.err.println("Invalid action: " + action + " at state: " + state + "!!!");
				System.exit(INV);
				return INV;
			}
		} else if (state == RD_8a) {
			if (action == P)
				return TD_10a;
			else if (action == R)
				return RD_10a;
			else {
				System.err.println("Invalid action: " + action + " at state: " + state + "!!!");
				System.exit(INV);
				return INV;
			}
		} else if (state == TU_10a || state == RU_10a || state == RD_10a || state == TD_10a) {
			return TERMINAL_STATE;
		}
		System.err.println("Invalid state: " + state + "!!!");
		System.exit(INV);
		return INV;
	}

	public static double reward(int state, int action, int nextState) {
		if (state == RU_8p) {
			if (action == P)
				return 2;
			else if (action == R)
				return 0;
			else if (action == S)
				return -1;
			else {
				System.err.println("Invalid action: " + action + " at state: " + state + "!!!");
				System.exit(INV);
				return INV;
			}
		} else if (state == TU_10p) {
			if (action == P)
				return 2;
			else if (action == R)
				return 0;
			else {
				System.err.println("Invalid action: " + action + " at state: " + state + "!!!");
				System.exit(INV);
				return INV;
			}
		} else if (state == RU_10p) {
			if (action == P) {
				return 2;
			} else if (action == R)
				return 0;
			else if (action == S)
				return -1;
			else {
				System.err.println("Invalid action: " + action + " at state: " + state + "!!!");
				System.exit(INV);
				return INV;
			}
		} else if (state == RD_10p) {
			if (action == P) {
				return 2;
			} else if (action == R)
				return 0;
			else {
				System.err.println("Invalid action: " + action + " at state: " + state + "!!!");
				System.exit(INV);
				return INV;
			}
		} else if (state == RU_8a) {
			if (action == P)
				return 2;
			else if (action == R)
				return 0;
			else if (action == S)
				return -1;
			else {
				System.err.println("Invalid action: " + action + " at state: " + state + "!!!");
				System.exit(INV);
				return INV;
			}
		} else if (state == RD_8a) {
			if (action == P)
				return 2;
			else if (action == R)
				return 0;
			else {
				System.err.println("Invalid action: " + action + " at state: " + state + "!!!");
				System.exit(INV);
				return INV;
			}
		} else if (state == TU_10a)
			return -1;
		else if (state == RU_10a)
			return 0;
		else if (state == RD_10a)
			return 4;
		else if (state == TD_10a)
			return 3;
		System.err.println("Invalid state: " + state + "!!!");
		System.exit(INV);
		return INV;
	}
}
