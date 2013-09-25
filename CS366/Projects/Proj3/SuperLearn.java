import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Collections;
import java.util.Random;
import java.util.Vector;

public class SuperLearn {
	static Random rnd = new Random(1);

	static final int WEIGHTSNUM = 968;
	static Vector<Double> weights = new Vector<Double>();
	static double alpha = 0.1/Tilecoder.numOfTilings;

	public static double f(double x1, double x2) {
		// linear function approximator.
		if (weights.size() == 0){
	        weights.setSize(WEIGHTSNUM);
	        Collections.fill(weights, 0.0);
		}
		
        Tilecoder.tilecode(x1, x2, Tilecoder.copyOfTI);
        double returnVal = 0.0;
        
        for (int i = 0; i < Tilecoder.numOfTilings; i++){
            returnVal += weights.elementAt(Tilecoder.copyOfTI[i]); 
        }
		return returnVal;
	}

	public static void learn(double x1, double x2, double y) {
		// gradient descent learning algorithm.
		double weightChange = alpha * (y - f(x1, x2));
		
		for (int j = 0; j < Tilecoder.numOfTilings; j++) {
			weights.setElementAt(weights.elementAt(Tilecoder.copyOfTI[j]) + weightChange, Tilecoder.copyOfTI[j]); 
		}
	}

	private static void printTest1(double x1, double x2, double y) {
		double fxbeforey = f(x1, x2);
		learn(x1, x2, y);
		double fxaftery = f(x1, x2);
		System.out.println("Example (" + x1 + ", " + x2 + ", " + y + "). f(x) before learning: " + fxbeforey
				+ " and after learning: " + fxaftery);
	}

	public static double targetFunction(double x1, double x2) {
		return Math.sin(x1 - 3) * Math.cos(x2) + rnd.nextGaussian() * 0.1;
	}

	public static void train(int numOfSteps) {
		for (int i = 0; i < numOfSteps; i++) {
			double x1 = rnd.nextDouble() * 6;
			double x2 = rnd.nextDouble() * 6;
			double y = targetFunction(x1, x2);
			learn(x1, x2, y);
		}

	}

	public static void writeF(String filename) {
		FileWriter fstreamout;
		try {
			fstreamout = new FileWriter(filename);
			BufferedWriter out = new BufferedWriter(fstreamout);
			int x1steps = 50, x2steps = 50;
			for (int i = 0; i < x1steps; i++) {
				for (int j = 0; j < x2steps; j++) {
					double y = f(i * 6.0 / x1steps, j * 6.0 / x2steps);
					out.write(y + ",");
				}
				out.write("\n");
			}
			out.close();
		} catch (IOException e) {
			e.printStackTrace();
		}
	}

	public static void printMSE() {
		int N = 10000;
		double totalSE = 0.0;
		for (int i = 0; i < N; i++) {
			double x1 = rnd.nextDouble() * 6.0;
			double x2 = rnd.nextDouble() * 6.0;
			double error = targetFunction(x1, x2) - f(x1, x2);
			totalSE += error * error;
		}
		System.out.println("The estimated MSE: " + totalSE / N);
	}

	public static void test1(String[] args) {
		printTest1(0.1, 0.1, 2.0);
		printTest1(4.0, 2.0, -1.0);
		printTest1(5.99, 5.99, 3.0);
		printTest1(4.0, 2.1, -1.0);
	}

	public static void main(String[] args) {
	  train(20);
		writeF("f20.csv");
		printMSE();

		for (int i = 0; i < 10; i++) {
			train(1000);
			printMSE();
		}
		writeF("f10000.csv");
	}
}
